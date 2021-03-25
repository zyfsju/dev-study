1. [Prerequisites](#prerequisites)
2. [Push Images to Container Registry](#acr)
    - [Build Docker Images](#build-docker)
    - [Log into ACR](#login-acr)
    - [Tag Local Image](#tag-docker)
    - [Push to ACR](#push-acr)
3. [Deploy to AKS](#aks)
    - [Prepare Manifest](#manifest)
    - [Connect to AKS](#connect-aks)
    - [Apply Manifest](#deploy-aks)
    - [Test Application](#test-aks)
    - [HTTPS Ingress Controller](#aks-ingress)
4. [Start and Stop App](#start-app)
    - [MySQL server](#start-mysql)
    - [Kubernetes Clusters](#start-k8s)

## Prerequisites <a name="prerequisites"/>

Install Azure CLI, or use Azure Cloud Shell on Azure portal.

## Push Images to Container Registry <a name="acr"/>

> More on [preparing applications for AKS](https://docs.microsoft.com/en-us/azure/aks/tutorial-kubernetes-prepare-app).

#### Build Docker Images <a name="build-docker"/>

#### Log into ACR <a name="login-acr"/>

To log into Azure,

```bash
az login
```

Set relevant shell variables.

```bash
RESOURCE_GROUP=<RESOURCE_GROUP>
ACR_NAME=<ACR_NAME>
```

To log into the ACR instance,

```bash
az acr login --name $ACR_NAME
```

To see a list of your current local images, use the docker images command:

```bash
docker images
```

To get the login server address,

```bash
az acr list --resource-group $RESOURCE_GROUP --query "[].{acrLoginServer:loginServer}" --output table
```

#### Tag Local Image <a name="tag-docker"/>

Modify `SRC_REPO`, `SRC_TAG`, `DEST_REPO`, `DEST_TAG` as needed.

```bash
ACR_LOGIN_SERVER=myacr.azurecr.io
SRC_REPO=<SRC_REPO> # change here
SRC_TAG=v0.0.1 # change here
DEST_REPO=<DEST_REPO> # change here
DEST_TAG=v0.0.1 # change here
SRC_IMG=$SRC_REPO:$SRC_TAG
DEST_IMG=$ACR_LOGIN_SERVER/$DEST_REPO:$DEST_TAG
docker tag $SRC_IMG $DEST_IMG
```

Run `docker images` again to verify the tags are applied.

#### Push to ACR <a name="push-acr"/>

With your image built and tagged, push it to your ACR instance. Use docker push and provide your own acrLoginServer address for the image name as follows:

```bash
docker push $DEST_IMG
```

To return a list of images that have been pushed to your ACR instance,

```bash
az acr repository list --resource-group $RESOURCE_GROUP --name $ACR_NAME --output table
```

To see the tags for a specific image,

```bash
az acr repository show-tags --name $ACR_NAME --repository $DEST_REPO --output table
```

## Deploy to AKS <a name="aks"/>

#### Prepare Manifest <a name="manifest"/>

Manifests are used to create, modify and delete K8s resources such as pods, deployments, services or ingresses. They are usually defined as `.yaml` or `.json` files. We can create objects on or delete them from a K8s cluster. from via commands such as `kubectl apply` or `kubectl delete`.

We can either come up with a K8s manifest for deployment from scratch or use a templating option to make the process more automated and organized, such as Helm and Kustomize.

> Refer to [Kubernetes Objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/object-management/)
>
> Refer to [Helm](https://docs.microsoft.com/en-us/azure/aks/quickstart-helm)
>
> Refer to [Kustomize](https://kubernetes.io/docs/tasks/manage-kubernetes-objects/kustomization/)

In this directory, the following templates are available. Be sure to inspect the manifest and modify items as needed before deployment.

-   [db-secret-template.yaml](./db-secret-template.yaml) for DB secret.
-   [cluster-issuer.yaml](./cluster-issuer.yaml) for TLS certificate cluster issuer.
-   [my-app-ingress.yaml](./my-app-ingress.yaml) for ingress controller.
-   [my-app.yaml](./my-app.yaml) for the web app frontend and backend API.

#### Connect to AKS <a name="connect-aks" />

To connect to the Kubernetes cluster from your local computer, you use `kubectl`, the Kubernetes command-line client.

If you use the Azure Cloud Shell, `kubectl` is already installed.

Set relevant shell variables.

```bash
RESOURCE_GROUP=<RESOURCE_GROUP>
AKS_CLUSTER=my-aks
ACR_NAME=myacr
```

To configure `kubectl` to connect to your Kubernetes cluster,

```bash
az aks get-credentials --resource-group $RESOURCE_GROUP --name $AKS_CLUSTER
```

To verify the connection to your cluster,

```bash
kubectl get nodes
```

#### Apply Manifest <a name="deploy-aks" />

To deploy your application, use the `kubectl apply` command. This command parses the manifest file and creates the defined [Kubernetes objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/).

```bash
YAML_PATH=<MY_YAML_PATH>
kubectl apply -f $YAML_PATH
```

**Secrets**
[Reference](https://medium.com/faun/how-to-use-secrets-from-azure-key-vault-in-azure-kubernetes-service-704973be5fc1)

We can inject sensitive data such as usernames and passwords into pods using the secret object.

Create the secret by

```bash
kubectl apply -f db-secret.yaml
```

#### Test Application <a name="test-aks" />

When the application runs, a Kubernetes service exposes the application front end to the internet. This process can take a few minutes to complete.

To monitor progress, use the `kubectl get service` command with the --watch argument.

```bash
kubectl get service my-app-front --watch
```

#### HTTPS Ingress Controller <a name="aks-ingress" />

> Reference: [Create an HTTPS ingress controller on Azure Kubernetes Service (AKS)](https://docs.microsoft.com/en-us/azure/aks/ingress-tls)

We first create 2 replicas of the ingress controllers, by installing `nginx-ingress` with [Helm](https://helm.sh/docs/intro/).

```bash
# Create a namespace for your ingress resources
kubectl create namespace ingress-basic

# Add the ingress-nginx repository
helm repo add ingress-nginx https://kubernetes.github.io/ingress-nginx

# Use Helm to deploy an NGINX ingress controller
helm install nginx-ingress ingress-nginx/ingress-nginx \
    --namespace ingress-basic \
    --set controller.replicaCount=2 \
    --set controller.nodeSelector."beta\.kubernetes\.io/os"=linux \
    --set defaultBackend.nodeSelector."beta\.kubernetes\.io/os"=linux
```

To get the public IP address, run `kubectl get service` command as follows.

```bash
$ kubectl --namespace ingress-basic get services -o wide -w nginx-ingress-ingress-nginx-controller
```

Configure an FQDN for the ingress controller IP address.

```bash
# Public IP address of your ingress controller
IP=<MY_EXTERNAL_IP> # get the EXTERNAL-IP address from the previous step

# Name to associate with public IP address
DNSNAME=<MY_DNS_NAME> # it will be first part of the URL of the web app, <MY_DNS_NAME>.<LOCATION>.cloudapp.azure.com

# Get the resource-id of the public ip
PUBLICIPID=$(az network public-ip list --query "[?ipAddress!=null]|[?contains(ipAddress, '$IP')].[id]" --output tsv)

# Update public ip address with DNS name
az network public-ip update --ids $PUBLICIPID --dns-name $DNSNAME

# Display the FQDN
az network public-ip show --ids $PUBLICIPID --query "[dnsSettings.fqdn]" --output tsv
```

The NGINX ingress controller supports TLS termination. We use cert-manager, which provides automatic `Lets Encrypt` certificate generation and management functionality.

To install the cert-manager controller:

```bash
# Label the ingress-basic namespace to disable resource validation
kubectl label namespace ingress-basic cert-manager.io/disable-validation=true

# Add the Jetstack Helm repository
helm repo add jetstack https://charts.jetstack.io

# Update your local Helm chart repository cache
helm repo update

# Install the cert-manager Helm chart
helm install \
  cert-manager \
  --namespace ingress-basic \
  --version v0.16.1 \
  --set installCRDs=true \
  --set nodeSelector."beta\.kubernetes\.io/os"=linux \
  jetstack/cert-manager
```

Use [cluster-issuer.yaml](./cluster-issuer.yaml) to create the cluster issuer. `Issuer` works in a single namespace, and `ClusterIssuer` works across all namespaces. We use `ClusterIssuer` here.

Make sure the web application services are running on AKS. If not, create them using [my-app.yaml](./my-app.yaml).

Create an ingress route using [my-app-ingress.yaml](./my-app-ingress.yaml) as a template. Update the hosts and host to the DNS name you created previously. Update `paths` as needed.

To verify that the certificate was created successfully. Verify `READY` is True, which may take several minutes.

```bash
$ kubectl get certificate --namespace ingress-basic
```

Open a web browser to `<MY_DNS_NAME>.<LOCATION>.cloudapp.azure.com`. Swap the name in brackets with the actual value, such as `my-app.eastus.cloudapp.azure.com`.

## Start and Stop App <a name="start-app"/>

The database and the application code served in Kubernetes clusters needs to be running to ensure the accessibility of the app. The MySQL server and the kubernetes services are created under one resource group, while the virtual machine sets on which kubernetes runs are in seperate resource groups.

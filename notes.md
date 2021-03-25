# 20200225

Raw data: vehicle, video, radar
generated: event finding, manual validation, regression tests, HPC usage data

MySQL, FORD-DAT2 MOART
meta-data: weather conditions, driving scenarios, resimability, day/night, bridge/tunnel

# 20200327

$ sudo -u postgres psql # open a session in the terminal
$ psql -U postgres -d testdb -h 127.0.0.1 -p 5432 # log into the a table, -U is for user

# 20200401

$ ip addr # shows all ip info
$ nohup python3 app.py > output.log &

# 20200420

docker-compose for different environments, prod and local

1. have a main yaml, with prod.yaml and local.yaml or env files, overwrite env var, map port 5000 to different ports. For prod, change volume mapping
2. make them in different networks (networking in docker)
3. make container_name vary by env (prod/local)
4. more env var, - "CELERY_BROKER_URL": "redis://redis-prod/0", - "CELERY_RESULT_BACKEND": "redis://redis-prod/0", - DB_URL - HOST_URL
   test locally, make sure they won't affect each other

# 20200811

metaclasses

A class, in Python, is an object, and just like any other object, it is an instance of "something". This "something" is what is termed as a Metaclass. This metaclass is a special type of class that creates other class's objects. Hence, metaclass is responsible for making new classes. This allows the programmer to customize the way classes are generated.

To create a metaclass, overriding of new() and init() methods is usually done. new() can be overridden to change the way objects are created, while init() can be overridden to change the way of initializing the object. Metaclass can be created by a number of ways. One of the ways is to use type() function. type() function, when called with 3 parameters, creates a metaclass. The parameters are :-

Class Name
Tuple having base classes inherited by class
A dictionary having all class methods and class variables
Another way of creating a metaclass comprises of 'metaclass' keyword. Define the metaclass as a simple class. In the parameters of inherited class, pass metaclass=metaclass_name

Metaclass can be specifically used in the following situations :-

when a particular effect has to be applied to all the subclasses
Automatic change of class (on creation) is required
By API developers

# 20210308

```bash
ln test test2 # create a hard link (direct reference via its inode) for test, named test2
ln -s test test2 # create symbolic link
unlink # remove files
```

Hardlinks are not available on the BeeGFS filesystem, so we use symbolic links. They were available on the Lustre file system (when server was in kokomo) so we used them there. Extremely useful when available.

If the link is going to be quickly removed (it's for temporary scripting) might be more efficient to use the symbolic link? but otherwise the hardlinks are almost always better IMO. ah, disadvantage of hardlink. You have to know where all potential links are if you wish to remove the data vs. sym links, they just become dead.

Potential use:

-   It'll be very useful to testing scripts in HPCC. Create symlinks for a handful of logs in a folder and run them through a script, so that I don't need to copy and I can select only a few but all of them for testing.

# 20210322

## Interview

technical
-algorithm, dynamic programming
-system design/OOD

behavior

-   amazon's 14 leadership principles

Do not limit your self to LinkedIn
General job boards
https://www.linkedin.com/jobs/
https://www.indeed.com/
http://www.dice.com/
http://angel.co/jobs
http://hired.com
https://www.themuse.com/jobs
http://stackoverflow.com/jobs
http://jobs.github.com
http://itjobcafe.com
http://toptechjobs.com
http://www.techcareers.com
http://www.justtechjobs.com
http://www.techfetch.com

Resources for mapping of resume with job description :
https://skillsyncer.com/

https://www.jobscan.co/

3 Ps - prepare, Practice, Perform
Coding Interview resources:

• BOOK: Cracking the Coding Interview: 189 Programming Questions and Solutions by Gayle Laakmann McDowell, (http://www.crackingthecodinginterview.com/)
• BOOK: Elements of Programming Interviews - (a guide to interviewing for software development roles- C++, Java,or Python) https://elementsofprogramminginterviews.com/ free PDF sample of the Python book at https://lnkd.in/gEGgcVa
• ONLINE PRACTICE: https://leetcode.com/

STAR technique of interviews:
https://www.thebalancecareers.com/what-is-the-star-interview-response-technique-2061629

https://www.linkedin.com/groups/8209939/
https://www.facebook.com/Udacity/?tn-str=k*F

https://www.themuse.com/advice/4-ways-you-can-take-back-control-during-a-neverending-interview-process
https://www.themuse.com/advice/4-survival-tips-for-an-allday-interview
here is one more
https://www.quora.com/What-are-the-best-tips-to-handle-6-hour-long-interviews

Write down the questions they asked and what I gave them

STAR - R most important

## Big Data

Q: Does spark work on hpcc without extra hardware? Is it still worthwhile to use spark alone?

A: Yes Spark works on hpcc without extra hardware and it may or may not be worthwhile. Spark accepts tables and data frames as input but right now none of our data exists in tabular form so there isn’t much point to use Spark. Pandas + HPCC is probably sufficient.

Q: what are the common technologies that use with Spark and can work without Hadoop? database like Hive? logging tools, etc?

A: Any data that is in the form of a table or text works with Spark, this can be any database. The pipeline begins by loading the vehicle data into parquet files.

```bash
squeue -u <USER_ID>
squeue | wc -l
sbatch -A <ACCOUNT> <EXE_FILE> --partition=<PARTITION_NAME>
srun -n1 -t0 -A <ACCOUNT> --pty /bin/bash -l
# To perform that on the compute node you'd want to specify the amount of memory and number of cores you want in your srun/sbatch command:
srun -A <PROJECT> -t 1440:00 -n 4 --mem=16384 --pty /bin/bash -l
srun -A (project) -t (timeout) -n (cores) --mem=(mem in MB) --pty /bin/bash -l

scontrol # change priority
scontrol show job <JOB_ID>

chmode 777 -R some_dir/ # Open permissions to everyone
find $(pwd) -regex ".*RCTB_DOE.*.mat" -exec cp {} some_dir \;;

find $(pwd) -maxdepth 4 -type d -execdir find {} -regex ".*.mat" -type f \;| wc -l

find . -regex "./[0-9].*.mat" -exec cp {} some_dir \;

gnome-terminal &
getent passwd <USER_ID>
```

```python
os.path.getmtime() # last modified time
for root, dirs, files in os.walk(root_dir): # find all nested files
```

### Linux Cheatsheet

```bash
netstat -lnp #show all ports and processes
sudo kill -9 $(sudo lsof -t -i:3000)

# .bashrc: some user defined shortcuts
source .bashrc


Create alias
vim ~/.bashrc # create my own commands

nohup node Server.js # run something without hangup
```

Tmux:

-   Split windows
-   Open another session
-   Allow you to detach it so that you can close it and check later

### Azure Resources

Azure VM:

-   Hosts gitlab-runner, PyPI and Airflow.
-   A basic VM with Windows (because we had to build python packages with windows dependencies)

Azure Kubernetes Service:

-   The service itself is free. You only pay for the VMs in the node pools.
    The container registry is integrated.
-   For now you can deploy K8s in a private network, use private IP and allow connections only from our internal network/VPN. There's no problem connecting to 3rd party APIs from a private K8s cluster.

Azure Database for PostgreSQL servers:

-   Directly on Azure, not under Docker, so that Azure handles the availability, backups and more.
-   If on K8s, we have to deal with backups, migrations, persistent storage etc.

CI/CD and Data Flow:

-   CI/CD runs on gitlab-runner.
-   CI/CD runs all tests and puts packages that are distributable onto PyPI server.
-   Images are pushed to Azure Container Registries. When a new image version is detected, it will gets deployed to K8s.
-   Airflow monitors and schedules jobs running on Slurm on HPC, including moving data from HPCC to Azure DB. So the VM doesn't need to be that strong because bulk of the work will be run on HPC. Database is hosted on Azure Database for PostgreSQL servers. The API on K8s can talk to the db.

### Jenkins

Workflow:

-   get permission to connect laptop to a node
-   get permission to create nodes on Jenkins to connect your machine to (configure menu option for nodes)
-   get permission to create jobs on Jenkins (configure menu option for nodes)
-   develop Groovy scripts that specify what to run on Jenkins server and how to run it

What's the benefit of using Jenkins?

-   Make test results traceable
-   Parallel -> faster
-   Dashboard, historical, email notification add more visibility, easier to maintain
-   Easy to integrate new tasks, flexible.
-   Less labor. No need to copy and paste code, submit slurm jobs, save results manually. CI/CD -> fully automated

# 20210324

```bash
docker-compose up --build
docker ps # show all runnng containers
docker exec -it <CONTAINER ID> bash # log into the docker container

# build an API docker image and connect to a MySQL database manually
docker build -t db-api -f .docker/Dockerfile .
docker run -it -e DB_NAME={DB_NAME} -e DB_USER={DB_USER} -e DB_PWD={DB_PWD} -e DB_PORT={DB_PORT} -e DB_HOST={DB_HOST} -p 8999:8000 db-api

# build docker image for azure kubernetes
TAG=v0.0.5
docker build -t db-api:${TAG} -f .docker/Dockerfile --build-arg ROOT_PATH="/api" .
```

# 20210325

## Azure

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

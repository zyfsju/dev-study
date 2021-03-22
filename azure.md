# Azure

### Intro

#### Why Cloud Development Is Important

Advantages of cloud computing:

-   Cost: cloud provider handles all upfront costs associated with buying hardware, along with ongoing maintenance costs
-   Scale: Most are pay-as-you-go depending on demand (elasticity), and can be expanded as needed
-   Reliability: management of backups, disaster recovery, etc. is made easier
-   Security: Policies and controls are already in place to protect your data

Elasticity: the ability to scale up or down resources to match demand

Downsides:

-   Internet-based, so it can be prone to outages and fluctuations in speed
-   Sensitive, private and core data is physically located on someone else's server
-   Cloud services will be tailored and customized for your specific cloud instance, potentially making it hard to quickly change providers

### Azure Compute Services

#### Virtual Machines vs. App Services

Virtual Machines: Infrastructure as a service (IaaS)

-   Full access to VMs
-   No hardware purchase necessary
-   Supports Linux and Windows
-   Flexible Types and Sizes available
-   Supports custom images
-   High availability and scaling

Limitations:

-   Generally more expensive
-   labor intensive

Use cases:

-   Control of OS or custom software
-   Testing and development

App Services:

-   Supports multiple languages
-   High availability and auto-scaling
-   Vertical and Horizontal Scaling
-   Supports Windows and Linux
-   Supports continuous deployment (CD)
-   Platform as a service (PaaS)
-   Cost based on App Service Plan
    -   Dev/Test
    -   Production
    -   Isolated

Limitations:

-   Limited access to host server
-   cost. always paying for the service plan, if your application isn't running.
-   hardware limitations, 14 GB of memory and 4 vCPU cores per instance
-   limited set of programming languages

Use cases:

-   Deploy lightweight applications or services
-   Non-High Performance computer needs

### Azure Storage

#### Big Picture: Storage

Benefits of using Azure for storage are:

-   Automated backup and recovery
-   An option to replicate data at multiple data centers worldwide to help prevent outages from unplanned events, such as hardware failure
-   Data analytics support
-   Data encryption for added security
-   Support for the storage of multiple data types, i.e. relational data, non-relational data or NoSQL data, and unstructured data such as images.
-   Scale up or scale out when demand is high and scale back when demand is low.
-   Eliminate the expense of having to purchase, install, configure, and maintain on premises hardware.

Azure Storage options are:

-   Azure SQL Server and SQL Database
-   Azure Blob Storage
-   Azure CosmosDB
-   Disk Storage
-   Azure Data Lake Storage
-   HPC Cache

#### Blob Storage

A Binary Large Object or Blob is a data type that can store unstructured (binary) data and is used to store images or videos in a database. Blobs

-   have higher latency than memory and local disk, and
-   don't have the indexing features that make databases efficient at running queries
-   are commonly used with databases to store non-queryable data, such as a profile picture for a user's profile. Each user record in the database would include the URL of the blob containing the user's photo

Azure Storage Accounts can contain multiple blob containers within them, such as "images" and "movies" containers, to organize different data files. Each container can have many blobs inside of them (the files themselves).

Blob storage tiers - hot, cold and archive. Set based on how frequently data will be accessed, with hot accessed the most frequently, with relatively low latency for requests, but higher costs.

Blob storage offers a rule-based policy you can use to transition data between these tiers, to optimize performance and cost.

-   Blobs may start in a hot container
-   could be moved to a cool container if they have not been modified in the past 30 days.
-   If they have not been modified in 90 days, they could be transitioned to Archive storage.
-   You could then perhaps delete them after a year of non-usage.

General-purpose v2 storage accounts provide support and the latest features for Azure Storage services such as blobs, Data Lake Gen2, Files, Disks, Queues, and Tables.

Q: You are trying to pull in some images from blob storage into your app, but have been unsuccessful. Which of the following might resolve this?

A:

-   Give the blob storage container a public endpoint
-   Add the access key for the blob storage account into the call

### Security and Monitoring Basics

#### Security Best Practices in Azure

Virtual machines:

-   Enable encryption on VMs
-   Identify and remediate exposed VMs that allow access from "any" source IP address
-   Install the latest security updates
-   Control VM access
-   Periodically redeploy your VMs to force a fresh version of the OS

App Services:

-   Authenticate through Azure Active Directory
-   Don't put credentials and other secrets in source code or GitHub
-   Perform security penetration testing
-   Monitor the security state of your App Service environments

#### OSAL2 with MSAL

OAuth 2.0 provider creates a token to authorize user with 3rd party. 3rd party does not directly manage user identity or authentication. OAuth 2.0 is the industry-standard protocal for authorization. Apps can delegate the responbility of maintaining their username and password information to a centralized identity provider.

-   Browser Pop-up to request authorization code at `/oauth2/v2.0/authorize`. Return Auth Code.
-   Request Access Token with auth code, client ID, etc at `/oauth2/v2/0/token`.
-   Call endpoint with access token at the secure endpoint. It validates token and returns secure data.

#### Monitoring and Logging

Benefits of logging:

-   Troubleshooting problems or preventing potential new ones
-   Improving application performance or maintainability
-   Automating operations that would otherwise require manual intervention

### Project

Github: [https://github.com/udacity/nd081-c1-provisioning-microsoft-azure-vms-project-starter](https://github.com/udacity/nd081-c1-provisioning-microsoft-azure-vms-project-starter)

## Azure CLI

## Azure Container Registry

Use Azure container registries with your existing container development and deployment pipelines, or use Azure Container Registry Tasks to

-   build container images in Azure on-demand, or
-   automate builds triggered by source code updates, updates to a container's base image, or timers.

# Atlas

## What is

1. Database as a service
2. Stores data in the cloud
3. Handles replication: maintainig redundant copies of data --> increase availability.

**Clusters**: a group of servers that store your data
**Replica set**: a cluster where each server stores the same data

## Why

1. Simplicity of setup: deploys and manages clusters for you
2. easy access to different cloud providers and regions
3. free access to experiment with new tools and features

**Features**

Data Explorer

Stitch: a serverless platform that makes it easier to use MongoDB and web and mobile applications

Charts: creates visualizations of data

Altas also allows you to configure users with different privileges levels.

# Mongo Shell

srv connection

```bash
mongo "mongodb+srv://cluster0-jxeqq.mongodb.net/test" --username m001-student -password m001-mongodb-basics
```

standard connection string

```bash
mongo "mongodb://cluster0-shard-00-00-jxeqq.mongodb.net:27017,cluster0-shard-00-01-jxeqq.mongodb.net:27017,cluster0-shard-00-02-jxeqq.mongodb.net:27017/test?replicaSet=Cluster0-shard-0" --authenticationDatabase admin --ssl --username m001-student --password m001-mongodb-basics
```

Databases, Collections, and Documents

Documents: Scalar Value Types

MongoDB Compass uses a 3rd party plugin for the geographical visualization of geospatial fields in your documents.

# MongoDB Query Language

### Filter

Equality filters: {usertype: 'Subscriber'}
Range filters: `$gte` `$lt`
`$` indicates it is an operator.
{"birth year": {"$gte": 1985, "$lt": 1990}}

# Data Modeling

A good data model ensures good performance, maximizes the productivity of your developers, and minimizes the overall cost of your solution

considerations:

1. Usage pattern
2. how you access data
3. which queries are critical to your application
4. ratios between reads and writes

flexible schema, document validation

### Document Model

Data Hierarchy
database, collection, documents

1. stores data as documents
2. document fields can be values, embedded documents, or arrays of values and documents
3. MongoDB is a Flexible Schema DB

### Constraints in Computer Applications

1. Hardware
    - RAM
    - SSD/Hard disk drive
2. Data
    - Size
    - Security, Sovereignty
3. Application
    - Network latency
4. Database Server/MongoDB
    - Max size of document (16 MB), atomicity of updates

Working set: the total body of data that the application uses in the course of normal operations

MongoDB --> Memory + FS Cache (frequently accessed documents and indexes) --> Disk

Tips:

1. Keep the frequently used documents and indexes in RAM. (working set)
2. Prefer solid state drives to hard disk drives.
3. historical data, data you don't use very often, hard disk drives are cheaper and may just work as well for this type of data.

Summary:

1. The nature of your data set and hardware define the need to model your data.
2. It is important to identify those exact constraints and their impact to create a better model.
3. As your software and the technological landscape change, your model should be re-evaluated and updated accordingly.

### Modeling Methodology

Schema:

-   Collections
-   Fields
-   Shapes

-   Queries
-   Indexes
-   Data Sizing
-   Operations
-   Assumptions

Phase 1:

-   Scenarios
-   Business Domain Expert
-   Production Logs & Stats
-   Data Modeling Expert

Workload:

-   data size: amount of data in a few months, years
-   quantify ops: reads and writes
-   qualify ops

Phase 2:

Relationships:

-   identify
-   quantify
-   embed or link related entities

if one-to-one, they should go into one table

embed documents, or keep them separate?

Phase 3:
Patterns:

-   recognize
-   apply the ones for needed optimizations

Remain flexible by only doing the steps needed

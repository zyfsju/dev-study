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

Great Expectations:[Github](https://github.com/great-expectations/great_expectations)

Pinot: [doc](https://docs.pinot.apache.org/)

mlflow: [Github](https://github.com/mlflow/mlflow)

React 101: [Code Academy](https://www.codecademy.com/learn/react-101)

ASAM OpenSCENARIO: [User Guide](https://www.asam.net/index.php?eID=dumpFile&t=f&f=3496&token=df4fdaf41a8463e585495001cc3db3298b57d426#_scenario_creation)

ASAM: [URL](https://www.asam.net/about-asam/)

Graph Database: [doc](https://neo4j.com/developer/graph-database/)

Coursera Big Data: [URL](https://www.coursera.org/lecture/big-data-integration-processing/overview-of-information-integration-m1WXR)

Leetcode Problems: [URL](https://github.com/CyC2018/CS-Notes/blob/master/notes/Leetcode%20%E9%A2%98%E8%A7%A3%20-%20%E6%90%9C%E7%B4%A2.md)

## CAN

(1) channel-bus: one-to-many
(2) bus-network node: one-to-one
(3) network node - message: many-to-many
(4) message-signal: one-to-many

=> (5) channel-network node: one-to-manyI wrote a little something to help me understand why sometimes one signal corresponds to multiple channels, and why we start from one distinguishing AEB signal to determine the channel. You might find it useful too.

For one signal, it belongs to one message. Three cases:
• If this message only comes from one network node, then it corresponds to one channel, due to (5).
• Even if this message comes from multiple network nodes, it still corresponds to one channel, as long as these network nodes connect to the same channel.
• Only in the case that the message comes from multiple network nodes connecting to different channels, will the message/signal correspond to multiple channels.

Therefore, a collection of unique signals/messages that can distinguish the network node/channel from others are required to determine the right channel.

## Questions

-   dense_rank in SQL
-   data cube vs data warehouse
-   dimensional tables vs transactional tables
-   database partitioning vs indexing

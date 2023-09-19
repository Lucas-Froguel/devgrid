# DevGrid API

This system was designed for the interview process of DevGrid. 

# How it was designed

I wanted to keep everything as simple and clean as possible. My idea was to use mongodb for everything,
as the problem naturally maps to a document-based application. There are
two collections in mongo:  
1. Users collection: stores all the unique ids that represent users and the datetime along with the cities they want data from.
2. Cities collection: stores all the data collected from cities. 
 
As more than on user might request the same city, our architecture also optimizes allowing city data to be shared. There
is a tag called `checked`, which is auto set to false and is only set to true when the async job has checked (i.e. 
gathered the data from the api) the given city. 

The async job is managed by cron for simplicity. As this is a small job, there is no need for more robust job-managing 
applications, like airflow, for now. The job simply reads the oldest 60 cities in the db that have not been checked and 
tries to get their data, stopping in the case of failure. If the script takes more than 60s seconds, we also kill it, 
because a new job will start and keep doing the job - this way we avoid duplications. 

# How to run

In order to run the application, you only need two commands:
```bash
make build
```
And also
```bash
make up
```

This will build and run the container, which will be access via the api in the localhost at port 8000. 

# How to test

Just run 
```bash
make test
```
after having build the application. 

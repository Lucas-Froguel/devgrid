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
because a new job will start and keep doing the job - this way we avoid duplications and fulfill the requirement of
60 requests per minute the api imposes to us.

# How to run

In order to run the application, you only need three commands. First,
```bash
cp .env.template .env
```
However, this still requires you to manually insert the values for the keys, which will lead to some odd behavior if not
set appropriately. In light of this, together with the link to this application, the actual `.env` used by me will
also be sent. In this case, you can skip the above command. 
Then
```bash
make build
```
And also
```bash
make up
```

This will build and run the container, which will be accessed via the api in the localhost at port 8000. 

# How to test

Just run 
```bash
make test
```
after having build the application. 

# The endpoints

The endpoints are located at `http://localhost:8000/api/v1/add_cities/` and `http://localhost:8000/api/v1/get_cities/`. For 
convenience, we add two working codes that use curl to make the requests. The first one contains the list of ids form the 
given pdf. 
```bash
curl --location 'http://localhost:8000/api/v1/add_cities/' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "devgrid",
    "cities": [
        3439525, 3439781, 3440645, 3442098, 3442778, 3443341, 3442233, 3440781,
        3441572, 3441575, 3443207, 3442546, 3441287, 3441242, 3441686, 3440639,
        3441354, 3442057, 3442585, 3442727, 3439705, 3441890, 3443411, 3440054,
        3441684, 3440711, 3440714, 3440696, 3441894, 3443173, 3441702, 3442007,
        3441665, 3440963, 3443413, 3440033, 3440034, 3440571, 3443025, 3441243,
        3440789, 3442568, 3443737, 3440771, 3440777, 3442597, 3442587, 3439749,
        3441358, 3442980, 3442750, 3443352, 3442051, 3441442, 3442398, 3442163,
        3443533, 3440942, 3442720, 3441273, 3442071, 3442105, 3442683, 3443030,
        3441011, 3440925, 3440021, 3441292, 3480823, 3440379, 3442106, 3439696,
        3440063, 3442231, 3442926, 3442050, 3440698, 3480819, 3442450, 3442584,
        3443632, 3441122, 3441475, 3440791, 3480818, 3439780, 3443861, 3440780,
        3442805, 7838849, 3440581, 3440830, 3443756, 3443758, 3443013, 3439590,
        3439598, 3439619, 3439622, 3439652, 3439659, 3439661, 3439725, 3439748,
        3439787, 3439831, 3439838, 3439902, 3440055, 3440076, 3440394, 3440400,
        3440541, 3440554, 3440577, 3440580, 3440596, 3440653, 3440654, 3440684,
        3440705, 3440747, 3440762, 3440879, 3440939, 3440985, 3441074, 3441114,
        3441377, 3441476, 3441481, 3441483, 3441577, 3441659, 3441674, 3441803,
        3441954, 3441988, 3442058, 3442138, 3442206, 3442221, 3442236, 3442238,
        3442299, 3442716, 3442766, 3442803, 3442939, 3443061, 3443183, 3443256,
        3443280, 3443289, 3443342, 3443356, 3443588, 3443631, 3443644, 3443697,
        3443909, 3443928, 3443952, 3480812, 3480820, 3480822, 3480825
    ]
}'
```
with expected response being:
```json
{
    "user_id": "devgrid",
    "cities": [
        "3439525",
        "3439781",
        ...
        "3480825"
    ],
    "_id": "6508ef1033d5a26b7328d18f"
}
```
And also
```bash
curl --location --request GET 'http://localhost:8000/api/v1/get_cities/' \
--header 'Content-Type: application/json' \
--data '{
    "user_id": "devgrid"
}'
```
with expected response
```json
{
    "percentage": "90.419",
    "user_id": "devgrid"
}
```

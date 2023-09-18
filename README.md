# DevGrid API

This system was designed for the interview process of DevGrid. 

# How it was designed

My idea was to use mongodb for everything, as the problem naturally maps to a document-based application. There are
three collections in mongo. 
1. Requests collection: stores all the incoming requests along with datetime. 
2. Users collection: stores all the unique ids that represent users along with the cities they want data from.
3. Cities collection: stores all the data collected from cities.
As more than on user might request the same city, our architecture also optimizes allowing city data to be shared. 
The first collection was added for redundancy, but was not necessary.  

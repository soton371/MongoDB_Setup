# MongoDB_Setup

1. install mongodb from docs.mongodb.com and download & install mongodb compass
2. create new project
3. install mongoengine (pip3 install mongoengine)
4. create model (collection name of db)
5. connect with db (from mongoengine import connect  connect(db="hrms", host="localhost", port=27017))
6. run (uvicorn main:app --reload)

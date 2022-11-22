from http import client
from multiprocessing import connection
import pymongo
 
from pymongo import MongoClient 
 
connection_url='mongodb://localhost:27017/'
 
client=MongoClient(connection_url)
 
o=1
while(o!=0):
    print("\n1.Create Database\n2.Insert Document\n3.Fetch Document\n4.Update Document\n5.Delete Document\n6.Drop Collection")
    ch=int(input("\nEnter your choice:"))
 
    if ch==1:
        #CREATE A NEW DB
        database_name="student_database"
        student_db=client[database_name]
 
        collection_name="computer science"
        collection=student_db[collection_name]
 
        print(client.list_database_names())
 
    if ch==2:
        #INSERT 
        document={"Name":"Apurva",
        "Roll No ":  153,
        "Branch ": "CSE"}
        collection.insert_one(document)
 
        documents=[{"Name":"Roshan","Roll No":159,"Branch":"CSE"},{"Name":"Rahim","Roll No":155,"Branch":"CSE"},{"Name":"Ronak","Roll No":156,"Branch":"CSE"}]
        collection.insert_many(documents)
 
        print(client.list_database_names())
 
    if ch==3:
        #RETRIEVE
        query={"Name":"Raj"}
        print(collection.find_one(query))
 
        query={"Branch":"CSE"}
        result=collection.find(query)
        for i in result:
            print(i)
 
    if ch==4:
        #UPDATE
        query={"Roll No":{"$eq":153}}
        # present_data=collection.find_one(query)
        # new_data={'$set':{"Name":'Ramesh'}}
        #collection.update_one(present_data,new_data)
 
        present_data={"Branch":"CSE"}
        new_data={"$set":{"Branch":"ECE"}}
        collection.update_many(present_data,new_data)
 
    if ch==5:
        #DELETE
        query={"Roll No":153}
        collection.delete_one(query)
 
        query={"Branch":"ECE"}
        collection.delete_many(query)
 
    if ch==6:
        #DROP 
        collection.drop()
    
    o=input("Do you want to continue? Press 1, Else 0\n")

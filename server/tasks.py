import sys
import os
import json
sys.path.append("..")
from server.user import users, AddUser , FileName

def AddTask():
    try:
        user_id = int(input("enter user id : "))
    except ValueError:
        print("just ID")
        return
    for user in users:
        if user["Id"] == user_id:
            title = input("Task Title : ")
            important = input("Task important (* OR **) : ")
            description = input("Task description : ")
            
            task_id = len(user["Tasks"]) + 1
            
            task ={
                "TaskId" : task_id,
                "Title" : title,
                "Important" : important,
                "Description" : description ,
                "Completed" : False , 
                
            }
            user["Tasks"].append(task)
            print("task added succesfully.")
            
            with open(FileName, "w", encoding="utf-8") as f:
                json.dump(users, f, ensure_ascii=False, indent=2) 
            return  
    print("I can not found tihs user")
AddTask()
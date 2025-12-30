import json
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FileName = os.path.join(BASE_DIR, "database", "user.json")

if os.path.exists(FileName):
    with open(FileName, "r", encoding="utf-8") as f:
        users = json.load(f)
else:
    users = []

def AddUser():
    name = input("Your name: ")

    current_id = int(len(users) + 1)

    user_info = {
        "Id": current_id,
        "Name": name,
        "Tasks" : []
    }

    users.append(user_info)

    with open(FileName, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)

    print("User added:", user_info)
if __name__ == "__main__":
    AddUser()

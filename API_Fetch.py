import requests
import json

def fetch_users():
    url="https://jsonplaceholder.typicode.com/users"
    response =requests.get(url)
    #Checking the status 
    print(f"Status Code: {response.status_code}")

    if response.status_code==200:
        #Json to python list
        data=response.json()
        print(f"Total Records: {len(data)}")
        return data
    else:
        print(f"Error: {response.text}")
        return []

users=fetch_users()

#Saving the raw data
if users:
    with open("users_raw.json","w") as f:
        json.dump(users,f,indent=2)
    print("Saved raw file --> users_raw.json")

#See one record
print(users[0])
import requests
import json
def return_users():
    url = "http://127.0.0.1:5000/users"
    headers={
        "Content-Type": "application/json",
        "Accept": "application/json",
        "User-Agent":"Python-Requests-Client"
    }
    try:
        response=requests.get(url,headers=headers,timeout=5)
        response.raise_for_status()
        users=response.json()
        extract_data=[]
        for user in users:
            extract_data.append({
                "id":user["id"],
                "name":user["name"]
            })
        with open("users.json", "w",encoding='utf-8') as file:
            json.dump(extract_data, file, indent=4)
        print("Data dumped successfully into users.json")
    except requests.exceptions.HTTPError as http_err:
        print("HTTP error occurred",{http_err})
    except requests.exceptions.ConnectionError:
        print("Unable to connect to API")
    except requests.exceptions.Timeout:
        print("Timeout occurred")
    except requests.exceptions.RequestException as err:
        print("Unexpected error occurred",{err})
if __name__=="__main__":
    return_users()
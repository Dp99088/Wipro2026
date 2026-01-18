import json

data={
    "name":"Durga",
    "Age":23,
    "Skills":["Python","SQL"]
}

with open("data.json","w") as file:
    json.dump(data,file,indent=4)
import json
 
with open("mbappe-api.json", mode="r") as j_object:
   data = json.load(j_object)
   print(data)

import json

json_str =  '{"name" : "Piyush", "isTeacher" : null}'
py_obj = json.loads(json_str)  #load from string(loads) 
print(type(py_obj), py_obj)

py_obj = { #loads and dumps
    "name" : "Piyush",
    "isTeacher" : True,
    "Age" : 19
}
json_str = json.dumps(py_obj)    #dump to string(dumps)
print(type(json_str), json_str)

#load and dump for files
with open("data.json", "r") as f:
    py_obj = json.load(f)
    print(type(py_obj))

data = {
    "name" : "Piyush",
    "isTeacher" : True,
    "Age" : 19
}  

with open("data.json", "w") as f:
    json.dump(data, f, indent=4, sort_keys=True)
import json

# converting json string to python
some_syntax = '{ "name":"John", "age":30, "city":"New York" }'
dict = json.loads(some_syntax) # parsed a stroke to extract info

print(dict["age"])

#convert python to json
some_sode = {
    "name":"John", 
    "age": 30,
    "city":"New York"
}
get_json = json.dumps(some_sode, indent = 2, separators = (". ", "="), sort_keys=True)
print(get_json)
print(json.dumps(["some", "list", "elements"])) # gives array
print(json.dumps(42)) # gives number
print(json.dumps(True)) # gives true
print(json.dumps(65.123)) # gives number 
print(json.dumps(None)) # gives null


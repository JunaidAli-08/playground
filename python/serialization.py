import json
data=[4,8]
print(type(data))

json_string=(json.dumps(data))

print(type(json_string))

json_list=json.loads(json_string)
print(type(json_list))


import  yaml

yaml_data = open('inventory.yaml', 'r')

data = yaml.safe_load(yaml_data)

print(type(data))

print(data)

import json

json_data = json.dumps(data,indent=4)

print(json_data)
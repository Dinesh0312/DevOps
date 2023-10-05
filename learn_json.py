facts = {
         "inventory": {
             "device": [
                {
                     "name": "csr1kv1",
                     "version": "16.09",
                     "vendor": "cisco",
                     "uptime": "2 days",
                     "serial": "XB96861",
                     "snmp": [
                        {"name": "public", "permission": "ro"},
                        {"name": "private", "permission": "rw"}
                    ]
                }
            ]
        }
    }

print(type(facts))
print(facts['inventory']['device'][0]['uptime'])

import  json

print(json.dumps(facts))

facts_str = json.dumps(facts)

print(type(facts_str))

print(json.dumps(facts, indent=4))

#====================================================

vlan_ids = '{"name":"HR", "id": 100}'
interfaces = '["GigabitEthernet1", "GigabitEthernet2", "GigabitEthernet3", "GigabitEthernet4"]'

print(type(vlan_ids))
print(type(interfaces))

# print(vlan_ids['id'])

vlans_nums = json.loads(vlan_ids)
interface_names = json.loads(interfaces)

print(type(vlans_nums))
print(type(interface_names))

print(vlans_nums['id'])
print(interface_names[0])
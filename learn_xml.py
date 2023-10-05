
# import xml.etree.ElementTree as ET

# tree = ET.parse('inventory.xml')

# root_data = tree.getroot()

# print(root_data.tag)



# for child in root_data:
#     print(child.tag, child.attrib)

# for serial in root_data.iter('{https://www.cisco.com/ns/routers/prod}serial'):
#     print(serial.text)

# for device in root_data.findall('{https://www.cisco.com/ns/routers/prod}device'):
#      name= device.attrib['name']
#      serial= device.find('{https://www.cisco.com/ns/routers/prod}serial').text
#      print(name, serial)

# for snmp in root_data.iter('{https://www.cisco.com/ns/routers/dev}snmp'):
#     print(snmp.attrib)


#########Convert XML to JSON
import  sys
import  json
import  xmltodict

with open('inventory.xml') as xml_file:
    xml = xmltodict.parse(xml_file.read())

print(json.dumps(xml, indent=4))

#.replace("@", "") instructs to replace @ with nothing
print(json.dumps(xml, indent=4).replace("@", ""))

#second option: need to supply an extra argument to the xmltodict parse
with open('inventory.xml') as xml_file:
    xml = xmltodict.parse(xml_file.read(), attr_prefix='')

#If json.dumps is used again, no @ symbols will be seen:

print(json.dumps(xml, indent=4))
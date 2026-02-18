import json

with open('sample-data.json', 'r') as file:
    data = json.load(file)

print(f"{'DN':50} {'Description':18} {"Speed":7} {"MTU":5}")
print("-"*83)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]

    dn = attrs.get("dn", "")
    description = ""
    speed = attrs.get("speed", "")
    mtu = attrs.get("mtu", "")

    print(f"{dn:50} {description:18} {speed:7} {mtu:5}")
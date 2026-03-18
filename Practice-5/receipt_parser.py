import re
import json

with open("raw.txt", "r", encoding="utf-8") as file:
    text = file.read()

prices = re.findall(r".\sx\s(\d{1,3}(?: \d{3})*,\d{2})", text)


names = re.findall(r"[1-9]+\.\s*\n(.+)", text)


costs = re.findall(r"Стоимость\s*\n(.+)", text)
for i in range(len(costs)):
    costs[i] = re.sub(",00", "", costs[i])
    costs[i] = re.sub(" ", "", costs[i])
new_costs = list(map(int, costs))
total = 0
for cost in new_costs:
    total += cost

date_time = re.search(r"Время:\s*(\d{2}\.\d{2}\.\d{4})\s*(\d{2}:\d{2}:\d{2})", text)
date = date_time.group(1)
time = date_time.group(2)


payment = re.search(r"(Банковская карта|Наличные)", text).group(1)


data = []

for i in range(len(names)):
    item = {
        "name": names[i],
        "price": prices[i]
    }
    data.append(item)

receipt = {
    "item": data,
    "total": total,
    "date": date,
    "time": time,
    "payment" : payment
}

print(json.dumps(receipt, indent = 2,ensure_ascii = False))



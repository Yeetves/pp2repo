import re


file = open("raw_gpt.txt", "r", encoding="utf-8")
txt = file.read()
file.close()

first_task = re.findall(r"ab*", txt)
print(first_task)

second_task = re.findall(r"ab{2,3}", txt)
print(second_task)

third_task = re.findall(r"[a-z]+_[a-z]+", txt)
print(third_task)

fourth_task = re.findall(r"[A-Z][a-z]+", txt)
print(fourth_task)

fifth_task = re.findall(r"a.*?b", txt)
print(fifth_task)

sixth_task = re.sub(r"[,\.\s]", ":", txt)
print(sixth_task)

seventh_task = re.sub(r"_([a-z])", lambda m : m.group(1).upper(), txt)
print(seventh_task)

eighth_task = re.split(r"(?=[A-Z])", txt)
print(eighth_task)

ninth_task = re.sub(r"([A-Z])", r" \1", txt)
print(ninth_task)

tenth_task = re.sub(r"([a-z])([A-Z])", r"\1_\2", txt)
print(tenth_task)
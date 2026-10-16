"""[LEARNING LOGS] CuteCat CuteFox"""
import ast

n = int(input())
cats = {}
foxes = {}

for _ in range(n):
    data = ast.literal_eval(input())

    for name, code in data.items():
        if code.startswith("Cat"):
            cats[code] = name
        elif code.startswith("Fox"):
            foxes[code] = name

all_names = set(cats.values()) | set(foxes.values())

if "Cat01" not in cats and "Garfield" not in all_names:
    cats["Cat01"] = "Garfield"

if "Fox01" not in foxes and "Fubuki" not in all_names:
    foxes["Fox01"] = "Fubuki"

print(f"Cat : {len(cats)}")
print(f"Fox : {len(foxes)}")

for code in sorted(cats, key=lambda x: int(x[3:])):
    print(f"{cats[code]} : {code}")

for code in sorted(foxes, key=lambda x: int(x[3:])):
    print(f"{foxes[code]} : {code}")

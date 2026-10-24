"""[LEARNING LOGS] Impostor"""
import ast

players = {}

while True:
    data = input()

    if data == "Start":
        break

    players.update(ast.literal_eval(data))

dead = {}

while True:
    name = input()

    if name == "End":
        break

    if name in players:
        dead[name] = players.pop(name)

impostor_count = 0

for role in players.values():
    if role == "Impostor":
        impostor_count += 1

print(impostor_count, "Impostor Remains")

print("***Alive***")
for name, role in sorted(players.items()):
    print(f"{name} : {role}")

print("***Dead***")
for name, role in sorted(dead.items()):
    print(f"{name} : {role}")

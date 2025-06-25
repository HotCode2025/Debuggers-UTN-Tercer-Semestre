# Palabra reservada continue
for i in range(6):
    if i % 2 == 0:
        print(f"valor: {i}")

for i in range(6):
    if i % 2 != 0:
        continue
    print(f"valor: {i}")
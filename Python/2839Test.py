receive_kg = int(input())

if receive_kg % 5 == 0:
    print(receive_kg // 5)
    quit()

for i in range(receive_kg//5, 0, -1):
    remainder = receive_kg - (i * 5)
    if remainder % 3 == 0:
        print(f"{i + (remainder//3)}")
        quit()

if receive_kg % 3 == 0:
    print(receive_kg // 3)
    quit()

print("-1")

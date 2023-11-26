name = input("Enter your name:")
with open("name.txt", "w") as file:
    file.write(name)

with open("name.txt", "r") as file:
    name = file.read().strip()
print(f"Your name is {name}")

with open("number.txt", "r") as file:
    num1 = int(file.readline().strip())
    num2 = int(file.readline().strip())
print(num1 + num2)

total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())
print(total)

with open(r"C:\Users\KN Tech\Desktop\example.txt") as file:
    contents = file.read()
print(contents)
file.close()

with open("C:/Users/KN Tech/Desktop/example.txt") as file:
    contents = file.read()
print(contents)
file.close()

with open("../../pineng.txt") as file:
    contents = file.read()
print(contents)
file.close()


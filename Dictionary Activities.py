# ========== Dictionary Activities ==========
print("=" * 50)
print("Dictionary Activities")
print("=" * 50)

# Activity 1: Fill in the Blanks
print("\n🔹 Activity 1: Fill in the Blanks")
student = {
   "name": "Ana",
   "age": 20,
   "course": "IT"
}
print(student["name"])

# Activity 2: Add and Update
print("\n🔹 Activity 2: Add and Update")
student = {"name": "Ana", "age": 20}
student["grade"] = 95
student["age"] = 21   
print(student)

# Activity 3: Loop Through Dictionary
print("\n🔹 Activity 3: Loop Through Dictionary")
car = {"brand": "Toyota", "model": "Corolla", "year": 2020}
for key, value in car.items():
    print(f"{key} : {value}")

# Activity 4: Mini Phonebook
print("\n🔹 Activity 4: Mini Phonebook")
phonebook = {
    "Nicole": "09480673164",
    "Mico": "09943317430",
    "Marjorie": "09604169002"
}

name = input("Enter a name: ")

if name in phonebook:
    print(f"{name} number: {phonebook[name]}")
else:
    print(f"Sorry, {name} is not in the phonebook.")
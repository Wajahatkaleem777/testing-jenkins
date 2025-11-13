# ------------------------------
# 1️⃣ Comments and Description
# ------------------------------
# This Python program prints a message, does some math,
# takes user input, and defines a function.

# ------------------------------
# 2️⃣ Variables and Printing
# ------------------------------
name = "Wajahat"
age = 25

print("Hello,", name)
print("You are", age, "years old.")

# ------------------------------
# 3️⃣ Conditional Statements
# ------------------------------
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ------------------------------
# 4️⃣ Loops
# ------------------------------
print("\nCounting from 1 to 5:")
for i in range(1, 6):
    print(i)

# ------------------------------
# 5️⃣ Functions
# ------------------------------
def greet(person):
    """This function greets a person by name."""
    print(f"Welcome, {person}!")

greet(name)

# ------------------------------
# 7️⃣ Using Lists
# ------------------------------
fruits = ["apple", "banana", "mango"]
print("\nFruits list:", fruits)
for fruit in fruits:
    print(f"I like {fruit}!")

# ------------------------------
# End of Program
# ------------------------------
print("\nProgram finished successfully ✅")

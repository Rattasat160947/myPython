name = "Rattasat"
age = 22
height = 174.5
is_student = True

print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


score = int(input("Enter score: "))

if score >= 80:
    print("A")
elif score >= 70:
    print("B")
elif score >= 60:
    print("C")
else:
    print("F")
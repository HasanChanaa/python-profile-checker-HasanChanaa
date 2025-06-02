name = input("Enter your name: ")
age = int(input("Enter your age: "))
GPA = float(input("Enter your GPA (0 - 5): "))
field = input("Enter your field of interst: ")
graduated = input("Did you graduate? (yes/no): ")

print("Name              : " + name )
print("Age               : " + str(age))
print("GPA               : " + str(GPA))
print("Field of Interest : " + field)
print("Graduated         : " +'Yes' if graduated == 'yes' else 'No')

if GPA >= 3.5 and age < 25 and graduated == "yes":
    print("You are eligible for a scholarship!")
elif age < 30 and GPA >= 2.5:
    print("You are eligible for an internship!")
else:
    print("You are not eligible for neither a scholarship nor an internship. Please apply again later.")
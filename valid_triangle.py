a = int(input("Enter 1st angle of a triangle ABC: "))
b = int(input("Enter 2nd angle of the triangle ABC: "))
c = int(input("Enter 3rd angle of the triangle ABC: "))

ABC = a+b+c
if (ABC == 180):
    print("The Triangle ABC is Valid")
else:
    print("The Triangle ABC is InValid")
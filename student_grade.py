sub1 = float(input("Enter Marks for 1st Subject: "))
sub2 = float(input("Enter Marks for 2nd Subject: "))
sub3 = float(input("Enter Marks for 3rd Subject: "))
sub4 = float(input("Enter Marks for 4th Subject: "))
sub5 = float(input("Enter Marks for 5th Subject: "))

percentage = ((sub1 + sub2 + sub3 + sub4 + sub5)/500)*100
if(percentage >= 60):
    print(f'The percentage is: {percentage} 1st Division')
elif(percentage >= 50 and percentage <=59):
    print(f'The percentage is: {percentage} 2nd Division')
elif(percentage >= 40 and percentage <=49):
    print(f'The percentage is: {percentage} 3rd Division')
elif(percentage <40):
    print(f'The percentage is: {percentage} FAIL')
userWieght:float = float(input("Enter Your Wieght (kg):"))
userHeight:float = float(input("Enter Your Height (Meter):"))

bmi:float = userWieght / (userHeight ** 2 )

print(bmi)
if bmi < 18.5:
    print("You are underweight. Watch your health.")
elif bmi < 24.9:
    print("You are fit & healthy.")
else: 
    print("You are overweight, you need to work out more and watch your diet.")
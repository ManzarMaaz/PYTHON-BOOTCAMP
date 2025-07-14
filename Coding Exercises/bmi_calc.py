weight = float(input("Enter your Weight in KGs : ")
height = float(input('Enter your Height in Meters : ')

bmi = weight / (height ** 2)

if bmi < 18.5 :
    print("You're underweight")

elif 18.5 <= bmi < 25:
    print("You're normal weight")

elif bmi >= 25:
    print("You're overweight")

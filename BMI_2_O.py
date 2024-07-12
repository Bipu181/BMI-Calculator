
height=float(input("What is you Height In metrs?\n"))
weight=float(input("What is you Weight In Kilograms?\n"))
bmi=weight/(height**2)
if(bmi<18.5):
    print(f"Your BMI is {round(bmi)}, you are underweight.")
elif(bmi>=18.5 and bmi <25):
    print(f"Your BMI is {round(bmi)}, you have a normal weight.")
elif(bmi>=25 and bmi <30):
    print(f"Your BMI is {round(bmi)}, you are slightly overweight.")
elif(bmi>=30 and bmi <35):
    print(f"Your BMI is {round(bmi)}, you are obese.")
else:
    print(f"Your BMI is {round(bmi)}, you are clinically obese.")
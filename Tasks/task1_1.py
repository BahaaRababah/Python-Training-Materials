Name=input("Enter your name: ")
Age=int(input("Enter your age: "))
Weight=float(input("Enter your weight (kg): "))
Employment_Status=input("Are you employed? (Y/n): ")
employed = (Employment_Status.strip().upper()== "Y")
height=1.75
bmi=Weight/(height**2)

print(f"Name{Name}")
print(f"Age{Age}")
print(f"Weight: {Weight} kg")
print(f"Employed: {employed}")
print(f"Height: {height} m")
print(f"BMI: {bmi:.2f}")
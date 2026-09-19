try: 
  numerator=float(input("Enter a numerator: "))
  denominator=float(input("Enter a denominator: "))
  result=numerator/denominator

except ValueError:
  print("Error: Please enter numbers only.")

except ZeroDivisionError:
  print("Error: Cannot divide by zero.")

else:
  print(f"Success! The result is {result}")

finally:
  print("Calculation attempt complete.")
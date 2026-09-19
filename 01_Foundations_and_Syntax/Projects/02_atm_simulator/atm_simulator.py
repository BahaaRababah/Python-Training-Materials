x = 200.0
atm = True

while atm:
    print(f"\nCurrent balance: ${x}")

    y = float(input("Enter withdrawal amount: $"))

    if y > 0 and y <= x:
        x -= y

        print(f"Dispensed: ${y}")
        print(f"New balance: ${x}")

    elif y > x:
        print(f"Error: Insufficient funds. Maximum available: ${x}")

    else:
        print("Error: Withdrawal amount must be strictly greater than zero.")

    if x == 0.0:
        print("Account empty. Thank you for using the ATM!")
        atm = False
        break
x=5
co=True

while co:
    name =input("Enter your name : ")
    n_t=int(input("Enter hoe number tekets : "))

    if n_t>0 and n_t<=x:
        x-=n_t
        print(f"Success! {name} bought {n_t} tickets.")
    elif n_t>x:
        print(f"soory!{name}")
    else:
        print("Invalid input.")
    if x == 0:
        print("Sold out!")
        co = False
        break
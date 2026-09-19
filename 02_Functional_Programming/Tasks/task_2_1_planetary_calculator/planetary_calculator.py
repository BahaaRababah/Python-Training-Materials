def calculate_weight(m,p="Earth"):

    if p=="Earth":
      gra=9.8

    elif p=="Mars":
       gra=3.71
    
    elif p=="Jupiter":
       gra=24.79

    return  m * gra



print(calculate_weight(100))
print(calculate_weight(100,"Mars"))
print(calculate_weight(100,"Jupiter"))


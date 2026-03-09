a = float(input("Enter temp: "))  # Use float for flexibility in input
b = input("Enter degrees (k, c or f): ").lower()

if b == "c":
    # Celsius to Kelvin and Fahrenheit
    k = a + 273.15
    f = (a * 9/5) + 32
    print(f"Temperature in Kelvin: {k:.2f}")
    print(f"Temperature in Fahrenheit: {f:.2f}")
    
elif b == "k":
    # Kelvin to Celsius and Fahrenheit
    c = a - 273.1565
    f = (c * 9/5) + 32
    print(f"Temperature in Celsius: {c:.2f}")
    print(f"Temperature in Fahrenheit: {f:.2f}")
    
elif b == "f":
    # Fahrenheit to Celsius and Kelvin
    c = (a - 32) * 5/9
    k = c + 273.15
    print(f"Temperature in Celsius: {c:.2f}")
    print(f"Temperature in Kelvin: {k:.2f}")
    
else:
    print("Invalid input. Please enter 'c' for Celsius, 'k' for Kelvin, or 'f' for Fahrenheit.")

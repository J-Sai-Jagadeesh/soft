def function(number):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"

n = int(input("Enter The Number:"))
result = function(n)
print(f"The number {n} is {result}")

def safe_divide(a,b):
    try:
        result = a/b;
        return result

    except ZeroDivisionError:
        print("Cannot divide by zero")
        return None

    except TypeError:
        print("Invalid data type.Input Number only")
        return None

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

output = safe_divide(num1,num2)

print(output)

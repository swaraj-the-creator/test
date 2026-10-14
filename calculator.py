try:
    num1 = float(input("Enter a decimal number: "))
    num2 = float(input("Enter a decimal number: "))
    def add(num,num3):
        num = num1
        num3 = num2
        total = num + num3
        return total
    def subtract(num8,num9):
            num8 = num1
            num9 = num2
            total1 = num8 - num9
            return total1
    def divide(num7,num6):
            num7 = num1
            num6 = num2
            total2 = num7 / num6
            return total2
    def multiplication(num5,num4):
            num5 = num1
            num4 = num2
            total3 = num5 * num4
            return total3
    ad = add(num1,num2)
    sub = subtract(num1,num2)
    div = divide(num1,num2)
    mul = multiplication(num1,num2)
    print("\nSum of ",num1," and ",num2," is ",ad)
    print(f"Subtracted value of {num1} and {num2} is {sub}")
    print(f"Product of {num1} and {num2} is {mul}")
    print(f"Remainder of {num1} and {num2} is {div}")

except ValueError:
      print("You need to enter values in decimal numbers")
except ZeroDivisionError:
      print("Any of the number can't be zero")

try:
    num = int(input("Enter your numerator"))
    den = int(input("Enter your denominator"))
    result = num/den
except ZeroDivisionError:
    print("Denominator cannot be zero")
except ValueError:
    print("Invalid input ")
else:
    print("Result:",result)
finally:
    print("All Operation have been completed")
    
inchLength = 0
cmLength = 0

inchLength = float(input("Enter length in inches (negative value to quit): "))

while inchLength >= 0:
    cmLength = inchLength * 2.54
    print(f"{inchLength:.1f} inches is {cmLength:.2f} centimeters")
    inchLength = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")
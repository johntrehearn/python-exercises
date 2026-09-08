numberEntered = input("Enter a number: ")
numberList = []

while numberEntered != "":
    numberList.append(int(numberEntered))
    numberEntered = input("Enter a number: ")

numberList.sort(reverse=True)

print("The greatest numbers in descending order:")
for number in numberList[:5]:
    print(f"{number:.1f}")   
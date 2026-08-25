zander = float(input("Enter the length of the zander in centimeters: "))

difference = 42 - zander

if zander < 42:
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {difference:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")

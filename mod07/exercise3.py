gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

def gallons_to_liters(gallons):
    while gallons >= 0:
        print(f"{gallons} American gallons is {gallons * 3.785:.2f} liters.")
        gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    else:
        print("Program finished.")

gallons_to_liters(gallons)

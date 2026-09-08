diameterPizza1 = float(input("Enter the diameter of the first pizza (cm): "))
pricePizza1 = float(input("Enter the price of the first pizza (euros): "))

diameterPizza2 = float(input("Enter the diameter of the second pizza (cm): "))
pricePizza2 = float(input("Enter the price of the second pizza (euros): "))

def calculate_unit_price(diameter, price):
    diameter = diameter / 100
    radius = diameter / 2
    area = 3.1416 * (radius ** 2)
    unitPrice = price / area
    return unitPrice

unitPricePizza1 = (calculate_unit_price(diameterPizza1, pricePizza1))
unitPricePizza2 = calculate_unit_price(diameterPizza2, pricePizza2)

print(f"Unit price of the first pizza: {unitPricePizza1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unitPricePizza2:.2f} euros/m²")

if unitPricePizza1 < unitPricePizza2:
    print("The first pizza provides better value for money. ")
else:
    print("The second pizza provides better value for money. ")
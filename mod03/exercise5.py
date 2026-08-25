talents = float(input("Enter talents: "))
pounds = float(input("Enter pounds: "))
lots = float(input("Enter lots: "))

talentsToPounds = talents * 20
talentsToLots = talentsToPounds * 32
talentsToGrams = talentsToLots * 13.3

poundsToLots = pounds * 32
poundsToGrams = poundsToLots *13.3
lotsToGrams = lots * 13.3

total_grams = talentsToGrams + poundsToGrams + lotsToGrams

kilograms = int(total_grams // 1000)
remaining_grams = total_grams % 1000

print("The weight in modern units:")
print(f"{kilograms} kilograms and {remaining_grams:.2f} grams.")
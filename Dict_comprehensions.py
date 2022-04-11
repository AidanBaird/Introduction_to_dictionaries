drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {drink:caff for drink, caff in zip(drinks, caffeine)}

#zipped_drinks = {drink:caff for drink, caff in zip(drinks, caffeine)}

print(zipped_drinks)
print("")
print(drinks_to_caffeine)
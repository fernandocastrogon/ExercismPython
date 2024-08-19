def convert(number):
    rainDrop = ""
    if number % 3 == 0:
        rainDrop = rainDrop + "Pling"
    if number % 5 == 0:
        rainDrop = rainDrop + "Plang"
    if number % 7 == 0:
        rainDrop = rainDrop + "Plong"

    if not rainDrop:
        return str(number)
    else:
        return rainDrop


from pyscript import document

non_metals = {
    "H": ["Hydrogen", 1, 1.008],
    "C": ["Carbon", 6, 12.011],
    "N": ["Nitrogen", 7, 14.007],
    "O": ["Oxygen", 8, 15.999],
    "P": ["Phosphorus", 15, 30.974],
    "S": ["Sulfur", 16, 32.06],
    "F": ["Fluorine", 9, 18.998],
    "Cl": ["Chlorine", 17, 35.45],
    "Br": ["Bromine", 35, 79.904],
    "I": ["Iodine", 53, 126.90],
    "He": ["Helium", 2, 4.003],
    "Kr": ["Krypton", 36, 83.798],
    "Rn": ["Radon", 86, 222]
}


def search_element(event):
    symbol = document.getElementById("symbol").value.strip().capitalize()

    if symbol in non_metals:
        element = non_metals[symbol]

        document.getElementById("result").innerText = "Element Found!"

        document.getElementById("information").innerHTML = (
            "Element Symbol: " + symbol + "<br>" +
            "Element Name: " + element[0] + "<br>" +
            "Atomic Number: " + str(element[1]) + "<br>" +
            "Atomic Mass: " + str(element[2])
        )

    else:
        document.getElementById("result").innerText = "Element Not Found!"

        document.getElementById("information").innerText = (
            "The element does not exist in the non-metals list."
        )
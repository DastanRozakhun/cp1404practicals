"""
Hex Colours
Estimate: 15 minutes
Actual:   20 minutes
"""

COLOUR_CODES = {
    "Aliceblue": "#f0f8ff", 
    "Antiquewhite": "#faebd7", 
    "Aqua": "#00ffff", 
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff", 
    "Beige": "#f5f5dc", 
    "Bisque": "#ffe4c4", 
    "Black": "#000000",
    "Blanchedalmond": "#ffebcd", 
    "Blue": "#0000ff"
    }

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"The hex code for {colour_name} is {COLOUR_CODES[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()

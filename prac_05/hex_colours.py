"""
Doa Roys
CP1404 Practicals week 5

"""


COLOR_NAME_TO_CODE = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                     "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378", "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4": "#458b74", "azure1": "#f0ffff"}
print(COLOR_NAME_TO_CODE)

color_name = input("Enter a color name from above:")
while color_name != "":
    if color_name in COLOR_NAME_TO_CODE:
        print(COLOR_NAME_TO_CODE[color_name])
    else:
        print("Choose color name from the given option.")
    color_name = input("Enter a color name:")
print("Thank You")
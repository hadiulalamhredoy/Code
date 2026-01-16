sentence = "Tasfin  is  a  good  boy."   # there are double spaces

if "  " in sentence:          # check if "  " (two spaces) is inside sentence
    print("Double space found!")
    print("Position:", sentence.find("  "))   # tells where the first one starts
else:
    print("No double space found")

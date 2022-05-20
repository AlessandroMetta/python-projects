import sys

states = {
"Oregon" : "OR",
"Alabama" : "AL",
"New Jersey": "NJ",
"Colorado" : "CO"
}
capital_cities = {
"OR": "Salem",
"AL": "Montgomery",
"NJ": "Trenton",
"CO": "Denver"
}

if len(sys.argv) == 2:
    for elem in capital_cities.items():
        if elem[1] != sys.argv[1]:
            continue
        for element in states.items():
            if element[1] != elem[0]:
                continue
            print(element[0])
            break
        break

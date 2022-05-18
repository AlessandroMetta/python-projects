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

if len(sys.argv) != 2:
	exit(0)

try:
	print(capital_cities[states[sys.argv[1]]])
except KeyError:
        sys.exit("Unkown state.")

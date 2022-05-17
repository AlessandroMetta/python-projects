import sys

try:
	print(int(sys.argv[1]) * 3600 + int(sys.argv[2]) * 60 + int(sys.argv[3]))
except ValueError:
        sys.exit("All arguments must be integers. Exit.")
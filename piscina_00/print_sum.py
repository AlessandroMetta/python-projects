import sys

sum = 0
for i in sys.argv[1:]:
	try:
		sum += int(i)
	except ValueError:
 	       sys.exit("All arguments must be integers. Exit.")

print(sum)
import os, sys
# Scans js files in list of files for keyword. eg // to find comments
print("\t\t------JS Scanner------")

if len(sys.argv) < 2:
	print("Usage: python3 " + sys.argv[0] + " file keyword")
	sys.exit()

location = sys.argv[1]
keyword = sys.argv[2]

print("\nfile to search: " + location)
print("Looking for: " + keyword)
file = open(location, "r")

for line in file:
	if ".js" in line:
		print("\n\n--------------------------------------" + line + "\n\n")
		
		os.system("curl " + line[:-1] + " | grep -e " + "'" + keyword + "'")
		continue
	else:
		continue
sys.exit()

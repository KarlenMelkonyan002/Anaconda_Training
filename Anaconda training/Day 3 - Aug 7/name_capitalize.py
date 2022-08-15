file_1 = open("p022_names.txt", "r")
file_2 = open("result.txt", "w")
lines = file_1.readlines()

for line in lines:
    new = line.title()
    file_2.write(new)
file_1.close()
file_2.close()

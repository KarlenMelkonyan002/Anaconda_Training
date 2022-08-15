file = open("test.txt", "r")
file_ = open("test1.txt", "w")
lines = file.readlines()

for line in lines:
    new = line.title()
    print(new)
    file_.write(new)
file.close()
file_.close()

file = open("test.txt", "r")
lines = file.readlines()
sum_ = 0

for line in lines:
    for c in line:
        if c.isdigit():
            sum_ = sum_ + int(c)
print(sum_)

file.close()

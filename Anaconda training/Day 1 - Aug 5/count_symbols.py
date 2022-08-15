file = open("test.txt", "r")

# read the content of file and replace spaces with nothing
data = file.read().replace(" ", "")

# get the length of the data
number_of_characters = len(data) - 2

print('Number of characters in text file :', number_of_characters)

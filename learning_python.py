myfile = "learning_python.txt"

with open(myfile) as file_object:
    lines = file_object.readlines()

words = ''
for line in lines:
    words += line.rstrip() + " "
    
print(words.replace('python', 'ruby'))



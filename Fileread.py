file = open("file_aide.txt", "rt")
data = file.read()
words = data.split()

print('Number of words in text file :', len(words))     

#output
Number of words in text file : 15

# open both files
with open('file_aide.txt','r') as firstfile, open('second.txt','a') as secondfile:
	
	# read content from first file
	for line in firstfile:
			
			# append content to second file
			secondfile.write(line)

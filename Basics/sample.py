
fd = open("file.txt","r")
content = fd.read()
print(content)

#For writing in the files
fd = open("file.txt","w")
new_content = "This is the edited text message"
fd.write(new_content)
fd = open("file.txt","r")
fd.seek(4,0) # Reading from certain cursor location
content=fd.read()
print(content)
fd.close()

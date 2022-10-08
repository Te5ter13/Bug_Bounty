import string
fd = open("/home/tester13/Hacking_tools/Wordlists/passwords/unix_passwords.txt","r")
wordlist=fd.read()
fd.close()
word_list=list(wordlist.split('\n'))
#print(word_list)

numbers = string.printable[0:10]
upper_case = string.printable[36:62]
lower_case= string.printable[10:36]
special_symbols = string.printable[62::]


for i in word_list:
    numbers_yes = False
    upper_case_yes= False
    lower_case_yes = False
    special_symbols_yes=False
    #print(i)
    for j in upper_case:
        if j in i:
           upper_case_yes = True
    for j in numbers:
        if j in i:
            numbers_yes = True
    for j in special_symbols:
        if j in i:
            special_symbols_yes = True
    if upper_case_yes == True and numbers_yes == True and special_symbols_yes == True:
        print("Valid Password is: {}".format(i))
        

 

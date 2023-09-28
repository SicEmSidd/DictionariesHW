#define variables

infile = open("sometext.txt")
reader = infile.read()
counter = 0
lentext = len(reader)
print(lentext)
localvar = ""
worddict = {}

while counter != lentext:
    if reader[counter].isalpha():
        #it would mess up the word count if we discriminated based on upper and lower case... let's change that
        currentletter = reader[counter].lower()
        localvar += currentletter
    #make sure we have a real letter first
    if not reader[counter].isalpha():
        #if there is a space, that means there is another word after it.
        if reader[counter] == " " and localvar != "":
            #if the word is in the dictionary, it should just append the value by 1
            if localvar in worddict:
                worddict[localvar] += 1
            #if the word is not in the dictionary, it should be defined
            if localvar not in worddict:
                worddict[localvar] = 1
            localvar = ""
        else:
            pass
    counter += 1
#this is to catch the last word because it would not have a space after it.
if localvar not in worddict:
    worddict[localvar] = 1
else:  
    worddict[localvar] += 1
print(worddict)

for k, v in worddict.items():
    print(f"Word: {k}\nNumber of times displayed: {v}\n")

infile.close()
import random
#we will use random to create a key for the encryption. I have no idea if this is easier or harder than inputting
#key values manually, or if it is more secure, but it seems cool to me, so I am doing it.

#initialize variables
infile = open("info_security.txt", "r")
reader = infile.read()
outfile = open("encrypted.txt", "w")
securitykey = {}

Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,:"
Alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz .,:!@#$%^&*()'/`~"

for i in Alphabet:
    randomvar = random.randint(0, len(Alphabet2)-1)
    randomletter = Alphabet2[randomvar]
    securitykey[i] = randomletter
    Alphabet2 = Alphabet2.replace(randomletter, "")

# print(Alphabet)
# print(Alphabet2)

# print(f"The following is the security key: {securitykey}")

printvar = ""
counter = 0

for i in range(0, len(reader)):
    printvar += securitykey[reader[i]]
outfile.write(printvar)

print("The following is the description of the key.")
for k, v in securitykey.items():
    print(f"{k} corresponds to {v}")

infile.close()
outfile.close()




# for k, v in securitykey:
#     print(k,v)
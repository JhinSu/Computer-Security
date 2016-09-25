#Polly want a cracker?
import hashlib
import binascii
import codecs

# It doesn't seem like the AsheleyMadison file had anything encrypted...
# According to the header: recid, id, username, userpassword, ...
# I guess I'll just make the script take the UID/PW
def bcrypt():
    for line in AshleyMadison:
        list = line.split(",")
        AshleyMadisonPlain.write(list[2] + ", " + list[3] + "\n")
	
# Convert each line into a md5 hash and compare files	
def md5(line):
    # eHarmony converted everything to upper case
    text = line.replace("\n","").upper()
    # Convert
    hashedText = hashlib.md5(text).hexdigest()
    #print(hashedText)

    # Check and Add
    if hashedText in eHarmonyHash:
        eHarmonyPlain.write(hashedText + ", " + text + "\n")
        #print(hashedText)


# SHA-256 + Salt
# SHA-256[(00-99)+($password)] is apparently the formula used
def sha256(line):
    textOriginal = line.replace("\n","")
    # Convert to SHA[(Salt+Password)]
    for salt in range(0, 100):
        text = str(salt) + textOriginal
        hashedText = hashlib.sha256(text).hexdigest()
        #print(hashedText)
        # Check and Add
        if hashedText in formspringHash:
            formspringPlain.write(hashedText + ", " + salt+ ", " + textOriginal + "\n")
            #print(hashedText)
            
# Open/Create Each Output File, Open Dictionary and Create Hashes 
print("Start")

# Output Files
eHarmonyPlain = open("eHarmonyPlain.txt", 'w')
formspringPlain = open("formspringPlain.txt", 'w')
AshleyMadisonPlain = open("AshleyMadisonPlain.txt", 'w')

# Input Files
AshleyMadison = open('AshleyMadison.txt', 'r')
formspring = open('formspring.txt', 'r')
eHarmony = open('eHarmony.txt', 'r')
dictionary = open('top100000.txt', 'r')
dictionarySmall = open('top10000.txt', 'r')

# Create Sets to Search Through Later
eHarmonyHash = set()
for line in eHarmony:
    eHarmonyHash.add(line.replace("\n",""))
formspringHash = set()
for line in formspring:
    formspringHash.add(line.replace("\n",""))

# Go Through Dictionary and Check
for line in dictionary:
    bcrypt()
    md5(line)

AshleyMadisonPlain.close()
eHarmonyPlain.close()

# Run sha256 afterwards with smaller dictionary incase of tech problems 
for line in dictionarySmall:
    sha256(line)

formspringPlain.close()
   
print "Finish"



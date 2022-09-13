from tables import *

#Function to test if A instruction
def isA(line):
    if not line.startswith('@'):
        return False

    dropped = line.strip('@')

    if dropped.isnumeric():
        return True
    
    #If it gets past here, it is a alpha numericic
    
    allowed = "_.$:"

    if dropped[0].isdigit():
        return False

    for char in dropped:
        if not char.isalnum() and not char in allowed:
            return False 
    
    return True

#Function to translate the A instruction
def translateA(line):
    dropped = line.strip('@')

    if dropped.isnumeric(): 
        return toBinary(int(dropped))
    else:
        return toBinary(symbolTable[dropped])

#Function to test if C instruction
def isC(line):
    if not (line.count('=') == 1 or line.count(';') == 1):
        return False

    thisLine = line.replace('=', ';')
    token = thisLine.split(';')

    if len(token) == 2:
        if(line.count('=') == 1):
            if not token[0] in destTable:
                return False
            if not token[1] in compTable:
                return False;
        else:
            if not token[0] in compTable:
                return False
            if not token[1] in jumpTable:
                return False;
    elif len(token) == 3:
        if not token[0] in destTable:
                return False;
        if not token[1] in compTable:
                return False;
        if not token[2] in jumpTable:
                return False;      
    else:
        return False
    
    return True
    
#Function to translate C instruction
def translateC(line):
    thisLine = line.replace('=', ';')
    token = thisLine.split(';')

    prefix = "111"
    dest = ""
    comp = ""
    jump = ""

    if len(token) == 2:
        if(line.count('=') == 1):
            dest = destTable[token[0]]
            comp = compTable[token[1]]
            jump = "000"
        else: 
            dest = "000"
            comp = compTable[token[0]]
            jump = jumpTable[token[1]]
    else:
        dest = destTable[token[0]]
        comp = compTable[token[1]]
        jump = jumpTable[token[2]]
        
    return (prefix + comp + dest + jump)

#Binary conversion function
def toBinary(num):
    binary = bin(num)
    binary = binary[2: len(binary)].zfill(16)
    return binary

#Main method
while True:
    asmName = input("Enter the name of the .asm file to assemble: ")
    try:
        file = open(asmName, "r")
        break
    except: 
        print('File not found, please try again')
        continue
    
 
fileName = asmName.replace(".asm", "") + ".hack"
binaryFile = open(fileName, "w")

pc = 0
nextAddress = 16


for line in file:
    commentRemoval = line.split("//")
    thisLine = commentRemoval[0]
    thisLine = thisLine.strip()
    thisLine = thisLine.replace(" ", "")
    
    if thisLine.count('(') == 1 and thisLine.count(')') == 1:
        thisLine = line.replace(")", "(")
        symbol = thisLine.split("(")
        if not symbol[1] in symbolTable:
              symbolTable[symbol[1]] = pc
    elif thisLine != "":
        pc += 1

file.seek(0)
glob = 0

for line in file:
    commentRemoval = line.split("//")
    thisLine = commentRemoval[0]
    thisLine = thisLine.strip()
    thisLine = thisLine.replace(" ", "")

    if thisLine == "":
        continue

    if isA(thisLine):
        AVal = thisLine.strip('@')
        if( not AVal.isdigit() and not AVal in symbolTable):
            symbolTable[AVal] = nextAddress
            nextAddress += 1
        binaryNum = translateA(thisLine)
        binaryFile.write(binaryNum + '\n')

    if isC(thisLine):
        binaryNum = translateC(thisLine)
        binaryFile.write(binaryNum + '\n')
        

print("Sucessfully assembled " + fileName)
binaryFile.close()
file.close()





    

    
    


from tables import *

def decipherC(instruction):
    dest = instruction[10:13]
    comp = instruction[3:10]
    jump = instruction[13:16]

    destination = "";
    computation = "";
    jumping = "";

    if jump == "000":
        destination = reverseDest[dest]
        computation = reverseComp[comp]
        return(destination + "=" + computation + "\n")      
    elif dest == "000":
        computation = reverseComp[comp]
        jumping = reverseJump[jump]
        return(computation + ";" + jumping + "\n")
    else:
        destination = reverseDest[dest]
        computation = reverseComp[comp]
        jumping = reverseJump[jump]
        return(destination + "=" + computation + ";" + jumping + "\n")


while True:
    hackName = input("Enter the name of the .hack file to disassemble: ")
    try:
        file = open(hackName, "r")
        break
    except:
        print('File not found, please try again')
        continue

fileName = hackName.replace(".hack", "") + ".asm"
assemblyFile = open(fileName, "w")

for line in file:
    if line.startswith("000"):
        assemblyFile.write("@" + str(int(line,2)) + "\n")
    if line.startswith("111"):
        assemblyFile.write(decipherC(line))

print("Sucessfully disasssembled " + fileName)
assemblyFile.close()
file.close()

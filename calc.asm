// Calculator application
// Enter operands to RAM[0] and RAM[1] 
// Enter operation choice to RAM[2]
// 1: +
// 2: -
// 3: *
// 4: /

//This portion checks which operator to use 
@R2
D=M
D = D - 1
@Add
D; JEQ
D = D - 1
@Sub
D; JEQ
D = D - 1
@Multiplication
D ; JEQ
D = D -1
@Division
D; JEQ

@End
0;  JMP 

//This does the addition  
(Add)
@R0 // A = 0 
D = M //  D = RAM[0]
@R1 //  A = 1
D = D + M //  D = D + RAM[1]
@R3  // A = 3
M = D // RAM[3] = D

@End
0; JMP


//This does the subtraction 
(Subtraction)
@R0 // A = 0 
D = M //  D = RAM[0]
@R1 //  A = 1
D = D - M //  D = D - RAM[1]
@R3  // A = 3
M = D // RAM[3] = D

@End
0; JMP

//This does the multiplication  
(Multiplication)
@R0
D=M //D = RAM[0]
@multZero
D; JEQ
@product  
M=D  //RAM[temp] = R0

@R1
D = M // D = RAM[1]
@multZero
D; JEQ
@negTest
D; JLT

@multLoop
0; JMP

//This handles the condition where one of the operands is negative  
(negTest)
@product 
D = M //D = RAM[temp]
@Exception
D; JLT

@R0
D = M 
M = -D

@R1
D = M
M = -D 

//This is the loop that handles the multiplication 
@multLoop
0; JMP

(multLoop)
@multStop
D-1; JEQ

@R0
D = M 
@product
M = D + M 

@R1
D = M
D = D - 1
M = D 

@multLoop
0; JMP

//This handles the last part of the multiplication
(multStop)
@product 
D = M //D =  RAM[temp]
@R3
M = D

@End
0; JMP 

//This handles the zero case
(multZero)
@R3
M = 0
@1024
M = 0

@End
0; JMP 

//This handles division 
(Division)
@R1
D = M //D = RAM[1]
@Exception
D; JLE

@R0
D = M //D = RAM[0]
@Exception
D; JLE

@R4
M = D

//Loop for division
@divLoop
0; JMP 

(divLoop)
@R1
D = D - M 

@R0
M = D 

@End
D;  JLT

@R3
D = M
M = D + 1; //RAM[3] += 1

@R0
D = M 

@R4
M = D //RAM[4]  = D 

@End
D;  JEQ

@divLoop
0; JMP

//Handles exceptions 
(Exception)
@1024
M = -1

@End
0; JMP

//End loop
(End)
@End
0; JMP

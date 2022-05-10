# CPSC-323-Project-3

# Prog1
[40 points] Same as the last problem in Project 2 (problem 6), include the S-->a=E  rule to the beginning of the grammar so that the grammar becomes this :

S -> a = E
E -> E+T     
E-> E- T      
E-> T
T->T*F       
T->T/F        
T->F
F->a             
F->b             
F—> ( E )

Remove left recursions and write the new grammar (5 points)
Compute FIRST and FOLLOW sets for S, E, T, F (and the other non terminals that were generated when eliminating recursion) in the new grammar (8 points)
Modify the predictive table to include the new rule (12 points)
Write a program to determine which of the following input strings are accepted or rejected by the grammar: (i) a = (a + a )*b$ , (ii) a=a*(b -a)$ , (iii) a=(a+a)b$. Submit it as Prog1. (15 points)

# Prog2
Write a program to read a postfix expression and compute its value. Submit it as Prog2. All variables are single letters, of type integer, and their value must be entered by the user.
 
# Prog3
Given the following CFG and the LR parsing table, write a program to trace input strings over the alphabet { i, +, - , *, / ), ( } and ending with $. Submit is as Prog3. Test it on two input strings (1) (i+i)*i$ and (2) (i*)$.  

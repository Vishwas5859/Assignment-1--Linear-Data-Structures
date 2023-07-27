
#Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?


def find(array, len, summ):
    print("Pairs whose sum is : ", summ)
    for i in range(len):
        for j in range(i, len):
            if (array[i] + array[j]) == summ:
                print(array[i], array[j])


array = [5, 2, 3, 4, 1, 6, 7]


summ = int(input("Enter the number: "))
print("Array = ", array)
find(array, len(array), summ)
#------------------------------------------------------------------------------------------------------------
# Q2. Write a program to reverse an array in place? In place means you cannot 
# create a new array. You have to update the original array.

def reverse_array(a):
    if len(a) == 1:
        return a
    return reverse_array(a[1:])+a[0:1]

 
arrary1 = [10,20,30,40,50]
print("The given array is: ",arrary1)
print("The reverse of array is", reverse_array(arrary1))
#------------------------------------------------------------------------------------------------------------
# Q3. Write a program to check if two strings are a rotation of each other?  

def checkRotation(s1, s2): 
    temp = '' 
  
    if len(s1) != len(s2): 
        return False

    temp = s1 + s1 
  
    
    if s2 in temp: 
        return True 
    else: 
        return False
    
string1 = "HELLO"
string2 = "LOHEL"
print(checkRotation(string1,string2))    
#------------------------------------------------------------------------------------------------------------

#Q4. Write a program to print the first non-repeated character from a string?

string = input("Enter a strimg: ")
index = -1
fnc = ""
 
if len(string) == 0 :
  print("EMTPY STRING");
 
for i in string:
    if string.count(i) == 1:
        fnc += i
        break
    else:
        index += 1
if index == len(string)-1 :
    print("All characters are repeating ")
else:
    print("First non-repeating character is:", fnc)

#------------------------------------------------------------------------------------------------
# Q5: Read about the Tower of Hanoi algorithm. Write a program to implement it.
# 
def tower_of_hanoi(n, source, destination, helper):
	if n==1:
		print ("Move disk 1 from peg", source," to peg", destination)
		return
	tower_of_hanoi(n-1, source, helper, destination)
	print ("Move disk",n," from peg", source," to peg", destination)
	tower_of_hanoi(n-1, helper, destination, source)		
# n = number of disks
n = 3
tower_of_hanoi(n,' A','B','C')     
#-------------------------------------------------------------------------------------------------
#Q6: 

def isOperator(x):
 
    if x == "+":
        return True
 
    if x == "-":
        return True
 
    if x == "/":
        return True
 
    if x == "*":
        return True
 
    return False
 
# Convertion of postfix to Prefix expression
 
def postToPre(post_exp):
 
    s = []
 
    # length of expression
    length = len(post_exp)
 
    # reading from right to left
    for i in range(length):
 
        # check if symbol is operator
        if (isOperator(post_exp[i])):
 
            # pop two operands from stack
            op1 = s[-1]
            s.pop()
            op2 = s[-1]
            s.pop()
 
            # concat the operands and operator
            temp = post_exp[i] + op2 + op1
 
            # Push string temp back to stack
            s.append(temp)
 
        # if symbol is an operand
        else:
 
            # push the operand to the stack
            s.append(post_exp[i])
 
    ans = ""
    for i in s:
        ans += i
    return ans
 
 
# Driver Code
if __name__ == "__main__":
 
    post_exp = "AB+CD-"
     
    # Function call
    print("Prefix : ", postToPre(post_exp))

#----------------------------------------------------------------------------------------------------
# Q7: Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []
     
    # read prefix in reverse order
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            # symbol is operand
            stack.append(prefix[i])
            i -= 1
        else:
           
            # symbol is operator
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
# Driver code
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))

#-------------------------------------------------------------------------------------------------------------    
#Q8: Write a program to check if all the brackets are closed in a given code snippet

def are_brackets_balanced(s):
    stack = []
    for ch in s:
        if ch in ('(', '{', '['):
            stack.append(ch)
        else:
            if stack and ((stack[-1] == '(' and ch == ')') or
                          (stack[-1] == '{' and ch == '}') or
                          (stack[-1] == '[' and ch == ']')):
                stack.pop()
            else:
                return False
    return not stack
 
expr = input("Enter the expression: ")
 
# Function call
if are_brackets_balanced(expr):
    print("Balanced")
else:
    print("Not Balanced")
#------------------------------------------------------------------------------------------------------   
#Q9. Write a program to reverse a stack.

class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
    def display(self):
        for data in reversed(self.items):
            print(data)
 
def insert_at_bottom(s, data):
    if s.is_empty():
        s.push(data)
    else:
        popped = s.pop()
        insert_at_bottom(s, data)
        s.push(popped)

def reverse_stack(s):
    if not s.is_empty():
        popped = s.pop()
        reverse_stack(s)
        insert_at_bottom(s, popped)
 
 
s = Stack()
data_list = input('Please enter the elements: ').split()
for data in data_list:
    s.push(int(data))
 
print('stack:')
s.display()
reverse_stack(s)
print('reversing the stack:')
s.display()        
#------------------------------------------------------------------------------------------------------  

# Q10. Write a program to find the smallest number using a stack.

def smallest(list):
    small= list[0]
    for i in list:
        if i<small:
            small=i
    return small

list=[3, 9, 7, 3, 6, 5, 7, 24, 6]
print("the list is: ")
print(smallest(list))
#------------------------------------------------------------------------------------------------------  


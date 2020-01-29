# =============================================================================
# # ABE 651 
# # 1/29/2020
# # Logan Heusinger
# # EX 5.2
# # Parts  2
# write function that prompts an input and converts to int. then check fermats
# theorem
# ============================================================================
a = int(input('a ')) # take user input and convert from str to int
b = int(input('b '))
c = int(input('c '))
n = int(input('n '))

def check_fermat(a,b,c,n): #setup function a^n+b^n=c^n is false for n>2
    left = a**n + b**n
    right = c**n
    
    if n < 3 : #check n
        print (' n must be greater than 2')
    elif left == right : #if the theorem is wrong
        print ("Holy smokes, Fermat was wrong")
    elif left != right : #if theorem is true
        print("no that doesnt work")

check_fermat(a,b,c,n)
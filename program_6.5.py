# =============================================================================
# # ABE 651 
# # 1/29/2020
# # Logan Heusinger
# # EX 6.5
# # Parts all
# write function that returns the greatest common denominator of a and b
# ============================================================================
a = int(input("Input a number for variable 'a'\n>"))#user inputs
b = int(input("Input a number for variable 'b'\n>"))


def gcd(a,b): # gcd(a,b) = gcd(b,r) and gcd(a,0) = a 
    if b == 0: #final statement with gcd(a,0)
        print(a)
        return a
    
    else: #recursive intermediate to get to gcd(a,0)
        r = a%b
        gcd(b,r)
        
gcd(a,b)  
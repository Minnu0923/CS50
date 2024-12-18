#return
#pow(power)
def main():
    x = int(input("What's x? "))
    print("x squared is", square(x))

def square(n):
    return pow(n,2) #power n is the number and 2 is the exponent

 #print("x squared is", square(x)) #NameError: name 'square' is not defined
 #output What's x? 3
#x squared is 9
main()
                
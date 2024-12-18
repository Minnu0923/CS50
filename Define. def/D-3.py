#parameters default value 
def hello(to="world"):
    print ("hello,", to)

hello()
name= input("What's you name? ")
hello(name)
"""output: hello, world
What's you name? minnu
hello, minnu"""

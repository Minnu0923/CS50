def main():
    name=input("What's your name? ")
    hello()



def hello(to="world"):
        print("hello,", name)

main()

""" output:print("hello,", name)
NameError: name 'name' is not defined
"""


        
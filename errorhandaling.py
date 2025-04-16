try:
    a=int(input("enter the number ")) # in pyhon we take inpute this way --- a = input("please enetr your inpute ")
    print(a)
except:
    print("The value if wrong ... please try againg")
    
else:
    print("Nothing went wrong") # this line only excuted when the program will run without any issue
    
finally:
    print("try except function has been used succsesfully") # this line will get executed at the end of code regardless of anything.
    
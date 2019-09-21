d=int(input(('please the number between 2 and 9')))
def dan(d):
    a=0
    for x in range(9):
        a=a+1
        b=d*a
        print(d,"x",a,"=",b)
    print()
dan(d)
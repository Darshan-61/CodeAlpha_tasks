n=int(input("GIVE THE INPUT FOR GENERATING FIBONACCI SERIES : "))
def fib_gen():
    x=0
    y=1
    for i in range(n):
        print(y)
        x,y=y,x+y
obj=fib_gen()        
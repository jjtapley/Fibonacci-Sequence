
def fibonacci(n):
    if n<0:
        print ("Incorrect ouput")
    elif n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)



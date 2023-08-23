oper = input("to sum enter 1 to min enter 2 to miltubli enter 3 to divid enter 4: ")
num1 = int(input("please enter the first number: "))
num2 = int(input("please enter the second number: "))

def main(n):
    while True:
        if n == "1":
            print("the result is " , sums(num1, num2))
            break
        elif n == "2":
            print("the result is " , mins(num1, num2))
            break
        elif n == "3":
            print("the result is " , milt(num1, num2))
            break
        elif n == "4":
            try:
                print("the result is " , div(num1, num2))
            except:
                print("zero is not valid")
            break
        else:
            raise("please enter 1 or 2")

def sums(x,y):
    return x+y

def mins(y,u):
    return y+u

def milt(h,j):
    return h*j

def div(t,i):
    return t/j


if __name__ == "__main__":
    main(oper)

def add(a, b):
    return a + b
   
def sub(a, b):
    return a - b

def main():
    num = input("Enter two integers: ")
    a, b = map(int,num.split())
    print(add(a,b))

if __name__ == '__main__':
    main()
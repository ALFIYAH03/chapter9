#chapter9
#no3

def star(n) :
    for r in range(1, n):
        bintang = "*" * (1+(r-1)*2)
        print(bintang.center(10))

star(5)

def star(n):
    a = n
    for data in range (n-30):
        x = 1+2*i
        print (('*'*x).center(a))
    for x in range (n):
        y = 5-2*x
        print (('*'*y).center(a))
star(7)

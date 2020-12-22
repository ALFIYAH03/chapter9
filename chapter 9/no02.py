#chapter9
#no2

def star(n) :
    for r in range(1, n):
        bintang = "*" * (1+(r-1)*2)
        print(bintang.center(10))

star(5)

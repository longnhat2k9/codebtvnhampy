import math

#bai 1
def snt(n): #ctc kiem tra so nguyen to
    if(n == 1): # n = 1 thi n khong la nguyen to
        return False
    for i in range(2, int(math.sqrt(n)) + 2):
        if(n%i == 0): # tim xem co uoc nao khac 1 va chinh no hay khong
            return False
    return True # neu khong tim duoc thi tra ve la so nguyen to

def bai1(): #ctc chay bai 1
    n = int(input("Nhap n:"))
    if(snt(n) == True):
        print(n, "la so nguyen to")
    else:
        print(n, "khong la so nguyen to")

bai1() #lenh khoi chay chuong trinh con bai 1

#bai 2 
def uoc(n): #ctc tinh tong uoc cua n
    sum = 1 # sum = 1 vi 1 la uoc cua moi so
    for i in range(2, int(math.sqrt(n)) + 2):
        if(n%i == 0): # kiem tra cac uoc cua no
            sum = sum + i # neu co uoc thi cong vao bien sum
    return sum == n # lenh tra ve n co la so hoan hao hay khong

def bai2():
    n = int(input("Nhap n:"))
    if(uoc(n) == True):
        print(n, "la so hoan hao")
    else:
        print(n, "khong la so hoan hao")

bai2() #lenh khoi chay bai 2


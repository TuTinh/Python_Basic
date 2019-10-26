import turtle
import math

# Bài 1: In toàn bộ các số chẵn từ 1000 đến 2000.
# for x in range(1000, 2000):
#    if x % 2 == 0:
#        print(x)

# Bài 2: Tính giai thừa ko dùng vòng lặp
# x = int(input("Nhập x = "))
# def GiaiThua(x):
#    if x == 0:
#        return 1
#    else:
#        return x * GiaiThua(x - 1)
# print(GiaiThua(x))

# Bài 3:Nhập một số n, hãy tạo ra dictionary chứa các phần tử dạng i:i*2 với (i chạy từ 1 đến n) và in ra dictionary đó.
# Ví dụ với n là 3 thì đầu ra sẽ là: {1: 2, 2: 4, 3: 6}
def bai3():
    n = int(input("Nhap số n = "))
    d = dict()
    for i in range(1, n + 1):
        d[i] = i * 2
    print(d)


# bài 4:Nhập vào một dãy số ngăn cách bởi dấu phẩy, hãy tạo và in ra một list và một tuple từ các số đó
def bai4():
    n = str(input("Nhap dãy so cách nhau bởi dấu phẩy:"))
    list = n.split(',')
    t = tuple(list)
    print(list)
    print(t)


# bài 5:Viết hàm tính giá trị bình phương một số. Lưu ý: phải sử dụng toán tử **
def bai5():
    x = int(input("Nhập vào x = "))
    print(x ** 2)


# Định nghĩa một class đơn giản để biểu diễn một đàn gà. Trong đó có 2 phương thức:
# getChickenNumber: để nhận số lượng con gà người dùng nhập vào
# countChikenLegs: để in ra số chân gà của đàn gà đó

class chicken(object):
    def __int__(self):
        self.x = 0

    def getChickenNumber(self):
        self.x = int(input("nhap so gà : "))

    def countChickenLegs(self):
        print(self.x * 2)


# graphic
def GUI():
    t = turtle.Screen()
    t.bgcolor("pink")
    t0 = turtle.Turtle()
    t0.color("red")
    t0.shape("turtle")
    # t0.up()
    for i in range(20, 120, 5):
        t0.stamp()
        t0.forward(i)
        t0.right(25)
    t.exitonclick()


def GUI1():
    t = turtle.Screen()
    t0 = turtle.Turtle()
    t0.color("blue")
    t0.shape("turtle")
    t0.penup()
    for i in range(10):
        t0.forward(65)
        t0.stamp()  # đánh dấu
        t0.forward(-80)
        t0.stamp()
        t0.right(36)
    t.exitonclick()


def GUI2():
    t = turtle.Screen()
    t.bgcolor("pink")
    t0 = turtle.Turtle()
    t0.color("brown")
    t0.shape("turtle")
    t0.pen(30)
    t0.penup()
    for i in range(3):
        t0.forward(50)
        t0.stamp()

    t.exitonclick()


def GUI3():
    t = turtle.Screen()
    t.bgcolor("black")
    t0 = turtle.Turtle()
    # t0.shape("circle")
    t0.color("yellow")
    # t0.penup()

    for i in range(0, 100):
        t0.forward(7)
        t0.left(3.6)
        t0.filling()
        t0.fillcolor("red")
    print('Current heading is: ',t0.heading())
    t.exitonclick()

def GUI4():
    t = turtle.Turtle()
    t.shape("triangle")
    t.color("pink")
    n = int(input('Nhap n = '))
    for i in range(n):
        t.forward(100)
        t.stamp()
        t.right(360)
        t.forward(-100)
        t.right(360)
        t.right(360 / n)
    t.shape("circle")
def math1():
    a = 3
    b = 4
    c = math.hypot(a, b)
    print(c)


if __name__ == '__main__':
    math1()
#   t = turtle.Screen()
#   t.bgcolor("pink")
#   t0 = turtle.Turtle()
#   t0.shape("arrow")

#   t0.color('blue')
#   t0.pensize(13)
#   for i in (1, 2):
#       t0.speed(10)
#       t0.forward(60)
#       t0.right(90)
#       t0.forward(70)
#       t0.right(90)

#   t0.penup()
#   t0.pendown()
#   t0.speed(100)
#   t0.forward(100)


# t.exitonclick()

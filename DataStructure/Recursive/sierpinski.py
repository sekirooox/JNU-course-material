from turtle import *


def drawTriangle(points: tuple, color, turtle):
    turtle.fillcolor(color)
    turtle.up()
    turtle.goto(points[0])
    turtle.down()# 准备工作

    turtle.begin_fill()  # 开始填充颜色
    turtle.goto(points[1])
    turtle.goto(points[2])
    turtle.goto(points[0])
    turtle.end_fill()  # 结束填充颜色
def getmid(p1,p2:tuple):
    mid1=(p1[0]+p2[0])/2
    mid2=(p1[1]+p2[1])/2
    return mid1,mid2
def sierpinski(p:list,degree,turtle):
    colormap=['black','white']
    if degree%2==0:
        drawTriangle(p,colormap[0],turtle)
    else:
        drawTriangle(p,colormap[1],turtle)
    if degree>0:
        # 使用list构造
        sierpinski([p[0],
                    getmid(p[0],p[1]),
                    getmid(p[0],p[2])],
                   degree-1,turtle)
        sierpinski([p[1],
                    getmid(p[1],p[0]),
                    getmid(p[1],p[2])],
                   degree-1,turtle)
        sierpinski([p[2],
                    getmid(p[2],p[1]),
                    getmid(p[2],p[0])],
                   degree-1,turtle)

if __name__ == '__main__':
    turtle = Turtle()
    win = turtle.getscreen()
    win.title("Draw Triangle")

    # 设置三角形顶点坐标
    points = [(-200, -100), (0, 200), (200, -100)]

    # 绘制三角形，设置颜色为蓝色（可以根据需要修改颜色）
    sierpinski(points,5,turtle)

    # 设置点击窗口关闭
    win.exitonclick()
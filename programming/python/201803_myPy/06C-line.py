# 6-3. 선을 반복해서 그리는 프로그램
import turtle as t

angle = 88     # 거북이가 왼쪽으로 회전할 각도를 지정함 (변경 가능)

t.bgcolor("black")
t.color("yellow")
t.speed(0)          # 가장 빠르게

for x in range(200): # 200 번 반복
    t.forward(x)     # x 만큼 앞으로 이동 (실행을 반복하면서 선이 길어짐)
    t.left(angle)  # 거북이가 360/n 만큼 왼쪽으로 회전



# 6-2. 원을 반복해서 그리는 프로그램
import turtle as t

n = 50 # n개의 원을 그린다.

t.bgcolor("black")
t.color("green")
t.speed(0)          # 가장 빠르게

for x in range(n): # n 번 반복
    t.circle(80)   # 반지름이 80인 원을 그린다.
    t.left(360/n)  # 거북이가 360/n 만큼 왼쪽으로 회전



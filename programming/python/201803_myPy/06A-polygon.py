import turtle as t

n = 5 # 오각형을 그립니다.

t.color("purple")
t.begin_fill()

for x in range(n): # n 번 반복
    t.forward(50)  # 50픽셀 만큼 이동
    t.left(360/n)  # 거북이가 360/n 각도 만큼 왼쪽으로 회전

t.end_fill()    # 색칠할 영역을 마무리 함


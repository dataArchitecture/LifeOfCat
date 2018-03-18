import turtle as t

# 삼각형 그리기
t.color("red") # 펜 색상을 "빨간색"으로 바꿉니다.
for x in range(3):
    t.forward(100) # 거북이가 100만큼 앞으로 이동합니다.
    t.left(120)    # 거북이가 왼쪽으로 120도 회전합니다.

# 사각형 그리기
t.color("green") # 펜 색상을 "녹색"으로 바꿉니다.
t.pensize(3)     # 펜 굵기를 3으로 바꿉니다.
for x in range(4):
    t.forward(100) # 거북이가 100만큼 앞으로 이동합니다.
    t.left(90)     # 거북이가 왼쪽으로 90도 회전합니다.

# 원 그리기
t.color("blue")  # 펜 색상을 "파란색"으로 바꿉니다.
t.pensize(5)     # 펜 굵기를 5로 바꿉니다.
t.circle(50)   # 반지름이 50인 원을 그립니다.

import math
import matplotlib.pyplot as plt
import numpy as np

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

g = 9.8  # 중력가속도
rad = float(input("각도 : "))  # 던진 각도
v0 = float(input("처음속도(m/s) : "))  # 처음 속도

# 초기 속도를 x와 y 성분으로 나누기
v0x = v0 * cos(rad)
v0y = v0 * sin(rad)

# x 좌표 계산 (시간)
t = np.linspace(0, 2 * v0y / g, num=1000)

# y 좌표 계산
x = v0x * t
y = v0y * t - 0.5 * g * t**2

plt.plot(x, y)
plt.xlabel('(m)')
plt.ylabel('(m)')
plt.title('3417')
plt.grid(True)

# x와 y축의 비율을 고정
plt.axis('equal')

plt.show()


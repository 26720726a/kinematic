import math

# ==============================
# 각도 변환
# ==============================

degree = 30

# degree -> radian
radian = math.radians(degree)

# radian -> degree
degree_again = math.degrees(radian)


# ==============================
# 삼각함수
# ==============================
# 각도 델타 를 각 삼각 함수에 넣기 

theta = math.radians(30)

sin_theta = math.sin(theta)
cos_theta = math.cos(theta)
tan_theta = math.tan(theta)


# ==============================
# 역삼각함수
# ==============================

x = 0.5

asin_x = math.asin(x)
acos_x = math.acos(x)
atan_x = math.atan(x)


# ==============================
# atan2
# ==============================

x = 1.0
y = 1.0

theta = math.atan2(y, x)

print("atan2 radian :", theta)
print("atan2 degree :", math.degrees(theta))


# ==============================
# 제곱 / 제곱근
# ==============================

a = 4

square = a ** 2
root = math.sqrt(a)


# ==============================
# 입력 예제
# ==============================

# 정수
# a, b = map(int, input().split())

# 실수
# a, b = map(float, input().split())


# ==============================
# 출력 자리수
# ==============================

value = 1.23456789

print(f"{value:.6f}")


# ==============================
# acos 범위 보정
# ==============================

D = 1.000000001

D = max(-1.0, min(1.0, D))

theta = math.acos(D)
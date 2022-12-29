# 116
# 10진수
print(1 * 10**2 + 1 * 10**1 + 6 * 10**0)

# 2진수 1110100(2)
print(1 * 2**6 + 1 * 2**5 + 1 * 2**4 + 0 *
      2**3 + 1 * 2**2 + 0 * 2**1 + 0 * 2**0)

#  bin 함수
x = 116
print(bin(x))  # 0b1110100  0b : 2진수

#  비트(bit) : 이진수에서 글자 하나

# shift 연산자
# 0b1001이라는 수를 왼쪽으로 한 칸 옮기는데, 빈자리는 0으로 채운다고 생각해보자. 0b10010이 될 것이다.
b = 0b1001
print(bin(b << 1))
# 0b10010

a = 0b1100
print(a << 1)
# 24

print(bin(b << 3))
# 0b1001000

print(a << 3)
# 96

# 왼쪽으로 한 칸 이동할 때 마다 2배가 되는 효과가 생긴다
# 오른쪽으로 이동 : >> , 숫자가 줄어든다

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 11:42:20 2024

@author: jcp
"""

# 함수(Function)

# [문제]
# 함수를 이용하여 사칙연산 계산기를 만들라.
# 계산가능 : 더하기, 빼기, 나누기, 곱하기, 나머지, 제곱
# -총합누적, 평균
# -히스토리(이력)

# 전역변수
total = 0
count = 0
hists = []

# 더하기
def add(a, b):
    return a + b

# 빼기
def sub(a, b):
    return a - b

# 나누기
def div(a, b):
    return a / b

# 곱하기
def mul(a, b):
    return a * b

# 나머지
def mod(a, b):
    return a % b

# 제곱
def square(a,b):
    return a ** b

# 총합 누적
def tot(nums):
    total=0
    for num in nums:
        total += num
    
    return total

# 평균
# def avg(nums):
#     return tot(nums) / len(nums)
def tot():
    return total

def avg():
    return total / count

def recalc():
    t = 0
    for n in hists:
        t += n
    return t, t / len(hists) # 튜플(총합, 평균)
# 히스토리
def hist():
    pass

# 계산기
def calc(a, op, b):
    if op == '+':
        c = add(a, b)
    elif op == '-':
        c = sub(a, b)
    elif op == '*':
        c = mul(a, b)
    elif op == '/':
        c = div(a, b)
    elif op =='%':
        c = mod(a, b)
    elif op == '**':
        c = square(a, b)
    else:
        return 0
        
    # 전역변수
    global total
    global count
        
    # 누적
    count += 1 # 연산횟수 누적
    total += c # 연산결과 누적
    hists.append(c) # 계산결과 보관
    return c # 단위연산 결과 리턴

# %%
calc(10, '+', 20)
calc(2, '*', 4)
calc(10, '/', 2)
calc(2, '**', 3)
print('총합:', total)
print('총합:', tot())
print('평균:', avg())
print('검산', recalc())
# calc() 함수에서 지원하지 않는 연산자
calc(2,  '&', 3)       # 0

# %%
# 계산기
# 하고자할 연산 선택
while True:
    print("1: 더하기")
    print("2: 빼기")
    print("3: 곱하기")
    print("4: 나누기")
    print("5: 나머지")
    print("6: 제곱")
    print("7: 총합 누적")
    print("8: 평균")
    print("anykey : 종료")
    choice = int(input("하고자할 연산을 선택하시오 : "))
    if choice == 1:
        print("더하기")
        # 인수입력
        n1 = int(input("더할 숫자 1 입력 : "))
        n2 = int(input("더할 숫자 2 입력 : "))
        # 출력
        print(f"{n1} + {n2} = {add(n1, n2)}")
    
    elif choice == 2:
        print("빼기")
        print("a-b를 실행합니다.")
        # 인수입력
        n1 = int(input("a를 입력 : "))
        n2 = int(input("b를 입력 : "))
        # 출력
        print(f"{n1} - {n2} = {sub(n1, n2)}")
        
    elif choice == 3:
        print("곱하기")
        #
        n1 = int(input("숫자1 입력 : "))
        n2 = int(input("숫자2 입력 : "))
        # 출력
        print(f"{n1} * {n2} = {mul(n1, n2)}")
    elif choice == 4:
        print("나누기")
        print("a/b를 실행합니다.")
        #
        n1 = int(input("a를 입력 : "))
        n2 = int(input("b를 입력 : "))
        # 출력
        print(f"{n1} / {n2} = {div(n1, n2)}")
    elif choice == 5:
        print("나머지")
        print("a % b를 실행합니다.")
        #
        n1 = int(input("a를 입력 : "))
        n2 = int(input("b를 입력 : "))
        # 출력
        print(f"{n1} % {n2} = {mod(n1, n2)}")
    elif choice == 6:
        print("6: 제곱")
        print("a ** b를 실행합니다.")
        n1 = int(input("a를 입력 : "))
        n2 = int(input("b를 입력 : "))
        # 출력
        print(f"{n1} ** {n2} = {square(n1, n2)}")
    elif choice == 7:
        print("7: 총합 누적")
        print("입력한 숫자들을 모두 더합니다.")
        nums = input("숫자들을 공백 기준으로 입력하세요. :").split()
        for i in range(len(nums)):
            nums[i] = int(nums[i])
        # 출력
        for num in nums:
            print(num, end='')
            if num == nums[len(nums)-1]:
                print("=", end='')
            else:
                print("+", end='')
        print(tot(nums))
    elif choice == 8:
        print("8: 평균")
        print("입력한 숫자들의 평균을 구합니다.")
        nums = input("숫자들을 공백 기준으로 입력하세요. :").split()
        for num in nums:
            num = int(num)
        # 출력
        print("평균 : ", avg(nums))
    else:
        print("종료")
        break
# 히스토리
# %%

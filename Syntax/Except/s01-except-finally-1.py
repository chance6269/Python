# -*- coding: utf-8 -*-

# 예외처리(Exception)
# try ~ except

# 예외가 발생하는 경우
#  - 잘못된 동작을 했을 때
#  - 실행할 때 발생
#  - 프로그램이 종료

# 예외처리:
    # - 비정상적 상황으로 인해서 프로그램이 중단없이 실행 가능하도록 처리

# Exception: 모든 예외 처리 클래스의 최상위 클래스 

# %%

def compute(x,y):

    try:
        if x < 0 or x > 100:
            return -1
        z = x / y
    except:
        print("예외발생")
    else: # 예외가 발생되지 않으면 처리
        print("정상처리")
    # finally: 
        # print("finally:작업종료")
    print("작업종료")

    return z
# %%

print(compute(10,3))
# 정상처리
# finally:작업종료
# 작업종료
# 3.3333333333333335

# %%
print(compute(-1, 3))
# finally:작업종료
# -1
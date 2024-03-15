# 멀티라인(다중라인)
# \n(CRLF,CR,FF) 
# LF(\n) : 라인피드
sml = """안녕하세요?
반갑습니다.
환영합니다.
"""

print(sml)

cr = ord('\r')
lf = ord('\n')
ff = ord('\f')
ht = ord('\t')
print(cr, hex(cr)) # 13 0xd
print(lf, hex(lf)) # 10 0xa
print(ff, hex(ff)) # 12 0xc
print(ht, hex(ht)) # 9 0x9
# %%
# LF(\n)
ssl = "안녕하세요\n반갑습니다.\n환영합니다.\n"
print(ssl)
# %%
# CR(\r) : 캐리지 리턴, 커서를 맨 앞으로 이동
ss1 = '안녕하세요\r반갑습니\r환영\r' # 환영습니요
print(ss1)
# %%
# FF(\f) : 폼 피드, 다음 페이지
# ss2 = '안녕하세요?\f반갑습니다.\f환영합니다.\f'
# print(ss2)

# %%
# Windows : CRLF(\r\n)
ss3 = "안녕하세요?\r\n반갑습니다.\r\n환영합니다.\r\n"
print(ss3)

# %%
# Horizontal Tap
# 8칸

print('1234567890' * 5)
print('ABC\tDEFGHIJK\tLMNOPQ\tEND')
# 12345678901234567890123456789012345678901234567890
# ABC	DEFGHIJK	LMNOPQ	END

# Windows CMD
# 12345678901234567890123456789012345678901234567890
# ABC     DEFGHIJK        LMNOPQ  END

# %%
# BS(Backspace)
print("ABC\bD") # ABD
print("ABC\b\bD") # ADC
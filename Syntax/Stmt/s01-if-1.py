# -*- coding: utf-8 -*-


# 파이썬은 여러 줄로 기술이 안되므로
# 역슬래시(\)로 명령문 연결

score = 100

grade = 'A' if score >= 90 else \
        'B' if score >= 80 else \
        'C' if score >= 70 else 'D'
        
print(f"점수는 {score} 이며 등급은 {grade} 입니다.")
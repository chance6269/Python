# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 10:01:50 2024

@author: jcp
"""
import sys
import studentscore as sc

args = sys.argv[1:]

score = sc.StudentScore(args[0])


# 총점, 평균 추가
score.compute()

# 파일 쓰기
score.write(args[1])

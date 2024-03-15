# -*- coding: utf-8 -*-


# 파일 입출력
# 함수 : open(), close(), read(), write(), readline(), readlines()
# 파일 입출력 순서:
    #  - 오픈
    #  - 읽기나 쓰기
    #  - 닫기
# 파일의 종류:
    #  - 텍스트(ASCII, UTF-8) : txt, csv, py, java, c, cpp, xml, html, sql, json
    #  - 바이너리(Binary) : doc, hwp, xls, pdf, jpg, gif, exe, dll
# %%

# 텍스트 파일 처리

# 파일 객체 얻기 : 쓰기용
# 파일이름, 모드, 인코딩
# 파일생성 위치 : Spyder IDE(Browser a Working Directory)
# 모드'w': 파일 생성, 덮어쓰기
score_file = open("./score.txt", 'w', encoding="utf8")
print("수학: 77", file=score_file)
print("영어: 88", file=score_file)
score_file.close()

# score.txt:
    
# 수학: 77
# 영어: 88
# (ctrl+z)

# %%

score1_file = open("./score-1.txt", 'w', encoding="utf8")
score1_file.write("국어: 100\n")
score1_file.write("수학: 70\n")
score1_file.write("영어: 80\n")
score1_file.close()

# %%

# 모드'a' : 파일 생성 or 내용 추가.
score2_file = open("./score-1.txt", 'a', encoding="utf8")
score2_file.write("국어: 100\n")
score2_file.write("수학: 70\n")
score2_file.write("영어: 80\n")
score2_file.write("과학: 80\n")
score2_file.close()


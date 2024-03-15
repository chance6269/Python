# 파일 입출력

# [문제]
# 1. 국어, 영어, 수학, 과학 점수를 텍스트 파일로 생성
# - 아래와 같이 텍스트 편집기로 작성
#  예시)
#   이름,국어,영어,수학,과학
#   홍길동,100,90,80,70
#   이순신,100,90,80,70
#   강감찬,100,90,80,70

# 2. 생성된 파일을 읽어서 총점, 평균을 구하라.
#   이름,국어,영어,수학,과학,총점,평균
#   홍길동,100,90,80,70,340,85
#   이순신,100,90,80,70,340,85
#   강감찬,100,90,80,70,340,85
score = open('./score.txt','r',encoding='utf8')
st_list = []
while True:
    txtline = score.readline()
    if not txtline:
        print('EOF')
        break
    st_list.append(txtline)

score.close()
# print(st_list)
# \n 제거, 점수 추출
var_names = st_list.pop(0).replace('\n','').split(',') # 변수명 제거

for i in range(len(st_list)):
    st_list[i] = st_list[i].replace('\n', '')
    st_list[i] = st_list[i].split(',')
    for j in range(len(st_list[i])-1):
        st_list[i][j+1] = int(st_list[i][j+1])
        
    # 총점, 평균 추가
    tot = 0
    for j in range(1, len(st_list[i])):
        tot += st_list[i][j]
    avg = tot / 4
    st_list[i].append(tot)
    st_list[i].append(avg)
# print(st_list)

# 3. 위 1, 2에서 처리한 성적을 새로운 파일에 저장
new_score = open('./new_score.txt','w', encoding='utf8')
# 변수명 추가
var_names.append('총점')
var_names.append('평균')
print(var_names)

# 파일 쓰기
new_score.write(",".join(var_names))
new_score.write("\n")

for line in st_list:
    for i in range(len(line)):
        line[i] = str(line[i])    
    new_score.write(",".join(line))
    new_score.write("\n")


new_score.close()
# %%
# 4. 파일이 없는 경우 예외처리를 한다.
try:
    score = open('./score3.txt','r',encoding='utf8')
    st_list = []
    while True:
        txtline = score.readline()
        if not txtline:
            print('EOF')
            break
        st_list.append(txtline)
except FileNotFoundError:
    print("해당 파일 없음")
finally:
    score.close()

# \n 제거, 점수 추출
var_names = st_list.pop(0).replace('\n','').split(',') # 변수명 제거

for i in range(len(st_list)):
    st_list[i] = st_list[i].replace('\n', '')
    st_list[i] = st_list[i].split(',')
    for j in range(len(st_list[i])-1):
        st_list[i][j+1] = int(st_list[i][j+1])
        
    # 총점, 평균 추가
    tot = 0
    for j in range(1, len(st_list[i])):
        tot += st_list[i][j]
    avg = tot / 4
    st_list[i].append(tot)
    st_list[i].append(avg)

new_score = open('./new_score.txt','w', encoding='utf8')
# 변수명 추가
var_names.append('총점')
var_names.append('평균')
print(var_names)

# 파일 쓰기
new_score.write(",".join(var_names))
new_score.write("\n")

for line in st_list:
    for i in range(len(line)):
        line[i] = str(line[i])    
    new_score.write(",".join(line))
    new_score.write("\n")

new_score.close()
# %%
# 5. 해당 코드를 일반 함수를 만들어 코딩
def read_line_list(file): # 파일의 각 라인을 묵어 리스트로 반환하는 함수
    lst = []
    while True:
        txtline = file.readline()
        if not txtline:
            print('EOF')
            break
        lst.append(txtline)
    
    return lst

def rep_split(str): # 문자열의 \n 제거, ','기준 리스트로 반환하는 함수
    return str.replace('\n','').split(',')

# 마지막에 \n 추가, 리스트를 ','기준 조인 후 문자열로 반환하는 함수
def list_join(lst):
    lst = ",".join(lst)
    return lst + "\n"
# %%
try:
    score = open('./score.txt','r',encoding='utf8')
    st_list = read_line_list(score) # 파일 각 라인을 요소로 리스트 생성.
except FileNotFoundError:
    print("해당 파일 없음")
finally:
    score.close()

# \n 제거, 문자열 분할
for i in range(len(st_list)):
    st_list[i] = rep_split(st_list[i])
        
    # 총점, 평균 추가
    # 변수명 제외, 이름 제외하고 int형으로 변환
    if i == 0:
        continue
    else:
        tot = 0
        for j in range(1, len(st_list[i])):
            int_score = int(st_list[i][j])
            tot += int_score
        avg = tot / 4
        # str 형태로 리스트에 추가
        st_list[i].append(str(tot))
        st_list[i].append(str(avg))

# 변수명 추가
st_list[0].append('총점')
st_list[0].append('평균')

# 파일 쓰기
new_score = open('./new_score2.txt','w', encoding='utf8')
for line in st_list:
    # 이중리스트를 문자열 리스트로 변환 후 쓰기
    new_score.write(list_join(line))

new_score.close()

# %%
# 6. 클래스로 만들어 코딩

def rep_split(str): # 문자열의 '\n' 제거, 공백 제거, ','기준 리스트로 반환하는 함수
    splist = str.replace('\n','').split(',')
    for sp in splist:
        sp = sp.strip()
    return splist


def make_line(lst): # 리스트를 ','기준 조인 후 문자열로 변환 후 '\n'을 더해 반환하는 함수
    lst = ",".join(lst)
    return lst + "\n"

class DataFrame():
    
    def __init__(self, filename):
        try:
            file = open(filename,'r',encoding='utf8')
            lines = []
            while True:
                txtline = file.readline()
                if not txtline:
                    print('EOF')
                    break
                lines.append(txtline)
        
            for i in range(len(lines)):
                lines[i] = rep_split(lines[i])
                
            self.vars = lines[0] # 컬럼명 리스트
            self.rows = lines[1:] # 데이터 리스트(행)의 리스트
        except FileNotFoundError:
            print("해당 파일 없음")
        finally:
            file.close()
        
    def add_var(self, name):
        self.vars.append(name)
        
    def write(self, filename):
        file = open(filename, 'w', encoding='utf8')
        file.write(make_line(self.vars))
        for line in self.rows:
            file.write(make_line(line))
        
        file.close()
        
# %%
df = DataFrame('./score.txt')


# 총점, 평균 추가
# 변수명 제외, 이름 제외하고 int형으로 변환
for row in df.rows:
    tot = 0
    for i in range(1, len(row)):
        int_score = int(row[i])
        tot += int_score
    avg = tot / 4
    # str 형태로 리스트에 추가
    row.append(str(tot))
    row.append(str(avg))

# 변수명 추가
df.add_var('총점')
df.add_var('평균')

# 파일 쓰기
df.write('./new_score9.txt')


# %%
# 7. 처리한 파일 이름을 외부에서 임의로 지정하여 처리한다.
#   - 교재 p 183 참조
#   - 파일(score.txt) 읽어서 성적처리 결과 파일(score-result.txt) 생성   
#   - python score.txt score-result.txt
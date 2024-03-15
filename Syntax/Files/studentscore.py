
def split_line(str): # 문자열의 '\n' 제거, 공백 제거, ','기준 리스트로 반환하는 함수
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
                lines[i] = split_line(lines[i])
                
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
        
class StudentScore(DataFrame):
    
    def compute(self):
        self.add_var("총점")
        self.add_var("평균")
        for row in self.rows:
            tot = 0
            for i in range(1, len(row)):
                int_score = int(row[i])
                tot += int_score
            avg = tot / 4
            # str 형태로 리스트에 추가
            row.append(str(tot))
            row.append(str(avg))
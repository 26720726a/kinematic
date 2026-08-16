'''
# 자료형 
#'',"" 로 감싸면 문자 자료형 ('10') -> 이때 10은 숫자형이 아닌 문자형
print('hello world') # 문자형 
print(10) # 숫자형 출력 
print(True) # 불리안 자료형
print(False)

# 변수 : 값을 저정하는 공간 
# 변수 이름 = 값
a= 1
b=2
c='good'
print(a) # 변수 값을 출력 
print(b)
print(c)
# 변수 명으로 공백이나 특수 문자 불가 ( _ 는 사용 가능),  숫자로 시작 할수 없음 ,대소문자 구분, 예약어 사용 불가 

#형 변환 
#int ('2') 정수로float('1,5') 실수로 str(2) 문자로 -> 알아 볼 수 있는 형태만 넣어야함 
#int(float('3.14')) 문자열-> 실수형 -> 정수형 변화 정수는 소수점 아래를 버림 
#bool() 불리안으로 값이 있으면 T 값이 없으면 F 
a = 'hello' ,'   ',1,-2  # true
b ='',0,None               #false

# 연산자 
#+,-,*,/
# % 나머지, //몫 **거듭제곱, 부등호 == 같다 != 다르다 , 
print(5%2) # 1
print(5//2) # 2
print(5**3) # 125 
print(not 3<5) # False
print(bool('False')) # False 라는 값이 있음 -> True  출력 
#in 포함 not in 미포함
print('c'in 'cat') # T 
print('c' not in 'cat') # F

# a 는 b 보다 크거나 같고 c 는 d 보다 작거나 같다 
# b<=a and c <=d
'''
# 주석 
# # 한줄 ''' 여러줄 
'''
#인덱스 : 몇번째 슬라이싱 
long='python'
print(long[0]) # p
print(long[-1]) # n 
print(long[1:5]) # 1부터 4까지만 
print(long[:]) # 처음부터 끝까지 

# 문자열 처리 

snack = '꿀꽈배기'
two = '2개'
juseyo = snack + two
print(juseyo)
juseyo += '주세요' 
print(juseyo)

num1=3
num1=num1+2
print(num)
num2=3
num2+=2
print(num)

# 문자열 길이 구하가 len()
print (len(snack)) # snack의 문자열 길이 구함 

#########python 내장형################ 검색 
#메소드 
#문자열.메소드(...)
letter = 'how are YOU?'
print(letter.lower()) # 모두 소문자 ->how are you?
print(letter.upper()) # 모두 대문자 ->HOW ARE YOU?
print(letter.capitalize()) #첫 글자만 대문자 ->How are you?
print(letter.title()) # 단어들으 첫글자 대문자  -> How Are You?
print(letter.swapcase()) # 대소문자를 바꿈  -> HOW ARE you?
print(letter.split()) # 문자열을 띄어쓰기 기준으로 나눔 -> ['how', 'are', 'YOU?']
print(letter.count('h')) # 문장 속에 h 의 개수  -> 1
s='나도 고등학교 다녀!!!'
print(s.startswith('나')) # h로 시작하는지 확인 -> True
print(s.endswith('고등학교')) # h로 시작하는지 확인 -> False
print(s.strip('!')) #! 제거 -> 나도 고등학교 다녀
print(s.replace('고등학교','대학교')) # 문자열 교체 -> 나도 대학교 다녀!!!
print(s.find('학교')) # 글자 위치 찾기 -> 5
print(s.center(20,'-')) # 다른 문다들 사이에 가운데 -> ---나도 고등학교 다녀!!!----


#문자열 포멧 
python ='파이썬'
java='자바'
print(python + java) # 파이썬자바
print('개발언어에는',python,',',java,'등이 있어요')
print('개발언어에는 {},{} 등이 있어요'.format(python,java)) #개발 언어에는 파이썬,자바등이 있어요
print('개발언어에는 {1},{0} 등이 있어요'.format(python,java)) # 개발언어에는 자바,파이썬 등이 있어요
# f-string
print(f'개발 언어에는 {python},{java}등이 있어요') #개발 언어에는 파이썬,자바등이 있어요 

# 탈출 문자 
#\n 줄바꿈 

##################################################################
#리스트[] : 여러개의 값을 저장
list=[1,3.14,True,'아무거나','중복가능','중복가능'] # [] 빈 리스트 생성 , 자료형 상관 없음 

print(list) # [1, 3.14, True, '아무거나', '중복가능', '중복가능']

print(list[1])# 3.14 -> 순서가 있어서 슬라이싱 가능 
print('아무거나'in list)

list[0]=9
print(list) # [9, 3.14, True, '아무거나', '중복가능', '중복가능']
list.append('추가')
print(list) # [9, 3.14, True, '아무거나', '중복가능', '중복가능', '추가']
list.remove('중복가능')
print(list) # [9, 3.14, True, '아무거나', '중복가능', '추가']

list2= ['리스트','합치기']
list.extend(list2)
print(list) # [9, 3.14, True, '아무거나', '중복가능', '추가', '리스트', '합치기']

#insert(위치, 값) 원하는 위치 값 추가 
#pop(위치) 원하는 위치 값 삭제 
#clear()  모든 값 삭제
#sort() 값 순서대로 정렬
#reverse() 순서 뒤집기
#copy()리스트 복사
#count(찾을 값) 어떤값 몇개있는지 
#index(찾을 값) 어떤 값이 어디에 있는지 
##################################################################
#튜플() -> 수정 불가능 = 일기 전용 리스트 
tuple= (1,3.14,'아무거나','중복') 
print(tuple)

(p1,p2,p3,p4)=tuple # 언패킹 -> 개수 맞춰야함 
print(p1)

list(tuple)-> 리스트로 반환해서 수정 가능

numbers= (1,2,3,4,5,6,7,8,9,10)
(one,two,*others)=numbers  # (one,*others,ten)
print (others) # [3, 4, 5, 6, 7, 8, 9, 10] -> 리스트로 나옴 

##################################################################
# 세트{} 순서없고 중복 안됨 

a={'1','2','3'}
b={'3','4','5'}
print(a.intersection(b)) #교집합-> {'3'} 
print(a.union(b))# 합집합 ->{'1', '3', '5', '4', '2'}
print(a.difference(b)) # 차집합 a-b {'2', '1'}

#인덱스를 통해서 접근 불가 
a={'1','2','3'}
b={'3','4','5'}
a.add('4') # 추가
b.remove('4') # 제거 
print(a)
print(b)
a.clear()
print(a) # set()
del b # 세트 완전 삭제 
#copy() 세트 복사 
#discard(삭제할 값) 값 삭제 (해당 값이 없어도 에러 발생 X)
#isdisjoint(비교할 세트) 두세트에  겹치는 값이 없는지 여부 
#issubset(비교할 세트) 다른 세트의 부분집합인지 여부 
#issuperset(교할 세트） 다른 세트의 상위집합인지 여부
#update(추가할 세트) 다른세트의 값들을 더함 

##################################################################
#딕셔너리
#딕셔너리 = {key1:value1,key2:value2, ...}
person={
    '이름':'나귀욤',
    '나이':7,
    '키':120,
    '몸무게':23
}
print(person['이름']) # 키에 해당하는 value 값 -> 나귀욤
print(person.get('별명')) # 없는 key 인경우 None 출력 
person['최종학력']='유치원' # 추가, 수정 가능   딕셔너리[key]=value
print(person)
person.update({'키':130,'몸무게':30}) # 여러개 업데이트 가능 
print(person)
person.pop('최종학력') # 제거 키값 입력 
print(person)
print(person.keys())
print(person.values())
print(person.items())

#########################################################
#조건문 
#if 조건1 : 
#   이 문장
#elif 조건2 :
#   요 문장
#elif 조건3 :
#   요기 문장
#else:
#   저 문장
#다음 문장

yellow_card=0
foul=True
if foul:
    yellow_card+=1
    if yellow_card==2:
        print('퇴장')
    else:
        print('경고')
else:
    print('주의')
############################################################
#range

#range(start,stop)
range(1,10) # 1 이상 10 미만 
range(1,10,2) # 1,3,5,7,9

#########################################################
#반복문 
#for 변수 in 반복 범위 또는 대상:
#   반복 수행 문장 
for x in range(10): # 0~9까지
    print(f'팔별려 뛰기 {x}회')

person={'이름':'나귀욤','나이':7,'키':120, '몸무게':23 }

for v in person.values(): # values 값
    print(v) 
for v in person.keys(): # keys 값
    print(v) 
for k,v in person.items(): # items 값
    print(k,v) 

fruit='apple'

for i in fruit:
    print(i) # a p p l e 한줄에 하나씩 출력

##########################################################
#while문
"""
while 조건:
    반복 수행 문장
"""
weight = 0
item=3
max=25
while weight+item<max:
    weight+=item
    print('짐추가 가능')
print(f'총 무게는 {weight}입니다')

#break -> 반복문내부에서 조건 만족시 탈출로 사용 
drama=['시즌1','시즌2','시즌3','시즌4','시즌5']

for x in drama:
    if x == '시즌3':
        print('stop')
        break
    print(f'계속 시청 {x}')
"""
계속 시청 시즌1
계속 시청 시즌2
stop
"""

###################################################
#continue
drama=['시즌1','시즌2','시즌3','시즌4','시즌5']

for x in drama:
    if x == '시즌3':
        print('skip')
        continue
    print(f'계속 시청 {x}')
"""
계속 시청 시즌1
계속 시청 시즌2
skip
계속 시청 시즌4
계속 시청 시즌5
"""

#######################################################
#list comprehension
list=[1,2,3,4,5]
new_list=[]

for x in list:
    if x<=3:
        new_list.append(x)

print(new_list)

new_list=[x for x in list if x<=3] # 한줄로 줄임 

print(new_list)
'''
#####################################################
# 함수 
"""
def 함수명 ( 전달 값1, 전달값2 ):
    작업 
    return 반환 값 # 즉시 함수를 나감 
def 함수명 ( 전달 값1=기본 값 ):
    작업 
    return 반환 값 # 즉시 함수를 나감 

함수명(value) # 호출 필요 
"""
#######################################################
#사용자 입력 
'''
name=input('이름이 무엇인가요?') # 입력값은 모두 문자열로 저장됨 
print(name)

num=int(input('몇명인가요?'))

if num > 4 :
    print('입장 불가')
else:
    print('입장 가능')
    
########################################################
# 파일 입출력 
# f=open('파일이름','모드',encoding='utf8') utf8은 한글
f=open('list.txt','w',encoding='utf8') # 열기 w 쓰기 모드 
f.write('김00\n') # 쓰기 
f.write('이00\n')
f.write('박00\n')
f.close() # 닫기

#f=open('list.txt','r',encoding='utf8') # r 읽기 모드
#contents = f.read()
#print(contents)
#f.close()

f=open('list.txt','r',encoding='utf8')
for line in f:
    print(line,end='')
f.close()

#with
# 자동으로 파일을 닫아줌 
with open('list.txt','r',encoding='utf8') as f: # f로 파일 내용 받아옴 
    for line in f:
        print(line,end='')

############################################################
# class
# 설계도 + 설명서 
"""
class 클래스명:
    정의
   
class BlackBox:
    pass # 정의를 미룸 -> 아직 안정했을때 사용    

b1=BlackBox() # b1 객체
b1.name='까망이'
print(b1.name)
print(isinstance(b1,BlackBox))
"""

class BlackBox:
    def __init__(self,name,price): # __init__ 객체가 생성될때 사용으로 사용 
        self.name=name # name,price는멤버 변수 
        self.price=price
    def set_travel_mode(self,min): # 함수를 넣을 수 있음  self는 객체 자기 자신 
        print(str(min)+'분동안만 여행모드 on')
    def name_min(self,min):
        print(f'{self.name} {min} 분 동안 여행 모드 on')
b1=BlackBox('까망이',200000)
b1.nickname='1호' # b1 에만 새로운 정보 추가 
print(b1.name,b1.price,b1.nickname)
b2=BlackBox('하양이',100000)
print(b2.name,b2.price)
b1.set_travel_mode(20)

b1.name_min(20) # 까망이 20 분 동안 여행 모드 on    
BlackBox.name_min(b1,20) # 위에거와 같음 
'''
#############################################
#상속













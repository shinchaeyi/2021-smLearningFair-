#1: 정보입력
name = input('이름을 입력하세요.: ')
student_number= input('학번을 입력하세요.: ')
print('')

#2: 수강신청 설명
print('안녕하세요. 상명대학교 1학년 1학기 디자인학부 수강신청 프로그램입니다.\n')
print('수강신청 목록은 교양필수 ,교양선택, 전공 3가지 입니다.\n')
print('교양 필수는 기초교양 3학점, 상명핵심역량교양 4학점이 이수기준 입니다.\n')
print('교양 선택은 일반교양 4학점, 균형교양 3학점이 이수기준 입니다.\n')
print('전공은 기초디자인1(2학점)과 관찰과표현(2학점)을 수강하셔야합니다.\n')
print('')

#3: 교양필수 수강신청
basic={'컴퓨팅사고와게임디자인':1,
'English foundations':1,'교양과인성':1,'사회봉사':1}
smu={'사회와문화':1,'디자인프레젠테이션':1,'색채심리학':2,'디지털사진윤리':2}
print('')

#4: 교양선택 수강신청
normal={'실무영어':1,'디자인개념과원리':2,'우리꽃의이해':2,'도자와생활':1}
balance={'인간과언어':2,'법학의세계':1,'경영학개론':1,'우주의역사':1}
print('')

#5: 강의 담기
mylist=[]
mylist.append('기초디자인1')
mylist.append('관찰과표현')

print('기초교양 강의목록입니다.')
print('기초교양은 3학점이 채워질 때까지 추가하셔야합니다.\n')
basic_score=0
while basic_score<3:
    alist=input(str(list(basic.keys()))+'중 수강하고자하는 강의는?: ')
    mylist.append(alist)
    print('%s는 %s학점 입니다.'%(alist,basic[alist]))
    basic_score= basic_score+int(basic[alist])
print('기초교양',basic_score,'학점을 신청하셨습니다.\n')

print('상명핵심역량교양 강의목록입니다.')
print('상명핵심역량교양은 4학점이 채워질 때까지 추가하셔야합니다.\n')
smu_score=0
while smu_score<4:
    blist=input(str(list(smu.keys()))+'중 수강하고자하는 강의는?: ')
    mylist.append(blist)
    print('%s는 %s학점 입니다.'%(blist,smu[blist]))
    smu_score= smu_score+int(smu[blist])
print('상명핵심역량교양',smu_score,'학점을 신청하셨습니다.\n')

print('일반교양 강의목록입니다.')
print('일반교양은 4학점이 채워질 때까지 추가하셔야합니다.\n')
normal_score=0
while normal_score<4:
    clist=input(str(list(normal.keys()))+'중 수강하고자하는 강의는?: ')
    mylist.append(clist)
    print('%s는 %s학점 입니다.'%(clist,normal[clist]))
    normal_score= normal_score+int(normal[clist])
print('일반교양',normal_score,'학점을 신청하셨습니다.\n')

print('균형교양 강의목록입니다.')
print('균형교양은 3학점이 채워질 때까지 추가하셔야합니다.\n')
balance_score=0
while balance_score<3:
    dlist=input(str(list(balance.keys()))+'중 수강하고자하는 강의는?: ')
    mylist.append(dlist)
    print('%s는 %s학점 입니다.'%(dlist,balance[dlist]))
    balance_score= balance_score+int(balance[dlist])
print('균형교양',balance_score,'학점을 신청하셨습니다.\n')

#6: 현재 수강신청 목록
print('현재 나의 수강신청 목록입니다.')
print(mylist)
print('')

#7:현재 수강신청 학점
print('현재 나의 수강신청 학점입니다.')
print(int(4+basic_score+smu_score+normal_score+balance_score))

#8:마무리
print('')
print(name+'학생의 상명대학교 1학년 1학기 디자인학부 수강신청이 완료되었습니다!')







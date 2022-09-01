
# # 애완동물을 소개해 주세요~
# animal ="강아지"
# name ="연탄이"
# age =4
# hobby ="산책"
# is_adult = (age >=3)


# print("우리집" + animal + "의 이름은 " + name + "이에요")
# #print(name + "는" + str(age) + "살이며," + hobby + "을 아주 좋아해요")
# print(name,"는",age,"살이며",hobby,"을 아주 좋아해요")
# print(name + "는 어른 일까요?" + str(is_adult))



# station = "사당"
# print(station+ " 행 열차가 들어오고 있습니다")
# station = "신도림"
# print(station+ " 행 열차가 들어오고 있습니다")
# station = "인천공항"
# print(station+ " 행 열차가 들어오고 있습니다")



# print(2**3) # 2^3
# print(5%3) # 5를 3으로 나눈 나머지
# print(5//3) #5를 3으로 나눈 몫
# print (3==3)  #True
# print(3==4) #False
# print(not(1!=3)) #True의 not이므로 False
# print((3>0) and (3<5)) #True
# print((3>0) & (3<5)) #True
# print((3>0) or (3>5)) #or = 둘중 하나라도 만족하면 되므로 True
# print((3>0)|(3>5)) #True


# ########### 수식 ############

# print(2+3*4)
# number = 2**4
# print(number)
# number +=2 #number = number + 2
# print(number)



# ########## 숫자처리 함수 ###########
# print(abs(-5)) #abs=절댓값
# print(pow(4,2)) #4^2 = 4**2
# print(max(5,12)) #maximum값
# print(min(5,30)) #minimum값
# print(round(3.14)) #반올림값
# print(round(5.87))

# from math import* #math라이브러리 불러오기
# print(floor(4.99)) #내림값
# print(ceil(3.14)) #올림값
# print(sqrt(16)) #제곱근, root(16) = 4


# ########## 랜덤함수 ###########
# from random import* #랜덤함수 호출

# print(random())
# rand = random() #0.0 ~ 1.0 이하의 임의의 값 생성
# print(rand)
# rand = random() *10 #0.0에서 10.0이하의 임의의 값 생성
# print(rand)
# print(int(rand)) #int=정수값만 제공
# rand = (random()*10)+1 #1에서 10.0이하의 임의의 값 생성
# print(int(rand))

# print(randrange(1,46)) #1에서 46미만의 임의의 값 생성

# print(randint(1,45)) #1에서 45이하의 임의의 값 생성

# from random import*
# print("스터디 날짜 정하기")
# randDate = randrange(4,28)
# print("오프라인 스터디 모임 날짜는 매월",str(randDate),"일로 선정되었습니다")

# ######### 문자열 ##########
# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence4 = """
# 나는 소년이고,
# 파이썬은 쉬워요
# """
# print(sentence4)

# ######### 슬라이싱 ###########
# #문장에서 필요한 정보 추출
# jumin="990928-1234567"
# print("성별 : " +jumin[7])
# print("연 : " + jumin[0:2]) # 0-2직전까지
# print("월 : " +jumin[2:4])
# print("일 : "+jumin[4:6])
# print("생년월일 : "+jumin[0:6]) # = jumin[:6]
# print("뒤 7자리 : "+jumin[7:14]) # =jumin[7:]
# print("뒤 7자리(뒤에서부터) : "+jumin[-7:]) #맨 뒤에서 7번째부터 



# ######### 문자열처리 함수 ##########

# python = "python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("python","Java"))

# index = python.index("n") #문자가 몇번째에 존재하는지
# print(index)
# index = python.index("n",index+1) #2번째 문자 찾기
# print(index)

# print(python.find("n"))
# print(python.find("Java")) #원하는 문자가 없을 경우 -1을 반환
# print(python.index("Java")) #에러 발생

# print(python.count("n")) #원하는 문자 갯수 반환

# ########## 문자열 포맷 ############
# print("a"+"b")
# print("a","b")

# # (방법 1)
# print("나는 %d살입니다." % 20)
# print("나는 %s를 좋아해요" %'파이썬')
# print("Apple 은 %c로 시작해요." % 'A')
# age = 20
# color = "빨간"
# print("나는 %d살이며 %s색을 좋아해요" %(age, color))

# #s
# print("나는 %s살입니다." % 20)
# print("나는 %s색과 %s색을 좋아해요" %("파란","빨간"))


# # (방법 2)
# print("나는 {}살 입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요".format("파란","빨간"))
# print("나는 {1}색과 {0}색을 좋아해요".format("파란","빨간"))

# # (방법 3)
# print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20,color="빨간"))

# # (방법 4)
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며 {color}색을 좋아해요.")

# ############ 탈출 문자 ###############

# # \" \' : 문장 내에서 따옴표

# print("백문이 불여일견 \n백견이 불여일타")
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print("저는 \'나도코딩\'입니다.")

# # \\ : 문장내에서 \
# print("C:\\Users\\오태화\\Desktop\\pyton workspace>")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스(한 글자 삭제)
# print("Redd\bApple")

# # \t : 탭
# print("Red\tApple")


# # 사이트별로 비밀번호를 마들어 주는 프로그램을 작성하시오
# # http://naver.com

# cite = "http://naver.com"
# findCiteName = cite[7:12]
# print("%s"% findCiteName)
# MakePassword = findCiteName[:3],len(findCiteName),findCiteName.count("e"),"!"
# print("%s%d%d%s"% MakePassword)


# # 풀이
# url = "http://naver.com"
# my_str = url.replace("http://", "")
# print(my_str)
# my_str = my_str[:my_str.index(".")]
# print(my_str)
# password = my_str[:3] + str(len(my_str)) + str(my_str.count('e')) + '!'
# print(password)


# ########### 리스트 ############

# # 지하철 칸 별로 10명, 20명, 30명
# subway1 = 10
# subway2 = 20
# subway3 = 30

# subway = [10, 20, 30]
# print(subway)

# subway = ["유재석","조세호","박명수"] # 0, 1, 2번째
# print(subway)

# # 조세호씨가 몇 번째 칸에 타고 있는가?
# print(subway.index("조세호"))

# # 하하씨가 다음 정류장에서 다음 칸에 탐
# subway.append("하하") 
# print(subway)

# # 정형돈씨를 유재석/조세호 사이에 태움
# subway.insert(1,"정형돈")
# print(subway)

# # 지하철에 있는 사람을 한 명씩 뒤에서 꺼냄
# print(subway.pop())
# print(subway)

# # 같은 이름의 사람이 몇 명 있는지 확인
# subway.append("유재석")
# print(subway.count("유재석"))

# # 정렬
# num_list = [5,2,4,3,1]
# num_list.sort()
# print(num_list)

# #순서 뒤집기 가능
# num_list.reverse()
# print(num_list)

# #모두 지우기
# num_list.clear()
# print(num_list)

# # 다양한 자료형 함께 사용
# mix_list = ["조세호",20,True]
# print(mix_list)

# # 리스트 확장
# num_list.extend(mix_list)
# print(num_list)


# ############### 사전 ################# 
# cabinet = {3:"유재석", 100:"김태호"}
# print(cabinet[3])
# print(cabinet[100])

# print(cabinet.get(3))
# #print(cabinet[5])
# print(cabinet.get(5))
# print("hi")
# print(cabinet.get(5,"사용 가능"))

# cabinet = {3:"유재석", 100:"김태호"}
# print(3 in cabinet)
# print(5 in cabinet)


# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet.get("A-3"))

# # 새 손님
# print(cabinet)
# cabinet["C-20"] = "조세호"
# print(cabinet)
# print(cabinet.get("C-20"))
# cabinet["A-3"] = "김종국"
# print(cabinet.get("A-3"))

# # 간 손님
# del cabinet["A-3"]
# print(cabinet)

# # key 들만 출력
# print(cabinet.keys())

# # value 들만 출력
# print(cabinet.values())

# # key value 둘다 출력
# print(cabinet.items())

# # 목욕탕 페점
# cabinet.clear()
# print(cabinet)

# ########### 튜플 ############# 
# # // 값 추가,변경 불가

# menu = ("돈까스","치즈까스")
# print(menu)

# name = "김종국"
# age =20
# hobby = "코딩"
# print(name,age,hobby)

# name, age, hobby = "김종국" , 20, "코딩"
# print(name, age, hobby)

# ########## 세트(집합) ############ 
# # //중복 x , 순서 x
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석","김태호","양세형"}
# python = set(["유재석","박명수"])

# # 교집합 (java 와 python을 모두 할 수 있는 사람)
# print(java & python)
# print(java.intersection(python))

# # 합집합 (java도 할 수 있거나 python도 할 수 있는 사람)
# print(java | python)
# print(java.union(python))

# # 차집합 (java를 할 수 있지만 python을 할 줄 모르는 사람)
# print(java-python)
# print(java.difference(python))

# # python 할 줄 아는 사람이 늘어남
# python.add("김태호")
# print(python)

# # java를 잊었어요
# python.remove("김태호")
# print(java)

# ########## 자료구조의 변경 ############
# menu = {"커피","우유","주스"}
# print(menu,type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu,type(menu))

# # 추첨 프로그램

# from random import*
# print(" --- 당첨자 발표 --- ")
# lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20] 
# shuffle(lst)
# chicken = sample(lst,1)
# print("치킨 당점자 : " + str(chicken))
# lst = set(lst)
# chicken = set(chicken)
# lst = lst - chicken
# lst = list(lst)
# shuffle(lst)
# coffee = sample(lst,3)
# print("커피 당첨자 : " + str(coffee))
# print(" --- 축하합니다! --- ") 


# # (해설)
# from random import*
# users = range(1,21) #1부터 20까지 숫자를 생성
# #print(type(users))
# users = list(users)
# #print(type(users))
# shuffle(users)

# winners = sample(users,4) #4명 중에서 1명은 치킨, 나머지는 커피
# print(" --- 당첨자 발표 --- ")
# print(" 치킨 당첨자 : {0}".format(winners[0]))
# print(" 커피 당첨자 : {0}".format(winners[1:]))
# print(" --- 축하합니다 --- ")

# ############ if ##############

# weather = input("오늘 날씨는 어때요? ") #사용자의 입력값을 받음 input
# if weather == "비" or weather =="눈":
#   print("우산을 챙기세요")
# elif weather =="미세먼지" :
#     print("마스크를 챙기세요")
# else :
#     print("준비물 필요없어요")



# temp = int(input("기온은 어때요? ")) #정수형일 경우에는 int로 감싼다
# if 30<= temp :
#     print("너무 더워요, 나가지 마세요")
# elif 10<= temp and temp<30:
#     print("괜찮은 날씨에요")
# elif 0<= temp < 10:  # and를 생략한 문장
#     print("외투를 챙기세요")
# else :
#     print("너무 추워요 나가지마세요")


# ############ for ############

# for waiting_no in [0,1,2,3,4] :
#    print("대기번호 : %d" % waiting_no)

# for waiting_no in range(5) :
#     print("대기번호 : %d"%waiting_no)

# for waiting_no in range(1,6) :
#     print("대기번호 : %d" %waiting_no)


# starbucks = ["아이언맨","토르","아이엠 그루트"]
# for customer in starbucks :
#     print("%s님, 커피가 준비되었습니다"% customer)


# ########### while ##############
# customer = "토르"
# index = 5
# while index >=1 : 
#     print("%s님, 커피가 준비 되었습니다. %d번 남았어요" %(customer, index))
#     index -= 1
#     if index ==0:
#         print("커피는 폐기처분 되었습니다")

# customer = "아이언맨"
# index = 0
# while True:
#     print("%s님, 커피가 준비되었습니다. 호출 : %d회"%(customer, index))
#     index +=1  # ctrl +c 로 프로그램 종료

# customer = "토르"
# person = "unknown"

# while person != customer :
#     print("%s님, 커피가 준비되었습니다" %customer)
#     person = input("이름이 어떻게 되세요? ")
#     if person == customer :
#       print("커피 가져가세요~!!")


# ######### continue / break ##########
# absent = [2,5] #결석
# no_book = [7] #책을 갖고오지 않음
# for student in range(1,10) :
#     if student in absent : 
#         continue
#     elif student in no_book :
#         print("오늘 수업 여기까지,, %d는 교무실로 따라와" %student)
#         break
#     else :
#         print("%d야 책을 읽어줘"%student)


# # 출석번호가 1 2 3 4, 앞에 100을 붙이기로함  -> 101, 102, 103 , 104
# students = [1,2,3,4,5]
# print(students)
# students = [i +100 for i in students]
# print(students)   


# # 학생 이름을 길이로 변환
# students = ["Iron man","Thor","I am groot"]
# print(students)
# students = [len(i) for i in students]
# print(students)


# # 학생 이름을 대문자로 변환
# students =["Iron man", " Thor", "I am groot"]
# students = [i.upper() for i in students]
# print(students)



# # 50명의 승객과 매칭
# # 조건1 : 승객별 운행 소요시간을 5-50분 사이로 난수설정
# # 조건2 : 소요시간 5-15분 사이의 승객만 매칭해야함

# #출력문 예제
# # {0} 1번째손님 (소요시간 : 14분)
# # { } 2번째손님 (소요시간 : 40분)
# # { } 3번째손님 (소요시간 : 2분)
# #.... {0} 50번째손님 (소요시간 : 15분)

# # 총 탑승 승객 : n 인

# from random import*
# print(" ===== COCOA TAXI SERVICE =====\n")
# customer = randint(1,50)
# index = 1
# totalCustomer =0

# while index <= 50 :
#     elapsedTime = randint(5,50)
#     if elapsedTime<= 15 and elapsedTime>=5 :
#        print(" (0) %d번째 손님 (소요시간 : %d분)\n"%(index, elapsedTime)) 
#        index += 1
#        totalCustomer +=1
#     else :
#         print(" ( ) %d번째 손님 (소요시간 : %d분)\n"%(index, elapsedTime))
#         index += 1

#     if index ==50 :
#         print(" 총 탑승 승객 : %d 인"%totalCustomer)
#         break


# # 해설

# from random import*
# cnt = 0 #총 탑승 승객수
# for i in range(1,51) : # 1 - 50 사이의 수 (승객)
#     time = randrange(5,51) # 5분 -15분 사이의 시간
#     if 5 <= time <= 15 : 
#         print("[0] %d번째 손님 (소요시간 : %d)" %(i, time))
#         cnt += 1
#     else : 
#         print("[ ] %d번째 손님 (소요시간 : %d)"%(i, time))

# print ( "총 탑승 승객 : %d분 "%cnt)


# ########## 함수 #############

# def open_account () :
#     print("새로운 계좌가 생성되었습니다.")

# def deposit(balance, money) :
#     print("입금이 완료되었습니다. 잔액은 %d원 입니다"%(balance + money))
#     return balance + money

# def withdraw(balance, money) :
#     if balance >= money : # 잔액이 출금보다 많으면 출금 가능
#         print("출금이 완료되었습니다. 잔액은 %d 원입니다."%(balance - money))
#         return balance - money
#     else :
#         print("출금이 완료되지 않았습니다. 잔액은 %d원입니다."%balance)

# def withdraw_night(balance,money) : #저녁에 출금(수수료 있음)
#     comission = 100
#     return comission, balance - money - comission

# open_account()
# balance = 0 #잔액
# balance = deposit(balance, 1000) #함수 내 print값 및 반환값 반환
# balance = withdraw(balance, 500)
# comission, balance = withdraw_night(balance, 300)
# print(balance) #return값 호출
# print("수수료는 %d원이며, 잔액은 %d원입니다."%(comission, balance))



# # 기본값
# def profile(name,age,main_language) :
#     print("이름 : %s\n나이 : %d\n주 사용 언어 : %s"%(name,age,main_language))

# profile("오태경",24,"python")
# profile("오태화",26,"C++")

# # 같은 학교 같은 학년 같은 반 같은 수업
# # 나이와 언어는 모두 같음
# def profile(name,age=17,main_language="파이썬") :
#     print("이름 : %s\n나이 : %d\n주 사용 언어 : %s"%(name,age,main_language))

# profile("유재석")
# profile("김태호")


# # 키워드값
# def profile(name, age, main_lang) :
#     print(name, age, main_lang)

# profile(name = "유재석",main_lang="파이썬",age =20)


# # 가변인자
# def profile(name, age, *language) : 
#     print("이름 : %d\t나이 : %d\t"%(name, age),end = " ") # end -> 줄바꿈 안하고 이어서 출력
#     for lang in language :
#         print(lang,end="")
#     print()    


# print("유재석",20,"python","C","C++","Java","C#","JacaScript")
# print("김태호",25,"kotlin","Swift")    


# # 지역변수와 전역변수

# gun = 10
# def checkpoint(soldiers) : #경계근무
#     global gun #전역 공간에 있는 gun 사용
#     gun = gun - soldiers 
#     print("[함수 내] 남은 총 : %d"%gun)

# def checkpoint_ret(gun,soldiers) :
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : %d"%gun)
#     return gun

# print("전체 총 : %d"%gun)
# gun = checkpoint_ret(gun,2) #2명이 경계근무 나감
# print("남은 총 : %d"%gun)


# # 표준 체중 구하기
# # 표준 체중 : 각 개인의 키에 적당한 체중
# #(성별에 따른 공식)
# # 남자 = 키(m) X 키(m) X 22
# # 여자 = 키(m) X 키(m) X 21

# # 조건1 : 표준 체중은 별도의 함수 내에서 계산
# # 함수명 : std_weight   전달값 : 키(height), 성별(gender)

# # 조건 2 : 표준 체중은 소수점 둘째자리까지 표시

# # (출력 예제)
# # 키 175cm 남자의 표준 체중은 67.38kg입니다.
# def std_weight(height, gender) : 
#     if gender == "man" :
#         return height * height * 22
#     elif gender == "woman" :
#         return height * height * 21

# def transform(height) : 
#     meterheight = height * 100
#     return meterheight

# print(" =========== 표준 체중 구하기 ===========\n")
# print(" (남성은 man,  여성은 woman을 입력해주세요)\n")

# gender = input(" 성별을 입력하세요 : ")
# height = float(input(" 본인의 키(m)를 입력하세요 : "))

# print(" 키 %dcm의 표준 체중은 %.2fkg입니다."%(transform(height),std_weight(height,gender)))



# ########## 표준 입출력 ############

# print("Python","Java")
# print("Python"+"Java")

# print("Python","Java",sep=",")
# print("Python","Java",sep=",",end=" ?\n")
# print("무엇이 더 재밌을까요?")

# import sys

# print("Python","Java",file=sys.stdout)
# print("Python","Java",file=sys.stderr)


# scores = {"수학":0, "영어":50, "코딩":100}
# for subject, score in scores.items() :  #.items -> subject와 score모두 보내줌
#    # print(subject, score)
#    print(subject.ljust(8),str(score).rjust(4), sep=":") #.ljust -> 8개의 공간을 만들고 왼쪽으로 졍렬
#                                                #.rjust -> 4개의 공간을 만들고 오른쪽으로 정렬

# # 은행 대기 순번표
# # 001, 002, 003, ....
# for num in range(1,21) :
#     print("대기번호 : " + str(num).zfill(3)) #.zfill -> 3개의 공간을 만들고 남은 공간을 0으로 채움


# answer = input("아무 값이나 입력하세요 : ")
# print("입력하신 값은 "+answer+"입니다.")
# # 사용자 입력값은 무조건 문자열 형태로 출력됨 ,,



# # 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
# print("{0: >10}".format(500)) # 빈자리는 -> space로 넣고 오른쪽 정렬을 하되 10자리 공간을 확보하여 500을 출력하여라

# # 양수일때는 +로 표시, 음수일 땐 -로 표시 
# print("{0: >+10}".format(500))
# print("{0: >-10}".format(-500))

# # 왼쪽 정렬하고, 빈칸을 _로 채움
# print("{0:_<+10}".format(500))

# # 3자리마다 .(comma)를 찍어주기
# print("{0:,}".format(10000000000))

# # 3자리마다 .를 찍어주기, +-부호도 붙이기
# print("{0:+,}".format(10000000000))

# # 3자리마다 콤마를 찍어주기, 부호도 붙이고, 자릿수 확보하기
# # 빈자리는 ^로 채워주기
# print("{0:^<+30,}".format(100000000000000000))

# # 소수점 출력
# print("{0:f}".format(5/3))
# print("{0:.2f}".format(5/3))



# ########### 파일 입출력 ############

# score_file = open("score.txt","w",encoding="utf8") #utf9 -> 한글파일
# print("수학 : 0", file=score_file)
# print("영어 : 50",file=score_file)
# score_file.close()


# score_file = open("score.txt","a",encoding="utf8")
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()



# score_file = open("score.txt","r",encoding ="utf8")
# print(score_file.read())
# score_file.close()


# score_file = open("score.txt","r",encoding="utf8")
# print(score_file.readline(),end="") # 줄 별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
# print(score_file.readline(),end="") # end="" -> 줄바꿈 x
# print(score_file.readline(),end="")
# print(score_file.readline(),end="")
# score_file.close()


# score_file = open("score.txt","r",encoding="utf8")
# while True : 
#      line = score_file.readline()
#      if not line : 
#          break
#      print(line)
# score_file.close()


# score_file = open("score.txt","r",encoding="utf8")
# lines = score_file.readlines() #list 형태로 저장
# for line in lines : 
#     print(line,end="")
# score_file.close()



# ############ pickle ################
# # 프로그램에서 사용하는 데이터를 파일형태로 저장하는 것
# import pickle
# profile_file = open("profile.pickle","wb") # wb = writing binary
# profile = {"이름":"박명수","나이":30,"취미":["축구","골프","코딩"]}
# print(profile)
# pickle.dump(profile, profile_file) #profile에 있는 정보를 file에 저장
# profile_file.close()


# import pickle
# profile_file = open("profile.pickle","rb")
# profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
# print(profile)
# profile_file.close()



# ############ with ################
# import pickle
# with open("profile.pickle","rb") as profile_file :
#     print(pickle.load(profile_file))



# with open("study.txt","w",encoding="utf8") as study_file :
#     study_file.write("파이썬을 열심히 공부하고 있어요")

# with open("study.txt","a",encoding="utf8") as study_file :
#     study_file.write("")
#     study_file.write("프로그램 공부 정말 재미있어요")

# with open("study.txt","r",encoding="utf8") as study_file :
#     print(study_file.read())



# # 매주 1회 작성 보고서
# # -- x 주차 주간보고 --
# # 부서 : 
# # 이름 :
# # 업무 요악 :

# # 1주차부터 50주차까지의 보고서 파일 만드는 프로그램 작성
# # 조건 : 파일명은 '1주차.txt', '2주차.txt', ...와 같이 만듦

# from random import*
# for week in range(1,51) :
#    with open("%d주차.txt"%week, "w", encoding= "utf8") as report_file :
#        report_file.write("==== %d주차 주간보고 ====\n"%week)
#        report_file.write("Department : \n")
#        report_file.write("Name : \n")
#        report_file.write("Summary of Work : \n")


# from random import*
# for week in range(1,51) :
#    with open("%d주차.txt"%week, "r", encoding= "utf8") as report_file :
#     print(report_file.read())



# ########### 클래스 #############

# # 마린 : 공격 유닛, 군인, 총을 쏠 수 있음
# name = "마린" #유닛의 이름
# hp = 40 # 유닛의 체력
# damage = 5 # 유닛의 공격력

# print("%s 유닛이 생성되었습니다."%name)
# print("체력 : %d, 공격력 : %d"%(hp,damage))

# # 탱크 : 공격 유닛, 탱크, 포를 쏠 수 있음, 일반 모드/시즈 모드
# tank_name = "탱크"
# tank_hp =150
# tank_damage = 35

# print("%s 유닛이 생성되었습니다."%tank_name)
# print("체력 : %d, 공격력 : %d"%(tank_hp,tank_damage))

# def attack(name, location, damage) :
#     print("%s : %s 방향으로 적군을 공격합니다. [공격력 : %d]"%(\
#         name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "12시", tank_damage)

# tank2_name = "탱크"
# tank2_hp =150
# tank2_damage = 35

# print("%s 유닛이 생성되었습니다."%tank2_name)
# print("체력 : %d, 공격력 : %d"%(tank2_hp,tank2_damage))


# class unit : 
#     def __init__(self, name, hp, damage) :
#      self.name = name 
#      self.hp = hp
#      self.damage = damage
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))


# marine = unit("마린", 40, 5)
# marine2 = unit("마린", 40, 5)
# tank = unit("탱크",150,35)  



# # __init__ -> 생성자 
# # marine, tank -> 객체(class로 부터 만들어지는 것들)

# # 멤버 변수 (self.~) -> class 내에서 정의된 변수

# # 레이스 : 공중 유닛, 비행기, 클로킹(상대방에게 보이지 않음)
# wraith1 = unit("레이스",80,5)
# print("유닛 이름 : %s, 공격력 : %d"%(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것(빼앗음)
# wraith2 = unit("빼앗은 레이스",80,5)
# wraith2.clocking = True

# if wraith2.clocking == True :
#     print("%s는 현재 클로킹 상태입니다."%wraith2.name)




# ############# 메소드 #################

# class unit : 
#     def __init__(self, name, hp, damage) :
#      self.name = name 
#      self.hp = hp
#      self.damage = damage
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))


# class AttackUnit :
#     def __init__(self, name, hp, damage) :
#      self.name = name 
#      self.hp = hp
#      self.damage = damage
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))

#     def attack(self, location) :
#      print("%s : %s 방향으로 적군을 공격합니다. [공격력 %d]" \
#          %(self.name, location, self.damage))  # location -> 변수

#     def damaged(self, damage) : 
#      print("%s : %d 데미지를 입었습니다." %(self.name, damage))
#      self.hp -= damage
#      print("%s : 현재 체력은 %d 입니다."%(self.name, self.hp)) 
#      if self.hp <= 0 :
#         print("%s : 파괴되었습니다."%self.name)

# # 파이어뱃 : 공격유닛, 화염방사기
# firebat1 = AttackUnit("파이어뱃",50,16) 
# firebat1.attack("5시")
# firebat1.damaged(25)
# firebat1.damaged(25)         


# ############## 상속 ##############  
# # //class unit 과 class attackunit의 구성이 꽤 비슷하므로 class unit의 정보를 상속받을 수 있음,,
# # 메딕 : 의무병

# # 일반 유닛
# class unit : 
#     def __init__(self, name, hp) :
#      self.name = name 
#      self.hp = hp


# # 공격 유닛
# class AttackUnit(unit) :
#     def __init__(self, name, hp, damage) :
#      unit.__init__(self, name, hp)
#      self.damage = damage
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))

#     def attack(self, location) :
#      print("%s : %s 방향으로 적군을 공격합니다. [공격력 %d]" \
#          %(self.name, location, self.damage))  # location -> 변수

#     def damaged(self, damage) : 
#      print("%s : %d 데미지를 입었습니다." %(self.name, damage))
#      self.hp -= damage
#      print("%s : 현재 체력은 %d 입니다."%(self.name, self.hp)) 
#      if self.hp <= 0 :
#         print("%s : 파괴되었습니다."%self.name)

# ############## 다중상속 ###################
# # 드랍쉽 : 공중유닛, 수송기, 공격 불가

# # 날 수 있는 기능을 가진 클래스
# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location) :
#         print("%s : %s 방향으로 날아갑니다. [속도 : %d]"\
#             %(name, location, self.flying_speed))

    
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed) :
#        AttackUnit.__init__(self, name, hp, damage)
#        Flyable.__init__(self, flying_speed)


# # 발키리 : 공중 공격 유닛, 한번에 14발 미사일 발사
# valkyrie = FlyableAttackUnit("발키리",200,6,5)
# valkyrie.fly(valkyrie.name, "3시")




# # 메소드 오버로딩 -> 자식 메소드에서 클래스 사용
# # 일반 유닛
# class unit : 
#     def __init__(self, name, hp, speed) :
#      self.name = name 
#      self.hp = hp
#      self.speed = speed
#     def move(self, location) : 
#         print("[지상 유닛 이동]")
#         print("%s : %s 방향으로 이동합니다. [속도 : %d]"\
#             %(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(unit) :
#     def __init__(self, name, hp, damage, speed) :
#      unit.__init__(self, name, hp, speed)
#      self.damage = damage
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))

#     def attack(self, location) :
#      print("%s : %s 방향으로 적군을 공격합니다. [공격력 %d]" \
#          %(self.name, location, self.damage))  # location -> 변수

#     def damaged(self, damage) : 
#      print("%s : %d 데미지를 입었습니다." %(self.name, damage))
#      self.hp -= damage
#      print("%s : 현재 체력은 %d 입니다."%(self.name, self.hp)) 
#      if self.hp <= 0 :
#         print("%s : 파괴되었습니다."%self.name)

# # 날 수 있는 기능을 가진 클래스
# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location) :
#         print("%s : %s 방향으로 날아갑니다. [속도 : %d]"\
#             %(name, location, self.flying_speed))

    
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed) :
#        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
#        Flyable.__init__(self, flying_speed)

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 벌쳐 : 지상 유닛, 기동성이 좋음
# vulture = AttackUnit("벌쳐",80,10,20)

# # 배틀크루저 : 공중 유닛, 체력도 굉장히 좋음, 공격력도 좋음
# battlecruiser = FlyableAttackUnit("배틀크루저",500,25,3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")




# # 일반 유닛
# class unit : 
#     def __init__(self, name, hp, speed) :
#      self.name = name 
#      self.hp = hp
#      self.speed = speed
#     def move(self, location) : 
#         print("[지상 유닛 이동]")
#         print("%s : %s 방향으로 이동합니다. [속도 : %d]"\
#             %(self.name, location, self.speed))

# # 공격 유닛
# class AttackUnit(unit) :
#     def __init__(self, name, hp, damage, speed) :
#      unit.__init__(self, name, hp, speed)
#      self.damage = damage
     
#      print("%s 유닛이 생성되었습니다."%(self.name))
#      print("체력 : %d, 공격력 : %d" %(self.hp, self.damage))

#     def attack(self, location) :
#      print("%s : %s 방향으로 적군을 공격합니다. [공격력 %d]" \
#          %(self.name, location, self.damage))  # location -> 변수

#     def damaged(self, damage) : 
#      print("%s : %d 데미지를 입었습니다." %(self.name, damage))
#      self.hp -= damage
#      print("%s : 현재 체력은 %d 입니다."%(self.name, self.hp)) 
#      if self.hp <= 0 :
#         print("%s : 파괴되었습니다."%self.name)

# # 날 수 있는 기능을 가진 클래스
# class Flyable :
#     def __init__(self, flying_speed) :
#         self.flying_speed = flying_speed
    
#     def fly(self, name, location) :
#         print("%s : %s 방향으로 날아갑니다. [속도 : %d]"\
#             %(name, location, self.flying_speed))

    
# # 공중 공격 유닛 클래스
# class FlyableAttackUnit(AttackUnit, Flyable) :
#     def __init__(self, name, hp, damage, flying_speed) :
#        AttackUnit.__init__(self, name, hp, 0, damage) # 지상 speed = 0
#        Flyable.__init__(self, flying_speed)

#     def move(self, location) :
#         print("[공중 유닛 이동]")
#         self.fly(self.name, location)


# # 건물 생성
# class BuildingUnit(unit) :
#     def __init__(self, name, hp, location) :
#         # unit.__init__(self, name, hp, 0)
#         super().__init__(name, hp, 0) # 다중 상속일 경우 처음 것만 상속됨
#         self.location = location

# 서플라이 디폿 : 건물, 1개 건물 = 8개 만큼의 유닛 생성
# suppy_depot = BuildingUnit("서플라이 디폿", 500, "7시")

#def game_start() :
    #print("[알림] 새로운 게임을 시작합니다.")

#def game_over() :
    #pass

#game_start()
#game_over()



# class House :
#     def __init__(self, location,house_type,deal_type,price,completion_year) :
#         self.location = location
#         self.house_type = house_type
#         self.deal_type = deal_type
#         self.price = price
#         self.completion_year=completion_year
#     def show_detail(self) :
#         print(self.location,self.house_type,self.deal_type,self.price,self.completion_year)


# houses = []
# house1 = House("강남","아파트","매매","10억","2010년")
# house2 = House("마포","오피스텔","전세","5억","2007년")
# house3 = House("송파","빌라","월세","500/50","2000년")

# houses.append(house1)
# houses.append(house2)
# houses.append(house3)

# print("총 {0}대의 매물이 있습니다\n".format(len(houses)))
# for house in houses:
#     house.show_detail()



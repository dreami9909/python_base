# # 사이트별 비밀번호 만들기
# pagename = input("사이트의 주소를 입력하세요 : ")
# cuthttps = pagename.replace("http://","")
# findot = cuthttps.find('.')
# sitename = cuthttps[:findot]
# password = sitename[:3] + str(len(sitename)) + str(sitename.count('e')) + '!'
# print("생성된 비밀번호는 {}입니다.".format(password))

# list = []
# dictionary = {key:값} # del dictionary[key]
# tuple = ()
# set = {} // 중복 x

############ 다중상속 ###########

# class attackunit :
# class flyable :
# class flyableattackunit(attackunit, flyable) : # 다중상속

########### 오버라이딩 ############
# 함수 재정의 -> 다른 클래스에서 정의된 함수를 호출하여 함수를 재정의함

########### pass #############
#그냥 넘어가기

########## super #############
# Unit.__init(self,a,b,c) -> super().__init(a,b,c) 


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



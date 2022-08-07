# 사이트별 비밀번호 만들기
pagename = input("사이트의 주소를 입력하세요 : ")
cuthttps = pagename.replace("http://","")
findot = cuthttps.find('.')
sitename = cuthttps[:findot]
password = sitename[:3] + str(len(sitename)) + str(sitename.count('e')) + '!'
print("생성된 비밀번호는 {}입니다.".format(password))


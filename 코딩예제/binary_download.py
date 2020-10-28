# 모듈을 읽어 드립니다.
from urllib import request

#urlopen() 함수로 구글의 메인페이지를 읽습니다.
target=request.urlopen("http://www.hanbit.co.kr/images/common/logo_hanbit.png")
output=target.read()
print(output)

# write binary 모드로
file=open("output.png", "wb")
file.write(output)
file.close()

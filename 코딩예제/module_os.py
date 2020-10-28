from os import *

# 기본 정보를 몇 개 출력해 봅시다.
print("현재 운영체제:", name)
print("현재 폴더:", getcwd())
print("현재 폴더 내부의 요소:", listdir())

# 폴더를 만들고 제거합니다.[폴더가 비어있을 때만 제거 가능].
mkdir("hello")
rmdir("hello")

# 파일을 생성하고 + 파일 이름을 변경합니다.
with open("original.txt", "w") as file:
    file.write("hello")
rename("original.txt", "new.txt")

# 파일을 제거합니다.
remove("new.txt")
# unlink("new.txt")

# 시스템 명령어 실행
system("dir")

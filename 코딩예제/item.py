# 변수를 선언합니다.
example_dictionary={
    "키a": "값a",
    "키b": "값b",
    "키c": "값c",
    }

# 딕셔너리의 item() 함수 결과 출력하기
print("# 딕셔너리의 item() 함수")
print("item():", example_dictionary.items())
print()

# for 반복문과 item() 함수 조합해서 사용하기
print("# 딕셔너리의 item() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print("dictionary[{}]={}".format(key, element))

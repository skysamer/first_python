# test_module.py 파일
PI=3.141592

def number_input():
    output=input("숫자 입력>")
    return float(output)

def get_circumstance(radius):
    return 2*PI*radius

def get_circle_area(radius):
    return PI*radius**2

# 5-9 f_string_example.py
import datetime

name = "김철수"
age = 25
pi = 3.14159
price = 1234
percentage = 0.855
today = datetime.date(2025, 7, 20)

print(f"이름: {name}, 나이: {age}")
print(f"원주율: {pi:.2f}")
print(f"가격: {price:,}원")
print(f"퍼센트: {percentage * 100:.2f}%")
print(f"날짜: {today:%Y년 %m월 %d일}")
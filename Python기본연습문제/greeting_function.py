# 6-3 greeting_function.py
def greet(name, message="안녕하세요", suffix="님!"):
    print(f"{message}, {name}{suffix}")

greet("김철수")
greet("John", "Hello", "!")
greet("이영희", "안녕하세요", "님! 좋은 하루 되세요!")
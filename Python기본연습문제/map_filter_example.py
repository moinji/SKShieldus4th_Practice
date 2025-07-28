# 5-7 map_filter_example.py
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"원본 숫자: {numbers}")

squares = list(map(lambda x: x ** 2, numbers))
print(f"모든 수의 제곱: {squares}")

greater_than_5 = list(filter(lambda x: x > 5, numbers))
print(f"5보다 큰 수들: {greater_than_5}")

gt5_squared = list(map(lambda x: x ** 2, greater_than_5))
print(f"5보다 큰 수들의 제곱: {gt5_squared}")
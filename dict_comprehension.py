# 5-5 dict_comprehension.py
squares = {i: i ** 2 for i in range(1, 6)}
even_squares = {i: i ** 2 for i in range(1, 11) if i % 2 == 0}

print(f"1부터 5까지의 제곱 딕셔너리: {squares}")
print(f"짝수만의 제곱 딕셔너리: {even_squares}")
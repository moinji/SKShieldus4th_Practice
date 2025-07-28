# 3-8 remove_duplicates.py
original = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
unique_sorted = sorted(set(original))
print(f"원본 리스트: {original}")
print(f"중복 제거 후: {unique_sorted}")
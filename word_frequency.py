# 7-3 word_frequency.py
from collections import Counter

text = '''파이썬은 프로그래밍 언어입니다. 파이썬은 배우기 쉬운 언어입니다. 
파이썬은 강력한 언어입니다.'''

words = text.replace("\n", " ").replace(".", "").split()
count = Counter(words)

print("단어 빈도 분석 결과:")
for word, freq in count.items():
    print(f"{word}: {freq}번")
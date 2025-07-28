# 2-4 word_counter.py
sentence = input("문장을 입력하세요: ").strip()
cleaned = ' '.join(sentence.split())
word_count = len(cleaned.split())
print(f"공백 제거: {cleaned}")
print(f"단어 개수: {word_count}개")
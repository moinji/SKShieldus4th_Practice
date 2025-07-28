# 3-7 word_length.py
words = ['cat', 'elephant', 'dog', 'butterfly', 'ant']
longest = max(words, key=len)
shortest = min(words, key=len)
print(f"단어 목록: {words}")
print(f"가장 긴 단어: {longest} ({len(longest)}글자)")
print(f"가장 짧은 단어: {shortest} ({len(shortest)}글자)")
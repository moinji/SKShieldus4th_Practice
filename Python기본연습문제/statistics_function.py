# 6-4 statistics_function.py
import math

def analyze_list(numbers):
    avg = sum(numbers) / len(numbers)
    max_val = max(numbers)
    min_val = min(numbers)
    variance = sum((x - avg) ** 2 for x in numbers) / len(numbers)
    std_dev = math.sqrt(variance)
    return avg, max_val, min_val, std_dev

nums = [10, 20, 30, 40, 50]
avg, max_val, min_val, std_dev = analyze_list(nums)
print(f"숫자들: {nums}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std_dev:.2f}")
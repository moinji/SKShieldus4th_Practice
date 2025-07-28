# 7-2 csv_grade_processor.py
import csv

grades = [['김철수', 85], ['이영희', 92], ['박민수', 78], ['최수진', 95]]

with open("grades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(grades)

print("학생 성적이 grades.csv에 저장되었습니다.\n")

print("성적 분석 결과:")
total = 0
for name, score in grades:
    print(f"{name}: {score}점")
    total += score
print(f"전체 평균: {total / len(grades):.1f}점")

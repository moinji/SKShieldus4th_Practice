# 8-3 system_info.py
import os
import sys

print(f"현재 작업 디렉토리: {os.getcwd()}")
print(f"Python 버전: {sys.version}")
print(f"운영체제: {os.name}")
print(f"환경 변수 PATH 일부: {os.environ.get('PATH', '')[:40]}")

file_path = "/Users/username/documents/report.txt"
dirname, filename = os.path.split(file_path)
name, ext = os.path.splitext(filename)

print("파일 경로 정보:")
print(f"- 디렉토리: {dirname}")
print(f"- 파일명: {name + ext}")
print(f"- 확장자: {ext}")
print(f"파일 존재 여부: {os.path.exists(file_path)}")
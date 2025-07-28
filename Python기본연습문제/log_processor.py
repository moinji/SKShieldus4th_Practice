# 7-5 log_processor.py
import logging

logging.basicConfig(filename='app.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

logging.warning("메모리 사용량이 높습니다")
logging.error("데이터베이스 연결 실패")
logging.warning("디스크 공간 부족")
logging.error("파일을 찾을 수 없음")

print("로그 파일이 생성되었습니다.\n")

print("ERROR 레벨 로그들:")
with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

print("\nWARNING 레벨 로그들:")
with open("app.log", "r", encoding="utf-8") as f:
    for line in f:
        if "WARNING" in line:
            print(line.strip())

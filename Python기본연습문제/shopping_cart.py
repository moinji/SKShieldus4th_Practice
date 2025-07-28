# 3-5 shopping_cart.py
cart = {
    '사과': {'수량': 2, '가격': 1000},
    '바나나': {'수량': 3, '가격': 800},
    '오렌지': {'수량': 1, '가격': 1500}
}
print("쇼핑 카트:")
total = 0
for item, info in cart.items():
    item_total = info['수량'] * info['가격']
    total += item_total
    print(f"{item}: {info['수량']}개 (개당 {info['가격']}원) = {item_total}원")
print(f"총 가격: {total}원")
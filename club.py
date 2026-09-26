people = [
    {"name": "Орлов", "grade": 7, "hours": 12},
    {"name": "Белова", "grade": 9, "hours": 20},
    {"name": "Шаров", "grade": 10, "hours": 16},
    {"name": "Новикова", "grade": 8, "hours": 9}
]

def label(per):
    return f"фамилия: {per['name']}, {per['grade']} класс, {per['hours']} ч."

for p in people:
    text = label(p)
    print(text)
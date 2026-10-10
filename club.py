import csv

people = []

def person(row):
    return {"name":row['name'], "grade":int(row['grade']), "hours":int(row['hours'])}
with open('club.csv', encoding='utf-8') as f:
    reader = csv.DictReader(f)

    total = 0
    for row in reader:
        row_int = person(row)
        people.append(row_int)
        total += row_int["hours"]
print(total)




try:
    with open('SUN.csv', 'w', encoding='utf-8', newline="") as f:
        write = csv.DictWriter(f, fieldnames=["name", "grade", "hours"])
        write.writeheader()

        for row in people:
            if row['grade'] >= 9:
                write.writerow(row)
except FileNotFoundError:
    print("ошибка, ля ля ля")
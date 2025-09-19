courses = []

with open("dados/courses.csv","r", encoding=("utf-8")) as file:
    for line in file:
        language, category = line.strip().split(",")
        course = {}
        course["language"] = language
        course["category"] = category
        courses.append(course) 

print(courses)

for course in sorted(courses, key=lambda c: c["language"]):
    print(f"{course['language']} - {course['category']}")
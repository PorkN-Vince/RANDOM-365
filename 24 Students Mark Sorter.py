students= {
    "Student 1": 85,
    "Student 2": 92,
    "Student 3": 78,
    "Student 4": 90,
}

rank = sorted(students.items(), key=lambda x: x[1], reverse=True)


for key, value in rank:
    print(key, " got", value, " marks.")
grades = {"Swaraj": 90, "Aayush": 96, "Rudra": 92, "Samaksh": 88, "Harshwardan": 73}
total = 0
for name in grades:
    total = total + grades[name]
average = total / len(grades)
print("Class average:", average)
top_name = ""
top_score = 0
for name in grades:
    if grades[name] > top_score:
        top_name = name
        top_score = grades[name]
print("Highest score:", top_name, top_score)
lookup = input("Look up a student: ")
print("Score:", grades.get(lookup, "Not found"))

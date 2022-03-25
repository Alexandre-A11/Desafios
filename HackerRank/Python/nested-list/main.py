if __name__ == "__main__":
    students_names = []
    students_scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students_names.append(name)
        students_scores.append(score)
    second_smallest = sorted(set(students_scores))[1]
    index = students_scores.index(second_smallest)
    students_names_smaller = []
    for i in range(len(students_names)):
        if students_scores[i] == second_smallest:
            students_names_smaller.append(students_names[i])
    for name in sorted(students_names_smaller):
        print(name)

# Testes:
# students = [
#     "Harry",
#     37.21,
#     "Berry",
#     37.21,
#     "Tina",
#     37.2,
#     "Akriti",
#     41,
#     "Harsh",
#     39,
# ]

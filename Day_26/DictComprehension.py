import random


# new_dict = {new_key : new_value for item in list}

# new_dict = {new_key : new_value for (key, value) in dict.items()}

student_names = ["John", "Mark", "Peter", "Paul", "George", "Ringo", "Mike"]

students_scores = {student : random.randint(60, 100) for student in student_names}

passed_students = {student : score for (student, score) in students_scores.items() if score >= 70}
print(passed_students)
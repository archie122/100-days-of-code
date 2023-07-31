import pandas

student_data = {
    "student": ["Anastasia", "Dima", "Katherine", "James", "Emily", "Michael", "Matthew", "Laura", "Kevin", "Jonas"],
    "score" : [87, 76, 66, 98, 70, 85, 91, 21, 23, 45]
}

student_data_frame = pandas.DataFrame(student_data)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.score)
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = sorted(students)
av_grade_0 = sum(grades[0]) / len(grades[0])
av_grade_1 = sum(grades[1]) / len(grades[1])
av_grade_2 = sum(grades[2]) / len(grades[2])
av_grade_3 = sum(grades[3]) / len(grades[3])
av_grade_4 = sum(grades[4]) / len(grades[4])
av_grades = [av_grade_0,av_grade_1, av_grade_2, av_grade_3, av_grade_4]
av_grades = {students_list[0] : av_grades[0],
             students_list[1] : av_grades[1],
             students_list[2] : av_grades[2],
             students_list[3] : av_grades[3],
             students_list[4] : av_grades[4]}
print(av_grades)


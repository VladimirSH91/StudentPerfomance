from collections import defaultdict
import csv

class Student:

    def __init__(self, filename: list):
        self.filename = filename

    def get_student_grades(self, filename: list) -> defaultdict:
        student_dict = defaultdict(list)
        for file in filename:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    student = row.get('student_name')
                    grade_str = row.get('grade')
                    if student is None or grade_str is None:
                        print('Пропущено поле student_name или grade в строке, пропускаем')
                        continue
                    if not grade_str.isnumeric():
                        print(f'Некорректное значение оценки: {grade_str}, пропускаем')
                        continue
                    grade = int(grade_str)
                    student_dict[student].append(grade)
                except Exception as e:
                    print(f'Ошибка при обработке строки {row}: {e}')
                    continue
        return student_dict

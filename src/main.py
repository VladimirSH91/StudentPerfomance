import argparse
import csv
from collections import defaultdict

import tabulate

from report import GradeReport

def get_student_grades(files: str) -> dict:
    try:
        student_dict = defaultdict(list)
        for file in files:
            file = csv.DictReader(file)
            for row in file:
                student = row['student_name']
                if not row['grade'].isnumeric():
                    raise ValueError('некорректное значение')
                grade = int(row['grade'])

                student_dict[student].append(grade)

        return student_dict

    except ValueError:
        return

def average_grade(student_dict: dict) -> dict:
    average_dict = defaultdict(float)
    for key, item in student_dict.items():
        average_dict[key] = sum(item) / len(item)
    sorted_dict = dict(sorted(average_dict.items(), key=lambda i: i[1], reverse=True))
    return sorted_dict

def main():
    parser = argparse.ArgumentParser(description='student performance', exit_on_error=False)
    parser.add_argument('--files', dest='files', nargs='+',
                        type=argparse.FileType(mode='r', encoding='utf-8'))
    parser.add_argument('--report', dest='report', choices=['student-performance'])

    try:
        args = parser.parse_args()
        student_grades = get_student_grades(files=args.files)
        student_report = average_grade(student_dict=student_grades)

        report = GradeReport(report_dict=student_report, report_name="Grade Report")
        rows = report.grade_report(report_dict=student_report)
        print(tabulate.tabulate(rows, headers=['Student', 'Average Grade'], tablefmt="pipe"))

    except argparse.ArgumentError:
        print('Файл не найден')

    except AttributeError:
        print('некорретная оценка')


if __name__ == '__main__':
    main()

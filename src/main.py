import argparse
from collections import defaultdict

import tabulate

from report import GradeReport
from student import Student

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
        student_grades = Student(filename=args.files)
        grades = student_grades.get_student_grades(filename=args.files)
        student_report = average_grade(student_dict=grades)

        report = GradeReport(report_dict=student_report, report_name="Grade Report")
        rows = report.grade_report(report_dict=student_report)
        print(tabulate.tabulate(rows, headers=['Student', 'Average Grade'], tablefmt="pipe"))

    except argparse.ArgumentError:
        print('Файл не найден')

    except AttributeError or  KeyError:
        print('некорретная оценка')


if __name__ == '__main__':
    main()

import csv
import argparse
from collections import defaultdict
import tabulate


def open_file(files: str) -> dict:
    student_dict = defaultdict(list)
    for file in files:
        with open(file, 'r', encoding='Utf-8', newline='') as csvfile:
            file = csv.DictReader(csvfile)
            for row in file:
                student = row['student_name']
                grade = int(row['grade'])
                student_dict[student].append(grade)

    return student_dict


def average_grade(student_dict: dict) -> dict:
    average_dict = defaultdict(float)
    for key, item in student_dict.items():
        average_dict[key] = sum(item) / len(item)
    sorted_dict = dict(sorted(average_dict.items(), key=lambda i: i[1], reverse=True))
    return sorted_dict

parser = argparse.ArgumentParser(description='student performance')
parser.add_argument('--files', dest='files', nargs='+')
# parser.add_argument('--report', dest='report')

args = parser.parse_args()

open_file(files=args.files)
average_grade(open_file(files=args.files))

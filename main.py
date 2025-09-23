import csv
import argparse
import tabulate


def print_file(pr_file):
    for row in pr_file:
        print(row)

def open_file(files):
    with open(files, 'r', encoding='Utf-8', newline='') as csvfile:
        file = csv.reader(csvfile)
        print_file(file)


parser = argparse.ArgumentParser(description='student performance')
parser.add_argument('--files', dest='files')
# parser.add_argument('--report', dest='report')

args = parser.parse_args()

open_file(args.files)

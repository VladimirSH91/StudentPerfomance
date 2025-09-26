from io import StringIO
import main

def test_get_student_grades1():
    data1 = StringIO("student_name,grade,\nСтудент1,5\nСтудент2,4\n")
    data2 = StringIO("student_name,grade\nСтудент1,3\nСтудент3,3\n")
    result = main.get_student_grades([data1, data2])
    expected = {
        'Студент1': [5, 3],
        'Студент2': [4],
        'Студент3': [3]
    }
    assert result == expected

def test_get_student_grades2():
    data1 = StringIO("student_name,subject,grade,\nСтудент1,химия,5\nСтудент2,география,4\n")
    data2 = StringIO("student_name,grade\nСтудент1,3\nСтудент3,3\n")
    result = main.get_student_grades([data1, data2])
    expected = {
        'Студент1': [5, 3],
        'Студент2': [4],
        'Студент3': [3]
    }
    assert result == expected

def test_get_student_grades3():
    data1 = StringIO("student_name,grade,\nСтудент1,5\nСтудент2,4\n")
    result = main.get_student_grades([data1])
    expected = {
        'Студент1': [5],
        'Студент2': [4],
    }
    assert result == expected

def test_average_grade():
    student_dict = {
        'Студент2': [4.5, 5.0, 3.0],
        'Студент1': [5.0, 4.0, 4.0],
        'Студент3': [3.5, 4.5]
    }

    check_dict = {
        'Студент1': 4.333333333333333,
        'Студент2': 4.166666666666667,
        'Студент3': 4.0
    }

    sorted_dict = main.average_grade(student_dict)
    for key, item in sorted_dict.items():
        assert check_dict[key] == sorted_dict[key]


def test_grade_report(capsys):
    student_dict = {
        'Студент1': [5.0],
        'Студент2': [4.5],
    }

    output = (
        "| Student   | Average Grade   |\n"
        "|:----------|:----------------|\n"
        '| Студент1  | [5.0]           |\n'
        "| Студент2  | [4.5]           |\n"
    )
    main.grade_report(student_dict)
    captured = capsys.readouterr()
    assert captured.out == output

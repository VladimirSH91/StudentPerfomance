from abc import ABC

class Report(ABC):
    def __init__(self, report_name: str = "Generic Report"):
        self.report_name = report_name


class GradeReport(Report):
    def __init__(self, report_dict: dict, report_name: str = "Grade Report"):
        super().__init__(report_name)
        self.report_dict = report_dict

    def grade_report(self, report_dict: dict) -> list:
        rows = [(student, avg) for student, avg in report_dict.items()]
        return rows

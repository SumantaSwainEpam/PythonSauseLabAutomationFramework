import os

class ReportManager:

    @staticmethod
    def create_report_directory():
        base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        report_dir = os.path.join(base_dir, "reports")
        os.makedirs(report_dir, exist_ok=True)
        return report_dir

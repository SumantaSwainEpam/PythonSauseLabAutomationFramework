import os
import logging
from datetime import datetime

class LoggerManager:
    _logger = None

    @staticmethod
    def get_logger(name: str = "TestLogger"):
        if LoggerManager._logger is None:
            # Base path: project_root/Loggers/
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            log_dir = os.path.join(base_dir, "Loggers")
            os.makedirs(log_dir, exist_ok=True)


            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            log_file_path = os.path.join(log_dir, f"{name}_{timestamp}.log")


            logger = logging.getLogger(name)
            logger.setLevel(logging.DEBUG)


            file_handler = logging.FileHandler(log_file_path)
            formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

            # Console handler (optional)
            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            LoggerManager._logger = logger

        return LoggerManager._logger

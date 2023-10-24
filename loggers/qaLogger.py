import logging
import time


class QALogger:
    """
    This is a class for LambdaLogger.
    To define log and its functions

    Class variables:
    :logger_name : represents logger_name: function name
    :type logger_name : str
    :log_level : represents the level of log
    :type log_level : logging instance
    """

    def __init__(self, logger_name, log_level=logging.INFO):
        """
        Constructor to LambdaLogger class,
        set some usable methods while logging
        """

        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(log_level)

        self.json_formatter = logging.Formatter(
            '{"timestamp": "%(asctime)s GMT +00:00", "name": "%(name)s", '
            '"level": "%(levelname)s", "filename" : %(filename)s, "lineno" : %(lineno)s, "message": %(message)s}',
            datefmt="%Y-%m-%d %H:%M:%S",
        )

        self.filter = self.LogFilter()

        self.json_handler = logging.StreamHandler()
        self.json_handler.setLevel(log_level)
        self.json_handler.addFilter(self.filter)
        self.json_formatter.converter = time.gmtime

        self.logger.addHandler(self.json_handler)

    class LogFilter(logging.Filter):
        """
        Method to add filter in logs
        """

        def filter(self, record):
            # Add any additional filtering logic here if needed
            return True

    def set_verbose_format(self):
        """
        Method to set verbose format
        """
        self.verbose_handler.setFormatter(self.verbose_formatter)

    def set_json_format(self):
        """
        Method to set json format
        """
        self.json_handler.setFormatter(self.json_formatter)

    def get_logger(self):
        """
        Method to return current object of LambdaLogger
        """
        return self.logger

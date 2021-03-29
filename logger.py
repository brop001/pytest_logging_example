import logging
import os
import shutil


class PyTestLogger:

    session_log_dir_name = "Pytest_logs"
    workspace = "C:\\dev"
    log_source_dir = "pytest_project"
    log_destination_root_path = "C:\\dev\\Log"
    log_level_name_list = ["debug", "info", "warning", "error", "critical"]

    def __init__(self, log_file_name, log_level_list):
        """ Initialize self.  See help(type(self)) for accurate signature. """

        self.logger = logging.getLogger(log_file_name)
        self.logger.setLevel(logging.DEBUG)
        self.log_file_name = log_file_name
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s')
        self.log_level_list = log_level_list
        self.in_progress_flag = False

        if self.log_level_list.count(logging.DEBUG):
            self.file_handler_debug = logging.FileHandler(self.log_file_name + "_" +
                                                          PyTestLogger.log_level_name_list[0] + ".log", mode="w")
            self.file_handler_debug.setLevel(logging.DEBUG)

        if self.log_level_list.count(logging.INFO):
            self.file_handler_info = logging.FileHandler(self.log_file_name + "_" +
                                                         PyTestLogger.log_level_name_list[1] + ".log", mode="w")
            self.file_handler_info.setLevel(logging.INFO)

        if self.log_level_list.count(logging.WARNING):
            self.file_handler_warning = logging.FileHandler(self.log_file_name + "_" +
                                                            PyTestLogger.log_level_name_list[2] + ".log", mode="w")
            self.file_handler_warning.setLevel(logging.WARNING)

        if self.log_level_list.count(logging.ERROR):
            self.file_handler_error = logging.FileHandler(self.log_file_name + "_" +
                                                          PyTestLogger.log_level_name_list[3] + ".log", mode="w")
            self.file_handler_error.setLevel(logging.ERROR)

        if self.log_level_list.count(logging.CRITICAL):
            self.file_handler_critical = logging.FileHandler(self.log_file_name + "_" +
                                                             PyTestLogger.log_level_name_list[4] + ".log", mode="w")
            self.file_handler_critical.setLevel(logging.CRITICAL)

        self.update_formatter()

    @classmethod
    def set_session_log_dir_name(cls, dir_name):  # real signature unknown
        cls.session_log_dir_name = dir_name

    def set_formatter(self, formatter):
        if not self.in_progress_flag:
            self.formatter = logging.Formatter(formatter)
            self.update_formatter()
        else:
            raise Exception("Failed to set formatter! Logging is in progress! Please call this function before "
                            "start_logger() or after stop_logger()!")

    def update_formatter(self):
        if self.log_level_list.count(logging.DEBUG):
            self.file_handler_debug.setFormatter(self.formatter)
        if self.log_level_list.count(logging.INFO):
            self.file_handler_info.setFormatter(self.formatter)
        if self.log_level_list.count(logging.WARNING):
            self.file_handler_warning.setFormatter(self.formatter)
        if self.log_level_list.count(logging.ERROR):
            self.file_handler_error.setFormatter(self.formatter)
        if self.log_level_list.count(logging.CRITICAL):
            self.file_handler_critical.setFormatter(self.formatter)

    def start_logger(self):
        self.in_progress_flag = True
        if self.log_level_list.count(logging.DEBUG):
            self.logger.addHandler(self.file_handler_debug)
        if self.log_level_list.count(logging.INFO):
            self.logger.addHandler(self.file_handler_info)
        if self.log_level_list.count(logging.WARNING):
            self.logger.addHandler(self.file_handler_warning)
        if self.log_level_list.count(logging.ERROR):
            self.logger.addHandler(self.file_handler_error)
        if self.log_level_list.count(logging.CRITICAL):
            self.logger.addHandler(self.file_handler_critical)

    def stop_logger(self):

        if self.log_level_list.count(logging.DEBUG):
            self.file_handler_debug.close()
            self.logger.removeHandler(self.file_handler_debug)
        if self.log_level_list.count(logging.INFO):
            self.file_handler_info.close()
            self.logger.removeHandler(self.file_handler_info)
        if self.log_level_list.count(logging.WARNING):
            self.file_handler_warning.close()
            self.logger.removeHandler(self.file_handler_warning)
        if self.log_level_list.count(logging.ERROR):
            self.file_handler_error.close()
            self.logger.removeHandler(self.file_handler_error)
        if self.log_level_list.count(logging.CRITICAL):
            self.file_handler_critical.close()
            self.logger.removeHandler(self.file_handler_critical)

        self.in_progress_flag = False

    def save_log_files(self, test_name, file_name):

        test_suite_dir = file_name
        session_dir = PyTestLogger.session_log_dir_name

        log_source_path = os.path.join(PyTestLogger.workspace, PyTestLogger.log_source_dir)
        log_save_path = os.path.join(PyTestLogger.log_destination_root_path, session_dir, test_suite_dir, test_name)

        log_files_list = list()

        for root, dirs, files in os.walk(log_source_path):
            for file in files:
                for log_level_name in self.log_level_name_list:
                    if ((self.log_file_name + "_" + log_level_name + ".log") == file) or ("witef.log" == file):
                        log_files_list.append(os.path.join(root, file))

        if not os.path.exists(log_save_path):
            os.makedirs(log_save_path)

        for path in log_files_list:
            print(path)
            shutil.copy(path, log_save_path)


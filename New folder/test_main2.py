import pytest
import logging
import os
import shutil
import logger
import time

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
#
# formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
#
# file_handler_debug = logging.FileHandler("debug.log")
# file_handler_debug.setFormatter(formatter)
# file_handler_debug.setLevel(logging.DEBUG)
#
# file_handler_info = logging.FileHandler("info.log")
# file_handler_info.setFormatter(formatter)
# file_handler_info.setLevel(logging.INFO)
#
# file_handler_warning = logging.FileHandler("warning.log")
# file_handler_warning.setFormatter(formatter)
# file_handler_warning.setLevel(logging.WARNING)
#
# file_handler_error = logging.FileHandler("error.log")
# file_handler_error.setFormatter(formatter)
# file_handler_error.setLevel(logging.ERROR)
#
# file_handler_critical = logging.FileHandler("critical.log")
# file_handler_critical.setFormatter(formatter)
# file_handler_critical.setLevel(logging.CRITICAL)
#
#
# logger.addHandler(file_handler_debug)
# logger.addHandler(file_handler_info)
# logger.addHandler(file_handler_warning)
# logger.addHandler(file_handler_error)
# logger.addHandler(file_handler_critical)

log2 = logger.PyTestLogger("test_suite", [logging.DEBUG, logging.INFO])
log = logger.PyTestLogger("test", [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL])


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    log2.start_logger()
    log2.logger.info('Before all test')
    log2.logger.info(logger.PyTestLogger.session_log_dir_name)

    yield
    log2.logger.info('After all test')
    time.sleep(1)
    log2.stop_logger()
    log2.save_log_files("test_suite_log", os.path.basename(__file__).replace(".py", ""))


@pytest.fixture(autouse=True)
def run_test(request):
    log.start_logger()
    log.logger.info('Before test')
    log.logger.info(logger.PyTestLogger.session_log_dir_name)
    yield
    log.logger.info('After test')
    time.sleep(1)
    log.stop_logger()
    log.save_log_files(request.node.name, os.path.basename(__file__).replace(".py", ""))


@pytest.mark.test_a
@pytest.mark.all
def test_a():
    log.logger.debug('A This is a debug message')
    log.logger.info('A This is an info message')
    log.logger.warning('A This is a warning message')
    log.logger.error('A This is an error message')
    log.logger.critical('A This is a critical message')
    pass


@pytest.mark.test_b
@pytest.mark.all
def test_b():
    log.logger.debug('B This is a debug message')
    log.logger.info('B This is an info message')
    log.logger.warning('B This is a warning message')
    log.logger.error('B This is an error message')
    log.logger.critical('B This is a critical message')
    pass

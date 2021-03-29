import pytest
import logging
import os
import logger


log2 = logger.PyTestLogger("test_suite", [logging.DEBUG, logging.INFO])
log = logger.PyTestLogger("test", [logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL])


@pytest.fixture(scope="session", autouse=True)
def do_something(request):
    log2.start_logger()
    log2.logger.info('Before all test')
    log2.logger.info(logger.PyTestLogger.session_log_dir_name)
    yield
    log2.logger.info('After all test')
    log2.stop_logger()
    log2.save_log_files("test_suite_log", os.path.basename(__file__).replace(".py", ""))


@pytest.fixture(autouse=True)
def run_test(request):
    log.start_logger()
    log.logger.info('Before test')
    log.logger.info(logger.PyTestLogger.session_log_dir_name)
    yield
    log.logger.info('After test')
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

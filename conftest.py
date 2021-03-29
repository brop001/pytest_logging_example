import logger
import os


def pytest_configure(config):
    """
    Allows plugins and conftest files to perform initial configuration.
    This hook is called for every plugin and initial conftest
    file after command line options have been parsed.
    """


def pytest_sessionstart(session):
    """
    Called after the Session object has been created and
    before performing collection and entering the run test loop.
    """
    test_log_session_dir_name = "test_log_dir_name"
    test_log_session_dir_path = os.path.join("C:\\dev\\Log", test_log_session_dir_name)

    session_couter = 2

    while os.path.exists(test_log_session_dir_path):
        test_log_session_dir_path = os.path.join("C:\\dev\\Log", test_log_session_dir_name + "#" + str(session_couter))
        session_couter += 1

    logger.PyTestLogger.set_session_log_dir_name(test_log_session_dir_path)


def pytest_sessionfinish(session, exitstatus):
    """
    Called after whole test run finished, right before
    returning the exit status to the system.
    """
    log_source_path = os.path.dirname(__file__)
    log_files_list = list()

    for root, dirs, files in os.walk(log_source_path):
        for file in files:
            if file.endswith(".log"):
                log_files_list.append(os.path.join(root, file))

    for path in log_files_list:
        print("asddfgfgh")
        os.remove(path)


def pytest_unconfigure(config):
    """
    called before test process is exited.
    """
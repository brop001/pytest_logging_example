import os


def save_and_clean_log_files():

    workspace = "C:\\dev"
    log_source_dir = "pytest_project"
    log_save_dir = "Log"

    log_source_path = os.path.join(workspace, log_source_dir)
    log_save_path = os.path.join(workspace, log_save_dir)

    log_files_list = list()

    for root, dirs, files in os.walk(log_source_path):
        for file in files:
            if file.endswith(".log"):
                log_files_list.append(os.path.join(root, file))

    for path in log_files_list:
        print(path)


save_and_clean_log_files()
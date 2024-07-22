from prefect import flow, task
import os

from utils.shell_utils import ShellTask


@task(name="Create text file via cmd.exe")
def create_text_file_if_not_exists(file_path: str):
    """
    Task to create a new text file only if it does not already exist.
    This task can only successfully finish on Windows machine.
    It will always fail on Unix-based machine.
    """
    if not os.path.exists(file_path):
        command = f'cmd.exe /c echo. > {file_path}'
        result = ShellTask(command=command).run()

        print(f"Attempted to create file. Result: {result}")
    else:
        print("File already exists. Did not create.")


@task(name="Verify file creation")
def verify_file_creation(file_path: str):
    """Task to verify if the file exists."""
    if os.path.exists(file_path):
        return "File exists."
    else:
        return "File does not exist."


@flow(name="Create text file via cmd.exe with parameters", log_prints=True)
def create_text_file_flow(filename: str = "text.txt"):
    file_path = f'C:\\{filename}'
    create_text_file_if_not_exists(file_path)
    result = verify_file_creation(file_path)
    print(result)


if __name__ == "__main__":
    create_text_file_flow()

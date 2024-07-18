import os
import re

from prefect import flow, task


@task
def is_valid_filename(filename):
    """
    Check if the filename is in snake case and contains only letters and numbers.
    Snake case is defined here as lowercase letters and underscores, with optional numbers,
    and no leading or trailing underscores.
    """
    pattern = r'^[a-z0-9]+(_[a-z0_9]+)*(\.[a-z0-9]+)?$'
    return re.match(pattern, filename) is not None


@task
def list_filenames(folder_path):
    """
    List all filenames in the specified folder.
    """
    return os.listdir(folder_path)


@task
def check_filenames(filenames):
    """
    Check each filename and categorize them as valid or invalid.
    """
    valid_files = []
    invalid_files = []

    for filename in filenames:
        if is_valid_filename(filename):
            valid_files.append(filename)
        else:
            invalid_files.append(filename)

    return valid_files, invalid_files


@flow(name="Verify correctness of filenames", log_prints=True)
async def verify_filenames_flow(folder_path: str = "content_files"):
    """
    Flow to verify filenames in a specified folder and fail if any are invalid.
    """
    filenames = list_filenames(folder_path)
    valid_files, invalid_files = check_filenames(filenames)

    print("Valid filenames:", valid_files)
    if invalid_files:
        print("Invalid filenames:", invalid_files)
        raise ValueError(f"Some filenames do not match the required pattern. Invalid filenames: {invalid_files}")
    else:
        print("All filenames are valid.")


if __name__ == "__main__":
    verify_filenames_flow()

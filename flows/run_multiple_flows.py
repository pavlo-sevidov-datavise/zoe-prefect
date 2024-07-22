from prefect import flow

from content_filenames_verification_flow import verify_filenames_flow
from simple_print_flow import simple_print_flow


@flow(name="Run multiple flows", log_prints=True)
def run_multiple_flows():
    simple_print_flow()
    verify_filenames_flow()


if __name__ == "__main__":
    run_multiple_flows()

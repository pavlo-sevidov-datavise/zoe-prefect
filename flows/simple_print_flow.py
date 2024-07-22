from prefect import flow


@flow(log_prints=True)
def simple_print_flow():
    print("Hello, World!")


if __name__ == "__main__":
    simple_print_flow()

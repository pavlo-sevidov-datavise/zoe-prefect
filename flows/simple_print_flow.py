from prefect import flow, task


@task
def print_hellp_task():
    print("Hello world from Prefect!")


@flow(name="Print hello from Prefect", log_prints=True)
async def simple_print_flow():
    print_hellp_task()


if __name__ == "__main__":
    simple_print_flow()

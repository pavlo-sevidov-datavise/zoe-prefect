from prefect import flow, task

from utils.shell_utils import ShellTask

DEFAULT_COMMAND = "seq 1 100 | xargs -I{} sh -c 'date; sleep 3'"


@task
def run_shell_task(command: str):
    print(f"Going to execute command='{command}'")
    result = ShellTask(command).run()
    print(f"Finished running external program. Result: {result}")


@flow(name="Run shell command and capture output", log_prints=True)
async def run_shell_flow(command: str = DEFAULT_COMMAND):
    run_shell_task(command)


if __name__ == "__main__":
    run_shell_flow()

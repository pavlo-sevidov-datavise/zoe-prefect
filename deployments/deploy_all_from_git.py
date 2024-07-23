from datetime import timedelta

from prefect.client.schemas.schedules import IntervalSchedule

from deployments_utils import Deploy

deployments_data = [
    {
        "name": "Run multiple flows",
        "entrypoint": "flows/run_multiple_flows.py:run_multiple_flows"
    },
    {
        "name": "Create text file on Windows",
        "entrypoint": "flows/create_file_on_windows.py:create_text_file_flow"
    },
    {
        "name": "Run long running shell command and capture real-time logs",
        "entrypoint": "flows/run_shell_command.py:run_shell_flow"
    },
]

EVERY_5_MINUTES_SCHEDULE = IntervalSchedule(interval=timedelta(minutes=5), timezone="UTC")

if __name__ == "__main__":
    for data in deployments_data:
        Deploy(
            deployment_name=data["name"],
            git_url="https://github.com/pavlo-sevidov-datavise/zoe-prefect.git",
            entrypoint=data["entrypoint"],
            work_pool_name="docker-container-workers-pool",
            schedule=EVERY_5_MINUTES_SCHEDULE
        )

from datetime import timedelta
from typing import Any, Dict, Union

from prefect import flow
from prefect.client.schemas.schedules import IntervalSchedule
from prefect.runner.storage import GitRepository, GitCredentials, Block

EVERY_5_MINUTES_SCHEDULE = IntervalSchedule(interval=timedelta(minutes=5), timezone="UTC")


class Deploy:

    def __init__(
            self,
            deployment_name: str,
            git_url: str,
            entrypoint: str,
            work_pool_name: str = "default-pool",
            branch: str = 'main',
            credentials: Union[GitCredentials, Block, Dict[str, Any], None] = None,
    ):
        flow.from_source(
            source=GitRepository(
                url=git_url,
                branch=branch,
                credentials=credentials
            ),
            entrypoint=entrypoint
        ).deploy(
            name=deployment_name,
            work_pool_name=work_pool_name,
            schedule=EVERY_5_MINUTES_SCHEDULE,
            build=False
        )

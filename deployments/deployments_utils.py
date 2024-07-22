from typing import Any, Dict, Union, Optional

from prefect import flow
from prefect.client.schemas.schedules import SCHEDULE_TYPES
from prefect.runner.storage import GitRepository, GitCredentials, Block


class Deploy:

    def __init__(
            self,
            deployment_name: str,
            git_url: str,
            entrypoint: str,
            work_pool_name: str = "default-pool",
            branch: str = 'main',
            credentials: Union[GitCredentials, Block, Dict[str, Any], None] = None,
            schedule: Optional[SCHEDULE_TYPES] = None,
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
            schedule=schedule,
            build=False
        )

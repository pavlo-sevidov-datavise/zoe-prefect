import asyncio

from prefect import flow

from content_filenames_verification_flow import verify_filenames_flow
from simple_print_flow import simple_print_flow


@flow(name="Run multiple flows in parallel", log_prints=True)
async def run_multiple_flows():
    run_in_parallel = [simple_print_flow(), verify_filenames_flow()]
    await asyncio.gather(*run_in_parallel)


if __name__ == "__main__":
    asyncio.run(run_multiple_flows())

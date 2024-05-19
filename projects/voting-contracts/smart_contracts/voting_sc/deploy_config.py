import logging

import algokit_utils
from algosdk.v2client.algod import AlgodClient
from algosdk.v2client.indexer import IndexerClient

logger = logging.getLogger(__name__)


# define deployment behaviour based on supplied app spec
def deploy(
    algod_client: AlgodClient,
    indexer_client: IndexerClient,
    app_spec: algokit_utils.ApplicationSpecification,
    deployer: algokit_utils.Account,
) -> None:
    from smart_contracts.artifacts.voting_sc.client import (
        VotingScClient,
    )

    app_client = VotingScClient(
        algod_client,
        creator=deployer,
        indexer_client=indexer_client,
    )

    app_client.deploy(
        on_schema_break=algokit_utils.OnSchemaBreak.AppendApp,
        on_update=algokit_utils.OnUpdate.AppendApp,
    )

    voting_str = "Cheese"
    logger.info(f"Calling 'create_voting' with parameter '{voting_str}'...")
    app_client.create_voting(voting_str=voting_str)

    logger.info("Retrieving the Global State of the SC...")
    voting_global_state = app_client.get_global_state()
    logger.info(voting_global_state)
    logger.info(voting_global_state.voting_str)
    logger.info(voting_global_state.voting_str.as_str)

    logger.info("Calling 'get_voting_str'...")
    response = app_client.get_voting_str()
    logger.info(
        f"Response: "
        f"'{response}'"
        f"\nOnly with the return value from response: '{response.return_value}'"
    )

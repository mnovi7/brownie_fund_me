from brownie import FundMe, network, config, MockV3Aggregator
from scripts.common import get_account, deploy_mocks, LOCAL_BLOCKCHAIN_ENVIRONMENTS


def deploy_fund_me():
    account = get_account()

    network_active = network.show_active()
    print(f"The active network is {network_active}")
    if network_active not in LOCAL_BLOCKCHAIN_ENVIRONMENTS:
        price_feed_address = config["networks"][network_active]["eth_usd_price_feed"]
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network_active].get("verify"),
    )
    print(fund_me.address)
    return fund_me


def main():
    deploy_fund_me()

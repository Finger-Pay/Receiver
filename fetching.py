import requests

# Define the testnet addresses for each blockchain
eth_address = "0x82bdcAdb11Bc09040738720D6a84F4706aaa81Ca"  # Sepolia testnet address
neo_address = "0xd277949D38BfaFBb7A2D3517aA0c885A68621f8e"  # Neo testnet address

# Etherscan API key
etherscan_api_key = "QSRJW9C5QWC9BTK4Z86DBHBUNHUNWBP5MG"  # Replace with your Etherscan API key

def fetch_ethereum_transaction_amounts():
    # Use Etherscan testnet API to fetch transaction history for Ethereum Sepolia testnet
    etherscan_url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={eth_address}&apikey={etherscan_api_key}"
    response = requests.get(etherscan_url).json()

    if response.get("status") == "1":
        transactions = response.get("result", [])
        print("Ethereum Sepolia Transaction Amounts:")
        for tx in transactions:
            value_in_eth = int(tx['value']) / 10**18  # Convert Wei to Ether
            print(f"Value: {value_in_eth} ETH")
    else:
        print(f"Error fetching Ethereum Sepolia transactions: {response.get('message')}")
    print("\n")


def fetch_neo_transaction_amounts(neo_address=None):
    if neo_address is None:
        print("Error: No Neo address provided.")
        return

    # Using NeoTracker API for Neo N3 TestNet
    neo_api_url = f"https://testnet.api.neotube.io/v1/address/{neo_address}/transactions?page=1&size=20"
    
    try:
        response = requests.get(neo_api_url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()

        if "items" in data:
            print(f"Neo Testnet Transaction Amounts for address {neo_address}:")
            for tx in data["items"]:
                # In this API, we need to look at the 'transfers' field
                for transfer in tx.get('transfers', []):
                    if transfer['from'] == neo_address:
                        amount = float(transfer['amount']) / 1e8  # Convert from integer to float
                        asset = transfer['asset']
                        print(f"Transaction ID: {tx['hash']}, Amount: {amount} {asset}")
        else:
            print("No transactions found or unexpected response structure.")
    except requests.RequestException as e:
        print(f"Error fetching Neo Testnet transactions: {e}")
    
    print("\n")

def print_all_transaction_amounts():
    # Example Neo N3 TestNet address
    example_address = "0xd277949D38BfaFBb7A2D3517aA0c885A68621f8e"
    fetch_neo_transaction_amounts(example_address)

if __name__ == "__main__":
    print_all_transaction_amounts()

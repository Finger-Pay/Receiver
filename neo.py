import requests


def get_transactions_from_new_api(address):
    # API URL for NeoX4 (Make sure this is the correct one for your needs)
    api_url = f"https://xt4scan.ngd.network/api/v1/address/{address}/transactions"

    response = requests.get(api_url)

    if response.status_code == 200:
        return response.json()  # Assuming the API returns JSON data
    else:
        return f"Error fetching data: {response.status_code}, {response.text}"

# Example usage
# Replace with a valid Neo address; ensure it's in the correct format
neo_address = "Aeq59NyZtgj5AMQvdiG5uhb1AaFX8rk4xD"  # Example Neo address
transaction_history = get_transactions_from_new_api(neo_address)
print(transaction_history)



# import requests

# def get_transaction_history_from_explorer(address):
#     # NeoScan API URL (for Mainnet or Testnet)
#     api_url = f"https://api.neoscan.io/api/main_net/v1/get_address_abstracts/{address}/1"

#     # Send request to NeoScan API
#     response = requests.get(api_url)

#     if response.status_code == 200:
#         data = response.json()
#         return data['entries']  # List of transaction entries
#     else:
#         return f"Error fetching data: {response.status_code}"

# # Example usage
# neo_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"  # Replace with actual Neo address
# transaction_history = get_transaction_history_from_explorer(neo_address)

# for tx in transaction_history:
#     print(f"Transaction ID: {tx['txid']}, Time: {tx['time']}, Type: {tx['type']}, Amount: {tx['amount']}")


# import requests

# def get_transaction_history(address):
#     # NEO RPC Node URL (you can use any Neo public node or deploy your own)
#     rpc_url = "https://neo3-testnet.neoline.io"  # Replace with actual Neo node URL
    
#     # JSON-RPC request data for `getnep17transfers`
#     data = {
#         "jsonrpc": "2.0",
#         "method": "getnep17transfers",
#         "params": [address],
#         "id": 1
#     }
#     print(address)
#     # Send request to the Neo node
#     response = requests.post(rpc_url, json=data)
    
#     if response.status_code == 200:
#         result = response.json().get("result")
#         if result:
#             return result
#         else:
#             return "No transactions found or error in fetching."
#     else:
#         return f"Error: {response.status_code}"

# # Example usage
# neo_address = "0xf39Fd6e51aad88F6F4ce6aB8827279cffFb92266"  # Replace with the actual Neo address
# transaction_history = get_transaction_history(neo_address)

# print("Transaction History:", transaction_history)

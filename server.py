from flask import Flask, jsonify
import requests
import time
import threading

app = Flask(__name__)

# Define the testnet addresses for each blockchain
eth_address = "0x82bdcAdb11Bc09040738720D6a84F4706aaa81Ca"  # Sepolia testnet address
sol_address = "your_solana_devnet_address_here"     # Solana devnet address
neo_address = "0xd277949D38BfaFBb7A2D3517aA0c885A68621f8e"       # Neo testnet address

# Testnet explorer URLs
eth_url = f"https://sepolia.etherscan.io/address/{eth_address}"
sol_url = f"https://explorer.solana.com/address/{sol_address}?cluster=devnet"
neo_url = f"https://testnet.xt4scan.ngd.network/address/{neo_address}"

# API endpoint to send transaction data
api_url = "hhttp://127.0.0.1:5005/transaction"

def check_ethereum():
    # Implement logic to monitor Ethereum Sepolia transactions via Etherscan testnet API
    etherscan_api_key = "your_etherscan_api_key"
    etherscan_url = f"https://api-sepolia.etherscan.io/api?module=account&action=txlist&address={eth_address}&apikey={etherscan_api_key}"
    
    latest_eth_tx = None

    while True:
        response = requests.get(etherscan_url).json()
        if response.get("status") == "1":
            transactions = response.get("result", [])
            if transactions:
                # Check for new transactions
                new_tx = transactions[-1]  # Get the latest transaction
                if new_tx['hash'] != latest_eth_tx:
                    latest_eth_tx = new_tx['hash']
                    send_transaction(new_tx)
        time.sleep(10)  # Poll every 10 seconds

def check_solana():
    # Implement logic to monitor Solana devnet transactions via Solscan
    solana_url = f"https://public-api.solscan.io/account/{sol_address}?cluster=devnet"

    latest_sol_tx = None

    while True:
        response = requests.get(solana_url).json()
        if response and "txs" in response:
            new_tx = response["txs"][0]  # Latest transaction
            if new_tx['txHash'] != latest_sol_tx:
                latest_sol_tx = new_tx['txHash']
                send_transaction(new_tx)
        time.sleep(10)  # Poll every 10 seconds

def check_neo():
    # Implement logic to monitor Neo testnet transactions via XT4 scan testnet
    neo_api_url = f"https://testnet.xt4scan.ngd.network/api/v1/address/transactions/{neo_address}"

    latest_neo_tx = None

    while True:
        response = requests.get(neo_api_url).json()
        if response and "transactions" in response:
            new_tx = response["transactions"][0]  # Latest transaction
            if new_tx['txid'] != latest_neo_tx:
                latest_neo_tx = new_tx['txid']
                send_transaction(new_tx)
        time.sleep(10)  # Poll every 10 seconds

def send_transaction(transaction):
    # Send the transaction data to the API endpoint
    response = requests.post(api_url, json=transaction)
    if response.status_code == 200:
        print(f"Transaction sent successfully: {transaction}")
    else:
        print(f"Failed to send transaction: {response.content}")

# Start threads to monitor each blockchain
def start_monitoring():
    eth_thread = threading.Thread(target=check_ethereum)
    sol_thread = threading.Thread(target=check_solana)
    neo_thread = threading.Thread(target=check_neo)

    eth_thread.start()
    sol_thread.start()
    neo_thread.start()

# API endpoint to start monitoring
@app.route("/start-monitoring", methods=["GET"])
def start_monitoring_endpoint():
    start_monitoring()
    return jsonify({"status": "Monitoring started!"})

if __name__ == "__main__":
    app.run(port=5003, debug=True)

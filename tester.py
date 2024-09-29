from flask import Flask, request, jsonify

app = Flask(__name__)

# Endpoint to receive transaction data
@app.route('/transaction', methods=['POST'])
def receive_transaction():
    # Get the transaction data from the request
    transaction_data = request.json
    
    # Log the received transaction data
    print("Received transaction:", transaction_data)
    
    # Return a success response
    return jsonify({"status": "Transaction received", "data": transaction_data}), 200

if __name__ == "__main__":
    # Run the server on port 5001
    app.run(port=5005, debug=True)
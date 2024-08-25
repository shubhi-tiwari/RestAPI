from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['POST'])
def post_data():
    try:
        data = request.get_json()
        items = data.get('data', [])

        numbers = [item for item in items if item.isdigit()]
        alphabets = [item for item in items if item.isalpha()]

        lowercase_alphabets = [item for item in alphabets if item.islower()]
        highest_lowercase_alphabet = max(lowercase_alphabets, default='', key=lambda x: x.lower())

        response = {
            'is_success': True,
            'user_id': 'john_doe_17091999',
            'email': 'john@xyz.com',
            'roll_number': 'ABCD123',
            'numbers': numbers,
            'alphabets': alphabets,
            'highest_lowercase_alphabet': [highest_lowercase_alphabet]
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'is_success': False, 'error': str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        'operation_code': 1
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

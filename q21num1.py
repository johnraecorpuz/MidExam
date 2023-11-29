from flask import Flask, request, jsonify
app = Flask(__name__)
message = [
    {"heart_id": 1, "date": "2023-01-01", "heart_rate": 75},
    {"heart_id": 2, "date": "2023-01-02", "heart_rate": 80},
    {"heart_id": 3, "date": "2023-01-03", "heart_rate": 85},
    {"heart_id": 4, "date": "2023-01-04", "heart_rate": 82},
    {"heart_id": 5, "date": "2023-01-05", "heart_rate": 88},
    
]

# 1  Create a REST API using FLASK insert a new heart record to a JSON file. The heart rate information is composed of heart_id, date and heart_rate.  (2 points)
@app.route('/insert_heart', methods=['POST'])
def insert_heart():
    new_heart = request.get_json()
    heart_data.append(new_heart)
    return jsonify({"message": "Heart record added successfully"}), 200

# 2. Create a REST API using FLASK to read a heart information from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (2 points)
@app.route('/read_all_hearts', methods=['GET'])
def read_all_hearts():
    return jsonify(heart_data)

# 3.Create a REST API using FLASK to read a heart information of a specific heart_id from a JSON file. The heart rate information is composed of heart_id, date and heart_rate. (2 points)
@app.route('/read_heart/<int:heart_id>', methods=['GET'])
def read_heart(heart_id):
    heart = next((item for item in heart_data if item["heart_id"] == heart_id), None)
    if heart:
        return jsonify(heart)
    else:
        return jsonify({"message": "Heart record not found"}), 404

# 4.  Create a REST API using FLASK to update a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (2 points)
@app.route('/update_heart/<int:heart_id>', methods=['PUT'])
def update_heart(heart_id):
    heart = next((item for item in heart_data if item["heart_id"] == heart_id), None)
    if heart:
        updated_data = request.get_json()
        heart.update(updated_data)
        return jsonify({"message": "Heart record updated successfully"})
    else:
        return jsonify({"message": "Heart record not found"}), 404

# 5. Create a REST API using FLASK to delete a heart record of a specific heart_id. The heart rate information is composed of heart_id, date and heart_rate.  (2 points).
@app.route('/delete_heart/<int:heart_id>', methods=['DELETE'])
def delete_heart(heart_id):
    global heart_data
    heart_data = [item for item in heart_data if item["heart_id"] != heart_id]
    return jsonify({"message": "Heart record deleted successfully"})

if __name__ =='__main__':
    app.run()


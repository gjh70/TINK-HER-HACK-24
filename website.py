from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

services = [
    {"id": 1, "name": "Plumbing", "rate": 50},
    {"id": 2, "name": "Electrician", "rate": 60},
    {"id": 3, "name": "Cleaning", "rate": 30}
]

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/services', methods=['GET'])
def get_services():
    return jsonify(services)

@app.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = next((service for service in services if service['id'] == service_id), None)
    if service:
        return jsonify(service)
    else:
        return jsonify({"error": "Service not found"}), 404

@app.route('/book_service', methods=['POST'])
def book_service():
    data = request.json
    service_id = data.get('service_id')
    hours = data.get('hours')
    if not service_id or not hours:
        return jsonify({"error": "Service ID and hours are required"}), 400
    
    service = next((service for service in services if service['id'] == service_id), None)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    
    total_cost = service['rate'] * hours
    return jsonify({"total_cost": total_cost})

if __name__ == '__main__':
    app.run(port=3000)

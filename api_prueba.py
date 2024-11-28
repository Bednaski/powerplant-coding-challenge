from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.route('/productionplan', methods=['POST'])
def production_plan():
    try:
        # Receive the payload from the request
        data = request.json

        # Validate required fields in the payload
        required_keys = ["load", "fuels", "powerplants"]
        for key in required_keys:
            if key not in data:
                raise ValueError(f"Required field missing in the payload: {key}")

        load = data["load"]
        fuels = data["fuels"]
        powerplants = data["powerplants"]

        # Validate basic data types and values
        if not isinstance(load, (int, float)) or load <= 0:
            raise ValueError("The load must be a positive number.")
        if not isinstance(fuels, dict) or not isinstance(powerplants, list):
            raise ValueError("'fuels' must be a dictionary and 'powerplants' must be a list.")

        # Calculate cost per MWh for each powerplant
        for plant in powerplants:
            if plant["type"] == "gasfired":
                plant["cost"] = (fuels["gas(euro/MWh)"] + 0.3 * fuels["co2(euro/ton)"]) / plant["efficiency"]
            elif plant["type"] == "turbojet":
                plant["cost"] = fuels["kerosine(euro/MWh)"] / plant["efficiency"]
            elif plant["type"] == "windturbine":
                plant["cost"] = 0
                plant["pmax"] *= fuels["wind(%)"] / 100  # Adjust Pmax based on wind percentage

        # Sort powerplants by merit order (lowest cost first)
        powerplants.sort(key=lambda x: x["cost"])

        # Distribute the load among powerplants
        remaining_load = load
        production_plan = []

        for plant in powerplants:
            if remaining_load <= 0:
                production_plan.append({"name": plant["name"], "p": 00})
                continue

            pmin = plant["pmin"]
            pmax = plant["pmax"]

            # Calculate production while respecting Pmin, Pmax, and remaining load
            production = max(pmin, min(pmax, remaining_load))
            production_plan.append({"name": plant["name"], "p": round(production, 1)})
            remaining_load -= production

        # Validate if the entire load was met
        if remaining_load > 0:
            raise ValueError("The load cannot be fully met with the available powerplants.")

        # Return the production plan as JSON
        return jsonify(production_plan)

    except ValueError as ve:
        # Handle validation errors
        logging.error(f"Validation error: {ve}")
        return jsonify({"error": str(ve)}), 400
    except KeyError as ke:
        # Handle missing keys in the payload
        logging.error(f"Missing key error: {ke}")
        return jsonify({"error": f"Missing key in payload: {ke}"}), 400
    except Exception as e:
        # Handle unexpected errors
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred. Check the payload and try again."}), 500

if __name__ == '__main__':
    # Run the application on port 8888 and accept requests from all hosts
    app.run(host='0.0.0.0', port=8888, debug=True)

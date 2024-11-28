# **Production Plan API**

This API calculates an optimal production plan for a set of power plants to meet a specified energy load, based on input parameters like fuel costs, plant efficiency, and power limits. The API processes this data to minimize costs while adhering to operational constraints such as minimum and maximum output limits and plant efficiency.

---

## **Project Overview**

The **Production Plan API** is designed to:
- Receive energy load requirements and details about power plants (e.g., fuel type, efficiency, operational constraints).
- Calculate the most cost-effective energy distribution across the plants.
- Return a production plan as a JSON response, specifying the energy output for each plant.

### **How It Works**

- **Inputs**: A JSON payload including:
  - **Energy load (`load`)**: The amount of energy (MWh) to be generated.
  - **Fuel costs (`fuels`)**: Costs for gas, kerosene, CO2 emissions, and wind percentage.
  - **Power plant parameters (`powerplants`)**: Efficiency, minimum/maximum production limits, and type (gas, turbojet, wind).

- **Output**: A JSON response listing the optimal production levels for each plant, ensuring:
  - The total energy matches the required load.
  - Cost-effectiveness, based on fuel costs and efficiency.
  - Compliance with operational constraints (`pmin` and `pmax`).

---

## **Project Structure**

```bash
  project/
├── requirements.txt              # Dependencies for the project
├── Dockerfile                    # Docker configuration for containerization
├── src/                          # Folder containing source code
│   ├── app.py                    # Flask server for the API
│   └── production_plan.py        # Algorithm to calculate production plans
└── test/                         # Folder containing test cases
    └── test_app.py               # Unit tests for the Flask application
```bash


You should see output like this:

bash

Running on http://127.0.0.1:8888 (Press CTRL+C to quit)
The API will now be accessible at http://127.0.0.1:8888/productionplan.

# powerplant-coding-challenge
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

- **`api_prueba`**: This file contains the code of the application: Contains the logic for calculating the production plan, including sorting plants by merit order and distributing the load. And sets up the Flask server and exposes the /productionplan API endpoint.

- **requirements.txt**: Lists the required dependencies for the project.


## Getting Started

### Prerequisites

Before starting, ensure you have:
- **Python 3.8** or higher installed on your system.
- **pip** (Python package manager) installed for managing dependencies.

### Installation

1. **Clone or Download** the project files to your local machine.
2. **Install dependencies** by navigating to the project directory in your terminal and running:

   ```bash
   pip install -r requirements.txt
   ```

## Running the API

This section provides step-by-step instructions to run the Production Plan API, send a request, and verify the output.

### 1. Start the API

- Open a terminal in the project directory where `api_prueba.py` are located.
- Run the following command to start the Flask API:

  ```bash
  python api_prueba.py
  ```
  
- If the server starts successfully, you should see output in the terminal indicating that the API is running, with a message similar to:

  ```bash
  Running on http://127.0.0.1:8888 (Press CTRL+C to quit)
  ```

### 2. Send a Input JSON by POST Request to the API
- Send by POST a data in JSON including details like the energy load, fuel costs, and power plant specifications.

- Open another terminal window in the same directory where `payload.json` is located.

- Use the following `curl` command to send a `POST` request to the `/productionplan` endpoint:
```bash
curl -X POST http://localhost:8888/productionplan \
-H "Content-Type: application/json" \
-d 'PUT HERE INFORMATION STRUTURED AS JSON'
```

### 3. Verify the Output

- After the request completes successfully, you should recive back the information of each plan must produce.

- ## Explanation of How the API Works

### API Endpoint 
- The API has one endpoint, `/productionplan`, which only accepts POST requests with JSON data as input.

### Calculation

- The function in `production_plan.py` processes this input data to calculate the optimal production levels for each plant. The goal is to distribute the energy output to meet the specified load in the most cost-effective way, taking into account each plant’s efficiency, minimum and maximum output limits, and fuel costs.

### Output

- The API send the information back with specify each plant's production level in MWh.




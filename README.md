# powerplant-coding-challenge


## Running the API
1. Start the API
To start the API locally:

Navigate to the directory where app.py is located.
Run the Flask server:
```bash

python app.py
You should see output like this:

```bash

Running on http://127.0.0.1:8888 (Press CTRL+C to quit)
The API will now be accessible at http://127.0.0.1:8888/productionplan.

2. Prepare the Input JSON
Create a JSON file (e.g., payload.json) with the required fields. Example:

json

{
  "load": 910,
  "fuels": {
    "gas(euro/MWh)": 13.4,
    "kerosine(euro/MWh)": 50.8,
    "co2(euro/ton)": 20,
    "wind(%)": 60
  },
  "powerplants": [
    {
      "name": "gasfiredbig1",
      "type": "gasfired",
      "efficiency": 0.53,
      "pmin": 100,
      "pmax": 460
    },
    {
      "name": "windpark1",
      "type": "windturbine",
      "efficiency": 1,
      "pmin": 0,
      "pmax": 150
    }
  ]
}
3. Test the API
Use curl or Postman to send a POST request to the /productionplan endpoint:

```bash

curl -X POST http://localhost:8888/productionplan \
-H "Content-Type: application/json" \
-d @payload.json

4. Output
The API will return a JSON response specifying the production plan. Example:

json
Copiar código
[
  {
    "name": "windpark1",
    "p": 90.0
  },
  {
    "name": "gasfiredbig1",
    "p": 460.0
  }
]

5. Running Tests
To run unit tests:

```bash

python -m unittest discover -s test

Using Docker
Build the Docker Image
```bash

docker build -t productionplan-api .
Run the API in a Docker Container
```bash


docker run -p 8888:8888 productionplan-api
You can now access the API at http://127.0.0.1:8888/productionplan.

Explanation of the Algorithm
Calculation Steps
Merit Order:

Power plants are sorted by cost efficiency (cheapest first).
Load Distribution:

The algorithm iteratively assigns energy production to power plants while respecting:
Minimum and maximum production limits (pmin and pmax).
Remaining load to be fulfilled.
Cost Calculation:

For gas and kerosene plants:
Cost = Fuel Cost+( CO2 Cost × 0.3 )Efficiency
Cost =  Efficiency Fuel Cost+(CO2 Cost×0.3)
​
 
For wind turbines:
Cost is zero.
Output Validation:

Ensures the total production matches the requested load.
Error Handling
The API handles and logs the following errors:

Validation Errors: Missing or invalid fields in the payload.
Calculation Errors: Infeasible solutions where the load cannot be met.
Unexpected Errors: General exceptions logged for debugging.
Future Improvements
Support for renewable energy variability.
Integration with external fuel pricing APIs.
Extended error reporting for debugging.

This API provides a robust foundation for managing energy production planning efficiently while minimizing costs.



from flask import Flask, request, jsonify
import pandas as pd
import pickle

app = Flask(__name__)

# Load trained AI model
try:
    model = pickle.load(open("ai_model.pkl", "rb"))
except Exception as e:
    print("Error loading model:", e)
    model = None

# Load plastic data
try:
    plastic_data = pd.read_csv("plastic_data.csv")
except Exception as e:
    print("Error loading CSV:", e)
    plastic_data = None

# Test if Flask is working
@app.route('/')
def home():
    return "Flask is working!"

# Debugging route to check if /predict is accessible
@app.route('/predict', methods=['GET'])
def test_predict():
    print("GET /predict route accessed")  # Debugging line
    return jsonify({"message": "Predict route is working!"})

# Main prediction route
@app.route('/predict', methods=['POST'])
def predict():
    print("POST /predict route accessed")  # Debugging line
    try:
        if plastic_data is None:
            return jsonify({"error": "Plastic data not loaded"}), 500
        if model is None:
            return jsonify({"error": "AI model not loaded"}), 500

        # Get user input
        data = request.get_json()
        product_name = data.get('product', '').lower()
        quantity = int(data.get('quantity', 0))
        raw_material = data.get('raw_material', None)  # Raw material can be good, better, best, or average
        single_use = data.get('single_use', None)  # Yes or No for single use

        print(f"Received product: {product_name}, quantity: {quantity}, raw_material: {raw_material}, single_use: {single_use}")  # Debugging line

        # Initialize suggestions
        suggestions = {}

        # If raw_material input is provided
        if raw_material:
            if raw_material in ['average', 'worst']:
                suggestions["raw_material_warning"] = "Not recommended to use 'average' or 'worst' raw materials. Consider using 'good', 'better', or 'best' raw materials for better results."
            
            if raw_material == 'best':
                suggestions["raw_material_suggestion"] = "Best quality material used, continue with current strategy."
            
            if raw_material == 'good':
                suggestions["raw_material_suggestion"] = "Good quality materials, consider upgrading to 'best' for better sustainability."

        # If single_use input is provided
        if single_use:
            if single_use == 'yes':
                suggestions["single_use_warning"] = "Single-use plastic is recommended for manufacturing. Please ensure proper disposal and recycling processes. However, consider alternatives as single-use plastic usage is increasingly restricted globally under laws such as the EU Plastics Strategy."
            elif single_use == 'no':
                suggestions["single_use_warning"] = "Single-use plastic is not recommended. It cannot be reused and poses environmental challenges. Consider alternatives as many countries have banned or restricted single-use plastic under laws such as the Plastic Waste Management Rules in India or the EU Directive on Single-Use Plastics."

        # Check if product exists in database
        if product_name and product_name not in plastic_data['product'].values:
            return jsonify({"error": "Product not found in database"}), 400

        # If product and quantity inputs are provided
        if product_name and quantity > 0:
            # Get plastic waste per unit and compute total waste
            plastic_per_unit = plastic_data.loc[plastic_data['product'] == product_name, 'total_plastic_waste'].values[0]
            total_plastic = plastic_per_unit * quantity

            # Generate suggestions based on total plastic waste
            if total_plastic > 400:  # Scenario 1: High plastic waste
                suggestions["status"] = "Manufacturing not recommended"
                suggestions["message"] = "Plastic waste exceeds the threshold as per environmental regulations like the EU Waste Framework Directive!"
                suggestions["suggestions"] = {
                    "immediate_actions": [
                        "Consider using biodegradable or recyclable materials in compliance with the EU Plastics Strategy.",
                        "Reduce production volume to minimize waste, as per the Plastic Waste Management Rules 2016 in India.",
                        "Switch to more sustainable raw materials to adhere to environmental guidelines."
                    ],
                    "cost_reduction": [
                        "Optimize production processes to reduce waste and energy consumption, in line with Sustainability Standards.",
                        "Review machinery for potential energy savings and process efficiency improvements."
                    ]
                }

            elif 150 < total_plastic <= 400:  # Scenario 2: Acceptable plastic waste
                suggestions["status"] = "Manufacturing allowed within safe limits"
                suggestions["message"] = "Plastic waste within safe limits according to National/Local Waste Management Regulations."
                suggestions["suggestions"] = {
                    "profit_suggestions": [
                        "Focus on increasing sales and marketing to expand reach.",
                        "Negotiate for better pricing with raw material suppliers."
                    ],
                    "operational_efficiency": [
                        "Review production processes for optimization opportunities.",
                        "Invest in machinery upgrades to improve efficiency and reduce emissions."
                    ]
                }

            elif 50 < total_plastic <= 150:  # Scenario 3: Moderate plastic waste
                suggestions["status"] = "Manufacturing approved with caution"
                suggestions["message"] = "Plastic waste is moderate. Caution required as per environmental guidelines."
                suggestions["suggestions"] = {
                    "cost_reduction": [
                        "Review operational efficiency to minimize waste and adhere to sustainable practices.",
                        "Consider using more sustainable raw materials to comply with Government Sustainability Goals."
                    ],
                    "immediate_actions": [
                        "Monitor waste closely to avoid exceeding the limits set by Environmental Standards.",
                        "Investigate alternative materials to reduce plastic dependency."
                    ]
                }

            elif total_plastic <= 50:  # Scenario 4: Low plastic waste
                suggestions["status"] = "Highly profitable manufacturing"
                suggestions["message"] = "Plastic waste is minimal, highly profitable manufacturing with minimal environmental impact."
                suggestions["suggestions"] = {
                    "profit_suggestions": [
                        "Increase production volume to maximize profits while keeping environmental impact low.",
                        "Consider entering new markets for your product."
                    ],
                    "sustainability": [
                        "Promote your product's eco-friendly manufacturing process in line with Global Sustainability Goals.",
                        "Use best quality materials to maintain environmental benefits and avoid future regulatory penalties."
                    ]
                }

            # Adjust status for raw material quality
            if raw_material in ['average', 'worst']:
                suggestions["status"] = "Not recommended for manufacturing"
                suggestions["message"] = "The raw material is of low quality ('average' or 'worst'). It's advised to improve material quality before manufacturing in compliance with sustainability practices and regulations."

        return jsonify(suggestions)
    
    except Exception as e:
        print("Error in /predict:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)

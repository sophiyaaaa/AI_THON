# AI-Enhanced Prevention of Industrial Plastic Waste

## Overview
This project is an AI-driven solution designed to assess and reduce plastic waste in industrial manufacturing. By leveraging machine learning models, it predicts the environmental impact of manufacturing decisions and suggests optimal waste management strategies. The system integrates real-time data analysis, regulatory compliance checks, and sustainability recommendations.

## Features
- AI-powered waste assessment and reduction recommendations
- Real-time predictions based on manufacturing inputs
- Compliance monitoring with environmental regulations
- Customized sustainability strategies for industries
- Integration with existing industrial processes
- User-friendly API for seamless deployment
  
## Tech Stack
- **Backend:** Flask (Python)
- **Machine Learning and Artificial Intelligence:** Scikit-Learn, Pandas, NumPy,Random Forest
- **Database:** CSV-based storage (can be extended to SQL/NoSQL databases)
- **Model Deployment:** Pickle for AI model serialization


## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/sophiyaaaa/AI_THON.git
   cd your-repo-name
   ```
2. Install dependencies:
   ```sh
   pip install flask pandas numpy scikit-learn
   ```
3. Run the Flask application:
   ```sh
   python app.py
   ```
4. Access the API at:
   ```sh
   http://localhost:5001
   ```

## API Endpoints
- **`GET /`** – Check if Flask is working
- **`POST /predict`** – Provide manufacturing details and receive waste assessment & recommendations
  - **Input:** JSON object with `product`, `quantity`, `raw_material`, and `single_use`
  - **Output:** AI-generated sustainability recommendations
    
## Features and functionalities:
 *"Optimizing Plastic Lifecycle Management in Manufacturing,"* leverages AI to enhance sustainability. Key features include:  
1. *Raw Material Optimization*: AI suggests eco-friendly materials and evaluates their environmental impact.  
2. *Production Efficiency*: Identifies inefficiencies, reduces waste, and monitors real-time metrics.  
3. *Single-Use Plastic Reduction*: Recommends reusable/biodegradable alternatives and integrates sustainable design tools.  
4. *Waste Management*: Classifies waste, suggests recycling/upcycling, and explores waste-to-energy solutions.  
5. *Regulatory Compliance*: Ensures adherence to environmental laws and generates automated reports.  
6. *Scalability*: Modular, cloud-based, and integrates with existing systems. Advanced features include predictive analytics, NLP, gamification, and carbon tracking, driving cost savings, compliance, and reduced environmental impact.

   
## Usage Example
Send a POST request with JSON data:
```json
{
    "product": "plastic bottle",
    "quantity": 100,
    "raw_material": "good",
    "single_use": "yes"
}
```
Response:
```json
{
    "status": "Manufacturing allowed within safe limits",
    "message": "Plastic waste within safe limits according to National/Local Waste Management Regulations.",
    "suggestions": {
        "profit_suggestions": [
            "Focus on increasing sales and marketing to expand reach.",
            "Negotiate for better pricing with raw material suppliers."
        ],
        "operational_efficiency": [
            "Review production processes for optimization opportunities.",
            "Invest in machinery upgrades to improve efficiency and reduce emissions."
        ]
    }
}
```

## Future Enhancements
- Expand the database with industry-specific waste benchmarks
- Integrate with IoT sensors for real-time waste tracking
- Develop a user-friendly web dashboard
- Implement blockchain for transparent sustainability tracking

- *Team Members*: Sophiya Ahmad, Aarja Bhatnagar, and Sahil Chinchore.  
- *Collaboration*: Worked together to identify the problem statement and build the idea.  
- *Research*: Analyzed challenges in plastic lifecycle management and studied existing loops.  
- *Innovation*: Researched sustainable practices and designed an AI-driven solution.  
- *Solution Focus*: Optimized plastic usage, production efficiency, and waste management.  
- *Contributions*: Each member contributed to brainstorming, research, and framework development.  
- *Outcome*: Developed a scalable system addressing:  
  - Raw material optimization.  
  - Production efficiency.  
  - Single-use plastic reduction.  
  - Waste management.  
  - Regulatory compliance.  
- *Impact*: Created an innovative solution to reduce environmental impact while maintaining operational efficiency in manufacturing.

## License
This project is licensed under the MIT License.

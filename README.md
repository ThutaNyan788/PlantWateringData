# 🌱 Smart Irrigation AI System

An intelligent plant watering system that uses machine learning to predict when to activate the water pump based on environmental sensor data.

## 📋 Overview

This project provides:
- A **Decision Tree ML model** trained on soil moisture, temperature, and humidity data
- A **FastAPI server** that receives sensor readings and returns pump activation predictions
- Designed to work with **ESP32** microcontrollers for IoT smart irrigation

## 🗂️ Project Structure

```
PlantWateringData/
├── main.py              # FastAPI server for predictions
├── train.py             # ML model training script
├── requirements.txt     # Python dependencies
├── pump_model.pkl       # Trained model (generated after training)
└── data/
    └── plant_data.csv   # Training dataset (3000+ samples)
```

## 📊 Dataset

The training data includes:
| Feature | Description |
|---------|-------------|
| Soil Moisture | Soil moisture sensor reading (0-1023) |
| Temperature | Ambient temperature (°C) |
| Air Humidity | Relative humidity (%) |
| Pump Data | Target label (0 = OFF, 1 = ON) |

## 🚀 Getting Started

### Prerequisites
- Python 3.10+

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ThutaNyan788/PlantWateringData.git
   cd PlantWateringData
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Train the model:
   ```bash
   python train.py
   ```

4. Start the API server:
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

## 🔌 API Endpoints

### Health Check
```
GET /
```
Returns server status.

### Predict Pump State
```
POST /esp32/button
```

**Request Body:**
```json
{
  "temperature": 28.5,
  "humidity": 65.0,
  "soil_moisture": 450.0
}
```

**Response:**
```json
{
  "pump": 1
}
```
- `pump: 1` → Turn pump ON
- `pump: 0` → Keep pump OFF

## 🛠️ Technologies Used

- **FastAPI** - Modern web framework for building APIs
- **scikit-learn** - Machine learning (Decision Tree Classifier)
- **pandas** - Data manipulation
- **joblib** - Model serialization
- **Pydantic** - Data validation

## 📈 Model Performance

The Decision Tree classifier is trained with `max_depth=4` to prevent overfitting while maintaining good accuracy on the sensor data.

## 📄 License

This project is open source and available under the MIT License.
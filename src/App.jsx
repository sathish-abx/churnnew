// App.jsx
// eslint-disable-next-line no-unused-vars
import React, { useState } from "react"; // Keep this import
import axios from "axios";
import "./App.css";

function App() {
  const [formData, setFormData] = useState({
    gender: "Female",
    SeniorCitizen: 0,
    Partner: "No",
    Dependents: "No",
    tenure: 1,
    PhoneService: "No",
    MultipleLines: "No phone service",
    InternetService: "DSL",
    OnlineSecurity: "No",
    OnlineBackup: "No",
    DeviceProtection: "No",
    TechSupport: "No",
    StreamingTV: "No",
    StreamingMovies: "No",
    Contract: "Month-to-month",
    PaperlessBilling: "No",
    PaymentMethod: "Electronic check",
    MonthlyCharges: 100,
    TotalCharges: 1000,
  });

  const [prediction, setPrediction] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Convert SeniorCitizen from "Yes"/"No" to 1/0
      const dataToSend = {
        ...formData,
        SeniorCitizen: formData.SeniorCitizen === "Yes" ? 1 : 0,
      };

      const response = await axios.post("http://localhost:8000/predict", dataToSend);
      setPrediction(response.data);
    } catch (error) {
      console.error("Error making prediction:", error);
    }
  };

  return (
    <div className="app">
      <h1>Customer Churn Prediction</h1>
      <form onSubmit={handleSubmit}>
        {/* Row 1 */}
        <div className="row">
          <label>
            Gender:
            <select name="gender" value={formData.gender} onChange={handleChange}>
              <option value="Female">Female</option>
              <option value="Male">Male</option>
            </select>
          </label>
          <label>
            Senior Citizen:
            <select
              name="SeniorCitizen"
              value={formData.SeniorCitizen}
              onChange={handleChange}
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </label>
          <label>
            Partner:
            <select name="Partner" value={formData.Partner} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </label>
          <label>
            Dependents:
            <select name="Dependents" value={formData.Dependents} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </label>
          <label>
            Tenure:
            <input
              type="number"
              name="tenure"
              value={formData.tenure}
              onChange={handleChange}
              min="1"
              max="200"
            />
          </label>
        </div>

        {/* Row 2 */}
        <div className="row">
          <label>
            Phone Service:
            <select name="PhoneService" value={formData.PhoneService} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </label>
          <label>
            Multiple Lines:
            <select name="MultipleLines" value={formData.MultipleLines} onChange={handleChange}>
              <option value="No phone service">No phone service</option>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </label>
          <label>
            Internet Service:
            <select name="InternetService" value={formData.InternetService} onChange={handleChange}>
              <option value="DSL">DSL</option>
              <option value="Fiber optic">Fiber optic</option>
              <option value="No">No</option>
            </select>
          </label>
          <label>
            Online Security:
            <select name="OnlineSecurity" value={formData.OnlineSecurity} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
        </div>

        {/* Row 3 */}
        <div className="row">
          <label>
            Online Backup:
            <select name="OnlineBackup" value={formData.OnlineBackup} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
          <label>
            Device Protection:
            <select name="DeviceProtection" value={formData.DeviceProtection} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
          <label>
            Tech Support:
            <select name="TechSupport" value={formData.TechSupport} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
          <label>
            Streaming TV:
            <select name="StreamingTV" value={formData.StreamingTV} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
        </div>

        {/* Row 4 */}
        <div className="row">
          <label>
            Streaming Movies:
            <select name="StreamingMovies" value={formData.StreamingMovies} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
              <option value="No internet service">No internet service</option>
            </select>
          </label>
          <label>
            Contract:
            <select name="Contract" value={formData.Contract} onChange={handleChange}>
              <option value="Month-to-month">Month-to-month</option>
              <option value="One year">One year</option>
              <option value="Two year">Two year</option>
            </select>
          </label>
          <label>
            Paperless Billing:
            <select name="PaperlessBilling" value={formData.PaperlessBilling} onChange={handleChange}>
              <option value="No">No</option>
              <option value="Yes">Yes</option>
            </select>
          </label>
          <label>
            Payment Method:
            <select name="PaymentMethod" value={formData.PaymentMethod} onChange={handleChange}>
              <option value="Electronic check">Electronic check</option>
              <option value="Mailed check">Mailed check</option>
              <option value="Bank transfer (automatic)">Bank transfer (automatic)</option>
              <option value="Credit card (automatic)">Credit card (automatic)</option>
            </select>
          </label>
        </div>

        {/* Row 5 */}
        <div className="row">
          <label>
            Monthly Charges:
            <input
              type="number"
              name="MonthlyCharges"
              value={formData.MonthlyCharges}
              onChange={handleChange}
              min="100"
              max="10000"
              step="0.01"
            />
          </label>
          <label>
            Total Charges:
            <input
              type="number"
              name="TotalCharges"
              value={formData.TotalCharges}
              onChange={handleChange}
              min="1000"
              max="100000"
              step="0.01"
            />
          </label>
        </div>

        <button type="submit">Predict</button>
      </form>

      {prediction && (
        <div className="result">
          <h2>Prediction Result:</h2>
          <p>Result: {prediction.result}</p>
          <p>Churn Probability: {prediction.churn_probability}%</p>
        </div>
      )}
    </div>
  );
}

export default App;
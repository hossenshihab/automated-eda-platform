# 📊 Automated EDA Platform

An interactive **Automated Exploratory Data Analysis (EDA) Platform** built using **Python**, **Streamlit**, and **Plotly**.

The platform allows users to upload any CSV dataset and instantly generate data profiling reports, statistical summaries, interactive visualizations, AI-powered insights, and perform common data cleaning operations—all without writing a single line of code.

---

## 🚀 Features

### 📂 Dataset Upload

- Upload any CSV dataset
- Automatic dataset loading
- Dataset overview

---

### ❤️ Dataset Health

- Data Quality Score
- Dataset Grade
- Missing value statistics
- Duplicate statistics

---

### 📈 Dataset Analysis

- Numerical Summary
- Categorical Summary
- Missing Value Summary
- Duplicate Summary
- Correlation Matrix
- Dataset Memory Usage
- Dataset Information

---

### 📊 Interactive Visualization

Supports:

- Histogram
- Distribution Plot
- Box Plot
- Violin Plot
- Scatter Plot
- Line Plot
- Bar Chart
- Pie Chart
- Correlation Heatmap
- Missing Value Chart

All visualizations are interactive using Plotly.

---

### 🧹 Data Cleaning Dashboard

Perform one-click cleaning operations:

- Fill Missing Values (Mean)
- Fill Missing Values (Median)
- Fill Missing Values (Mode)
- Drop Missing Rows
- Remove Duplicate Rows
- Encode Categorical Variables
- Standard Scaling
- Min-Max Scaling
- Drop Columns

Export cleaned datasets as CSV.

---

### 🧠 AI Insights Dashboard

Automatically generates:

- Dataset Readiness Score
- Dataset Status
- Missing Value Recommendations
- Duplicate Recommendations
- Outlier Detection
- Correlation Insights
- Overall Machine Learning Readiness

---

## 🖥️ Screenshots

### Home

![Home page](assets\screenshots\home.png)

---

### Dataset Upload

![Dataset upload 1](assets\screenshots\upload.png)

![Dataset upload 2](assets\screenshots\upload2.png)

---

### Analysis Dashboard

![Analysis-numeric](assets\screenshots\analysis_numeric.png)

![Analysis-categorical](assets\screenshots\analysis_categorical.png)

![Analysis-missing](assets\screenshots\analysis_missing.png)

![Analysis-correlation](assets\screenshots\analysis_correlation.png)

---

### Visualization Dashboard

*(Add screenshot here)*

---

### Cleaning Dashboard

*(Add screenshot here)*

---

### AI Insights Dashboard

*(Add screenshot here)*

---

## 📦 Installation

Clone the repository

```bash
git clone https://github.com/hossenshihab/automated-eda-platform.git
```

Move into the project

```bash
cd automated-eda-platform
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🛠️ Technologies Used

- Python
- Streamlit
- Plotly
- Pandas
- NumPy
- Scikit-learn

---

## 📁 Project Structure

```text
automated-eda-platform/
│
├── .streamlit/
│
├── data/
│
├── notebooks/
│
├── src/
│   ├── analyzer.py
│   ├── cleaner.py
│   ├── data_loader.py
│   ├── insights.py
│   ├── profiler.py
│   └── visualizer.py
│
├── app.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## 🎯 Future Improvements

- Support Excel Files
- PDF Report Generation
- AutoML Integration
- Feature Importance
- Model Recommendation
- Dark Theme
- Data Drift Detection
- Time Series Analysis

---

## 👨‍💻 Author

**Shihab Hossen**

Computer Science & Engineering

Port City International University

Chattogram-4202, Bangladesh

GitHub

https://github.com/hossenshihab

---

## ⭐ Support

If you like this project,

⭐ Star this repository.
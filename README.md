# 📊 Startup Funding Analysis (Streamlit App)

An interactive **data analysis dashboard** built using **Streamlit**, **Pandas**, and **Matplotlib** to explore and visualize startup funding data.

> ⚠️ **Note:** The dataset contains some inconsistencies (missing values, formatting issues, and possible inaccuracies). Basic cleaning has been applied, but results should be interpreted with caution.

---

## 🚀 Features

### 🔹 Overall Analysis

* Total investment across all startups
* Maximum single funding round
* Average funding per startup
* Total number of funded startups
* Month-on-Month (MoM) trends:

  * Total investment
  * Number of deals

### 🔹 Investor Analysis

* Most recent investments
* Biggest investments (bar chart)
* Sector-wise distribution (pie chart)
* Year-on-Year (YoY) trend

### 🔹 Startup Analysis *(In Progress)*

* UI structure implemented
* Can be extended with detailed startup insights

---

## 🛠️ Tech Stack

* **Streamlit** – UI & dashboard
* **Pandas** – Data manipulation
* **Matplotlib** – Visualization

---

## 📂 Project Structure

```bash
├── app.py                   # Main Streamlit application
├── projectSkeleton.py       # Initial/base structure of the project
├── startup_cleaned.csv      # Cleaned dataset
├── README.md                # Documentation
```

---

## 🧠 About `projectSkeleton.py`

This file contains the **initial structure / base logic** of the project.
It was used as a starting point before building the final Streamlit dashboard.

You can use it to:

* Understand the project flow step-by-step
* Compare raw vs final implementation
* Reuse or extend for future experiments

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/nadim45448/Indian-startup-funding-data-analysis.git
cd Indian-startup-funding-data-analysis
```

2. **Create virtual environment (recommended)**

```bash
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux
```
3. **Run the app**

```bash
streamlit run app.py
```
---

## 📊 Dataset

File: `startup_cleaned.csv`

### Columns:

* `startup` → Startup name
* `investors` → Investor names
* `amount` → Funding amount (in Crores)
* `date` → Investment date
* `vertical` → Sector
* `city` → Location
* `round` → Funding round

---

## 📈 Insights You Can Get

* Funding trends over time
* Top-funded startups
* Investor behavior patterns
* Sector-wise investment focus

---

## 🙌 Purpose

This project is built for **learning Streamlit and data analysis concepts**.

---

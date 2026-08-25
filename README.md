# 📊 Sales Data Analysis Dashboard

## 📌 Project Overview

The **Sales Data Analysis Dashboard** is a data analytics project built using **Python, Pandas, Matplotlib, and Microsoft Power BI**.

The project analyzes sales data to identify important business trends, product performance, regional performance, profitability, and monthly sales patterns.

Python is used for data generation, cleaning, validation, and analysis, while Power BI is used to create an interactive business intelligence dashboard.

---

## 🎯 Business Objectives

- Analyze overall sales and profit performance
- Identify the highest-performing product categories
- Compare sales performance across regions
- Analyze monthly sales trends
- Identify the top 10 products by sales
- Monitor key business KPIs
- Create an interactive dashboard for business decision-making

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Data processing and analysis |
| Pandas | Data cleaning and analysis |
| Matplotlib | Data visualization |
| Power BI | Interactive dashboard |
| Git | Version control |
| GitHub | Project hosting |

---

## 🔄 Project Workflow

```text
Sales Data
    ↓
Python Data Generation
    ↓
Data Cleaning & Validation
    ↓
Exploratory Data Analysis
    ↓
Sales & Profit Analysis
    ↓
Cleaned CSV Dataset
    ↓
Power BI
    ↓
Interactive Sales Dashboard
```

---

## 📂 Project Structure

```text
sales-data-analysis-dashboard
│
├── data
│   ├── sales_data.csv
│   ├── cleaned_sales_data.csv
│   └── sales_by_category.png
│
├── python
│   ├── create_sales_data.py
│   └── sales_analysis.py
│
├── dashboard
│   └── Sales_Analysis_Dashboard.pbix
│
└── README.md
```

---

## 🐍 Python Data Analysis

The Python analysis performs the following tasks:

- Loads the sales dataset
- Checks dataset structure
- Checks missing values
- Checks duplicate records
- Converts order dates into datetime format
- Calculates total sales
- Calculates total profit
- Calculates total quantity sold
- Calculates total orders
- Performs category-wise sales analysis
- Performs region-wise sales analysis
- Identifies top-performing products
- Performs monthly sales analysis
- Performs category-wise profit analysis
- Exports the cleaned dataset
- Creates a sales visualization using Matplotlib

---

## 📊 Power BI Dashboard

The Power BI dashboard provides an interactive view of sales performance.

### Key Performance Indicators

- **Total Sales**
- **Total Profit**
- **Total Quantity**
- **Total Orders**

### Dashboard Visualizations

- Sales by Category
- Sales by Region
- Monthly Sales Trend
- Top 10 Products by Sales

### Interactive Filters

- Category
- Region

Users can select different categories and regions to dynamically analyze the sales data.

---

## 🖼️ Dashboard Preview

The dashboard provides a visual overview of sales performance, profitability, regional performance, product performance, and monthly sales trends.

![Sales Performance Dashboard](./Screenshot%202026-08-25%20233532.png)

---

## 💡 Key Business Insights

The dashboard can be used to identify:

- Which product categories generate the highest sales
- Which regions contribute the most revenue
- Which products are the top performers
- How sales change over time
- Which categories generate higher profits
- Overall sales and profitability performance

---

## ▶️ How to Run the Python Analysis

### 1. Clone the repository

```bash
git clone https://github.com/kgpreddy41/sales-data-analysis-dashboard.git
```

### 2. Open the project directory

```bash
cd sales-data-analysis-dashboard
```

### 3. Install required libraries

```bash
pip install pandas matplotlib
```

### 4. Generate the sales dataset

```bash
python python/create_sales_data.py
```

### 5. Run the sales analysis

```bash
python python/sales_analysis.py
```

The cleaned dataset will be generated inside the `data` folder.

---

## 📈 Power BI Dashboard

Open the following file using **Power BI Desktop**:

```text
dashboard/Sales_Analysis_Dashboard.pbix
```

The dashboard can then be explored using the available charts and slicers.

---

## 🚀 Skills Demonstrated

This project demonstrates practical experience with:

- Python Programming
- Pandas
- Data Cleaning
- Exploratory Data Analysis
- Data Visualization
- Business Intelligence
- Power BI
- KPI Development
- Data Analysis
- Git & GitHub
- Dashboard Development

---

## 👨‍💻 Author

**KGPR Reddy**

GitHub:  
https://github.com/kgpreddy41

---

## ⭐ Project

If you find this project useful, consider giving the repository a ⭐ on GitHub.

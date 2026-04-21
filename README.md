# 🐍 Python for Chartered Accountants (CAs)

A comprehensive, interactive Streamlit web application designed to teach Python programming basics to Chartered Accountant students and finance professionals with zero prior coding experience. 

This educational dashboard uses practical, finance-specific examples—such as tax calculations, GST automation, and financial data analysis—to make learning practical, engaging, and highly relevant to professional CA practice.

---

## 🌟 Key Features

- **Interactive Learning Environment:** Written entirely as a Streamlit application, providing immediate visual feedback for Python execution.
- **Finance-Specific Scenarios:** Modules focus on real-world use cases like reconciliation reports, finding outliers in audit logs, and processing massive bank statements.
- **Advanced Visualizations:** Includes engaging interactive charts (Waterfall for P&L, Correlation Heatmaps, Boxplots for Anomaly Detection) using modern libraries like Matplotlib, Seaborn, and Plotly.
- **Machine Learning Integrations:** Dedicated modules to differentiate between Supervised and Unsupervised learning with built-in mock credit risk and fraud prediction tools.
- **Gamified Quiz Section:** End-of-course assessments that track module progress.

## 🗂️ Course Modules Included

1. **Home:** Introduction to the "Why" (Automating GST, Tax Calculations, KPIs).
2. **Python Basics:** Variables, Data Types, and dynamic Net Income calculations.
3. **Control Statements:** Conditional logic with a Tax Slab calculator and iteration loops.
4. **Data Structures:** Lists (Ledgers), Dictionaries (Client Info), Tuples & Sets (Tax Rates).
5. **File Operations:** Safe manipulation of `.txt` and `.csv` files (Audits and Reconciliations).
6. **Data Analysis:** Working with NumPy and Pandas as your ultimate Excel replacement.
7. **Data Preprocessing & EDA:** Identifying anomalies, handling missing PANs, and manipulating dirty datasets. 
8. **Advanced Visualization:** Visualizing distributions and relationships using robust libraries.
9. **Machine Learning Basics:** Concept demonstrations of ML applied to credit risk assessment.
10. **Mini Projects:** Practical tools including:
    - 📱 Income Tax Calculator
    - 🛒 GST Invoice Calculator
    - 📊 Expense Analyzer Dashboard
11. **Quiz Section:** Interactive progressive assessment.

## 🛠️ Technology Stack

- **Frontend & Navigation:** [Streamlit](https://streamlit.io/)
- **Data Manipulation:** `pandas`, `numpy`
- **Visualization:** `matplotlib`, `seaborn`, `plotly`

## 🚀 Installation & Setup

Want to run this project locally on your machine?

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/python-for-cas.git
   cd python-for-cas
   ```

2. **Create a virtual environment (Optional but Recommended):**
   ```bash
   # On Windows
   python -m venv venv
   venv\Scripts\activate

   # On macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   *Make sure your `requirements.txt` includes: `streamlit`, `pandas`, `numpy`, `matplotlib`, `seaborn`, and `plotly`.*

4. **Launch the Application:**
   ```bash
   streamlit run app.py
   ```
   This will start a local server and automatically open the application in your default web browser on port `8501`.

## 🤝 Contributing

Contributions to improve the curriculum, add more tax frameworks, or optimize the code are always welcome!
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/NewFinanceModule`)
3. Commit your Changes (`git commit -m 'Added depreciation calculator'`)
4. Push to the Branch (`git push origin feature/NewFinanceModule`)
5. Open a Pull Request

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---
*Created by CA Rajat Agrawal / Prokhata*

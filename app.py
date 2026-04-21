import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import io
# Setup Streamlit
st.set_page_config(page_title="Python for CAs", page_icon="📊", layout="wide", initial_sidebar_state="expanded")

# Initialize session state for quiz
if 'quiz_score' not in st.session_state:
    st.session_state.quiz_score = 0
if 'quiz_submitted' not in st.session_state:
    st.session_state.quiz_submitted = False

def home_section():
    st.title("🐍 Python for Chartered Accountants")
    st.markdown("### Why should a CA learn Python?")
    
    st.info("Python is essentially 'Excel on steroids'. While spreadsheets are great, Python allows you to automate repetitive tasks, handle massive datasets (millions of rows) without crashing, and create repeatable data pipelines.")
    
    st.markdown("#### Primary Use Cases in Finance & Tax:")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success("**1. GST Automation**\n\nAutomatically reconcile GSTR-2A with purchase registers in seconds, matching invoices algorithmically.")
        st.error("**2. Data Analysis**\n\nProcess enormous bank statements, identify suspicious transactions, and extract meaningful insights effortlessly.")
    with col2:
        st.warning("**3. Tax Calculations**\n\nBuild complex tax calculators that instantly update across thousands of client portfolios based on the latest tax slabs.")
        st.info("**4. Financial Dashboards**\n\nCreate interactive, real-time dashboards to showcase cash flows, expenditures, and KPIs to clients dynamically.")

    st.markdown("---")
    st.markdown("👈 **Get started by selecting a module from the sidebar navigation.**")


def basics_section():
    st.header("1. Python Basics: The Building Blocks")
    st.write("Before we conquer the data world, let's understand the basic vocabulary of Python.")
    
    tab1, tab2, tab3 = st.tabs(["Variables", "Data Types", "Interactive Demo"])
    
    with tab1:
        st.subheader("Variables (Storage Containers)")
        st.write("Think of a variable as a labeled box where you store data. In finance, this could be income, expenses, or client names.")
        st.code("""
# Storing financial data in variables
client_name = "ABC Corp"
annual_revenue = 5000000
tax_rate = 0.25
        """, language="python")
        
    with tab2:
        st.subheader("Data Types (The nature of data)")
        st.markdown("- **Integers (`int`)**: Whole numbers (e.g., `500`, `-200`)\n- **Floats (`float`)**: Decimal numbers (e.g., `18.5`, `99.99`)\n- **Strings (`str`)**: Text (e.g., `'Invoice #1001'`, `'GSTIN'`) \n- **Booleans (`bool`)**: True or False conditions (e.g., `is_audited = True`)")
        st.code("""
# Type examples
total_invoices = 50       # Integer
gst_percentage = 18.0     # Float
company_status = "Active" # String
is_compliant = True       # Boolean
        """, language="python")
        
    with tab3:
        st.subheader("Interactive Try-it-Out: Calculating Net Income")
        with st.container():
            st.write("Let's simulate how Python takes user input, converts its type, and calculates a result.")
            col1, col2 = st.columns(2)
            with col1:
                gross_income = st.number_input("Enter Gross Income (int/float):", value=1000000, step=10000)
                total_expenses = st.number_input("Enter Total Expenses (int/float):", value=450000, step=10000)
            
            with col2:
                st.write("**Python Code Equivalent:**")
                st.code(f"""
gross_income = float({gross_income}) 
total_expenses = float({total_expenses})
net_income = gross_income - total_expenses

print("Net Income is:", net_income)
                """, language="python")
                
                net_inc = gross_income - total_expenses
                st.success(f"**Output computed by Python:** Net Income is ₹ {net_inc:,.2f}")


def control_statements_section():
    st.header("2. Control Statements (Making Decisions)")
    st.write("Control statements allow Python to make decisions, just like a CA deciding which tax slab applies, or looping through hundreds of invoices to find anomalies.")
    
    st.subheader("If-Elif-Else (Conditional Logic)")
    st.write("Used to execute different blocks of code based on certain conditions.")
    
    col1, col2 = st.columns([1, 1])
    with col1:
        st.code("""
# Example: Tax Slab Routing
income = 800000

if income <= 300000:
    tax = 0
elif income <= 600000:
    tax = (income - 300000) * 0.05
else:
    tax = 15000 + (income - 600000) * 0.10

print("Tax liability:", tax)
        """, language="python")

    with col2:
        st.info("**Interactive Tax Slab Calculator (New Regime Mockup)**")
        user_income = st.number_input("Enter your income to evaluate tax logic:", value=800000, step=50000)
        
        if user_income <= 300000:
            calc_tax = 0
            slab_msg = "Slab 1: Up to 3L (0%)"
        elif user_income <= 600000:
            calc_tax = (user_income - 300000) * 0.05
            slab_msg = "Slab 2: 3L to 6L (5%)"
        elif user_income <= 900000:
            calc_tax = 15000 + (user_income - 600000) * 0.10
            slab_msg = "Slab 3: 6L to 9L (10%)"
        elif user_income <= 1200000:
            calc_tax = 45000 + (user_income - 900000) * 0.15
            slab_msg = "Slab 4: 9L to 12L (15%)"
        elif user_income <= 1500000:
            calc_tax = 90000 + (user_income - 1200000) * 0.20
            slab_msg = "Slab 5: 12L to 15L (20%)"
        else:
            calc_tax = 150000 + (user_income - 1500000) * 0.30
            slab_msg = "Slab 6: Above 15L (30%)"
            
        st.write(f"**Computed Tax:** ₹ {calc_tax:,.2f}")
        st.write(f"**Highest Applicable Slab:** {slab_msg}")

    st.markdown("---")
    st.subheader("For & While Loops (Iteration)")
    st.write("Loops allow you to run the same code over and over. E.g., summing up a list of 5,000 transactions.")
    
    st.code("""
# Let's say we have a list of invoice amounts
transactions = [5000, -200, 15000, 8000, -1500]
total_sales = 0

for t in transactions:
    if t > 0:  # Only add positive amounts (sales)
        total_sales += t

print("Total Sales for the month:", total_sales)
    """, language="python")


def data_structures_section():
    st.header("3. Data Structures (Organizing Information)")
    st.write("If variables are boxes, data structures are filing cabinets. They hold multiple items together.")
    
    tab1, tab2, tab3 = st.tabs(["Lists", "Dictionaries", "Tuples & Sets"])
    
    with tab1:
        st.subheader("Lists `[]`")
        st.write("An ordered, mutable (changeable) collection of items. Great for sequential data like a ledger.")
        st.code("""
# A list of monthly expenses
expenses = [12000, 15500, 9000, 22000]

expenses.append(5000)  # Adding a new expense
print(expenses[0])     # Accessing the first item (Index 0)
        """, language="python")
        
        st.info("Try modifying a List:")
        new_exp = st.text_input("Add a new expense amount (comma separated for multiple):", value="3000, 4500")
        base_list = [12000, 15000]
        try:
            added_list = [int(x.strip()) for x in new_exp.split(",") if x.strip().lstrip('-').isdigit()]
            final_list = base_list + added_list
            st.write(f"**Current List in Memory:** `{final_list}`")
            st.write(f"**Sum of all elements:** ₹ {sum(final_list):,}")
        except:
            st.error("Please enter valid numbers formatted properly (e.g., 3000, 4500).")

    with tab2:
        st.subheader("Dictionaries `{}`")
        st.write("A collection of Key-Value pairs. Highly useful for mapping client IDs to names or GST state codes.")
        st.code("""
# Dictionary holding Client Data
client_data = {
    'GSTIN': '27ABCDE1234F1Z5',
    'Name': 'Reliance Retail',
    'Turnover': 50000000
}

# Accessing the Name
print(client_data['Name'])
        """, language="python")
        
    with tab3:
        st.subheader("Tuples `()` and Sets `{}`")
        st.write("**Tuples**: Ordered, but unchangeable. Useful for fixed data like Tax Slabs or Months in a year.")
        st.write("**Sets**: Unordered, unindexed, and contain NO duplicate values. Great for finding unique entries.")
        st.code("""
# Tuple
months = ('Jan', 'Feb', 'Mar')

# Set (Removes duplicates automatically)
gst_rates = {0, 5, 12, 18, 28, 18, 5}
print(gst_rates)  # Output: {0, 5, 12, 18, 28}
        """, language="python")


def file_handling_section():
    st.header("5. File Handling & Operations")
    st.write("CAs deal with hundreds of files daily. Python can open, read, write, and extract data from invoices and ledgers automatically.")
    
    st.subheader("Reading and Writing Files")
    st.write("Using built-in Python functions, we can manipulate `.txt`, `.csv`, `.log`, and even `.pdf` files without physically opening them in an application.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Reading an Audit Log** (`'r'` Mode)")
        st.code('''
# Opening an audit log to find errors
with open("audit_log.txt", "r") as file:
    logs = file.readlines()
    for line in logs:
        if "ERROR" in line:
            print("Anomaly Found:", line)
        ''', language="python")
        
    with col2:
        st.markdown("**2. Writing a Reconciliation Report** (`'w'` Mode)")
        st.code('''
# Generating a quick text report
report = "Total Invoices Matched: 1540\\nPending: 12"

with open("reconciliation_summary.txt", "w") as file:
    file.write(report)
print("Report Generated!")
        ''', language="python")
        
    st.info("💡 Advanced libraries like Pandas (covered next) handle `.csv` and `.xlsx` files incredibly easily, making manual Excel fetching obsolete!")
    st.markdown("---")


def libraries_section():
    st.header("4. Libraries (NumPy & Pandas)")
    st.write("Libraries are pre-written bundles of code that save us from reinventing the wheel. Pandas and NumPy are the undisputed kings of Data Analytics in Python.")
    
    st.subheader("Pandas - Your Excel Replacement")
    st.write("Pandas handles tabular data using 'DataFrames'. Let's see it in action.")
    
    # Generate some sample CA data
    np.random.seed(42)
    dates = pd.date_range(start='2023-01-01', periods=20, freq='D')
    categories = np.random.choice(['Consulting', 'Audit', 'Tax Filing', 'Retainer'], 20)
    amounts = np.random.randint(5000, 50000, size=20)
    gst_applicable = np.where(categories == 'Audit', amounts * 0.18, amounts * 0) # Mock logic
    
    sample_df = pd.DataFrame({
        'Date': dates,
        'Service_Category': categories,
        'Base_Amount': amounts,
        'GST_Amount': gst_applicable.astype(int)
    })
    sample_df['Total_Invoice'] = sample_df['Base_Amount'] + sample_df['GST_Amount']
    
    st.write("Here is a mock `DataFrame` representing an invoice sales register generated via code:")
    st.dataframe(sample_df, use_container_width=True)
    
    st.write("### Data Manipulation with Pandas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**1. Filtering Data**")
        selected_cat = st.selectbox("Select a Category to filter:", sample_df['Service_Category'].unique())
        filtered_df = sample_df[sample_df['Service_Category'] == selected_cat]
        st.dataframe(filtered_df[['Date', 'Base_Amount']])
    with col2:
        st.markdown("**2. Grouping & Summarizing (Pivot Table equivalent)**")
        st.write("Total Revenue per Category:")
        grouped_df = sample_df.groupby('Service_Category')['Total_Invoice'].sum().reset_index()
        st.dataframe(grouped_df)

    st.markdown("---")
    st.subheader("Try it yourself: Upload a CSV File")
    st.write("Upload any small CSV (e.g., your bank statement or expense sheet snippet) to see Pandas instantly parse it.")
    
    # Let's create a template csv for them to download and try if they want
    template_csv = "Date,Description,Amount\n2023-10-01,Office Rent,25000\n2023-10-05,Printing,1500\n2023-10-15,Audit Fees,85000"
    st.download_button("Download Sample CSV to Test", data=template_csv.encode('utf-8'), file_name='sample_expense.csv', mime='text/csv')

    uploaded_file = st.file_uploader("Upload CSV", type="csv")
    if uploaded_file is not None:
        user_df = pd.read_csv(uploaded_file)
        st.write("**Preview of your Data:**")
        st.dataframe(user_df.head(), use_container_width=True)
        st.write(f"**Dataset Shape:** {user_df.shape[0]} Rows, {user_df.shape[1]} Columns")


def data_preprocessing_section():
    st.header("7. Data Preprocessing & Exploratory Data Analysis (EDA)")
    st.write("Raw data from clients is often messy: missing PANs, duplicate entries, and extreme outliers. Pandas provides tools to 'clean' this data (Preprocessing) and understand its structure (EDA).")
    
    tab1, tab2 = st.tabs(["Data Cleaning", "Exploratory Data Analysis (EDA)"])
    
    # Mock Messy Data
    raw_data = pd.DataFrame({
        'Invoice_ID': ['INV-001', 'INV-002', 'INV-002', 'INV-004', 'INV-005'],
        'Client_GSTIN': ['27A...', None, '27A...', '06B...', '29C...'],
        'Amount': [15000, 2000000, 2000000, np.nan, 12000] # Outlier and NaN
    })
    
    with tab1:
        st.subheader("Cleaning ledgers (Handling Missing Data & Duplicates)")
        st.write("Notice the duplicates and missing values in the raw dataset below:")
        st.dataframe(raw_data, use_container_width=True)
        
        st.code('''
# 1. Drop duplicate rows
clean_df = raw_data.drop_duplicates()

# 2. Fill Missing (NaN) values with 0
clean_df['Amount'].fillna(0, inplace=True)

# 3. Fill Missing text
clean_df['Client_GSTIN'].fillna('Unregistered', inplace=True)
        ''', language="python")
        
        clean_df = raw_data.drop_duplicates().copy()
        clean_df['Amount'] = clean_df['Amount'].fillna(0)
        clean_df['Client_GSTIN'] = clean_df['Client_GSTIN'].fillna('Unregistered')
        
        st.success("**Cleaned Data:**")
        st.dataframe(clean_df, use_container_width=True)
        
    with tab2:
        st.subheader("EDA: Catching Outliers & Summarizing")
        st.write("EDA helps us find anomalies. Look at the `Amount` column. Does `2,000,000` look like a normal transaction?")
        st.code('''
# Describe generates a statistical summary
summary = clean_df.describe()
print(summary)
        ''', language="python")
        st.dataframe(clean_df.describe(), use_container_width=True)
        st.warning("The statistical summary shows a massive max value compared to the 25th/50th percentiles. This is an outlier we should investigate!")


def visualization_section():
    st.header("5. Data Visualization")
    st.write("Communicating data to clients is as important as analyzing it. Matplotlib and Seaborn allow you to create stunning visualizations with a few lines of code.")
    
    # Generate data for plotting
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
    sales = [150, 200, 180, 220, 250, 300]
    expenses = [100, 120, 110, 130, 140, 160]
    profit = np.array(sales) - np.array(expenses)
    
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Chart Selector")
        chart_type = st.radio("Choose Chart Type:", 
            ("Vertical Bar Chart", "Line Chart", "Histogram (Invoice Sizes)", "Boxplot (Outlier Detection)", "Heatmap (Correlation)", "Waterfall Chart (Plotly)", "Donut Chart (Plotly)", "Time Series (Plotly)")
        )
    
    with col2:
        if "Plotly" not in chart_type:
            fig, ax = plt.subplots(figsize=(8, 4))
            fig.patch.set_facecolor('none')
            ax.set_facecolor('none')
            ax.spines['bottom'].set_color('gray')
            ax.spines['left'].set_color('gray')
            ax.tick_params(axis='x', colors='gray')
            ax.tick_params(axis='y', colors='gray')
            ax.yaxis.label.set_color('gray')
            ax.xaxis.label.set_color('gray')
            ax.title.set_color('gray')
    
            if chart_type == "Vertical Bar Chart":
                ax.bar(months, sales, label='Sales', color='#4c72b0')
                ax.bar(months, expenses, label='Expenses', color='#dd8452', alpha=0.9)
                ax.set_title("Monthly Sales vs Expenses")
                ax.legend()
                
            elif chart_type == "Line Chart":
                ax.plot(months, sales, marker='o', label='Sales', color='#4c72b0')
                ax.plot(months, profit, marker='s', label='Profit', color='#55a868', linestyle='--')
                ax.set_title("Sales & Profit Trend")
                ax.legend()
                
            elif chart_type == "Histogram (Invoice Sizes)":
                 mock_inv_sizes = np.random.normal(loc=15000, scale=4000, size=200)
                 ax.hist(mock_inv_sizes, bins=15, color='#8172b2', edgecolor='white')
                 ax.set_title("Distribution of Invoice Sizes")
                 ax.set_xlabel("Invoice Amount (₹)")
                 
            elif chart_type == "Boxplot (Outlier Detection)":
                 mock_inv_sizes = np.concatenate([np.random.normal(15000, 2000, 100), [45000, 50000, 52000]]) # Added outliers
                 sns.boxplot(x=mock_inv_sizes, color='#55a868', ax=ax)
                 ax.set_title("Boxplot highlighting extreme high value invoices")
                 
            elif chart_type == "Heatmap (Correlation)":
                 # Correlation between Sales, Expenses, and Marketing
                 data_corr = pd.DataFrame({'Sales': sales, 'Expenses': expenses, 'Marketing': [50, 70, 60, 80, 100, 120]})
                 corr_matrix = data_corr.corr()
                 sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax, cbar=False)
                 ax.set_title("Correlation Heatmap")
                 
            st.pyplot(fig)
            
        else:
            # Plotly Interactive Charts
            if chart_type == "Waterfall Chart (Plotly)":
                fig = go.Figure(go.Waterfall(
                    name = "P&L", orientation = "v",
                    measure = ["relative", "relative", "relative", "total"],
                    x = ["Revenue", "COGS", "Operating Expenses", "Net Profit"],
                    textposition = "outside",
                    text = ["+5M", "-2M", "-1M", "2M"],
                    y = [5000000, -2000000, -1000000, 2000000],
                    connector = {"line":{"color":"rgb(63, 63, 63)"}}
                ))
                fig.update_layout(title = "Profit & Loss Waterfall", showlegend = False, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='gray'))
                st.plotly_chart(fig, use_container_width=True)
                
            elif chart_type == "Donut Chart (Plotly)":
                exp_categories = ['Salaries', 'Rent', 'IT Utils', 'Travel']
                exp_values = [450, 200, 150, 80]
                fig = go.Figure(data=[go.Pie(labels=exp_categories, values=exp_values, hole=.5)])
                fig.update_layout(title="Operating Expense Distribution", paper_bgcolor='rgba(0,0,0,0)', font=dict(color='gray'))
                st.plotly_chart(fig, use_container_width=True)
                
            elif chart_type == "Time Series (Plotly)":
                ts_dates = pd.date_range(start='2020-01-01', periods=24, freq='ME')
                ts_sales = np.linspace(100, 200, 24) + np.sin(np.arange(24)) * 20 # Upward trend + seasonality
                fig = px.line(x=ts_dates, y=ts_sales, title="Interactive Time Series (Sales Trend & Seasonality)", labels={'x':'Date', 'y':'Sales Volumes'})
                fig.update_layout(paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font=dict(color='gray'))
                st.plotly_chart(fig, use_container_width=True)
        
    st.info("💡 In real CA practice, these charts can be generated programmatically for hundreds of clients and embedded automatically into PDF reports without touching a single Excel graph!")


def machine_learning_section():
    st.header("9. Machine Learning for Finance")
    st.write("Machine Learning (ML) is algorithms learning from historical data to make future predictions. It is essentially finding patterns in vast amounts of data—something CAs already do, but at massive scale!")
    
    st.markdown("### Supervised vs. Unsupervised Learning")
    col1, col2 = st.columns(2)
    with col1:
        st.success("**Supervised Learning**\\nWe provide labeled data (e.g., past loans marked as 'Default' or 'Paid'). The algorithm learns the mapping to predict if a *new* loan will default. Used for **Credit Risk Analysis**.")
    with col2:
        st.warning("**Unsupervised Learning**\\nWe provide unlabeled data. The algorithm finds hidden structures. For example, grouping similar transactions to flag anomalies. Used for **Fraud Detection**.")

    st.markdown("---")
    st.subheader("Interactive ML Demo: Credit Risk Assessor (Supervised)")
    st.write("Play with the parameters below. A mock ML model will evaluate the input and predict the probability of loan default.")
    
    # Mock credit risk model using a logistic function
    c1, c2, c3 = st.columns(3)
    with c1:
        debt_to_income = st.slider("Debt-to-Income Ratio (%)", 10, 80, 35)
    with c2:
        credit_score = st.slider("Credit Score (CIBIL)", 300, 900, 700)
    with c3:
        loan_amount = st.number_input("Loan Amount (Lakhs)", 1, 100, 10)
        
    # Mock probability formula
    dti_factor = (debt_to_income - 35) * 0.015
    credit_factor = (700 - credit_score) * 0.002
    loan_factor = loan_amount * 0.001
    
    probability = max(0.01, min(0.99, 0.15 + dti_factor + credit_factor + loan_factor))
    
    st.write("### Prediction Engine Result")
    if probability > 0.5:
        st.error(f"🚨 **High Risk of Default!** Probability: {probability:.1%}\\nRecommendation: Reject Loan or Require Collateral.")
    elif probability > 0.3:
        st.warning(f"⚠️ **Moderate Risk.** Probability: {probability:.1%}\\nRecommendation: Proceed with Caution, higher interest rate applicable.")
    else:
        st.success(f"✅ **Low Risk.** Probability: {probability:.1%}\\nRecommendation: Approve Loan.")


def projects_section():
    st.header("6. Mini Projects (Practical Application)")
    st.write("Let's bring everything together in 3 simple, practical tools every CA can relate to.")
    
    tab1, tab2, tab3 = st.tabs(["Income Tax Calculator", "GST Invoice Calculator", "Expense Analyzer Dashboard"])
    
    with tab1:
        st.subheader("📱 Income Tax Calculator (Old vs New Regime)")
        st.write("A simplified comparison tool.")
        p_col1, p_col2 = st.columns(2)
        with p_col1:
            inc = st.number_input("Gross Annual Income", value=1200000, step=100000, key="it_inc")
            deductions = st.number_input("Section 80C & Other Deductions (Old)", value=150000, step=10000, key="it_ded")
        
        with p_col2:
            st.markdown("#### Tax Calculations (Simplistic):")
            # Simplified mock calculations
            tax_new = (inc - 700000) * 0.1 if inc > 700000 else 0
            tax_new = max(tax_new, 0)
            
            taxable_old = max(inc - deductions, 0)
            tax_old = (taxable_old - 500000) * 0.2 if taxable_old > 500000 else 0
            tax_old = max(tax_old, 0)
            
            st.write(f"**Tax under New Regime:** ₹ {tax_new:,.2f}")
            st.write(f"**Tax under Old Regime:** ₹ {tax_old:,.2f}")
            if tax_new < tax_old:
                st.success("Recommendation: Opt for **New Regime**")
            elif tax_old < tax_new:
                st.success("Recommendation: Opt for **Old Regime**")
            else:
                st.success("Recommendation: Taxes are equal. You can choose either.")
                
    with tab2:
        st.subheader("🛒 GST Calculator")
        st.write("Easily ascertain CGST, SGST, and IGST components on base or total amounts.")
        
        calc_type = st.radio("Calculation Basis:", ("Add GST to Base Amount", "Extract GST from Total Amount"), horizontal=True)
        g_col1, g_col2 = st.columns(2)
        with g_col1:
            amt = st.number_input("Amount (₹)", value=10000.0, step=100.0)
            rate = st.selectbox("GST Rate (%)", [5, 12, 18, 28], index=2)
            is_inter_state = st.checkbox("Inter-state Supply (IGST)")
        
        with g_col2:
            if calc_type == "Add GST to Base Amount":
                gst_amt = amt * (rate / 100)
                total = amt + gst_amt
                base = amt
            else:
                base = amt / (1 + (rate / 100))
                gst_amt = amt - base
                total = amt
                
            st.write(f"**Base Amount:** ₹ {base:,.2f}")
            if is_inter_state:
                st.write(f"**IGST ({rate}%):** ₹ {gst_amt:,.2f}")
            else:
                st.write(f"**CGST ({rate/2}%):** ₹ {gst_amt/2:,.2f}")
                st.write(f"**SGST ({rate/2}%):** ₹ {gst_amt/2:,.2f}")
                
            st.write(f"### **Total Invoice Value:** ₹ {total:,.2f}")

    with tab3:
        st.subheader("📊 Expense Analyzer Dashboard")
        st.write("Generate a quick CSV report of expenses, analyze it, and download results.")
        
        # Simulated data
        mock_data = pd.DataFrame({
            'Description': ['Office Rent', 'Electricity', 'Software Subs', 'Travel', 'Stationery', 'Consultant Fees'],
            'Amount': [45000, 8000, 15000, 12000, 3000, 25000],
            'Category': ['Fixed', 'Variable', 'Variable', 'Variable', 'Variable', 'Fixed']
        })
        st.dataframe(mock_data, use_container_width=True)
        
        grouped = mock_data.groupby('Category')['Amount'].sum().reset_index()
        
        col_c, col_d = st.columns(2)
        with col_c:
            st.write("**Summary by Category:**")
            st.dataframe(grouped, hide_index=True)
            
        with col_d:
            # Provide CSV download button
            csv = grouped.to_csv(index=False).encode('utf-8')
            st.download_button(
                label="📥 Download Summary as CSV",
                data=csv,
                file_name='expense_summary.csv',
                mime='text/csv',
            )


def quiz_section():
    st.header("7. Knowledge Check (Quiz Section)")
    st.write("Test what you've learned. Select the correct options below.")
    
    questions = [
        {"q": "1. Which data type is used to store text in Python?", "options": ["int", "float", "str", "bool"], "ans": "str"},
        {"q": "2. Which Pandas data structure is used for tabular (Excel-like) data?", "options": ["Series", "DataFrame", "List", "Dictionary"], "ans": "DataFrame"},
        {"q": "3. Which option correctly opens a file for writing in Python?", "options": ["open('data.csv', 'r')", "open('data.csv', 'w')", "file('data.csv', 'open')", "open('data.csv', 'read')"], "ans": "open('data.csv', 'w')"},
        {"q": "4. Which visualization is BEST used to detect outliers in transaction sizes?", "options": ["Line Chart", "Pie Chart", "Boxplot", "Bar Chart"], "ans": "Boxplot"},
        {"q": "5. What category of Machine Learning predicts outcomes based on historical LABELED data?", "options": ["Supervised Learning", "Unsupervised Learning", "Automated Learning", "Reinforcement Learning"], "ans": "Supervised Learning"}
    ]
    
    with st.form("quiz_form"):
        user_answers = []
        for idx, q_dict in enumerate(questions):
            st.markdown(f"**{q_dict['q']}**")
            ans = st.radio(f"Options for Q{idx+1}", q_dict["options"], key=f"q_{idx}", label_visibility="collapsed")
            user_answers.append((ans, q_dict["ans"]))
            st.write("")
            
        submit_btn = st.form_submit_button("Submit Quiz")
        
    if submit_btn:
        score = sum(1 for usr, true_ans in user_answers if usr == true_ans)
        st.session_state.quiz_score = score
        st.session_state.quiz_submitted = True
        
    if st.session_state.quiz_submitted:
        st.markdown("### Results")
        total = len(questions)
        st.metric(label="Your Score", value=f"{st.session_state.quiz_score} / {total}")
        progress = st.session_state.quiz_score / total
        st.progress(progress)
        
        if st.session_state.quiz_score == total:
            st.balloons()
            st.success("🏆 Excellent! You're ready to automate your CA firm!")
        elif st.session_state.quiz_score >= 2:
            st.info("👍 Good job! A little more practice and you'll be a Python pro.")
        else:
            st.warning("Needs improvement. Keep reviewing the basics. You'll get it!")


def main():
    st.sidebar.title("📚 Course Navigation")
    
    sections = {
        "1. Home": home_section,
        "2. Python Basics": basics_section,
        "3. Control Statements": control_statements_section,
        "4. Data Structures": data_structures_section,
        "5. File Operations": file_handling_section,
        "6. Data Analysis (NumPy/Pandas)": libraries_section,
        "7. Data Preprocessing & EDA": data_preprocessing_section,
        "8. Advanced Visualization": visualization_section,
        "9. Machine Learning Basics": machine_learning_section,
        "10. Mini Projects": projects_section,
        "11. Quiz Section": quiz_section
    }
    
    choice = st.sidebar.radio("Navigate to module:", list(sections.keys()))
    
    st.sidebar.markdown("---")
    
    # Progress visualization (Optional Bonus tracking)
    st.sidebar.markdown("**Course Progress Tracker**")
    if 'completed_modules' not in st.session_state:
        st.session_state.completed_modules = set()
        
    # Clean up any old cached module names
    st.session_state.completed_modules = set(m for m in st.session_state.completed_modules if m in sections)
    st.session_state.completed_modules.add(choice)
    
    progress_val = len(st.session_state.completed_modules) / len(sections)
    progress_val = min(1.0, max(0.0, progress_val)) # Ensure it strictly stays within [0.0, 1.0]

    st.sidebar.progress(progress_val)
    st.sidebar.write(f"{int(progress_val * 100)}% Completed")
    
    
    st.sidebar.markdown("---")
    st.sidebar.info("**Author:** CA Rajat Agrawal.\n\n*Visit ❤️ Prokhata.com.*")
    
    # Render the selected section
    sections[choice]()

if __name__ == "__main__":
    main()

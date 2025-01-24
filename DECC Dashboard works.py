import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from streamlit_extras.metric_cards import style_metric_cards

# Set page configuration
st.set_page_config(
    page_title="Financial Dashboard",
    layout="wide",
    initial_sidebar_state="expanded",
    page_icon="📊",
)

# Sample Data
balance = "$25,580.75 (€24,526.50)"
budget_data = {
    "Germany Budget": {
        "Total": "$3,200.00",
        "Spent": "$3,166.19 (€3,036.30)",
        "Categories": {
            "Transportation": 62.80,
            "Rent": 1800.00,
            "Entertainment": 154.67,
            "Education": 123.54,
            "Utilities": 179.20,
            "Groceries": 845.98,
        },
    },
    "US Budget": {
        "Total": "$3,000.00",
        "Spent": "$2,801.97 (€2,687.30)",
        "Categories": {
            "Transportation": 113.67,
            "Mortgage": 1502.16,
            "Home maintenance": 312.43,
            "Utilities": 416.82,
            "Groceries": 456.89,
        },
    },
}
bills = [
    {"Name": "Germany Rent Payment", "Amount": 1800.00, "Due Date": "1st June"},
    {"Name": "O2 - Internet", "Amount": 39.99, "Due Date": "1st June"},
    {"Name": "REWAG - Utilities", "Amount": 30.00, "Due Date": "1st June"},
]

credit_cards = {
    "Total Credit Card Debt": "$5,420.10",
    "Star Card": "$1,645.98",
    "USAA": "$3,774.12",
    "Recommendation": "You're slightly over the recommended 30% (36.13%) utilization rate. Paying down $1,020 would bring your overall rate to 30% or below.",
}

investments = {
    "Total Investments": "$53,926.44",
    "Breakdown": {
        "Schwab": "$7,890.32",
        "Fidelity": "$12,487.23",
        "Thrift Savings Plan": "$33,548.89",
    },
}

ai_insight = "You have $231.84 (€222.33) remaining for both of your May 2024 household budgets."

# Style Improvements
def style_section_title(title):
    st.markdown(f"<h2 style='text-align: center; color: #4CAF50;'>{title}</h2>", unsafe_allow_html=True)

def style_subheader(text):
    st.markdown(f"<h3 style='color: #4CAF50;'>{text}</h3>", unsafe_allow_html=True)

# Create bar chart for category breakdown
def create_bar_chart(categories, title):
    labels = list(categories.keys())
    values = list(categories.values())

    fig, ax = plt.subplots(figsize=(6, 4))
    ax.barh(labels, values, color='skyblue')
    ax.set_xlabel("Amount ($)")
    ax.set_title(title)
    st.pyplot(fig)

# Main Content
st.title("📊 Financial Dashboard")
st.markdown("---")

# Balance Section
style_section_title("Balance (All Linked Accounts)")
st.metric(label="Current Balance", value=balance)
style_metric_cards()

# Budget Section
style_section_title("My Monthly Spending Analysis")
col1, col2 = st.columns(2)

with col1:
    style_subheader("Germany Budget")
    st.metric(label="Total Budget", value=budget_data["Germany Budget"]["Total"], delta=f"Spent: {budget_data['Germany Budget']['Spent']}")
    st.write("**Category Breakdown:**")
    create_bar_chart(budget_data["Germany Budget"]["Categories"], "Germany Budget Categories")

with col2:
    style_subheader("US Budget")
    st.metric(label="Total Budget", value=budget_data["US Budget"]["Total"], delta=f"Spent: {budget_data['US Budget']['Spent']}")
    st.write("**Category Breakdown:**")
    create_bar_chart(budget_data["US Budget"]["Categories"], "US Budget Categories")

# AI Financial Insights
st.markdown("---")
style_section_title("AI Financial Analyst Insights")
st.info(ai_insight)

# Bills Section
style_section_title("My Bills")
try:
    total_due = sum(bill['Amount'] for bill in bills)
    st.metric(label="Total Due in Next 7 Days", value=f"${total_due:.2f}")
    st.success("Bill data processed successfully!")
except (ValueError, KeyError) as e:
    st.error(f"Error calculating total due. Details: {e}")

for bill in bills:
    st.markdown(f"- **{bill['Name']}:** ${bill['Amount']:.2f} (Due: {bill['Due Date']})")

# Credit Card Section
style_section_title("My Credit Cards")
st.metric(label="Total Credit Card Debt", value=credit_cards["Total Credit Card Debt"])
st.write(credit_cards["Recommendation"])

# Investments Section
style_section_title("My Investments")
st.metric(label="Total Investments", value=investments["Total Investments"])
st.write("**Breakdown:**")
for account, value in investments["Breakdown"].items():
    st.markdown(f"- **{account}:** {value}")

# LLM Prompt Query Box
style_section_title("Ask Your Financial AI Assistant")
user_query = st.text_input("Type your question about cross-border spending or budgeting below:")
if user_query:
    st.write(f"**Your Question:** {user_query}")
    with st.spinner("Processing your query..."):
        # Simulated AI response
        st.info("AI Insight: Based on your budgets, focus on reducing utility expenses in Germany to save $50 monthly.")
else:
    st.write("Awaiting your question. Get tailored insights about your finances!")

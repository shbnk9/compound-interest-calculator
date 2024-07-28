import streamlit as st
import pandas as pd

def calculate_compound_interest(budget, interest, period):
    monthly_data = []
    current_balance = budget

    for month in range(1, period + 1):
        interest_earned = current_balance * interest / 100
        current_balance += interest_earned
        monthly_data.append((month, round(current_balance, 2), round(interest_earned, 2)))

    return monthly_data

st.title("Compound Interest Calculator")

budget = st.number_input("Enter the initial principal amount:", min_value=0.0, step=0.01, format="%.2f")
interest = st.number_input("Enter the monthly interest rate (as a percentage):", min_value=0.0, step=0.01, format="%.2f")
period = st.number_input("Enter the period of time in months:", min_value=1, step=1)

if st.button("Calculate"):
    if budget > 0 and interest > 0 and period > 0:
        monthly_data = calculate_compound_interest(budget, interest, period)
        total_interest = monthly_data[-1][1] - budget

        st.subheader("Month-by-Month Balance")

        # Create a dataframe from the monthly data
        df = pd.DataFrame(monthly_data, columns=['Month', 'Balance', 'Interest Earned'])
        st.dataframe(df)

        st.write(f"**Total Interest Earned: ${total_interest:.2f}**")
    else:
        st.write("Please enter positive values for principal, interest rate, and period.")

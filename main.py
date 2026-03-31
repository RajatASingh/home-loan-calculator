import streamlit as st
from loan_calculator import  loan_simulator
import plotly.graph_objects as go


# Set page config for wide layout
st.set_page_config(layout="wide", page_title="Home Loan Analyzer")

st.title("🏠 Home Loan Prepayment Analyzer")

# First row - 3 columns
col1, col2, col3 = st.columns(3)
with col1:
    loan_amount = st.number_input("Loan Amount", value=1800000, step=100000)
with col2:
    interest_rate = st.number_input("Interest Rate (%)", value=11.0, step=0.05)
with col3:
    emi = st.number_input("EMI", value=20000, step=1000)

# Second row - 3 columns
col4, col5, col6 = st.columns(3)
with col4:
    extra_payment = st.number_input("Extra Payment", value=20000, step=1000)
with col5:
    strategy = st.selectbox("Extra Payment Strategy", ["monthly", "quarterly", "alternate"])

# Third row - Button
col_spacer1, col_spacer2, col_button = st.columns([2.5, 2.5, 0.5])
with col_button:
    calculate_btn = st.button("Calculate", key="calculate_btn")

# Run simulation
if calculate_btn:
    st.divider()
    df_extra = loan_simulator(
        loan_amount, interest_rate, emi, extra_payment, strategy
    )

    df_base = loan_simulator(
        loan_amount, interest_rate, emi, 0, "monthly"
    )

    # Calculate summary statistics
    months_saved = len(df_base) - len(df_extra)
    interest_base = df_base["Interest"].sum()
    interest_extra = df_extra["Interest"].sum()
    interest_saved = interest_base - interest_extra
    total_paid_base = df_base["Total Payment"].sum()
    total_paid_extra = df_extra["Total Payment"].sum()
    savings_percentage = (interest_saved / interest_base) * 100 if interest_base > 0 else 0

    # Display summary metrics
    st.subheader("📈 Summary Statistics")
    
    # Row 1: Actual Interest Values
    interest_col1, interest_col2, interest_col3, interest_col4 = st.columns(4)
    
    with interest_col1:
        st.metric("Actual Interest (Normal)", f"₹{interest_base:,.2f}")
    with interest_col2:
        st.metric("Actual Interest (Extra Payment)", f"₹{interest_extra:,.2f}")
    with interest_col3:
        st.metric("Actual Interest Saved", f"₹{interest_saved:,.2f}", delta=f"✓ {savings_percentage:.1f}%")
    with interest_col4:
        st.metric("Months Saved", f"{months_saved} months")
    
    # Row 2: Amount Paid Values
    paid_col1, paid_col2, paid_col3, paid_col4 = st.columns(4)
    
    with paid_col1:
        st.metric("Actual Amount Paid (Normal)", f"₹{total_paid_base:,.2f}")
    with paid_col2:
        st.metric("Actual Amount Paid (Extra)", f"₹{total_paid_extra:,.2f}")
    with paid_col3:
        amount_diff = total_paid_base - total_paid_extra
        st.metric("Amount Difference", f"₹{amount_diff:,.2f}", delta="Paid more" if amount_diff < 0 else "Saved")
    with paid_col4:
        st.metric("Time to Clear", f"{len(df_extra)} months", delta=f"vs {len(df_base)} months")

    # Create tabs for results
    tab_graph, tab_table = st.tabs(["📊 Graphs", "📋 Table"])

    with tab_graph:
        st.subheader("Loan Balance Comparison")
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=df_base["Month"],
            y=df_base["Closing Balance"],
            mode='lines',
            name='Normal EMI',
            line=dict(width=2)
        ))
        
        fig.add_trace(go.Scatter(
            x=df_extra["Month"],
            y=df_extra["Closing Balance"],
            mode='lines',
            name='With Extra Payment',
            line=dict(width=2)
        ))
        
        fig.update_layout(
            title='Impact of Extra Payments on Loan Balance',
            xaxis_title='Month',
            yaxis_title='Balance (₹)',
            hovermode='x unified',
            template='plotly_white',
            height=500
        )
        
        st.plotly_chart(fig, use_container_width=True)

    with tab_table:
        st.subheader("Detailed Schedule (With Extra Payment)")
        st.dataframe(df_extra, use_container_width=True)
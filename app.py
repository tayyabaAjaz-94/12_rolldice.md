import streamlit as st
from db import initialize_database, log_roll, fetch_roll_history
from utils import roll_dice

# App configuration
st.set_page_config(page_title="🎲 Dice Roller", layout="centered")

# Initialize DB
initialize_database()

# Title and description
st.title("🎲 Professional Dice Roller")
st.markdown("""
Welcome to the **Dice Roller App**! Click the button to simulate a roll of two six-sided dice.
Each roll is saved to a database and displayed in the history below.
""")

# Main interaction
if st.button("🎲 Roll Dice", use_container_width=True):
    die1, die2, total = roll_dice()
    log_roll(die1, die2, total)
    st.success(f"You rolled a {die1} and a {die2}!")
    st.metric(label="🎯 Total", value=total)

# Divider
st.markdown("---")

# Roll history
st.subheader("📊 Recent Rolls")
rows = fetch_roll_history(limit=10)

if rows:
    st.table([
        {"Die 1": d1, "Die 2": d2, "Total": total, "Time": timestamp}
        for d1, d2, total, timestamp in rows
    ])
else:
    st.info("No rolls recorded yet.")

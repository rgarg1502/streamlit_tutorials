import streamlit as st

st.title("🍕 Restaurant Order Form")

# Create the order form
with st.form("order_form"):
    st.header("What would you like to order?")

    # Food items
    pizza = st.selectbox(
        "Pizza type", ["Margherita", "Pepperoni", "Vegetarian"])
    quantity = st.slider("Quantity", 1, 5, 1)

    # Extras
    extra_cheese = st.checkbox("Extra cheese (+$2)")
    extra_topping = st.checkbox("Extra topping (+$1.50)")

    # Special instructions
    instructions = st.text_area("Special instructions (optional)")

    # Calculate price
    base_price = {"Margherita": 12, "Pepperoni": 14, "Vegetarian": 13}[pizza]
    total = base_price * quantity
    if extra_cheese:
        total += 2
    if extra_topping:
        total += 1.50

    st.info(f"Current total: ${total:.2f}")

    # Submit button
    order_placed = st.form_submit_button("Place Order")

# After submission
if order_placed:
    st.balloons()
    st.success("🎉 Order placed successfully!")
    st.write(f"**Order summary:** {quantity}x {pizza}")
    if extra_cheese or extra_topping:
        st.write("**Extras:**")
        extras = []
        if extra_cheese:
            extras.append("Extra cheese")
        if extra_topping:
            extras.append("Extra topping")
        st.write(", ".join(extras))
    if instructions:
        st.write(f"**Instructions:** {instructions}")
    st.write(f"**Total paid:** ${total:.2f}")

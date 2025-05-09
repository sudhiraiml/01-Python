import streamlit as st
import random
import string

def generate_password(length):
    if length < 8 or length > 12:
        return "Password length must be between 8 and 12"
    
    # Define character sets
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = '@#$'
    
    # Ensure at least one character from each set
    password = [
        random.choice(upper),
        random.choice(lower),
        random.choice(digits),
        random.choice(special)
    ]
    
    # Fill the remaining length
    remaining_length = length - 4
    all_chars = upper + lower + digits + special
    password += [random.choice(all_chars) for _ in range(remaining_length)]
    
    # Shuffle the password list to make it random
    random.shuffle(password)
    
    return ''.join(password)

# Streamlit UI
st.title("🔒 Secure Password Generator")

length = st.slider("Select Password Length (8-12)", min_value=8, max_value=12, value=10)

if st.button("Generate Password"):
    password = generate_password(length)
    st.text_input("Generated Password", value=password, key="password", type="password")
    st.code(password, language='text')
    st.success("Password generated! Copy it from above.")

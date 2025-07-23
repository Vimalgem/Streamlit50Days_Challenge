import streamlit as st

st.title("📝 User Feedback Survey Form")
st.subheader("We'd love to hear your thoughts!")

# Basic Info
name = st.text_input("👤 Your Name")
email = st.text_input("📧 Your Email")

# Experience rating
experience = st.slider("😊 How was your experience with our service?", 1, 10, 5)

# Feedback category
category = st.radio("🗂️ What do you want to give feedback on?", 
                    ["Website", "Customer Service", "Product Quality", "Others"])

# Features liked
features = st.multiselect("💡 What features did you like?", 
                          ["Speed", "Design", "User-Friendly", "Support", "Price"])

# Suggestions
suggestions = st.text_area("✍️ Any suggestions for improvement?")

# Consent
consent = st.checkbox("I agree to share my feedback for improvement purposes.")

# Submit Button
if st.button("Submit"):
    if name and email and consent:
        st.success(f"🎉 Thank you, {name}! Your feedback has been recorded.")
        st.write("📄 **Your Feedback Summary**")
        st.write(f"📧 Email: {email}")
        st.write(f"⭐ Experience Rating: {experience}/10")
        st.write(f"🗂️ Category: {category}")
        st.write(f"💡 Features Liked: {', '.join(features)}")
        st.write(f"✍️ Suggestions: {suggestions if suggestions else 'None'}")
    else:
        st.error("❗ Please fill out your name, email and give consent to submit.")


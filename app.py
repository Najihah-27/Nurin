import streamlit as st

st.set_page_config(page_title="Glaucoma Detection System", layout="centered")

st.title("👁️ Glaucoma Detection System")
st.markdown("---")

st.image("images/example_eye.jpg", use_column_width=True)

st.subheader("What is Glaucoma?")
st.write("""
Glaucoma is a group of eye conditions that damage the optic nerve, often caused by high eye pressure.
Early detection is key to preventing vision loss.
""")

st.markdown("""
### 🧪 System Features:
- CNN-based glaucoma detection from retinal images
- Displays prediction and model accuracy
""")

st.markdown("---")

if st.button("Start Diagnosis ➡️"):
    st.switch_page("pages/1_Diagnosis.py")


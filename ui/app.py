import streamlit as st
import requests
import plotly.graph_objects as go

# Set page configuration
st.set_page_config(page_title="Resume Screening App", page_icon="📄", layout="wide")

# Custom CSS for fonts
st.markdown("""
<style>
h1 {
    font-family: 'Arial', sans-serif;
    color: #2E86AB;
}
h2, h3 {
    font-family: 'Georgia', serif;
    color: #A23B72;
}
</style>
""", unsafe_allow_html=True)

# Sidebar for instructions
with st.sidebar:
    st.header("📋 Instructions")
    st.markdown("""
    **How to use this app:**
    1. Upload a resume in PDF format.
    2. Click "Process Resume" to analyze it.
    3. View the candidate status, feedback, and skill match percentage.

    **Note:** Ensure the API server is running on localhost:8000.
    """)

# Main content
st.title("📄 Resume Screening App")
st.markdown("Upload your resume and get instant feedback on candidate suitability!")

# Create two columns for layout
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("📤 Upload Resume")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", help="Select a resume in PDF format")

    if uploaded_file is not None:
        st.success(f"✅ File uploaded: {uploaded_file.name}")
        print("File uploaded successfully:", uploaded_file.name)

        if st.button("🚀 Process Resume", type="primary"):
            with st.spinner("Processing resume... Please wait."):
                response = requests.post(
                    "http://localhost:8000/screening/",
                    files={"resume": uploaded_file}
                )

            if response.status_code == 200:
                st.success("🎉 Resume processed successfully!")
                response_data = response.json()

                with col2:
                    st.subheader("📊 Results")
                    st.metric("Candidate Status", response_data.get("candidate_status", "N/A"))
                    st.write("**Feedback:**", response_data.get("reason", "No feedback available"))
                    skill_match = response_data.get('skill_match_percentage', 0)
                    st.metric("Skills Matched", f"{skill_match}%")

                    # Progress bar for skill match
                    st.progress(skill_match / 100)

                    # Pie chart for matched vs unmatched skills
                    fig = go.Figure(data=[go.Pie(
                        labels=['Matched Skills', 'Unmatched Skills'],
                        values=[skill_match, 100 - skill_match],
                        marker_colors=['#2E86AB', '#A23B72']
                    )])
                    fig.update_layout(title_text="Skill Match Breakdown")
                    st.plotly_chart(fig)

            else:
                st.error(f"❌ Error processing resume: {response.text}")
                print("Error processing resume:", response.text)

# Footer
st.markdown("---")




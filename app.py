import os

import streamlit as st

from main import run_pipeline


st.title("AI DDR Generator")

inspection = st.file_uploader("Upload Inspection Report")
thermal = st.file_uploader("Upload Thermal Report")

if st.button("Generate Report"):
    if inspection and thermal:
        os.makedirs("data", exist_ok=True)

        with open("data/inspection.pdf", "wb") as f:
            f.write(inspection.read())

        with open("data/thermal.pdf", "wb") as f:
            f.write(thermal.read())

        try:
            result = run_pipeline("data/inspection.pdf", "data/thermal.pdf")
        except Exception as exc:
            st.error(f"Report generation failed: {exc}")
        else:
            st.markdown(result)
            st.success("Report Generated!")
    else:
        st.error("Please upload both PDF files before generating the report.")

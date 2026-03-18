# =============================================================================
# User Comparison Tool - Antigravity Style (Updated)
# Compare Users + Allocation + Max Loss
# =============================================================================

import streamlit as st
import pandas as pd

# -------------------------------------------------------------------------
# Page Configuration
# -------------------------------------------------------------------------
st.set_page_config(
    page_title="User Comparison Tool",
    layout="wide"
)

st.title("Antigravity - User Comparison Tool")
st.markdown(
    "Compare **All User Details** vs **Running Users**.\n\n"
    "Now includes comparison of **Allocation** and **Max Loss**.\n\n"
    "Filters Applied:\n"
    "- Remove `DLR ACC`\n"
    "- Remove `algo = 0`\n"
    "- Remove non-running servers"
)

# -------------------------------------------------------------------------
# File Upload
# -------------------------------------------------------------------------
col1, col2 = st.columns(2)

with col1:
    file1 = st.file_uploader("Upload All User Details File", type=["xlsx", "csv"])

with col2:
    file2 = st.file_uploader("Upload Running Users File", type=["xlsx", "csv"])

# -------------------------------------------------------------------------
# File Loader
# -------------------------------------------------------------------------
def load_file(file):
    if file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    else:
        return pd.read_csv(file)

# -------------------------------------------------------------------------
# Processing
# -------------------------------------------------------------------------
if file1 and file2:

    if st.button("Start Comparison"):

        df1 = load_file(file1)
        df2 = load_file(file2)

        st.success("Files uploaded successfully")

        # -------------------------------------------------------------
        # Step 1 : Remove Dealer Accounts ("DLR ACC")
        # -------------------------------------------------------------
        df1 = df1[~df1["server"].astype(str).str.contains("DLR ACC", case=False, na=False)]
        df2 = df2[~df2["server"].astype(str).str.contains("DLR ACC", case=False, na=False)]

        # -------------------------------------------------------------
        # Step 2 : Remove algo = 0
        # -------------------------------------------------------------
        df1 = df1[df1["algo"].fillna(0) != 0]
        df2 = df2[df2["algo"].fillna(0) != 0]

        # -------------------------------------------------------------
        # Step 3 : Remove non-running servers
        # -------------------------------------------------------------
        df1 = df1[~df1["server"].astype(str).str.contains("non", case=False, na=False)]
        df2 = df2[~df2["server"].astype(str).str.contains("non", case=False, na=False)]

        # -------------------------------------------------------------
        # Required Columns
        # -------------------------------------------------------------
        required_cols = ["userId", "server", "algo", "allocation", "max_loss"]

        df1 = df1[[col for col in required_cols if col in df1.columns]]
        df2 = df2[[col for col in required_cols if col in df2.columns]]

        # -------------------------------------------------------------
        # User Comparison
        # -------------------------------------------------------------
        users1 = set(df1["userId"])
        users2 = set(df2["userId"])

        unmatched_sheet1 = df1[df1["userId"].isin(users1 - users2)]
        unmatched_sheet2 = df2[df2["userId"].isin(users2 - users1)]

        # -------------------------------------------------------------
        # Merge for Value Comparison
        # -------------------------------------------------------------
        merged = pd.merge(df1, df2, on="userId", suffixes=("_sheet1", "_sheet2"))

        # Find mismatches
        mismatch = merged[
            (merged["allocation_sheet1"] != merged["allocation_sheet2"]) |
            (merged["max_loss_sheet1"] != merged["max_loss_sheet2"])
        ]

        # -------------------------------------------------------------
        # Metrics
        # -------------------------------------------------------------
        m1, m2, m3, m4 = st.columns(4)

        m1.metric("Sheet1 Active Users", len(df1))
        m2.metric("Sheet2 Running Users", len(df2))
        m3.metric("Unmatched Users", len(unmatched_sheet1) + len(unmatched_sheet2))
        m4.metric("Allocation/Max Loss Mismatch", len(mismatch))

        st.divider()

        # -------------------------------------------------------------
        # Display Results
        # -------------------------------------------------------------
        st.subheader("Users in All Users File but NOT Running")
        st.dataframe(unmatched_sheet1, use_container_width=True)

        st.subheader("Users Running but NOT in Master File")
        st.dataframe(unmatched_sheet2, use_container_width=True)

        st.subheader("Allocation / Max Loss Mismatch")
        st.dataframe(mismatch, use_container_width=True)

        # -------------------------------------------------------------
        # Export
        # -------------------------------------------------------------
        result = pd.concat([
            unmatched_sheet1.assign(Status="Missing in Running File"),
            unmatched_sheet2.assign(Status="Missing in Master File"),
            mismatch.assign(Status="Value Mismatch")
        ])

        csv = result.to_csv(index=False)

        st.download_button(
            label="Download Full Comparison Report",
            data=csv,
            file_name="comparison_report.csv",
            mime="text/csv"
        )

# -------------------------------------------------------------------------
# Footer
# -------------------------------------------------------------------------
st.markdown("---")
st.caption("Antigravity Monitoring Utility")
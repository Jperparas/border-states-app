import streamlit as st
from services.big_query_service import BigQueryService
from datasets.valid_states import VALID_STATES

bq = BigQueryService(
    project_id=st.secrets["GCP_PROJECT_ID"],
    api_key=st.secrets["GOOGLE_API_KEY"]
        )
state = st.selectbox("Select a state", sorted([s.title() for s in VALID_STATES]))
if st.button("Search"):
    try:
        bq.query_border_states(state)
        
        if bq.df is not None and not bq.df.empty:
            st.subheader(f"States bordering {state.title()}")
            for s in bq.df["neighbors_state"]:
                st.write(s)
        else:
            st.info("No bordering states")
    
    except ValueError as e:
        st.error(str(e))

# === Directory Structure ===
# ai_log_monitoring_app/
# ├── main.py                  # Streamlit entrypoint
# ├── log_processor.py         # Splits logs based on patterns
# ├── vector_store.py          # Embedding + Chroma setup
# ├── rag_chain.py             # RAG chain setup
# └── application_logs.txt     # Sample log file



# === main.py ===
import streamlit as st
from rag_chain import get_qa_chain

# Initialize the RAG QA chain
qa_chain = get_qa_chain()

# Set up the Streamlit page
st.set_page_config(page_title="Log Monitor", layout="wide")
st.title("Log Monitoring Assistant")

# Create the query input area
query = st.text_area("Ask a log question...", height=150)

# Create the submit button
if st.button("Ask"):
    if query:
        # Display a spinner while processing
        with st.spinner("Processing your query..."):
            # Get answer from the RAG chain using invoke instead of run
            answer = qa_chain.invoke(query)
            
        # Display results
        st.subheader("Question:")
        st.write(query)
        st.subheader("Answer:")
        st.write(answer)

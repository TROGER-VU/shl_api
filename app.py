# import streamlit as st
# import pandas as pd
# import numpy as np
# from sentence_transformers import SentenceTransformer
# from supabase import create_client
# # import os
# # from dotenv import load_dotenv

# # # ✅ Load environment variables
# # load_dotenv()

# # ✅ Load model
# model = SentenceTransformer("./models/all-MiniLM-L6-v2")

# # ✅ Embed function
# def embed(text):
#     embedding = model.encode(text)
#     return embedding.tolist()  # Supabase expects a list, not a NumPy array

# # ✅ Initialize Supabase client
# SUPABASE_URL = st.secrets["SUPABASE_URL"]
# SUPABASE_SERVICE_KEY = st.secrets["SUPABASE_SERVICE_KEY"]

# supabase = create_client(SUPABASE_URL, SUPABASE_SERVICE_KEY)

# # ✅ Querying function
# def query_recommendations(user_query, threshold=0.4, top_k=10):
#     query_vector = embed(user_query)
#     response = supabase.rpc("match_products", {
#         "query_embedding": query_vector,
#         "match_threshold": threshold,
#         "match_count": top_k
#     }).execute()
#     return response.data

# # ✅ Streamlit app setup
# st.set_page_config(page_title="SHL RAG Assistant", page_icon="📘", layout="centered")

# # Title
# st.markdown("<h1 style='text-align: center;'>📘 SHL RAG Assistant</h1>", unsafe_allow_html=True)
# st.markdown("<p style='text-align: center; color: gray;'>Ask anything related to SHL assessments and get the best matched solutions</p>", unsafe_allow_html=True)

# # Query input
# query = st.text_input("🔍 Type your query here:", placeholder="e.g. I want a short remote cognitive test with adaptive scoring")

# # ✅ Format results nicely
# def format_results(results):
#     formatted = []
#     for res in results:
#         formatted.append({
#             "Assessment Name": res.get("name", "N/A"),
#             "URL": f"[🔗 Link]({res.get('url', '#')})",
#             "Remote": "✅" if res.get("remote_testing") else "❌",
#             "Adaptive/IRT": "✅" if res.get("adaptive_irt") else "❌",
#             "Test Type": res.get("test_types", "N/A"),
#             "Duration": res.get("duration", "N/A"),
#             "Similarity": f"{res.get('similarity', 0):.2f}"
#         })
#     return pd.DataFrame(formatted)

# # ✅ On query submission
# if query:
#     with st.spinner("🔎 Matching assessments..."):
#         try:
#             results = query_recommendations(query, threshold=0.4)
#             if results:
#                 st.success("✅ Top Matching Assessments")
#                 df = format_results(results)
#                 st.markdown(df.to_markdown(index=False), unsafe_allow_html=True)
#             else:
#                 st.warning("⚠️ No results found. Try changing your query.")
#         except Exception as e:
#             st.error(f"❌ Error: {e}")

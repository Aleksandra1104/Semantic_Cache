import streamlit as st

from insert_pgvector import insert_qa
from semantic_search_pgvector import search_similar
from cache_actions import increment_hit_count


st.set_page_config(
    page_title="Semantic Ticket Cache",
    page_icon="🧠",
    layout="wide"
)

st.title("Semantic Ticket Cache")

st.write(
    "Enter a customer or client issue. The system searches previously resolved cases "
    "and returns the top semantic matches."
)

client_question = st.text_area(
    "Customer / client issue",
    placeholder="Example: I can log into the portal, but document uploads fail with an unknown error."
)

if st.button("Search cache"):
    if not client_question.strip():
        st.warning("Please enter a customer or client issue first.")
    else:
        results = search_similar(client_question, limit=3)
        st.session_state["results"] = results
        st.session_state["client_question"] = client_question


if "results" in st.session_state:
    results = st.session_state["results"]

    st.subheader("Top cached matches")

    if not results:
        st.info("No cached answers found yet.")
    else:
        for idx, row in enumerate(results, start=1):
            row_id, question, answer, category, hit_count, similarity = row

            with st.container(border=True):
                st.markdown(f"### Match {idx}")
                st.write(f"**Similarity:** {similarity:.4f}")
                st.write(f"**Category:** {category}")
                st.write(f"**Previous issue:** {question}")
                st.write(f"**Suggested answer:** {answer}")
                st.write(f"**Cache hits:** {hit_count}")

                if st.button(f"Use this answer", key=f"use_{row_id}"):
                    increment_hit_count(row_id)
                    st.success("Response selected. Cache hit count updated.")
                    st.info(answer)


st.divider()

st.subheader("Add new response to cache")

st.write(
    "If none of the suggestions are useful, enter the final support response below."
    "The issue and response will be saved as a new semantic cache entry."
)

new_answer = st.text_area("Support response")
new_category = st.text_input("Category", placeholder="Example: IAM, Networking, Email, Endpoint")

if st.button("Save new Q/A pair"):
    question_to_save = st.session_state.get("client_question", client_question)

    if not question_to_save.strip():
        st.warning("Please enter the customer or client issue first.")
    elif not new_answer.strip():
        st.warning("Please enter a support response.")
    elif not new_category.strip():
        st.warning("Please enter a category.")
    else:
        insert_qa(
            question=question_to_save,
            answer=new_answer,
            category=new_category
        )
        st.success("New Q/A pair saved to semantic cache.")
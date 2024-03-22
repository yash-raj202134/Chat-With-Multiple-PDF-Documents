import utils as ut
import streamlit as st


def main():
    st.set_page_config("Chat PDF")
    st.header("Chat with PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        ut.user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = ut.get_pdf_text(pdf_docs)
                text_chunks = ut.get_text_chunks(raw_text)
                ut.get_vector_store(text_chunks)
                st.success("Done")


if __name__ == "__main__":
    main()
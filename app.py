import streamlit as st
import requests

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF AI Assistant")

st.write(
    "Upload a PDF file and let the AI agent analyze and summarize it."
)

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"Selected file: {uploaded_file.name}")

    # =========================
    # ANALYZE PDF
    # =========================

    if st.button("Analyze PDF"):

        webhook_url = "https://essa2030.app.n8n.cloud/webhook/pdf-q"

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        with st.spinner("Analyzing PDF..."):

            try:

                response = requests.post(
                    webhook_url,
                    files=files,
                    timeout=90
                )

                if response.status_code == 200:

                    try:
                        result = response.json()

                        st.success(
                            "Analysis completed successfully."
                        )

                        st.divider()
                        st.subheader("📄 PDF Analysis")

                        if isinstance(result, dict):

                            answer = (
                                result.get("answer")
                                or result.get("output")
                                or result.get("text")
                            )

                            if answer:
                                st.write(answer)
                            else:
                                st.write(result)

                        else:
                            st.write(result)

                    except Exception:

                        st.success(
                            "Analysis completed successfully."
                        )

                        st.divider()
                        st.subheader("📄 PDF Analysis")
                        st.write(response.text)

                else:

                    st.error(
                        f"Request failed with status code: "
                        f"{response.status_code}"
                    )

                    st.write(response.text)

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )

            except Exception as e:

                st.error("Something went wrong.")
                st.write(e)


st.divider()

# =========================
# ASK ABOUT PDF
# =========================

st.subheader("💬 Ask about this PDF")

question = st.text_input(
    "Enter your question"
)

if st.button("Ask AI"):

    if uploaded_file is None:

        st.warning("Please upload a PDF first.")

    elif not question.strip():

        st.warning("Please enter a question.")

    else:

        question_webhook_url = (
            "https://essa2030.app.n8n.cloud/webhook/pdf-q"
        )

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        data = {
            "question": question
        }

        with st.spinner("Searching the PDF..."):

            try:

                response = requests.post(
                    question_webhook_url,
                    files=files,
                    data=data,
                    timeout=90
                )

                if response.status_code == 200:

                    try:
                        result = response.json()

                        st.success("Answer received.")
                        st.subheader("🤖 Answer")

                        if isinstance(result, dict):

                            answer = (
                                result.get("answer")
                                or result.get("output")
                                or result.get("text")
                            )

                            if answer:
                                st.write(answer)
                            else:
                                st.write(result)

                        else:
                            st.write(result)

                    except Exception:

                        st.success("Answer received.")
                        st.subheader("🤖 Answer")
                        st.write(response.text)

                else:

                    st.error(
                        f"Request failed with status code: "
                        f"{response.status_code}"
                    )

                    st.write(response.text)

            except requests.exceptions.Timeout:

                st.error(
                    "The request took too long. "
                    "Please try again."
                )

            except Exception as e:

                st.error("Something went wrong.")
                st.write(e)

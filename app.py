import streamlit as st
import requests

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF AI Assistant")

st.write(
    "Upload a PDF file and let the AI agent analyze, "
    "summarize, and answer questions about it."
)

# =========================
# UPLOAD PDF
# =========================

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

WEBHOOK_URL = "https://essa2030.app.n8n.cloud/webhook/pdf-q"


# =========================
# ANALYZE PDF
# =========================

if uploaded_file is not None:

    st.success(f"Selected file: {uploaded_file.name}")

    if st.button("Analyze PDF"):

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
                    WEBHOOK_URL,
                    files=files,
                    timeout=90
                )

                if response.status_code == 200:

                    st.success(
                        "Analysis completed successfully."
                    )

                    st.divider()
                    st.subheader("📄 PDF Analysis")

                    try:

                        result = response.json()

                        # Structured Output returned by n8n
                        if isinstance(result, dict):

                            # Main analysis
                            if "state" in result:

                                st.markdown(
                                    str(result["state"])
                                )

                            # Key points
                            if "cities" in result:

                                points = result["cities"]

                                if points:

                                    st.subheader(
                                        "🔑 Key Points"
                                    )

                                    for i, point in enumerate(
                                        points,
                                        start=1
                                    ):
                                        st.write(
                                            f"{i}. {point}"
                                        )

                            # Standard answer/output/text
                            elif "answer" in result:

                                answer = result["answer"]

                                if isinstance(answer, dict):

                                    if "state" in answer:
                                        st.markdown(
                                            str(
                                                answer["state"]
                                            )
                                        )

                                    if "cities" in answer:

                                        st.subheader(
                                            "🔑 Key Points"
                                        )

                                        for i, point in enumerate(
                                            answer["cities"],
                                            start=1
                                        ):
                                            st.write(
                                                f"{i}. {point}"
                                            )

                                else:
                                    st.markdown(
                                        str(answer)
                                    )

                            elif "output" in result:
                                st.markdown(
                                    str(result["output"])
                                )

                            elif "text" in result:
                                st.markdown(
                                    str(result["text"])
                                )

                            elif (
                                "state" not in result
                                and "cities" not in result
                            ):
                                st.write(result)

                        else:
                            st.write(result)

                    except Exception:
                        st.markdown(response.text)

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


# =========================
# ASK ABOUT PDF
# =========================

st.divider()

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
                    WEBHOOK_URL,
                    files=files,
                    data=data,
                    timeout=90
                )

                if response.status_code == 200:

                    st.success("Answer received.")

                    st.subheader("🤖 Answer")

                    try:

                        result = response.json()

                        if isinstance(result, dict):

                            # Current Structured Output
                            if "state" in result:
                                st.markdown(
                                    str(result["state"])
                                )

                            elif "answer" in result:

                                answer = result["answer"]

                                if isinstance(answer, dict):

                                    if "state" in answer:
                                        st.markdown(
                                            str(
                                                answer["state"]
                                            )
                                        )
                                    else:
                                        st.write(answer)

                                else:
                                    st.markdown(
                                        str(answer)
                                    )

                            elif "output" in result:
                                st.markdown(
                                    str(result["output"])
                                )

                            elif "text" in result:
                                st.markdown(
                                    str(result["text"])
                                )

                            else:
                                st.write(result)

                        else:
                            st.write(result)

                    except Exception:

                        st.markdown(response.text)

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

Essa
essa_92
Online
﻿
Shahad — 9/3/26, 5:39 PM
Attachment file type: unknown
AI_Agent_Day5_Shahad.ipynb
211.45 KB
mashael — 9:30 AM
Attachment file type: unknown
AI_Agent_Day5__mashael (1).ipynb
209.63 KB
Shahad — 10:27 AM
Shahad-Government Contract Intelligence Agent
Noof — 10:37 AM

Noof — 11:38 AM
You are an environmental report assistant.

Use the knowledge base tool to answer questions about the environmental report.

Answer only from the retrieved information.

If the answer is not found in the report, say:
"The information was not found in the report."

Do not invent information.
Noof — 11:47 AM
{
  "status": "success",
  "message": "PDF Agent webhook is working"
}
Noof — 12:29 PM
import streamlit as st
import requests

st.title("PDF AI Assistant")

uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success(f"File selected: {uploaded_file.name}")

    if st.button("Send PDF to n8n"):

        webhook_url = "PUT_YOUR_N8N_TEST_WEBHOOK_URL_HERE"

        files = {
            "file": (
                uploaded_file.name,
                uploaded_file.getvalue(),
                "application/pdf"
            )
        }

        response = requests.post(
            webhook_url,
            files=files
        )

        st.write("Status Code:", response.status_code)

        st.write("Response from n8n:")

        try:
            st.json(response.json())
        except:
            st.write(response.text)
Noof — 1:03 PM
={{ 
  {
    "status": "success",
    "text": $json.text
  }
}}
SaraXZ — 1:05 PM
{{ {
  "status": "success",
  "text": $json.text
} }}
Noof — 1:09 PM
You are a PDF analysis assistant.

Read the following PDF content and analyze it.

Return:
Document title
A short summary
Main topic
Five key points

Answer only using the PDF content.

PDF Content:

{{ $json.text }}
SaraXZ — 1:18 PM
Attachment file type: document
schema.rtf
774 bytes
Azizfahad — 1:24 PM
{ "type": "object", "properties": { "title": { "type": "string" }, "summary": { "type": "string" }, "main_topic": { "type": "string" }, "key_points": { "type": "array", "items": { "type": "string" } } }, "required": [ "title", "summary", "main_topic", "key_points" ] }
schna.txt
1 KB
SaraXZ — 1:33 PM
{{
  {
    status: "success",
    title: $json.output.title,
    summary: $json.output.summary,
    main_topic: $json.output.main_topic,
    key_points: $json.output.key_points
  }
}}

2.txt
1 KB
Noof — 1:35 PM
import streamlit as st
import requests

st.set_page_config(
    page_title="PDF AI Assistant",
    page_icon="📄",

app.py
2 KB
﻿
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

    if st.button("Analyze PDF"):

        webhook_url = https://essa2030.app.n8n.cloud/webhook-test/PDF-AGENT"

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
                    files=files
                )

                if response.status_code == 200:

                    result = response.json()

                    st.success("Analysis completed successfully.")

                    st.divider()

                    st.subheader("📌 Document Title")
                    st.write(result["title"])

                    st.subheader("📝 Summary")
                    st.write(result["summary"])

                    st.subheader("🎯 Main Topic")
                    st.write(result["main_topic"])

                    st.subheader("🔑 Key Points")

                    for i, point in enumerate(
                        result["key_points"],
                        start=1
                    ):
                        st.write(f"{i}. {point}")

                else:

                    st.error(
                        f"Request failed with status code: "
                        f"{response.status_code}"
                    )

                    st.write(response.text)

            except Exception as e:

                st.error("Something went wrong.")

                st.write(e)
app.py
2 KB

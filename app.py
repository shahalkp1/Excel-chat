import pandas as pd
import streamlit as st
from pandasai import SmartDatalake
from pandasai.llm import BambooLLM


if __name__ == "__main__":
    st.set_page_config(
        layout="wide",
        page_icon="./logo.svg",
        page_title="Chat with your Data!!!",
    )
    st.title("Chat with your Data!!!")
    
    with st.container():
        llm = BambooLLM(api_key=st.secrets["PANDASAI_API_KEY"])
        input_files = st.file_uploader(
            "Upload files", type=["xlsx", "csv"], accept_multiple_files=True
        )

        if len(input_files) > 0:
            data_list = []
            for input_file in input_files:
                if input_file.name.lower().endswith(".csv"):
                    data = pd.read_csv(input_file)
                else:
                    data = pd.read_excel(input_file)
                st.dataframe(data, use_container_width=True)
                data_list.append(data)
                df = SmartDatalake(
                    dfs=data_list,
                    config={
                        "llm": llm,
                        "verbose": True,
                    },
                )
            st.header("Ask anything!")
            input_text = st.text_area(
                "Enter your question"
            )
            if input_text is not None:
                if st.button("Query"):
                    result = df.chat(input_text)

                    col1, col2 = st.columns(2)

                    with col1:
                        st.header("Answer")
                        st.write(result)

                    with col2:
                        st.header("The corresponding code")
                        st.code(df.last_code_executed, language="python", line_numbers=True)
        else:
            st.header("No Files Uploaded")
            st.warning("Please upload Excel or CSV files to proceed.")
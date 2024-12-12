import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.JPG")

with col2:
    st.title("Bennie Sowah Jr")
    content = """
    Hi, I am Bennie! I am a Devops/Cloud Engineer and a Python developer. Results-driven Cloud Engineer with hands-on experience in Cloud Architecting, DevOps, SRE, Cloud Security, and Cloud Networking. 
    Proven track record of optimizing and automating mission critical cloud workloads, leading to significant cost savings and streamlined processes. 
    Proficient in configuring and leveraging tools such as AWS, Kubernetes, and Terraform to deliver efficient solutions. Adept at developing robust CI/CD pipelines that have reduced deployment times by up to 60% and improved overall release quality.
    Collaborative team player, fostering cooperation between software development, operations, and testing teams. Strong problem-solving skills and effective communicator, ensuring seamless cross-functional collaboration. Committed to staying current with industry trends and continuously enhancing skills through ongoing professional development.
    """
    st.info(content)

content2 = """
Below you can find some of the apps I have built in Python. Feel free to contact me!
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

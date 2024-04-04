import streamlit as st

# Set the page configuration
st.set_page_config(
    page_title="Amazon Product Database",
    page_icon=":shopping_cart:",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Set the background color
page_bg_color = """
<style>
body {
    background-color: #f0f0f0;
}
</style>
"""
st.markdown(page_bg_color, unsafe_allow_html=True)

# Title and subtitle
st.write("""
<div style='text-align: center; background-color: #e6e6e6; padding: 20px; border-radius: 10px;'>
    <h1 style='color: #333333;'>Amazon Product Database</h1>
    <p style='color: #666666;'>User interface for searching and managing products</p>
</div>
""", unsafe_allow_html=True)

# Search button
search_button = st.button("Search", use_container_width=True, help="Click to search for products")

# Custom CSS for the button
button_css = """
<style>
div.stButton > button:first-child {
    background-color: #ff9900;
    color: white;
    font-weight: bold;
    border-radius: 5px;
    padding: 10px 20px;
}
div.stButton > button:first-child:hover {
    background-color: #e68a00;
}
</style>
"""
st.markdown(button_css, unsafe_allow_html=True)

# Handle button click event
if search_button:
    st.write("You clicked the Search button!")

# st.write("""
#          #Simple App
#          User interface of Amazon product database
#          """)
# search_button = st.button("Search")
    
#     # Handle button click event
# if search_button:
#     st.write("You clicked the Search button!")
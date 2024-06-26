import streamlit as st
from pymongo import MongoClient


client = MongoClient(host="localhost", port=27017)

client = MongoClient('mongodb://localhost:27017/')

# collection name list
db_list = ['db_1', 'db_2', 'db_3']

# db1 = client['db_1']
# db2 = client['db_2']
# db3 = client['db_3']
# collection1 = db1['collection']
# collection2 = db2['collection']
# collection3 = db3['collection']

# Create a new database and collection
db_backup = client['db_backup']

# Create a new collection
collection_backup = db_backup['collection_backup']
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

search_input = st.text_input("Enter products information:")
search_button = st.button("Search", use_container_width=True, help="Click to search for products")
search_id = st.text_input("Enter products unique id:")
search_id_button = st.button("Search ID", use_container_width=True, help="Click to search for products id")
search_price = st.text_input("Enter products price:")
search_price_button = st.button("Search Price", use_container_width=True, help="Click to search for products price")

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
    # for db_name in db_list:
    #     collection0 = globals()[db_name]['collection']
    results = collection_backup.find({
        "$or": [
            {"title": {"$regex": search_input, "$options": "i"}},
            {"brand": {"$regex": search_input, "$options": "i"}}
        ]
    })
    st.write(f"Search by Product Information")
    for result in results:
        st.write(result)

if search_id_button:
    # for db_name in db_list:
    #     collection1 = globals()[db_name]['collection']
    results = collection_backup.find({
            "_id": {"$regex": search_id, "$options": "i"}
    })
    st.write("Search by Product ID:")
    for result in results:
        st.write(result)

if search_price_button:
    search_price_modified = search_price.strip()
    search_price_with_dollar = "$" + search_price_modified
    # for db_name in db_list:
    #     collection2 = globals()[db_name]['collection']
    results = collection_backup.find(
        {"price": search_price_with_dollar}
    )
    st.write("Search By Prices:")
    for result in results:
        st.write(result)

# st.write("""
#          #Simple App
#          User interface of Amazon product database
#          """)
# search_button = st.button("Search")
    
#     # Handle button click event
# if search_button:
#     st.write("You clicked the Search button!")
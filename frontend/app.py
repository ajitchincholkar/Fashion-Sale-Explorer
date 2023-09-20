import streamlit as st
import pandas as pd


# Function to load product data from a CSV file
@st.cache_data  # This decorator caches the data for improved performance
def load_data(brand):
    # Define the CSV file path based on the selected brand
    if brand == "Zara":
        csv_name = 'zara_onsale.csv'
    elif brand == "Uniqlo":
        csv_name = 'uniqlo_onsale.csv'
    else:
        return None

    # Load and return the product data
    df = pd.read_csv(f"backend/data/processed/{csv_name}")
    return df


# Streamlit backend
st.title("Products On Sale")

# Add a selectbox for choosing the brand (Zara or Uniqlo)
selected_brand = st.selectbox("Select Brand", ["Select", "Zara", "Uniqlo"])

# Load the product data based on the selected brand
df = load_data(selected_brand)

# Define the number of columns for displaying products side by side
num_columns = 3  # You can adjust this value as needed

try:
    # Calculate the number of products per column
    products_per_column = len(df) // num_columns
except Exception as e:
    st.write(" ")

# Create a custom layout using HTML and CSS
html_layout = """<style>
.column {
    float: left;
    width: calc(100% / """ + str(num_columns) + """);
    padding: 10px;
}
</style>
<div class="row">"""

# Display products side by side in multiple columns
for i in range(num_columns):
    html_layout += """<div class="column">"""
    try:
        for _, row in df.iloc[i * products_per_column: (i + 1) * products_per_column].iterrows():
            # Wrap only the image in an anchor tag to make it the hyperlink (if "product_link" exists)
            if "product_link" in row:
                product_image_with_link = f'<a href="{row["product_link"]}" target="_blank"><img src="{row["img_url"]}" alt="{row["product_name"]}" width="300"></a>'
            else:
                product_image_with_link = f'<img src="{row["img_url"]}" alt="{row["product_name"]}" width="300">'

            html_layout += f"""{product_image_with_link}<br>
                        {row["product_name"]}<br>
                        Discount Price: <strong>{row['price']:.1f}</strong><br>
                        Normal Price: {row['og_price']:.1f}<br><br>"""
        html_layout += """</div>"""
    except Exception as e:
        st.write(" ")

html_layout += """</div>"""

# Display the custom layout
st.markdown(html_layout, unsafe_allow_html=True)

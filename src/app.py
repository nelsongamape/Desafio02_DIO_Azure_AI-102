import streamlit as st
from services.blob_service import uploading_blob
from services.credit_card_service import analyze_credit_card

def configure_interface():
    st.title("File Upload - DIO CHALLENGE AI102-02")
    uploaded_file = st.file_uploader("Choose your img file", type=['jpg', 'png', 'jpeg'])
    
    if uploaded_file is not None:
        fileName = uploaded_file.name
        #Envio para o Blob Azure
        blob_url = uploading_blob(file, file_name)
        if blob_url is not None:
            st.write(f"File {fileName} Successfully Uploaded")
            credit_card_info = analyze_credit_card(blob_url) #Azure AI Analysis
            show_image_and_validation(blob_url, credit_card_info)
        else:
            st.write(f"Uploading {fileName} Failure")

def show_image_and_validation(blob_url, credit_card_info):
    st.image(blob_url, caption="Uploaded Image", use_column_width=true)
    st.write("Credit Card Analysis Result:")
    if credit_card_info and credit_card_info("card_name"):
        st.markdown(f"<h1 style='color: green;'>Valid Card</h1", unsafe_allow_html=true)
        st.write(f"Cardholder Name: {credit_card_info['card_name']}")
        st.write(f"Issuer Bank: {credit_card_info['bank_name']}")
        st.write(f"Expiration Date: {credit_card_info['expiration_date']}")
    else:
        st.markdown(f"<h1 style='color: red;'>NOT a valid Card</h1", unsafe_allow_html=true)
        st.write(f"This is NOT a valid credit card image")
    

if __name__ == "__main__":
    configure_interface()
    

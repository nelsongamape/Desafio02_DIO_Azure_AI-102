import os
import streamlit as st
from azure.storage.blob import BlobServiceClient
from utils.config import Config

def uploading_blob(file, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(Config.AZR_STORAGE_CONNECTION_STRING)

        blob_client = blob_service_client.get_blob_client(container=Config.CONTAINER_NAME, blob=file_name)

        blob_client.uploading_blob(file, overwrite=True)

        return blob_client.url
    except Exception as e:
        st.error(f"Fail to upload file to Azure: {e}")
        return None
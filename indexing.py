from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import pandas as pd
import re
import json

# Define your Azure Cognitive Search settings
service_name = 'aianytime-search'
index_name = 'mydata-index'
admin_key = '***********'
endpoint = f"https://{service_name}.search.windows.net/"
credential = AzureKeyCredential(admin_key)

# Load your Excel data into a DataFrame
file_path = 'data/ticket_data.xlsx'
df = pd.read_excel(file_path)

# Initialize the Azure Cognitive Search client
search_client = SearchClient(endpoint=endpoint, index_name=index_name, credential=credential)

# Upload data to the Azure Cognitive Search index
data = []
for _, row in df.iterrows():  
    data.append({  
        "@search.action": "upload", 
        "TicketID": row['Ticket ID'], 
        "TicketType": row['Ticket Type'], 
        "TicketSubject": row['Ticket Subject'],
        "TicketDescription" : row['Ticket Description'],
        "TicketStatus": row ['Ticket Status'],
        "TicketPriority": row['Ticket Priority'],
        "TicketChannel": row['Ticket Channel']
    })  

result = search_client.upload_documents(data)  
print("Upload result:", result)
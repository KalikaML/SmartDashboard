### Dashboard
1. Kalika Sales Dashboard visualization using PowerBI

### RAG

#### Basic RAG Architecture
 ![rag_image](https://www.clarifai.com/hs-fs/hubfs/rag-query-drawio%20(1)-png-2.png?width=2056&height=1334&name=rag-query-drawio%20(1)-png-2.png)

## RAG Usecases

### Gmail RAG
    1. Extract the PO order and proforma invoice data as [starting point](https://medium.com/@masego_m/accessing-gmail-with-python-a-beginners-guide-812e0068a568)

    #### Problem Statement : Build RAG on Kalika Enterprises Gmail Data

    #### Tasks

    1) Understand the details of various documents
        i) Proforma Invoice:A proforma invoice is a preliminary bill that a seller sends to a buyer before a sale is confirmed. It's a non-binding document that's used for planning, budgeting, and estimates. It's also used for customs clearance and financing
        ii) PO Dump : Pending and Processed data details
    2) Create the Parsing process
        1) Proforma Invoice
        - Searching a with proforma invoice for smtp mail python utility download attached file
        - Dump that on scheduling daily to s3
        - Extract the content using ocr engine and validate
            try:
            1) [Python package](https://pypi.org/project/invoice2data/)
            2) [Medium article](https://medium.com/@cherylinpz/simplifying-invoice-processing-extracting-tables-with-python-part1-95437f404efb)

       2)  PO dump
       _ On Daily basis Dump is in mail extract excel store in s3
       - Implement pg vector

       ## TODO
           1) Create PG vector on local
           2) Upload po_dump excel in PG vector and create a vector
           3) Test with Ollama local model and create a streamlit app
           4) Test for last 10 days documents with query and response
           5) Generate the report and share it with in team group and github

      3) Deploy on Ec2 for further building POC

## Financial Assistant RAG : B2C

   ### Problem Statement : Uploading Bank statement, Trading Documents(Last trading transaction,orders session details)
   give query response bot.

   1) User can upload documents such as bank statement, trading sheets with Upload button- UI
   2) create PG vector to store
   3) Ollama testing with local model

   ###### Sample Datasets
   [Kaggle](https://www.kaggle.com/datasets/abutalhadmaniyar/bank-statements-dataset?resource=download)
   ###### Limitation : Data privacy
   Solution: Give a isolated space

   ###### Points of discussion
   1) Explore the techniques for giving data privacy to user



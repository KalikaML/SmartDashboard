"""
Problem Statement : Build RAG on Kalika Enterprises Gmail Data
Tasks
1) Understand the details of various documents
    i) Proforma Invoice:A proforma invoice is a preliminary bill that a seller sends to a buyer before a sale is confirmed. It's a non-binding document that's used for planning, budgeting, and estimates. It's also used for customs clearance and financing
    ii) PO Dump : Pending and Processed data details
2) Create the Parsing process
    1) Proforma Invoice
    - Searching a with proforma invoice for smtp mail python utility download attached file
    - Dump that on scheduling daily to s3
    - Extract the content using ocr engine and valdate
   2)  PO dump
   _ On Daily basis Dump is in mail extract excel store in s3
   - Implement pg vector
"""

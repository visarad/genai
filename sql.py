import pandas as pd
from sqlalchemy import create_engine

# MySQL credentials — update these
engine = create_engine('mysql+pymysql://root:deepu143@localhost/sample')

# Correct path to your Excel file
df = pd.read_excel('/Users/pararthivellanki/Documents/WorkBooks/Parameters_Sets_and_LODs.xlsx')

print("Columns found:", df.columns.tolist())
print("Rows found:", len(df))

# Convert date columns
date_cols = ['Claim Date', 'DB Update Date', 'Insurance Expiry Date', 'Product Production Date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], dayfirst=True, errors='coerce')

# Rename columns to match table
df.columns = [
    'claim_date', 'customer_id', 'customer_zip_code', 'db_update_date',
    'insurance_expiry_date', 'insurance_status', 'model_line', 'original_source',
    'product_production_date', 'status', 'sub_model_line', 'sub_status',
    'vendor_id', 'holding_fee', 'insurance_amount', 'storage_fee', 'total_acquisition_cost'
]

# Load into MySQL
df.to_sql('parameters_sets_lods', con=engine, if_exists='append', index=False)

print(f"✅ Loaded {len(df)} rows successfully!")
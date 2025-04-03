import pandas as pd
from app.db.database import SessionLocal
from app.db.models import PEP
import os

def load_peps_from_excel(file_path: str = "pep_list.xlsx"):
    db = SessionLocal()

    existing = db.query(PEP).count()
    if existing > 0:
        print("PEP data already loaded — skipping Excel import.")
        db.close()
        return

    if not os.path.exists(file_path):
        print("PEP list file not found.")
        db.close()
        return

    df = pd.read_excel(file_path, skiprows=2)
    
    df = df.dropna(subset=[df.columns[1], df.columns[2]])

    df["full_name"] = df[df.columns[2]].astype(str).str.strip() + " " + df[df.columns[1]].astype(str).str.strip()

    df["birth_date"] = pd.to_datetime(df[df.columns[4]], dayfirst=True, errors="coerce").dt.date
    df["added_date"] = pd.to_datetime(df[df.columns[5]], dayfirst=True, errors="coerce").dt.date

    skipped = 0
    for _, row in df.iterrows():
        if pd.isna(row["full_name"]) or pd.isna(row["birth_date"]) or pd.isna(row["added_date"]):
            skipped += 1
            continue

        db.add(PEP(
            name=str(row["full_name"]),
            birth_date=row["birth_date"],
            added_date=row["added_date"]
        ))

    db.commit()
    db.close()
    print(f"Loaded {len(df) - skipped} entries from {file_path}")
    print(f"Skipped {skipped} rows due to missing data")

import pandas as pd
from app.db.database import SessionLocal
from app.db.models import PEP
import os

def load_peps_from_excel(file_path: str = "pep_list.xlsx"):
    from app.db.models import PEP

    db = SessionLocal()

    existing = db.query(PEP).count()
    if existing > 0:
        print("PEP data already loaded — skipping Excel import.")
        db.close()
        return

    if not os.path.exists(file_path):
        print("PEP list file not found.")
        return

    df = pd.read_excel(file_path, skiprows=2)
    df = df.dropna(subset=[df.columns[1], df.columns[2]])
    df["full_name"] = df[df.columns[2]].astype(str).str.strip() + " " + df[df.columns[1]].astype(str).str.strip()
    names = df["full_name"].unique()

    for name in names:
        db.add(PEP(name=str(name)))
    db.commit()
    db.close()
    print(f"Loaded {len(names)} names from {file_path}")

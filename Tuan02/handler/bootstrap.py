from repo.postgres_db import PostgreDatabase
import logging
db = PostgreDatabase()

def get_data_profile(name: str):
    try:
        result = db.et_profile(name=name)
        return result
    except Exception as e:
        logging.getLogger().info(f"[ERROR] get data profile from database: {str(e)}")
        
    
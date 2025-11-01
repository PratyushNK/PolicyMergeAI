import os
from sqlalchemy import create_engine
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL, connect_args={"options":"-c timezone=utc"})

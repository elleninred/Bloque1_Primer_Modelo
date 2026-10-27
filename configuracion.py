import os
from sqlalchemy import create_engine
# variable de entorno url
url_bd = os.environ["DATABASE_URL"]
engine = create_engine(url_bd, echo=True)
"""Write values to a Postgres DB for a Dreamforce '16 demo.
"""

import os
import psycopg2
import random
import urlparse


# Postgres configuration. Will be used if we write back to Salesforce with Heroku Connect.
db_url = os.environ.get("DATABASE_URL")
if not db_url:
    exit()

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(db_url)
conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

num_records = random.randint(1, 5)

with conn, conn.cursor() as cursor:
    for _ in range(num_records):
        cursor.execute(
            """INSERT INTO salesforce.patient_goals__c(name)
               VALUES('DB Name');"""
        )

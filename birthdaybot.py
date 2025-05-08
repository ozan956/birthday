import pandas as pd
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
import os

EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("EMAIL_PASSWORD")

df = pd.read_csv("birthdays.csv")
today = datetime.now().strftime("%m-%d")

for _, row in df.iterrows():
    if datetime.strptime(row["birthday"], "%Y-%m-%d").strftime("%m-%d") == today:
        msg = MIMEText(f"Mutlu yıllar {row['name']}! 🎉")
        msg["Subject"] = "Doğum Günün Kutlu Olsun!"
        msg["From"] = EMAIL
        msg["To"] = row["email"]

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL, PASSWORD)
            server.send_message(msg)

        print(f"{row['name']} için doğum günü mesajı gönderildi.")

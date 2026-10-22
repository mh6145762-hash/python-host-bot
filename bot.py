import os
import sqlite3
import subprocess
from pyrogram import Client, filters

app = Client(
    "PythonHostBot",
    api_id=33209479,
    api_hash="6f8e19c9ac42a183bf85c0d1701e45f1",
    bot_token="8947198114:AAHy8b1tOPOXIeBOBEAdfA0Fx04KbDL0B0I",
)

UPLOAD_DIR = "hosted_scripts"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# استرجاع وتشغيل جميع السكربتات تلقائياً بمجرد اشتغال البوت
def restore_and_run_scripts():
  conn = sqlite3.connect("scripts.db")
  cursor = conn.cursor()
  cursor.execute("SELECT filename, code FROM scripts")
  rows = cursor.fetchall()
  conn.close()

  for filename, code in rows:
    file_path = os.path.join(UPLOAD_DIR, filename)
    # كتابة الكود محلياً
    with open(file_path, "w", encoding="utf-8") as f:
      f.write(code)

    # تشغيل السكربت تلقائياً في الخلفية فور إقلاع البوت
    try:
      subprocess.Popen(["python3", file_path])
      print(f"✅ تم إعادة تشغيل السكربت تلقائياً: {filename}")
    except Exception as e:
      print(f"❌ فشل تشغيل {filename}: {e}")


# تشغيل الدالة فور إقلاع البوت
restore_and_run_scripts()


# (بقية كود استقبال الملفات وحفظها في قاعدة البيانات...)

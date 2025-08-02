import pandas as pd

# آدرس فایل CSV روی دسکتاپ (حتماً مسیر خودت رو درست بنویس)
file_path =file_path = r"C:\Users\Dunya Computer\Desktop\jobs.csv"# خواندن فایل CSV
df = pd.read_csv(file_path)

# مهارت مورد نظر
target_skill = "Python"

# شمارش مشاغلی که این مهارت را دارند
count = df['skills'].str.contains(target_skill, case=False).sum()

# چاپ نتیجه
print(f"تعداد مشاغل دارای مهارت {target_skill}: {count}")

# ذخیره نتیجه در فایل متنی
with open("output.txt", "w", encoding="utf-8") as f:
    f.write(f"تعداد مشاغل دارای مهارت {target_skill}: {count}")

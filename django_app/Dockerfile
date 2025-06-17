FROM python:3.10-slim

# تعیین پوشه کاری در داخل کانتینر
WORKDIR /app

# کپی فایل‌های مورد نیاز (مثلاً requirements.txt) به کانتینر
COPY requirements.txt /app/

# نصب وابستگی‌ها؛ در صورتی که فایل requirements.txt موجود نیست، ممکن است نیاز به اضافه کردن Django داشته باشید.
RUN pip install --no-cache-dir -r requirements.txt

# کپی کل پروژه به داخل کانتینر
COPY . /app

# باز کردن پورت مورد نظر
EXPOSE 8000

# اجرای سرور Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

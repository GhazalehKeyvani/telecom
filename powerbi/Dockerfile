FROM mcr.microsoft.com/windows/servercore:ltsc2019

# کپی فایل نصب Power BI Report Server (باید فایل نصبی را از منابع رسمی تهیه کنید)
COPY PowerBIReportServer.exe C:\temp\PowerBIReportServer.exe

# نصب Power BI Report Server به صورت silent
RUN C:\temp\PowerBIReportServer.exe /quiet /norestart

# باز کردن پورت 80 برای دسترسی
EXPOSE 80

# نقطه شروع برای اجرای سرویس
ENTRYPOINT ["C:\\Program Files\\Microsoft Power BI Report Server\\PBIRS\\Service\\PBIRS.exe"]

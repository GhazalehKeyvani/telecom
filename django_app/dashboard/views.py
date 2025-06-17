# dashboard/views.py

from django.shortcuts import render
import requests
from django.http import JsonResponse

def home(request):
    """
    این view دانلود یک صفحه وب است که در آن گزارش Power BI جاسازی شده است.
    (برای نمونه، فرض می‌کنیم سرور Power BI شما در آدرس http://localhost:8080 اجرا می‌شود.)
    """
    # در قالب HTML از iframe استفاده می‌کنیم.
    context = {}
        # 'powerbi_url': 'http://localhost:8080'  # آدرس سرور Power BI Report Server یا Embedded
    # }
    return render(request, 'dashboard/home.html', context)

def ask_question(request):
    """
    این view برای دریافت پرسش از کاربر از طریق AJAX (یا فرم ساده) و ارسال آن به سرویس LLM agents تعریف شده است.
    """
    if request.method == 'POST':
        question = request.POST.get('question', '')
        # فرض می‌کنیم سرویس LLM agent روی http://localhost:5000/ask در کانتینر llm_agents در حال اجراست.
        try:
            response = requests.post('http://llm_agents:5000/ask', json={'question': 'hello'})
            data = response.json()
            return JsonResponse({'answer': data.get('answer', 'No answer')})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    return JsonResponse({'error': 'Invalid request'}, status=400)

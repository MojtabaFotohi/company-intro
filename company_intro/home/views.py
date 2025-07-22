from django.shortcuts import render

def home(request):
    """
    صفحه اصلی شرکت؛ نمای کلی خدمات و دعوت به دیدن پروژه‌ها.
    """
    return render(request, 'home/home.html')


def about(request):
    """
    صفحه اصلی شرکت؛ نمای کلی خدمات و دعوت به دیدن پروژه‌ها.
    """
    return render(request, 'home/aboutus.html')


def contact(request):
    """
    صفحه اصلی شرکت؛ نمای کلی خدمات و دعوت به دیدن پروژه‌ها.
    """
    return render(request, 'home/contactus.html')

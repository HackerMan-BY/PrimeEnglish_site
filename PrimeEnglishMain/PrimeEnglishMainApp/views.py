from django.shortcuts import render

def frst(request):
    return render(request, 'main.html')
def contact(request):
    return render(request, 'contacts.html')
def lessons(request):
    return render(request, 'lessons_and_prices.html')
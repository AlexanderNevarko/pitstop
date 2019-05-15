from django.shortcuts import render


def main_page(request):
    return render(request, 'pitstop_app/main_page.html', {})

def jopa(request):
    return None
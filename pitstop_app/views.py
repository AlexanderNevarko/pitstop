from django.shortcuts import render


def main_page(request):
    return render(request, 'pitstop_app/main_page.html', {})


def jopa(request):
    if request.method == 'POST':
        predict = get_prediction(request.POST)
        return render(request, 'pitstop_app/prediction.html', predict)
    else:
        return render(request, 'pitstop_app/error.html', {})


def error(request):
    return render(request, 'pitstop_app/error.html', {})


def get_prediction(data):
    return {'predict' : 'Some prediction'}



from django.shortcuts import render
from django.http import HttpResponseRedirect


mock_terms = {
    "terms": [
        {"date": "Śr. 12.05.2021 17:30", "shared": True, "index": 0, "num": 12},
        {"date": "Śr. 12.05.2021 19:30", "shared": False, "index": 1, "num": 3},
        {"date": "Śr. 12.05.2021 21:30", "shared": True, "index": 2, "num": 8},
        {"date": "Czw. 20.05.2021 17:30", "shared": False, "index": 3, "num": 6},
    ]
}


def main(request):
    if request.method == 'POST':
        if request.POST.get('book'):
            return HttpResponseRedirect('/color')
    return render(request, 'main.html')


def choose_color(request):
    if request.method == 'POST':
        if request.POST.get('color'):
            request.session['color'] = request.POST.get('color')
            return HttpResponseRedirect('/size')
    return render(request, 'color.html')


def choose_size(request):
    if request.method == 'POST':
        if request.POST.get('size'):
            request.session['size'] = request.POST.get('size')
            return HttpResponseRedirect('/term')
    return render(request, 'size.html')


def choose_term(request):
    if request.method == 'POST':
        if request.POST.get('term'):
            print(request.POST.get('term'))
            request.session['term'] = request.POST.get('term')
            return HttpResponseRedirect('/confirm')
    return render(request, 'term.html', mock_terms)


def confirm_term(request):
    color_text = {'black': 'Czarne', 'white': 'Białe', 'colored': 'Kolor'}
    size_text = {'small': 'Małe', 'medium': 'Średnie', 'big': 'Duże'}

    chosen_term = {
        "date": mock_terms['terms'][int(request.session['term'])]['date'],
        "shared": mock_terms['terms'][int(request.session['term'])]['shared'],
        "color": request.session['color'],
        "color_text": color_text[request.session['color']],
        "size": request.session['size'],
        "size_text": size_text[request.session['size']]
    }
    return render(request, 'confirm.html', chosen_term)


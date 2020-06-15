from django.shortcuts import render
from django.http import HttpResponseRedirect


mock_terms = {
    "terms": [
        {"date": "Śr. 12.05.2021 17:30", "shared": True, "index": 0},
        {"date": "Śr. 12.05.2021 19:30", "shared": False, "index": 1},
        {"date": "Śr. 12.05.2021 21:30", "shared": True, "index": 2},
        {"date": "Czw. 20.05.2021 17:30", "shared": False, "index": 3},
        {"date": "Pt. 21.05.2021 17:30", "shared": False, "index": 4}
    ]
}


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
    chosen_term = {
        "date": mock_terms['terms'][int(request.session['term'])]['date'],
        "shared": mock_terms['terms'][int(request.session['term'])]['shared'],
        "color": request.session['color'],
        "size": request.session['size'],
    }
    return render(request, 'confirm.html', chosen_term)

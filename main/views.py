from django.shortcuts import render,redirect,get_object_or_404
from django.db.models import Q

from .models import *
from .forms import *



def fanlar(request):
    fanlar = Fan.objects.all()
    if request.method == 'Post':
        form = FanForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('fanlar')
    form = FanForm()
    context = {
        'fanlar': Fan.objects.all(),
        'form': form
}
    return render(request, 'kitoblar.html', context)

def ustozlar(request):
    form = UstozForm()
    ustozlar = Ustoz.objects.all()
    if request.method == 'Post':
        form = UstozForm(request.POST)
        data = form.cleaned_data
        Ustoz.objects.create(
            ism=data.get('ism'),
            jins=data.get('jins'),
            yosh=data.get('yosh'),
            daraja=data.get('daraja'),
            fan=data.get('fan'),
        )
        return redirect('ustozlar')

    form = UstozForm()
    context = {
        'Ustozlar': Ustoz.objects.all(),
        'form': form
}
    return render(request, 'ustozlar.html', context)

def yonalishlar(request):
    form = YonalishForm()
    yonalishlar = Yonalish.objects.all()
    if request.method == 'Post':
        form = YonalishForm(request.POST)
        data = form.cleaned_data
        Ustoz.objects.create(
            nom=data.get('nom'),
            aktiv=data.get('aktiv'),

        )
        return redirect('yonalishlar')

    form = YonalishForm()
    context = {
        'Yonalishlar': Yonalish.objects.all(),
        'form': form
}
    return render(request, 'yonalishlar.html', context)



def mualliflar(request):
    mualliflar = Muallif.objects.all()
    if request.method == 'Post':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('mualliflar')
    form = MuallifForm()
    context = {
        'mualliflar': Muallif.objects.all(),
        'form': form
}
    return render(request, 'mualliflar.html', context)

def records(request):
    records = Record.objects.all()
    if request.method == 'Post':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('records')
    form = RecordForm()
    context = {
        'records': Record.objects.all(),
        'form': form
}
    return render(request, 'records.html', context)


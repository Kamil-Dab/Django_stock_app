from django.shortcuts import render, redirect
from .models import StockQuery
from .forms import StockQueryForm
from django.contrib import messages
from .stockQueryHelper import get_records


def home(request):
    return render(request, 'home.html', {})


def stock_app(request):
    output = list()
    records = False
    if not request.user.is_authenticated:
        return render(request, 'home.html', {})
    form = StockQueryForm()
    if request.method == 'POST':
        form = StockQueryForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('stock_app')
        else:
            messages.error(request, form.errors['__all__'])
            return render(request, 'stock_app.html',
                          {
                              'form': form,
                              'records': records,
                              'output': output
                          })
    else:
        form_data = StockQuery.objects.order_by('-id')
        if len(form_data) == 0:
            return render(request, 'stock_app.html',
                          {
                              'form': form
                          })
        else:
            records = get_records(form_data[0])

            if len(records) == 0:
                messages.info(request, "There is no data in this date range!")
                output = list()
            else:
                for item in records:
                    output.append(item)
            return render(request, 'stock_app.html',
                          {
                              'form': form,
                              'form_data': form_data,
                              'records': records,
                              'output': output
                          })

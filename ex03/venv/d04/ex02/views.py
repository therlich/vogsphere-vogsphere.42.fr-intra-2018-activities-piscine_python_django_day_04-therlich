from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import MyForm
import datetime
import logging
debug_logger = logging.getLogger('debug_logger')

# Create your views here.
def ex02_form(request):

    logs=open('logs.log','r')

    if request.method=='POST':
        form=MyForm(request.POST)
        if form.is_valid():
            my_text=form.cleaned_data['your_text']
            debug_logger.debug(my_text)

    else:
        form=MyForm()

    return render(request, 'form_template.html', {'form':form, 'results':logs})

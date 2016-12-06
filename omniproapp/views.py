# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from omniproapp.models import BaselineProfileModel, MeasuredProfileModel
from omniproapp.forms import BaselineProfileForm, MeasuredProfileForm
from django.core.files.storage import FileSystemStorage

import os
import json
import csv


def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = BaselineProfileForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = BaselineProfileModel(baseline_file=request.FILES['baseline_file'])
            newdoc.save()
            # fs = FileSystemStorage()
            # file_url = fs.url(newdoc.baseline_file)
            data = handle_csv(os.path.join(settings.MEDIA_ROOT, newdoc.baseline_file.name))
            print(data)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = BaselineProfileForm()  # A empty, unbound form

    # Load documents for the list page
    documents = BaselineProfileModel.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'omniproapp/list.html',
        {'documents': documents, 'form': form}
    )


def handle_csv(file_to_open):
    f = open(file_to_open, 'rt')
    data = []
    try:
        reader = csv.reader(f)
        for row in reader:
            data.append([float(x) for x in row])
    finally:
        f.close()
    return json.dumps(data)

# def plot_csv(json_in):
#
#     return render(request,
#                   'omniproapp/plot.html',
#                   {'documents': documents, 'form': form})
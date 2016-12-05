# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.conf import settings
from omniproapp.models import Document
from omniproapp.forms import DocumentForm
from django.core.files.storage import FileSystemStorage

import os
import json
import csv

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            newdoc.save()
            # fs = FileSystemStorage()
            # file_url = fs.url(newdoc.docfile)
            data = handle_csv(os.path.join(settings.MEDIA_ROOT, newdoc.docfile.name))
            print(data)
            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'omniproapp/list.html',
        {'documents': documents, 'form': form}
    )


def list_to_json(list_in):
    return json.dumps(list_in)


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

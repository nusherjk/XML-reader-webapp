from django.shortcuts import render
import utils
# Create your views here.

def index(request):
    if request.method== 'GET':
        return render(request, 'upload.html')
    if request.method == 'POST':
        f = request.FILES['xmlfile']
        data =utils.xmlsplitter(f)
        return render(request, 'upload.html', context={'treeData': data})
    
from django.shortcuts import render

# Create your views here.
import datetime
def filters(request):
    dt=datetime.datetime.now()
    d={'data':'Hai this is filter Function','dt':dt,'c':8}
    return render(request,'filters.html',context=d)





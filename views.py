import csv, io
from django.shortcuts import render
from django.contrib import messages
from .  models import Profile
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
import json
from . forms import LeaseProfileForm
from dal import autocomplete
import simplejson

# Create your views here.
# one parameter named request
@csrf_exempt
def profile_upload(request):
    # declaring template
    template = "profile_upload.html"
    data = Profile.objects.all()
# prompt is a context variable that can have different values      depending on their context
    prompt = {
        'order': 'Order of the CSV should be name, email',
        'profiles': data    
              }
    # GET request returns the value of the data with the specified key.
    if request.method == "GET":
        return render(request, template, prompt)
    csv_file = request.FILES['file']
    # let's check if it is a csv file
    if not csv_file.name.endswith('.csv'):
        messages.error(request, 'THIS IS NOT A CSV FILE')
    data_set = csv_file.read().decode('UTF-8')
    # setup a stream which is when we loop through each line we are able to handle a data in a stream
    io_string = io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = Profile.objects.update_or_create(
            username=column[0],
            email=column[1],
          
    )
    context = {}
    return render(request, template, context)

def search_view(request):
    q = request.GET.get('material','zzz') #tfor name startwith me write('term','me')
    print(q)
    ret = []
    listado = Profile.objects.filter(username__istartswith=q).order_by("username")
    for l in listado:
        ret.append({'label':l.username}) #'value':l.id})
    mimetype='application/json'
    return HttpResponse(simplejson.dumps(ret),mimetype)  #content_type=kwds.get('mimetype','application/json'))
    
    #return render(request,'search.html')

class TenantAutocomplete(autocomplete.Select2QuerySetView):
        def get_queryset(self):
            # Don't forget to filter out results depending on the visitor !
            #if not self.request.user.is_authenticated():
             #   return Profile.objects.none()

            qs = Profile.objects.all()

            if self.q:
                qs = qs.filter(last_name__istartswith=self.q)

            return qs
def tenant_new(request,pk,uri):
    lease = get_object_or_404(Lease, pk=pk)
    title = 'tenant'
    uri = _get_redirect_url(request, uri)
    if request.method == "POST":
        form = LeaseProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)  
            profile.lease = lease      
            profile.save()
            messages.add_message(request, messages.SUCCESS, str(profile.id) + "-SUCCESS Object created sucssefully")


            return redirect(uri)
    else:
        form = LeaseProfileForm()
    return render(request, 'new.html', {'form': form, 'title': title, 'extend': EXTEND})

class SignUpView(CreateView):
    template_name = 'base.html'
    form_class = UserCreationForm


@csrf_exempt
def validate_username(request):
    """if request.is_ajax():
        q = request.GET.get('username', '')
        print(q)
        search_qs = Profile.objects.filter(username__startswith=q)
        results = []
    
        for r in search_qs:
            results.append(r.username)
        data = json.dumps(results)

        mimetype = 'application/json'
        return HttpResponseRedirect(data, mimetype)"""
    username = request.GET.get('username', None)
    print(username)

    search_qs = Profile.objects.filter(username__startswith=username)
    results = []    
    for r in search_qs:
        results.append(r.username)
    data1 = json.dumps(results)

    """data = {
        'is_taken': Profile.objects.filter(username__iexact=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'"""
    data={}    
    data['words'] = data1
    data = str(data)
    print(type(data))
    return HttpResponse(data)
    

    



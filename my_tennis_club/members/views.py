from django.template import loader
from django.http import HttpResponse

# importing models
from .models import Member

# Create your views here.
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template('all_members.html')
    context = {
        'mymembers': mymembers
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    mymember = Member.objects.get(id=id)
    template = loader.get_template("details.html")
    context = {
        "mymember": mymember
    }
    return HttpResponse(template.render(context, request))

def staffs(request):
    template = loader.get_template("staffs.html")
    return HttpResponse(template.render())
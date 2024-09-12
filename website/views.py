from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from website.models import Member, Conventions, Profile, Vote
from django.shortcuts import get_object_or_404, render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
  return render( 
    request, 
    template_name='website/pages/index.html', 
    context={'results': True,'term': "term"}
  );
                

def about(request):
  return render(
    request, 
      template_name='website/pages/about.html', 
  );

def vote(request, convention_id):
  return HttpResponse("You're voting on convention %s." % convention_id);

def members(request):
  members = list(Member.objects.values());
  return render(request,  
          template_name='website/pages/members.html',
          context= {'members': members}
        );

def member(request, member_id):
  member = get_object_or_404(Member, pk=member_id);
  return HttpResponse('task: %s' % member.first_name);

def conventions(request):
  conventions = list(Conventions.objects.values());
  return render(request,  "conventions.html", {"conventions": conventions});

def convention(request, convention_id):
  convention = get_object_or_404(Conventions, pk=convention_id);
  return HttpResponse('task: %s' % convention.active);
from django.shortcuts import render
from django.utils import timezone

from .models import *

# Please remove if this is not used anywhere  - Apr 9 2020
def online_hobby_list(request):
    online = OnlineClass.objects.filter(created_date=timezone.now())
    return render(request, 'online_hobby_list.html',
                  {'OnlineHobbies': online})


#
#
# # Create your views here.

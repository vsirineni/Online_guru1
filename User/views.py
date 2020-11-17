from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from django.views import generic
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives, BadHeaderError
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import date
import datetime
import random
import string
from .forms import UserCreationForm, UserChangeForm
from django.shortcuts import render, redirect,  get_object_or_404
from .forms import UserCreationForm, UserChangeForm, ContactForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib import messages
from User.models import User

#uncomment below line if view has to import from hobby-view instead of model
#from Hobbies.views import Hobbies
from Hobbies.models import *
from OnlineHobbies.models import OnlineClass, OnlineClassVideoPage, OnlineClassEnroll
from OnlineHobbies.models import OnlineClass
from Cart.models import Cart, CartItem
from User.models import User

class PasswordResetMPSEmailView(PasswordResetView):
    PasswordResetView.extra_email_context = {'mps_site_name': 'Time to Skill'}

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile_preview'))
    else:
        form = UserChangeForm(instance=request.user)
        return render(request, 'profile.html', {'form': form})

#view to display hobby_list March 28
def hobby_list(request):
    hobby = Inclass.objects.all()
    return render(request, 'hobby_list.html',
                  {'Hobbies': hobby})


#view to display online_hobby_list March 30
def online_hobby_list(request):
    online = OnlineClass.objects.filter()
    return render(request, 'online_hobby_list.html',
                  {'OnlineHobbies': online})

# this view is to open online class video page on click of getstarted for an online hobby class- Apr 9 2020
def online_onclick_getstarted(request,pk):
    onlineclassvideo=OnlineClassVideoPage.objects.all().filter(online_class_name_id=pk).first()
    return render(request, 'onlineclassesbase.html',
                         {'onlineclassvideos': onlineclassvideo})

@login_required()
def contact(request):
    """Send Contact Email"""
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            rate_services = form.data['rate_services']
            like_the_best = form.data['likethebest']
            username = request.user.username
            email = request.user.email
            how_can_we_improve = form.data['howcanweimprove']
            recommed_friends = form.data['recommed_friends']
            anything = form.data['anything']
            template = get_template('registration/review_us_template.txt')
            context = {
                'username': username,
                'email': email,
                'rate_services': rate_services,
                'like_the_best': like_the_best,
                'how_can_we_improve': how_can_we_improve,
                'recommed_friends': recommed_friends,
                'anything': anything
            }
            content = template.render(context)
            send_mail("Rating", content, email, [settings.EMAIL_HOST_USER, email])
            return redirect('review_thankyou')
    else:
        form = ContactForm()
        return render(request, 'review.html', {'form': form})


def get_user_pending_order(request):
    # get order for the correct user
    user_profile = User.objects.filter(username=request.user.username).first()
    order = Cart.objects.filter(user=user_profile, is_ordered=False)
    if order.exists():
        # get the only order in the list of filtered orders
        return order[0]
    return 0

@login_required()
def order_details(request, **kwargs):
    existing_order = get_user_pending_order(request)
    context = {
        'order': existing_order
    }
    return render(request, 'order_summary.html', context)

@login_required()
def add_to_cart(request, **kwargs):
    # get the user profile
    user_profile = User.objects.filter(username=request.user.username).first()
    # filter products by id
    hobbies = Inclass.objects.filter(class_name=kwargs.get('item_id', "")).first()
    # check if the user already owns this product

    #if hobbies in request.user.profile.ebooks.all():
    #    messages.info(request, 'You already own this ebook')
    #    return redirect(reverse('products:product-list'))

    # create orderItem of the selected product
    order_item, status = CartItem.objects.get_or_create(classes= hobbies)
    # create order associated with the user
    user_order, status = Cart.objects.get_or_create(user=user_profile, is_ordered=False)
    user_order.items.add(order_item)
    if status:
        # generate a reference code
        user_order.ref_code = generate_order_id()
        user_order.save()

    # show confirmation message and redirect back to the same page
    messages.info(request, "item added to cart")
    return redirect(reverse('hobby_list'))


@login_required()
def delete_from_cart(request, item_id):
    item_to_delete = CartItem.objects.filter(pk=item_id)
    if item_to_delete.exists():
        item_to_delete[0].delete()
        messages.info(request, "Item has been deleted")
    return redirect(reverse('order_summary'))


def generate_order_id():
    date_str = date.today().strftime('%Y%m%d')[2:] + str(datetime.datetime.now().second)
    rand_str = "".join([random.choice(string.digits) for count in range(3)])
    return date_str + rand_str

# this is for allowing the subscribe button to add users to NewsUsers Admin and send welcome mail
# - Updated 11 April 2020

# this is for enrolling user for an online hobby class - Apr 9 2020
def online_class_enroll(request,pk):
    print("im at online_class_enroll ")
    print(pk)
    enrollment, status = OnlineClassEnroll.objects.get_or_create(enrollment_status= True, username_id=request.user.id, online_class_name_id=pk)
    storage = messages.get_messages(request)
    storage.used = True
    if not status:  # if not created a new row for that user
        messages.success(request, 'Already enrolled!!!!!!!!!!')
    else:  # if created a new row for the user
        enrollment.save()
        messages.success(request, 'Congratulations! You have enrolled successfully, please click the Get Started to'
                                  ' start classes!')
    online = OnlineClass.objects.filter()
    return render(request,  'online_hobby_list.html', {'OnlineHobbies': online})

# April 5th confirmation email to be sent to user after checkout
def order_confirm(request, **kwargs):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    existing_order = get_user_pending_order(request)
    id=generate_order_id()
    subject = 'Thank you for your reservation at Time to Skill!'
    template = get_template('registration/thank_you_template')
    context = {
        'username': username,
        'email': email,
        'id' : id,
        'first_name' : first_name,
        'hobbies' : existing_order,
    }

    existing_order.is_ordered = True
    existing_order.save()
    message = template.render(context)
    send_mail(subject, message, email, [settings.EMAIL_HOST_USER,email])
    return render(request, 'order_confirm.html')
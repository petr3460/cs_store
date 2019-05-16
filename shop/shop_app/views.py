from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import ReviewForm

from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from social_django.models import UserSocialAuth
from django.http import HttpResponse
from django.views.decorators.http import require_POST
import json
from django.db.models import Q


def home(request, tag=None):
    if tag:
        tag = get_object_or_404(Tag, slug=tag)
        products = Product.objects.filter(tags=tag)
        header = 'раздел "{}"'.format(tag.name)
    else:
        products = Product.objects.all()
        header = 'Новинки месяца'
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(name__icontains=query)|
            Q(author__name__icontains=query)|
            Q(description__icontains=query)
            ).distinct()
        header = 'поиск "{}"'.format(query)
    elif not query and not tag:
        products = products[:4]
    tags = Tag.objects.all()
    context = {
        'header': header,
        'tags': tags,
        'products': products
    }
    return render(request, 'home.html', context)


@login_required
def settings(request):
    user = request.user
    tags = Tag.objects.all()
    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        vk_login = user.social_auth.get(provider='vk-oauth2')
    except UserSocialAuth.DoesNotExist:
        vk_login = None
    context = {
        'twitter_login': twitter_login,  
        'vk_login': vk_login,      
        'tags': tags, 
    }
    return render(request, 'settings.html', context)


@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('settings')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, 'password.html', {'form': form})


def product(request, product_slug):
    tags = Tag.objects.all()
    product = get_object_or_404(Product, slug=product_slug)
    other_products = Product.objects.filter(tags__in=product.tags.all()).distinct('id')
    reviews = Review.objects.filter(product=product)
    form = ReviewForm()
    
    context = {
        'tags': tags,
        'product': product,
        'reviews': reviews,
        'other_products': other_products,
        'form': form
    }

    return render(request, 'product.html', context)


@login_required
@require_POST
def review(request):
    if request.method == "POST":

        form = ReviewForm(request.POST)
        if(form.is_valid()):

            form = form.save(commit=False)
            form.author = request.user
            product_id = request.POST.get('id', None)
            form.product = get_object_or_404(Product, id=product_id)            
            form.save()
            #pdb.set_trace()            
            review = form.text
            user = form.author.get_full_name()
           
            

        return HttpResponse(json.dumps({'review': review, 'user': user},), content_type='application/json')
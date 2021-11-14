from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import case
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login as loginn
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .models import case
from django.conf import settings
from coinbase_commerce.client import Client
from django.views.decorators.csrf import csrf_exempt
from coinbase_commerce.webhook import Webhook
from django.views.decorators.http import require_http_methods
from coinbase_commerce.error import SignatureVerificationError, WebhookInvalidPayload
import logging
from django.http import HttpResponse
import time





# # Create your views here.
def home(request):
    cases =case.objects.all()
    users =User.objects.all()
    amount=1
    if request.method == 'POST':
        amount = request.POST.get('amount')
        print(amount)
        form=UserCreationForm(request.POST)
        form2 =AuthenticationForm(data=request.POST)
        if form2.is_valid():
            user=form2.get_user()
            loginn(request, user)
        if form.is_valid():
            form.save()
            new_user = authenticate(username=form.cleaned_data['username'],password=form.cleaned_data['password1'],)
            loginn(request, new_user)
    else:
        form2=AuthenticationForm()
    form = UserCreationForm()
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': amount,
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'customer_id': request.user.id if request.user.is_authenticated else None,
            'customer_username': request.user.username if request.user.is_authenticated else None,
        },
    }
    charge = client.charge.create(**product)
    return render(request,'index.html',{"form":form,'form2':form2,'case':cases,'users':users,'charge': charge})

def case_detail(request,case_title):
    t={"case":case.objects.get(case_title=case_title)}
    return render(request,'case_detail.html',t)
@login_required()
def user(request):
    client = Client(api_key=settings.COINBASE_COMMERCE_API_KEY)
    domain_url = 'http://localhost:8000/'
    product = {
        'name': 'Coffee',
        'description': 'A really good local coffee.',
        'local_price': {
            'amount': '0.01',
            'currency': 'USD'
        },
        'pricing_type': 'fixed_price',
        'redirect_url': domain_url + 'success/',
        'cancel_url': domain_url + 'cancel/',
        'metadata': {
            'customer_id': request.user.id if request.user.is_authenticated else None,
            'customer_username': request.user.username if request.user.is_authenticated else None,
        },
    }
    charge = client.charge.create(**product)

    return render(request,'user.html',{'charge': charge,})



def success_view(request):
    return redirect('landing')


def cancel_view(request):
    return redirect('landing')

@csrf_exempt
@require_http_methods(['POST'])
def coinbase_webhook(request):
    logger = logging.getLogger(__name__)

    request_data = request.body.decode('utf-8')
    request_sig = request.headers.get('X-CC-Webhook-Signature', None)
    webhook_secret = settings.COINBASE_COMMERCE_WEBHOOK_SHARED_SECRET

    try:
        event = Webhook.construct_event(request_data, request_sig, webhook_secret)

        # List of all Coinbase webhook events:
        # https://commerce.coinbase.com/docs/api/#webhooks

        if event['type'] == 'charge:confirmed':
            logger.info('Payment confirmed.')
            customer_id = event['data']['metadata']['customer_id']
            customer_username = event['data']['metadata']['customer_username']
            # TODO: run some custom code here
            # you can also use 'customer_id' or 'customer_username'
            # to fetch an actual Django user

    except (SignatureVerificationError, WebhookInvalidPayload) as e:
        return HttpResponse(e, status=400)

    logger.info(f'Received event: id={event.id}, type={event.type}')
    return HttpResponse('ok', status=200)















# def login(request):
#     if request.method=='POST':
#         form =AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             loginn(request, user)
#             return redirect('http://127.0.0.1:8000/user'+'/'+user.username)
#     else:
#         form=AuthenticationForm()
#     return render(request,'login.html',{'form':form})

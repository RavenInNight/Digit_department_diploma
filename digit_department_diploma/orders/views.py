from http import HTTPStatus

import stripe
from django.shortcuts import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings

#from common.views import TitleMixin

from .forms import OrderForm
from .models import Order
from products.models import Bag

stripe.api_key = settings.STRIPE_SECRET_KEY

class TitleMixin:
    title = 'None'

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class SuccessTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/payment_confirmation.html'


class CanceledTemplateView(TitleMixin, TemplateView):
    template_name = 'orders/canceled.html'


class ShippingView(TitleMixin, CreateView):
    template_name = 'orders/shipping.html'
    form_class = OrderForm
    success_url = reverse_lazy('payment_confirmation')
    title = 'доставка'

    def post(self, request, *args, **kwargs):
        super(ShippingView, self).post(request, *args, **kwargs)
        bags = Bag.objects.filter(user=self.request.user)
        checkout_session = stripe.checkout.Session.create(
            line_items=bags.stripe_products(),
            metadata={'order_id': self.object.id},
            mode='payment',
            success_url='{}{}'.format(settings.DOMAIN_NAME, reverse('payment_confirmation')),
            cancel_url='{}{}'.format(settings.DOMAIN_NAME, reverse('order_canceled')),
        )
        return HttpResponseRedirect(checkout_session.url, status=HTTPStatus.SEE_OTHER)
    
    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(ShippingView, self).form_valid(form)

@csrf_exempt
def stripe_webhook_view(request):
    payload = request.body
    sig_header = request.META['HTTP_STRIPE_SIGNATURE']
    event = None

    try:
        event = stripe.Webhook.construct_event(
            payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
        )
    except ValueError:
        return HttpResponse(status=400)
    except stripe.error.SignatureVerificationError:
        return HttpResponse(status=400)

    if event['type'] == 'checkout.session.completed':
        session = event['data']['object']

        fulfill_order(session)

    return HttpResponse(status=200)

def fulfill_order(session):
    order_id = int(session.metadata.order_id)
    order = Order.objects.get(id=order_id)
    order.update_after_payment()


class PaymentConfirmationView(TitleMixin, TemplateView):
    template_name = 'orders/payment_confirmation.html'
    title = 'подтверждение заказа'


class OrdersProfileView(TitleMixin, ListView):
    model = Order
    template_name = 'orders/orders.html'
    title = 'заказ'

    def get_context_data(self,  *, object_list=None, **kwargs):
        context = super(OrdersProfileView, self).get_context_data()
        context['data'] = Order.objects.filter(initiator=self.request.user).last()
        return context
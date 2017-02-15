from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST

from .models import Coupon
from .forms import CouponsApplyForm


@require_POST
def coupon_apply(request):
    now = timezone.now()    # get the current time-zone-aware datetime
    form = CouponsApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupon.objects.get(code__iexact=code,
                                        valid_from__lte=now,
                                        valid_to__gte=now,
                                        active=True)
            coupon_id = coupon.id

        except Coupon.DoesNotExist:
            coupon_id = None

        request.session['coupon_id'] = coupon_id    # store the coupon id in the user's session
        return redirect('cart:cart_detail')

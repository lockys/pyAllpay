# Create your views here.
# -*- coding: UTF-8 -*-
from django.shortcuts import redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# allPay setting.
from pyallpay import AllPay

import logging
import json
import hashlib
import datetime

"""
    Example of Django view using allPay.
"""

@csrf_exempt
def create_payment(request):
    """
        I used ajax call to call this method.
    """
    merchant_trade_no = hashlib.sha224(str(datetime.datetime.now())).hexdigest().upper()
    merchant_trade_no = merchant_trade_no[0:19]

    # Initialize the allPay config.
    ap = AllPay({'TotalAmount': 300, 'ChoosePayment': 'ATM', 'MerchantTradeNo': 'merchant_trade_no', 'ItemName': "Default Item Name"})
    dict_url = ap.check_out()
    print(dict_url)

    #if the second parameter is true, send out automatically the allpay form.
    form_html = ap.gen_check_out_form(dict_url, True)

    print form_html
    return HttpResponse(json.dumps({'status': '200', 'form_html': form_html}))


@csrf_exempt
def get_feedback(request):
    """
    Feedback from allpay after the customer paid.
    :param request:
    :return:
    """
    req_post = request.POST

    returns = AllPay.checkout_feedback(req_post)
    logging.info(str(returns))
    if returns:
        if returns['RtnCode'] == '1':
            """
              payment is paid by customer.
            """
            # do your work here.
            return HttpResponse('1|OK')
        else:
            return HttpResponse('0|Bad Request')
    else:
        return HttpResponse('0|Bad Request')

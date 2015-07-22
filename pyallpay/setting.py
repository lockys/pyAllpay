'''
    You personal setting of AllPay
'''
try:
    from django.conf import settings
except:
    settings = {}

ALLPAY_SANDBOX = getattr(settings, 'ALLPAY_SANDBOX', True)
AIO_SERVICE_URL = 'https://payment.allpay.com.tw/Cashier/AioCheckOut'
AIO_SANDBOX_SERVICE_URL = 'http://payment-stage.allpay.com.tw/Cashier/AioCheckOut'

'''
    Get these from AllPay management panel
'''
MERCHANT_ID = getattr(settings, 'MERCHANT_ID', '2000132')
HASH_KEY = getattr(settings, 'HASH_KEY', '5294y06JbISpM5x9')
HASH_IV = getattr(settings, 'HASH_IV', '5294y06JbISpM5x9')

'''
    Please specify your own URL, check out the allpay document for more details
    https://www.allpay.com.tw/Service/API_Help?Anchor=AnchorDoc
'''
RETURN_URL = getattr(settings, 'RETURN_URL', '')
CLIENT_BACK_URL = getattr(settings, 'CLIENT_BACK_URL', '')
PAYMENT_INFO_URL = getattr(settings, 'PAYMENT_INFO_URL', '')

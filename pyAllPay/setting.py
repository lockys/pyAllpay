__author__ = 'Calvin'

SANDBOX = True

AIO_SERVICE_URL = 'https://payment.allpay.com.tw/Cashier/AioCheckOut'
AIO_SANDBOX_SERVICE_URL = 'http://payment-stage.allpay.com.tw/Cashier/AioCheckOut'

MERCHANT_ID = 'YOUR_MERCHANT_ID' if not SANDBOX else '2000132'
HASH_KEY = 'YOUR_HASH_KEY' if not SANDBOX else '5294y06JbISpM5x9'
HASH_IV = 'YOUR_HASH_IV' if not SANDBOX else 'v77hoKGq4kWxNNIS'

# URL Setting.
RETURN_URL = 'YOUR_RETURN_URL'
ORDER_RESULT_URL = 'YOUR_ORDER_RESULT_URL'
PAYMENT_INFO_URL = 'YOUR_PAYMENT_INFO_URL'

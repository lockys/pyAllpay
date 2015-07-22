```
+-+-+-+-+-+-+-+-+
|p|y|a|l|l|p|a|y|
+-+-+-+-+-+-+-+-+
```
This is allPay(歐付寶) SDK implemented in Python. not All functions are implemented now.
CheckOutString(), CheckOut(), CheckOutFeedback() has been implemented.
In general, it could be used in web developed by Django ..etc

Features:
==
Checkout a payment in ...

- [x] CVS
- [x] ATM
- [x] WebATM
- [x] BarCode
- [x] Credit card

Dealing with the POST data returned by 歐付寶(allPay) after the a payment creates or the customer pay the payment.

How to Use:
==
You can install using pip. [current release](https://pypi.python.org/pypi/pyallpay)

    pip install pyallpay

Or ... clone this project and put the pyallpay folder under root directory of your project.

    git clone https://github.com/lockys/allPay.py.git

Then include pyallpay into your project if you directly cloned the source code.

    from pyallpay import AllPay

First, you are required to set your own merchant ID, HashIV, HashKey provided by the 歐付寶 in the setting.py

Set up the /your-app/settings.py in Django (Required step)
==
    ALLPAY_SANDBOX = False # False or True, The sandbox configuration depend on you.
    MERCHANT_ID = 'YOUR_MERCHANT_ID' # Default is '2000132'
    HASH_KEY = 'YOUR_HASH_KEY' # Default is '5294y06JbISpM5x9'
    HASH_IV = 'YOUR_HASH_IV' # Default is 'v77hoKGq4kWxNNIS'
    RETURN_URL = 'YOUR_RETURN_URL'
    ORDER_RESULT_URL = 'YOUR_ORDER_RESULT_URL'
    PAYMENT_INFO_URL = 'YOUR_PAYMENT_INFO_URL'

Pleae check out AllPay's documents for more details to know what those variable means :)
https://www.allpay.com.tw/Service/API_Help?Anchor=AnchorDoc

Initialize an allPay payment
==
Take Django as instance.([You can check out the detailed Django App](https://github.com/lockys/allPay.py/tree/master/demo_django_app)
)
In your Django view.

    from pyallpay import AllPay

    payment_info = {'TotalAmount': 10, 'ChoosePayment': 'ATM', 'MerchantTradeNo': 'xvd123test', 'ItemName': "test"}
    ap = AllPay(payment_info)
    # check out, this will return the dictionart containing checkValue...etc
    dict_url = ap.check_out()
    # generate the submit form html
    form_html = ap.gen_check_out_form(dict_url)

**form_html** is a form in HTML, pyallpay will automatically send the request to AllPay for you.
if you want to send by yourself, just disable **auto_send**, like the below code.

    form_html = ap.gen_check_out_form(dict_url, False)

and you have to do submit #allPay-Form in your JavaScript.

    $('#allPay-Form').submit();


Retrive the POST data from allPay(歐付寶)
==
    from pyallpay import AllPay
    returns = AllPay.checkout_feedback(request.POST) #Django for ex.

**returns** will be a dict. that contains the information returned from allPay(歐付寶)
For example, **returns['RtnCode']** indicates the current status of a payment.
Check out the [allPay Documentation](https://www.allpay.com.tw/Service/API_Help?Anchor=AnchorDoc) for more details.

Available payment.
==
CVS, Barcode, ATM, WebATM, Credit card
You could simulate to pay in the administator panel provided by allPay, but you should implement the view by your own in order to catch the feedback data from allPay.

Goal:
==
This final goal for this project is to implement the full functionalities of Allpay SDK in Python language.

Project Current Status:
==
This project is still a baby. Therefore, the bugs may exist. :smiley:
I'll try hard to implement all th methods of allPay SDK.

Already tested Environment
==
It's tested with Django 1.5 and python 2.7.5

LICENCE
==
MIT

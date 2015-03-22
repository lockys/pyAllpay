## allPay.py
This is allPay SDK implemented in Python. not All function is implemented now.
#### How to Use
clone this project and put the pyAllPay folder under your project root directory.
First, you are required to set your own merchant ID, HashIV, HashKey in the setting.py 
setting.py

    SANDBOX = False # False or True, The sandbox configuration depend on you.
    MERCHANT_ID = 'YOUR_MERCHANT_ID' if not SANDBOX else '2000132'
    HASH_KEY = 'YOUR_HASH_KEY' if not SANDBOX else '5294y06JbISpM5x9'
    HASH_IV = 'YOUR_HASH_IV' if not SANDBOX else 'v77hoKGq4kWxNNIS'

##### Initialize a allPay payment.
Take Django as instance.
In your Django view

    from pyallpay.allPay import AllPay
    ap = AllPay({'TotalAmount': 10, 'ChoosePayment': ATM, 'MerchantTradeNo': 'xvd123test', 'ItemName': "test"})
    # check out, this will return the dictionart containing checkValue...etc 
    dict_url = ap.check_out()
    # generate the submit form html
    form_html = ap.gen_check_out_form(dict_url)

#### Goal:
This final goal for this project is to implement the full functionalities of Allpay SDK in Python language.

#### Project Current Status:
This project is still a baby.
It's built with Django 1.5 and tested to create ATM, WebATM, Barcode, CVS (convenience store) payments successfully.
Also, Pay simulation is ok now. 

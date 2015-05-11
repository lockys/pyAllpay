## allPay.py
This is allPay(歐付寶) SDK implemented in Python. not All functions are implemented now.
CheckOutString(), CheckOut(), CheckOutFeedback() has been implemented.  
In general, it could be used in web developed by web framework in python such as flask, Django ..etc
#### Features:
Checkout a payment with following method.
-[x] CVS
-[x] ATM
-[x] WebATM
-[x] BarCode
-[x] Credit card
Dealing with the POST data After the a payment creates or the customer pay the payment.

#### How to Use:
Clone this project and put the pyAllPay folder under your project root directory.

    git clone https://github.com/lockys/allPay.py.git

First, you are required to set your own merchant ID, HashIV, HashKey provided by the 歐付寶 in the setting.py

##### - Set up the setting.py

    SANDBOX = False # False or True, The sandbox configuration depend on you.
    MERCHANT_ID = 'YOUR_MERCHANT_ID' if not SANDBOX else '2000132'
    HASH_KEY = 'YOUR_HASH_KEY' if not SANDBOX else '5294y06JbISpM5x9'
    HASH_IV = 'YOUR_HASH_IV' if not SANDBOX else 'v77hoKGq4kWxNNIS'

##### - Initialize an allPay payment
Take Django as instance.
In your Django view

    from pyallpay.allPay import AllPay

    payment_info = {'TotalAmount': 10, 'ChoosePayment': ATM, 'MerchantTradeNo': 'xvd123test', 'ItemName': "test"}
    ap = AllPay(payment_info)
    # check out, this will return the dictionart containing checkValue...etc
    dict_url = ap.check_out()
    # generate the submit form html
    form_html = ap.gen_check_out_form(dict_url)

**form_html** is a form in HTML, you have to submit this form in your front-ended side.  
For example(if you have included JQuery.):

    $('#allPay-Form').submit();


##### - Retrive the POST data from allPay(歐付寶)

    from pyallpay.allPay import AllPay
    returns = AllPay.checkout_feedback(request.POST) #Django for ex.

**returns** will be a dict. that contains the information returned from allPay(歐付寶)  
For example, **returns['RtnCode']** indicates the current status of a payment.  
Check out the [allPay Documentation](https://www.allpay.com.tw/Service/API_Help?Anchor=AnchorDoc) for more details.
#### Available payment.
CVS, Barcode, ATM, WebATM, Credit card    
You could simulate to pay in the administator panel provided by allPay, but you should implement the view by your own in order to catch the feedback data from allPay.
#### Goal:
This final goal for this project is to implement the full functionalities of Allpay SDK in Python language.
#### Project Current Status:
This project is still a baby. Therefore, the bugs may exist. :smiley:  
I'll try hard to implement all th methods of allPay SDK.  
#### Already tested Environment
It's tested with Django 1.5 and python 2.7.5  

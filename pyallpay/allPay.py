# -*- coding: UTF-8 -*-
import time
import datetime
import urllib
import hashlib
import logging
from utilities import do_str_replace
'''
    Configure your personal setting in setting.py
'''
from setting import HASH_IV, HASH_KEY
from setting import AIO_SANDBOX_SERVICE_URL, AIO_SERVICE_URL, RETURN_URL, CLIENT_BACK_URL, PAYMENT_INFO_URL
from setting import MERCHANT_ID
from setting import ALLPAY_SANDBOX


class AllPay():
    # If it is in sandbox mode ?
    is_sandbox = ALLPAY_SANDBOX

    def __init__(self, payment_conf, service_method='post'):
        self.url_dict = dict()

        # === BASIC CONFIG FOR ALLPAY ===
        self.service_method = service_method
        self.HASH_KEY = HASH_KEY
        self.HASH_IV = HASH_IV
        self.service_url = AIO_SANDBOX_SERVICE_URL if self.is_sandbox else AIO_SERVICE_URL

        self.url_dict['MerchantID'] = MERCHANT_ID
        self.url_dict['ReturnURL'] = RETURN_URL

        self.url_dict['MerchantTradeNo'] = hashlib.sha224(str(datetime.datetime.now())).hexdigest().upper() if not ('MerchantTradeNo' in payment_conf) else payment_conf['MerchantTradeNo']
        self.url_dict['PaymentType'] = 'aio'
        self.url_dict['TotalAmount'] = 300 if not ('TotalAmount' in payment_conf) else payment_conf['TotalAmount']
        self.url_dict['TradeDesc'] = 'Default Description' if not ('TradeDesc' in payment_conf) else payment_conf['TradeDesc']
        self.url_dict['ItemName'] = 'Default Item Name' if not ('ItemName' in payment_conf) else payment_conf['ItemName']
        self.url_dict['ChoosePayment'] = 'ATM' if not ('ChoosePayment' in payment_conf) else payment_conf['ChoosePayment']
        self.url_dict['MerchantTradeDate'] = time.strftime('%Y/%m/%d %H:%M:%S', time.localtime(time.time()))
        # self.url_dict['MerchantTradeDate'] = '2014/02/08 15:13:20'
        self.url_dict['ItemURL'] = '' if not ('ItemURL' in payment_conf) else payment_conf['ItemURL']
        self.url_dict['Remark'] = '' if not ('Remark' in payment_conf) else payment_conf['Remark']
        self.url_dict['ChooseSubPayment'] = '' if not ('ChooseSubPayment' in payment_conf) else payment_conf['ChooseSubPayment']
        self.url_dict['OrderResultURL'] = CLIENT_BACK_URL if not ('ClientBackURL' in payment_conf) else payment_conf['ClientBackURL']
        self.url_dict['ClientBackURL'] = CLIENT_BACK_URL if not ('ClientBackURL' in payment_conf) else payment_conf['ClientBackURL']

        if self.url_dict['ChoosePayment'] == 'ATM':
            self.url_dict['ExpireDate'] = '' if not ('ExpireDate' in payment_conf) else payment_conf['ExpireDate']
            self.url_dict['PaymentInfoURL'] = PAYMENT_INFO_URL if not ('PaymentInfoURL' in payment_conf) else payment_conf['PaymentInfoURL']
        elif self.url_dict['ChooseSubPayment'] == 'CVS':
            self.url_dict['Desc_1'] = '' if not ('Desc_1' in payment_conf) else payment_conf['Desc_1']
            self.url_dict['Desc_2'] = '' if not ('Desc_2' in payment_conf) else payment_conf['Desc_2']
            self.url_dict['Desc_3'] = '' if not ('Desc_3' in payment_conf) else payment_conf['Desc_3']
            self.url_dict['Desc_4'] = '' if not ('Desc_4' in payment_conf) else payment_conf['Desc_4']
            self.url_dict['PaymentInfoURL'] = PAYMENT_INFO_URL if not ('PaymentInfoURL' in payment_conf) else payment_conf['PaymentInfoURL']

    def check_out(self):
        sorted_dict = sorted(self.url_dict.iteritems())

        # insert the HashKey to the head of dictionary & HashIv to the end
        sorted_dict.insert(0, ('HashKey', self.HASH_KEY))
        sorted_dict.append(('HashIV', self.HASH_IV))

        result_request_str = do_str_replace(urllib.quote(urllib.urlencode(sorted_dict), '+%').lower())

        logging.info(urllib.quote(urllib.urlencode(sorted_dict), '+').lower())

        # md5 encoding
        check_mac_value = hashlib.md5(result_request_str).hexdigest().upper()
        self.url_dict['CheckMacValue'] = check_mac_value
        return self.url_dict

    @classmethod
    def checkout_feedback(cls, post):
        """
        :param post: post is a dictionary which allPay server sent to us.
        :return: a dictionary containing data the allpay server return to us.
        """
        logging.info('inside the feedback')
        returns = {}
        ar_parameter = {}
        check_mac_value = ''
        try:
            payment_type_replace_map = {'_CVS': '', '_BARCODE': '', '_Alipay': '', '_Tenpay': '', '_CreditCard': ''}
            period_type_replace_map = {'Y': 'Year', 'M': 'Month', 'D': 'Day'}
            for key, val in post.iteritems():

                print key, val
                if key == 'CheckMacValue':
                    check_mac_value = val
                else:
                    ar_parameter[key.lower()] = val
                    if key == 'PaymentType':
                        for origin, replacement in payment_type_replace_map.iteritems():
                            val = val.replace(origin, replacement)
                    elif key == 'PeriodType':
                        for origin, replacement in period_type_replace_map.iteritems():
                            val = val.replace(origin, replacement)
                    returns[key] = val

            sorted_returns = sorted(ar_parameter.iteritems())
            sz_confirm_mac_value = "HashKey=" + HASH_KEY

            for val in sorted_returns:
                sz_confirm_mac_value = "".join((str(sz_confirm_mac_value), "&", str(val[0]), "=", str(val[1])))

            sz_confirm_mac_value = "".join((sz_confirm_mac_value, "&HashIV=", HASH_IV))
            sz_confirm_mac_value = do_str_replace((urllib.quote_plus(sz_confirm_mac_value)).lower(), False)
            sz_confirm_mac_value = hashlib.md5(sz_confirm_mac_value).hexdigest().upper()

            logging.info('sz-checkMacValue: %s & checkMacValue: %s' % (sz_confirm_mac_value, check_mac_value))

            if sz_confirm_mac_value != check_mac_value:
                return False
            else:
                return returns
        except:
            logging.info('Exception!')

    def gen_check_out_form(self, dict_url, auto_send=True):
        """
        Generate The Form Submission
        :param dict_url:
        :return: the html of the form
        """
        form_html = '<form id="allPay-Form" name="allPayForm" method="post" target="_self" action="%s" style="display: none;">' % self.service_url

        for i, val in enumerate(dict_url):
            print val, dict_url[val]
            form_html = "".join((form_html, "<input type='hidden' name='%s' value='%s' />" % (val, dict_url[val])))

        form_html = "".join((form_html, '<input type="submit" class="large" id="payment-btn" value="BUY" /></form>'))
        if auto_send:
            form_html = "".join((form_html, "<script>document.allPayForm.submit();</script>"))
        return form_html

    @classmethod
    def query_payment_info(cls, merchant_trade_no):
        """
        Implementing ...
        :param merchant_trade_no:
        :return:
        """
        logging.info('== Query the info==')
        returns = {}
        logging.info(merchant_trade_no)

        return returns

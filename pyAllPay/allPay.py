__author__ = 'Calvin.J'

from pyallpay.setting import HASH_IV, HASH_KEY, AIO_SANDBOX_SERVICE_URL, AIO_SERVICE_URL, RETURN_URL, MERCHANT_ID, ORDER_RESULT_URL, PAYMENT_INFO_URL
import time
import datetime
import urllib
import hashlib
import logging


class AllPay():
    # If it is in sandbox mode ?
    is_sandbox = True

    def __init__(self, payment_conf, service_method='post'):
        self.url_dict = dict()

        # basic config.
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
        self.url_dict['OrderResultURL'] = ORDER_RESULT_URL if not ('OrderResultURL' in payment_conf) else payment_conf['OrderResultURL']
        self.url_dict['ClientBackURL'] = ORDER_RESULT_URL if not ('ClientBackURL' in payment_conf) else payment_conf['ClientBackURL']

        if self.url_dict['ChoosePayment'] == 'ATM':
            self.url_dict['ExpireDate'] = '' if not ('ExpireDate' in payment_conf) else payment_conf['ExpireDate']
            self.url_dict['PaymentInfoURL'] = PAYMENT_INFO_URL if not ('PaymentInfoURL' in payment_conf) else payment_conf['PaymentInfoURL']
        elif self.url_dict['ChooseSubPayment'] == 'CVS':
            self.url_dict['Desc_1'] = '' if not ('Desc_1' in payment_conf) else payment_conf['Desc_1']
            self.url_dict['Desc_2'] = '' if not ('Desc_2' in payment_conf) else payment_conf['Desc_2']
            self.url_dict['Desc_3'] = '' if not ('Desc_3' in payment_conf) else payment_conf['Desc_3']
            self.url_dict['Desc_4'] = '' if not ('Desc_4' in payment_conf) else payment_conf['Desc_4']
            self.url_dict['PaymentInfoURL'] = PAYMENT_INFO_URL if not ('PaymentInfoURL' in payment_conf) else payment_conf['PaymentInfoURL']


    @classmethod
    def do_str_replace(cls, string):
        mapping_dict = {'-': '%2d', '_': '%5f', '.': '%2e', '!': '%21', '*': '%2a', '(': '%28', ')': '%29', '%2f': '%252f', '%3a': '%253a'}

        for key, val in mapping_dict.iteritems():
            string = string.replace(val, key)

        return string

    def check_out(self):
        sorted_dict = sorted(self.url_dict.iteritems())

        # insert the HashKey to the head of dictionary & HashIv to the end
        sorted_dict.insert(0, ('HashKey', self.HASH_KEY))
        sorted_dict.append(('HashIV', self.HASH_IV))

        result_request_str = self.do_str_replace(urllib.quote(urllib.urlencode(sorted_dict), '+').lower())

        # md5 encoding
        check_mac_value = hashlib.md5(result_request_str).hexdigest().upper()
        self.url_dict['CheckMacValue'] = check_mac_value
        return self.url_dict

    @classmethod
    def checkout_feedback(cls, post):
        """
        :param post: post is a dictionary which allPay server sent to us.
        :return:
        """
        returns = {}
        try:
            payment_type_replace_map = {'_CVS': '', '_BARCODE': '', '_Alipay': '', '_Tenpay': '', '_CreditCard': ''}
            period_tpye_replace_map = {'Y': 'Year', 'M': 'Month', 'D': 'Day'}
            for key, val in post.iteritems():
                print key, val
                if key == 'CheckMacValue':
                    returns[key.lower()] = val
                else:
                    if key == 'PaymentType':
                        for origin, replacement in payment_type_replace_map.iteritems():
                            val = val.replace(origin, replacement)
                        returns[key.lower()] = val
                    elif key == 'PeriodType':
                        for origin, replacement in period_tpye_replace_map.iteritems():
                            val = val.replace(origin, replacement)
                        returns[key.lower()] = val
        except:
            raise NotImplementedError

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
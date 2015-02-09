# Create your views here.
from django.shortcuts import render
from pyallpay.allPay import AllPay
from pyallpay.setting import AIO_SANDBOX_SERVICE_URL, AIO_SERVICE_URL


def my_test_view(request):
    service_url = AIO_SANDBOX_SERVICE_URL if AllPay.is_sandbox else AIO_SERVICE_URL
    ap = AllPay({})
    dict_url = ap.check_out()
    print(dict_url)

    return render(request, "test_app/index.html", {"dict_url": dict_url, "service_url": service_url})

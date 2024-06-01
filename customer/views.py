from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from customer.models import customer_data, customer_info
from .forms import customer_form



def customer(request):

    # na =("sohag ","anika","rs","ds","ds","as")

    # ag = (21, 22, 33, 44, 55, 66, 77, 88, 99)
    # rol= (1, 2,3,4 ,5,6,7,8,9,10,11,12,13,14)
    #
    # context = {
    #
    #             'brand': 'Ford',
    #             'model': 'Mustang',
    #             'year': '1964',
    # }
    context = {
        "data": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    }


    return  render(request,"customer/customer.html",context=context)



def customer_list(request):
    cus_info=customer_data.objects.all()

    return render(request, "customer/customer.html",{"cus_info":cus_info} )


def customer_reg(request):

    if request.method == "POST":
        customer_freg = customer_form(request.POST)
        if customer_freg.is_valid():
          print(customer_freg.cleaned_data['password'])
          print(customer_freg.cleaned_data['repassword'])
          print('This is post method')
    else:
     customer_freg=customer_form()
     print("this get method")
    # customer_freg.order_fields(field_order=['email','first_name',' last_name'])
    return render(request,"customer/forms.html",{"customer_freg":customer_freg})


# Create your views here.





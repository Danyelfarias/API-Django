
# from django.http import HttpResponse
from django.shortcuts import render,redirect

from cars.models import Car
from cars.forms import  CarModelForm



def cars_view (request):
    # request -- é o que o usuario solicita
    # conhecido como GET
    print(request.GET)


    cars = Car.objects.all()
    # cars = Car.objects.all().order_by('model') -- maneira de organizar
    # cars = Car.objects.filter(brand = 1) --  mais um tipo de filtro 
    # ao brand__name = 'Fiat' -- esse seria pelo nome escrito
    # ao brand__contains = 'chavrolet' -- pesquisa por termo
    # ao brand__icontains = 'chavrolet' -- pesquisa por termo minusculo ou maiculo

    return render(request,
                  'cars.html',
                    {'cars': cars}
                    )
    # return HttpResponse('html') --usado para passar o html puro 

def new_car_view(request):
  if request.method == 'POST':
      new_car_form = CarModelForm(request.POST,request.FILES)
      if new_car_form.is_valid():
         new_car_form.save()
         return redirect('cars_list')
  else:
    new_car_form = CarModelForm()
  return render(request,'new_car.html',
                  {'new_car_form':new_car_form}
                    )
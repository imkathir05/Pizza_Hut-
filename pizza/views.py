from django.shortcuts import render
from .forms import PizzaForm,MultiplePizzaForm
from django.forms import formset_factory
from .models import Pizza

# Create your views here.

def homepage(request):
    return render(request,'home.html')

def order(request):
    created_pizza_pk= None
    multiple_form=MultiplePizzaForm() #emptyform
    if request.method == 'POST':
        filled_form = PizzaForm(request.POST)
        if filled_form.is_valid():
            note="Thanks for ordering %s and %s ,%s pizza"%(filled_form.cleaned_data['topping1'],
                                                            filled_form.cleaned_data['topping2'],
                                                            filled_form.cleaned_data['size'])
            print(filled_form.cleaned_data['topping1'])
            created_pizza=filled_form.save()  #save in DB
            created_pizza_pk=created_pizza.id
        else:
            note=('sorry try again..')
        new_form=PizzaForm()
        return render(request,'order.html',{'pizzaform':new_form,'note':note,'multiple_pizza_form':multiple_form,'created_pizza_pk':created_pizza_pk})
    else:
        form=PizzaForm()
        return render(request,'order.html',{'pizzaform':form,'multiple_pizza_form':multiple_form})

def pizzas(request):
    no_of_pizzas=2
    if request.method == 'GET':
        filled_multiple_form = MultiplePizzaForm(request.GET)
        if filled_multiple_form.is_valid():
            no_of_pizzas=filled_multiple_form.cleaned_data['number']
        print(no_of_pizzas)
    PizzaFormSet= formset_factory(PizzaForm,extra=no_of_pizzas)
    form_set = PizzaFormSet() #empty formset
    if request.method == 'POST':
        filled_formset = PizzaFormSet(request.POST)
        if filled_formset.is_valid():
            note='Thanks your order has been placed successfully '
            for form in filled_formset:
                print(form.cleaned_data['topping1'])
                form.save() #save form i db
            note = 'Thanks your order has been placed successfully '
        else:
            note='Sorry order again'
        return render(request, 'pizzas.html', {'form_set': form_set,'note':note})
    else:
        return render(request,'pizzas.html',{'form_set':form_set})


def edit(request,pk):
    note=''
    pizza_obj= Pizza.objects.get(pk=pk)
    form = PizzaForm(instance=pizza_obj)
    if request.method == 'POST':
        edited_form = PizzaForm(request.POST,instance=pizza_obj)  #filledform
        if edited_form.is_valid():
            edited_form.save()
            note="Your Order Edited successfully"
        else:
            note="Sorry Try Again...."
    return render(request,'edit.html',{'form':form,'pk':pk,'note':note})
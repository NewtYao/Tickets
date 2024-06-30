from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import SignUpForm, CreateTicket
from .models import Tickets


# Create your views here.
def home(request):
    # tickets = Tickets.objects.all()
    #check login or not
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You Have Been Logged In !")
            return redirect('home')
        else:
            messages.success(request, "There Was An Error Logging In ! Please Check Again. ")
            return redirect('home')
    else:
        return render(request, 'home.html', {})

# def login_user(request):
#     pass

def logout_user(request):
    logout(request)
    messages.success(request, "Have A Nice Day !")
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "You Have Successfully Registered !")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def create_ticket(request):
    ticket = CreateTicket(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if ticket.is_valid():
                create_ticket = ticket.save(commit=False)
                create_ticket.seller = request.user
                create_ticket.save()
                messages.success(request, "Ticket Created Successfully !")
                return redirect('create_ticket')
        return render(request, 'create_ticket.html', {'ticket':ticket})
    else:
        messages.success(request, "You Must Login First !")
        return redirect('home')
    
def my_tickets(request, pk):
    if request.user.is_authenticated:
        pk = request.user.id
        my_tickets = Tickets.objects.filter(seller_id=pk)
        return render(request, 'my_tickets.html', {'my_tickets':my_tickets})
    else:
        messages.success(request, "You Must Be Logged In To View That Page !")
        return redirect('home')


def delete_ticket(request, pk):
    if request.user.is_authenticated:
        deleted_ticket = get_object_or_404(Tickets, pk=pk, seller_id=request.user.id)
        deleted_ticket.delete()
        messages.success(request, 'The Ticket Has Been Deleted !')
        return redirect('my_tickets', pk)
    else:
        messages.success(request, "You Have To Login First!")
        return redirect('home')
        
def update_ticket(request, pk):
    if request.user.is_authenticated:
        current_ticket = get_object_or_404(Tickets, pk=pk, seller_id=request.user.id)
        update = CreateTicket(request.POST or None, instance=current_ticket)
        if update.is_valid():
            update.save()
            messages.success(request, "The Ticket Has Been Updated !")
            return redirect('my_tickets', pk)
        return render(request, 'update_ticket.html', {'ticket':update})
    else:
        messages.success(request, "You Have To Login First!")
        return redirect('home')
        


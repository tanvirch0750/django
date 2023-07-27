from django.http import HttpResponse
from django.shortcuts import render

data = [
    {
        "id": 1,
        "name": "John Doe",
        "phone_number": "123-456-7890",
        "address": "123 Main St"
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "phone_number": "987-654-3210",
        "address": "456 Elm St"
    },
    {
        "id": 3,
        "name": "Bob Johnson",
        "phone_number": "555-123-4567",
        "address": "789 Oak St"
    },
    {
        "id": 4,
        "name": "Alice Williams",
        "phone_number": "222-333-4444",
        "address": "101 Maple Ave"
    }
]


def contact(request):
   return render(request, './app/contact.html', context={'author': 'Tanvir', 'age': 17, 'persons': data})


def about(request):
   return render(request, './app/about.html')
    

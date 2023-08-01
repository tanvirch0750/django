from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Your Name")
    email = forms.EmailField(label="Your Email")
    birthDate = forms.DateField(label="Your Birthday")
    age = forms.IntegerField(label="Your Age")
    weight = forms.FloatField(label="Your Weight")
    balance = forms.DecimalField(label="Your Balance")
    check = forms.BooleanField(label="Do you agree with terms and condition?")
    appointment = forms.DateTimeField(label="Appointment time")
    CHOICES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]
    size= forms.ChoiceField(label="Select your size", choices=CHOICES)
    COLOR=[("red", "Red"), ("green", "Green"), ("yellow", "Yellow")]
    color= forms.MultipleChoiceField(label="Select Color", choices=COLOR)
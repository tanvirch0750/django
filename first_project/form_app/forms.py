from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Your Name", initial='Tanvir', help_text='Enter your name', required=False, disabled=False)
    # file = forms.FileField(label="Your profile image")
    email = forms.EmailField(label="Your Email")
    birthDate = forms.DateField(label="Your Birthday", widget=forms.DateInput(attrs= { 'type' : 'date'}))
    age = forms.IntegerField(label="Your Age")
    weight = forms.FloatField(label="Your Weight")
    balance = forms.DecimalField(label="Your Balance")
    check = forms.BooleanField(label="Do you agree with terms and condition?")
    appointment = forms.DateTimeField(label="Appointment time", widget=forms.DateInput(attrs= { 'type' : 'datetime-local'}))
    CHOICES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]
    size= forms.ChoiceField(label="Select your size", choices=CHOICES, widget=forms.RadioSelect)
    COLOR=[("red", "Red"), ("green", "Green"), ("yellow", "Yellow")]
    color= forms.MultipleChoiceField(label="Select Color", choices=COLOR, widget=forms.CheckboxSelectMultiple)
    message= forms.CharField(label='Your Message', widget=forms.Textarea(attrs= {'class': 'my-class', 'placeholder': 'Write your message'}))
from django.core import validators

from django import forms


class contactForm(forms.Form):
    name = forms.CharField(label="Your Name", initial='Tanvir', help_text='Enter your name', required=False, disabled=False, validators=[validators.MinLengthValidator(10, message='Enter a name with atleast 10 characters')])
    
    # file = forms.FileField(label="Your profile image", validators=[validators.FileExtensionValidator(allowed_extensions=['pdf', 'png'], message='File extension must me ended with .pdf')])
    
    email = forms.EmailField(label="Your Email")
    
    password = forms.CharField(label="Your password", widget=forms.PasswordInput)
    confirm_password = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    
    birthDate = forms.DateField(label="Your Birthday", widget=forms.DateInput(attrs= { 'type' : 'date'}))
    
    age = forms.IntegerField(label="Your Age", validators=[validators.MaxValueValidator(34, message='Age must be maximum 34'), validators.MinValueValidator(24, message='age must be atleast 24')])
    
    weight = forms.FloatField(label="Your Weight")
    
    balance = forms.DecimalField(label="Your Balance")
    
    check = forms.BooleanField(label="Do you agree with terms and condition?")
    
    appointment = forms.DateTimeField(label="Appointment time", widget=forms.DateInput(attrs= { 'type' : 'datetime-local'}))
    
    CHOICES=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')]
    size= forms.ChoiceField(label="Select your size", choices=CHOICES, widget=forms.RadioSelect)
    
    COLOR=[("red", "Red"), ("green", "Green"), ("yellow", "Yellow")]
    color= forms.MultipleChoiceField(label="Select Color", choices=COLOR, widget=forms.CheckboxSelectMultiple)
    
    message= forms.CharField(label='Your Message', widget=forms.Textarea(attrs= {'class': 'my-class', 'placeholder': 'Write your message'}))
    # validate data
    # def clean_name(self):
    #     valname = self.cleaned_data['name']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with atleast 10 characters')
    #     return valname
    # def clean_email(self):
    #     valemail = self.cleaned_data['email']
    #     if '.com' not in valemail:
    #          raise forms.ValidationError('Your email must contain .com')
    #     return valemail
    
    # shoortcut method
    # def clean(self):
    #     cleaned_data = super().clean()
    #     valname = self.cleaned_data['name']
    #     valemail = self.cleaned_data['email']
    #     if len(valname) < 10:
    #         raise forms.ValidationError('Enter a name with atleast 10 characters')
    #     if '.com' not in valemail:
    #          raise forms.ValidationError('Your email must contain .com')
         
         
    # password validation
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_confirm_pass = self.cleaned_data['confirm_password']
        if val_pass != val_confirm_pass:
             raise forms.ValidationError('Password does not match')
   
        
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# função para facilitar as sobrescritas dos padrões do django


def add_attrs(field, attr_name, attr_new_val):
    existing = field.widget.attrs.get(attr_name, '')
    field.widget.attrs[attr_name] = f'{existing} {attr_new_val}'.strip()

# função auxiliar especifica para placeholder


def add_placeholder(field, placeholder_val):
    add_attrs(field, 'placeholder', placeholder_val)


class RegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['username'], 'Your username')

    password2 = forms.CharField(
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'password',
        ]

        widgets = {
            'password': forms.PasswordInput()
        }

# o método clean_nome_do_campo,
# ex: clean_first_name, clean_password etc é específico de um campo
# apos a validação individual de cada campo,
# usa-se o método clean para validar vários campos

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')

        if password != password2:
            raise ValidationError({
                'password': 'Password and password2 must be equal.',
                'password2': 'Password and password2 must be equal.',
            })

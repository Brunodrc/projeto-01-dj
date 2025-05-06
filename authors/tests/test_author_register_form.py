# testes unitarios ou testes funcionais
# aqui serão realizados testes unitários
from unittest import TestCase
from authors.forms import RegisterForm

# pararealizer um teste semelhante nos demais testes
from parameterized import parameterized


class AuthorRegisterFormUnitTest(TestCase):
    @parameterized.expand([
        ('username', 'Your username'),
        ('email', 'Your e-mail'),
        ('password', 'Type your password'),
        ('password2', 'Repeat your password'),
    ])
    def test_fields_placeholder_is_correct(self, field, placeholder):
        form = RegisterForm()
        placeholder_get = form[field].field.widget.attrs['placeholder']
        self.assertEqual(placeholder, placeholder_get)

    @parameterized.expand([
        ('username', 'Obrigatório. 150 caracteres ou menos. '
         'Letras, números e @/./+/-/_ apenas.'),

    ])
    def test_fields_help_text_is_correct(self, field, needed):
        form = RegisterForm()
        current = form[field].field.help_text
        self.assertEqual(current, needed)

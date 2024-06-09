from django.test import TestCase
from applications.users.forms import UserRegisterForm
from datetime import datetime
from django.urls import  reverse,reverse_lazy
from applications.users.views import UserRegisterView



class TestViewRegister(TestCase):



    def setUp(self):
        
        pass

    def test_user_register_view(self):
        
        fecha = datetime.now()
        form_data = {
            'password1': '1234',
            'password2': '1234',
            "full_name":"yamil ferrufino",
            'email': 'yferru.9259@gmail.com',
            "dni": "38994623",
            "genero":"M",
            "celular":"1141619772"

        }
        form = UserRegisterForm(data=form_data)
        flag = form.is_valid()
        # Crear una instancia de la vista
        view = UserRegisterView()
        
        # Llamar al método form_valid
        response = view.form_valid(form)

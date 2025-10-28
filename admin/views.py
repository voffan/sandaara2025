from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView


class UserView(ModelView):
    form_base_class = SecureForm
    can_view_details = True
    column_list = (
        'id',
        'fullname',
        'nickname',
        'email',
        'address'
        )
    form_columns = [
        'fullname',
        'nickname',
        'email',
        'address',
        'password'
    ]
    column_details_list = (
        'id',
        'fullname',
        'nickname',
        'email',
        'address',
        'password',
        'pets',
        'user_donates'
        )


class PetView(ModelView):
    form_base_class = SecureForm
    can_view_details = True
    form_columns=[
        'name',
        'species',
        'needed',
        'owner'
    ]
    column_details_list = (
        'id',
        'name',
        'species',
        'owner',
        'needed',
        'balance',
        'pet_donates'
        )
    column_list = (
        'id',
        'name',
        'species',
        'owner',
        'needed',
        'balance'
        )


class DonateView(ModelView):
    form_base_class = SecureForm
    can_create = False

class SpeciesView(ModelView):
    form_base_class = SecureForm
    can_view_details = True
    form_columns = ['name']
    column_list = ['name']
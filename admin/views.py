from flask_admin.form import SecureForm
from flask_admin.contrib.sqla import ModelView
from flask_login import current_user
from flask import redirect, url_for


class AdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('login'))


class UserView(AdminModelView):
    form_base_class = SecureForm
    can_view_details = True
    column_list = (
        'id',
        'fullname',
        'nickname',
        'email',
        'address',
        'is_admin'
        )
    form_columns = [
        'fullname',
        'nickname',
        'email',
        'address',
        'password',
        'is_admin'
    ]
    column_details_list = (
        'id',
        'fullname',
        'nickname',
        'email',
        'address',
        'password',
        'pets',
        'user_donates',
        'is_admin'
        )


class PetView(AdminModelView):
    form_base_class = SecureForm
    can_view_details = True
    form_columns=[
        'name',
        'species',
        'needed',
        'owner',
        'file'
    ]
    column_details_list = (
        'id',
        'name',
        'species',
        'owner',
        'file',
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
        'balance',
        'file'
        )


class DonateView(AdminModelView):
    form_base_class = SecureForm
    can_create = False

class SpeciesView(AdminModelView):
    form_base_class = SecureForm
    can_view_details = True
    form_columns = ['name']
    column_list = ['name']
from flask import Flask, redirect, request, url_for
from config import Configuration
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import SQLAlchemyUserDatastore, Security, current_user


app = Flask(__name__)
app.config.from_object(Configuration)


db = SQLAlchemy(app)


# ADMIN панель

from models import *


class AdminMixin:
    def is_accessible(self):
        return current_user.has_role('admin')


    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('security.login', next = request.url))


class BaseModelView(ModelView):
    def on_model_change(self, form, model, is_created):
        model.generate_slug()
        return super(BaseModelView, self).on_model_change(form, model, is_created)


class AdminView(AdminMixin, ModelView):
    pass


class HomeAdminView(AdminMixin, AdminIndexView):
    pass


class ServiceAdminView(AdminMixin, BaseModelView):
    form_columns = ['img_link', 'service_title_de', 'service_intro_de', 'service_text_de','service_title_en',
    'service_intro_en', 'service_text_en', 'service_title_ru', 'service_intro_ru', 'service_text_ru']


class AboutAdminView(AdminMixin, BaseModelView):
    form_columns = ['img_link', 'about_heading_de','about_text_de', 'about_heading_en', 'about_text_en', 
    'about_heading_ru', 'about_text_ru']


class ContactAdminView(AdminMixin, BaseModelView):
    form_columns = [ 'link', 'fa_link', 'contacts_text_de', 'contacts_text_en', 'contacts_text_ru']


admin = Admin(app, 'BMKA', url = '/', index_view= HomeAdminView(name = 'Home'))
admin.add_view(ServiceAdminView(Service, db.session))
admin.add_view(AboutAdminView(About, db.session))
admin.add_view(ContactAdminView(Contacts, db.session))


# Flask - security

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

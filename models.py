from app import db
import re
from flask_security import UserMixin, RoleMixin


def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)


class Service(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))
    service_title_de = db.Column(db.String(50), nullable = False)
    service_intro_de = db.Column(db.String(255))
    service_text_de = db.Column(db.Text)
    service_title_en = db.Column(db.String(50), nullable = False)
    service_intro_en = db.Column(db.String(255))
    service_text_en = db.Column(db.Text)
    service_title_ru = db.Column(db.String(50), nullable = False)
    service_intro_ru = db.Column(db.String(255))
    service_text_ru = db.Column(db.Text)
    slug = db.Column(db.String(50), unique = True)


    def __init__(self, *args, **kwargs):
        super(Service, self).__init__(*args, **kwargs)
        self.generate_slug()


    def generate_slug(self):
        if self.service_title_en:
            self.slug = slugify(self.service_title_en)


class About(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))
    about_heading_de = db.Column(db.String(50))
    about_text_de = db.Column(db.Text)
    about_heading_en = db.Column(db.String(50))
    about_text_en = db.Column(db.Text)
    about_heading_ru = db.Column(db.String(50))
    about_text_ru = db.Column(db.Text)


class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    fa_link = db.Column(db.String(30))
    link = db.Column(db.String(255), nullable = False)
    contacts_text_de = db.Column(db.String(255))
    contacts_text_en = db.Column(db.String(255))
    contacts_text_ru = db.Column(db.String(255))


class CargoTransport(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))
    cargo_title_de = db.Column(db.String(255))
    cargo_amount_de = db.Column(db.String(255))
    cargo_title_en = db.Column(db.String(255))
    cargo_amount_en = db.Column(db.String(255))
    cargo_title_ru = db.Column(db.String(255))
    cargo_amount_ru = db.Column(db.String(255))


class PeopleTransport(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))
    transport_title_de = db.Column(db.String(255))
    transport_title_en = db.Column(db.String(255))
    transport_title_ru = db.Column(db.String(255))


class TechGadgets(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))



class HomeItems(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img_link = db.Column(db.String(255))


# Flask - security

roles_users = db.Table('roles_users',
    db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
    db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
)


class User (db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key = True)
    email = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role', secondary = roles_users, backref = db.backref('users', lazy = 'dynamic'))


class Role (db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key = True)
    name = db.Column(db.String(64), unique = True)
    description = db.Column(db.String(255))
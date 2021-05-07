from wtforms import Form, StringField, TextAreaField
from wtforms.validators import DataRequired

class ServiceForm (Form):
    img_link = StringField("Ссылка на картинку: ")

    service_title_de = StringField("Заголовок (на немецком)*: ", validators = [DataRequired()])
    service_intro_de = StringField("Вступительный текст (на немецком): ")
    service_text_de = TextAreaField("Текст (на немецком): ")
    
    service_title_en = StringField("Заголовок (на английском)*: ", validators = [DataRequired()])
    service_intro_en = StringField("Вступительный текст (на английском): ")
    service_text_en = TextAreaField("Текст (на английском): ")
    
    service_title_ru = StringField("Заголовок (на русском)*: ", validators = [DataRequired()])
    service_intro_ru = StringField("Вступительный текст (на русском): ")
    service_text_ru = TextAreaField("Текст (на русском): ")


class AboutForm (Form):
    img_link = StringField("Ссылка на картинку: ")

    about_heading_de = StringField("Заголовок (на немецком): ")
    about_text_de = TextAreaField("Текст (на немецком): ")

    about_heading_en = StringField("Заголовок (на английском): ")
    about_text_en = TextAreaField("Текст (на английском): ")

    about_heading_ru = StringField("Заголовок (на русском): ")
    about_text_ru = TextAreaField("Текст (на русском): ")


class ContactForm (Form):
    link = StringField("Ссылка для контакта*: ", validators = [DataRequired()])

    fa_link = StringField("fa-ссылка **  ***")

    contacts_text_de = StringField("Текст контакта (на немецком): ")
    contacts_text_en = StringField("Текст контакта (на английском): ")
    contacts_text_ru = StringField("Текст контакта (на русском): ")
    

class CargoForm (Form):
    img_link = StringField("Ссылка на картинку: ")

    cargo_title_de = StringField("Заголовок услуги (на немецком): ")
    cargo_amount_de = StringField("Диапазон (на немецком): ")

    cargo_title_en = StringField("Заголовок услуги (на английском): ")
    cargo_amount_en = StringField("Диапазон (на английском): ")

    cargo_title_ru = StringField("Заголовок услуги (на русском): ")
    cargo_amount_ru = StringField("Диапазон (на русском): ")


class PeopleForm (Form):
    img_link = StringField("Ссылка на картинку: ")

    transport_title_de = StringField("Заголовок услуги (на немецком): ")

    transport_title_en = StringField("Заголовок услуги (на английском): ")

    transport_title_ru = StringField("Заголовок услуги (на русском): ")



class TechGadgetForm (Form):
    img_link = StringField("Ссылка на картинку: ")


class HomeItemForm (Form):
    img_link = StringField("Ссылка на картинку: ")

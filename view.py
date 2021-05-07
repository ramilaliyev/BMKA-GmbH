from flask import render_template, url_for, request, redirect
from app import app, db
from models import Service, About, Contacts, CargoTransport, TechGadgets, HomeItems, PeopleTransport
from forms import ServiceForm, AboutForm, ContactForm, CargoForm, TechGadgetForm, HomeItemForm, PeopleForm
from flask_security import login_required


@app.route('/create-service', methods = ['POST','GET'])
@login_required
def create_service():
    if request.method == "POST":
        img_link = request.form['img_link']

        service_title_de = request.form['service_title_de']
        service_intro_de = request.form['service_intro_de']
        service_text_de = request.form['service_text_de']

        service_title_en = request.form['service_title_en']
        service_intro_en = request.form['service_intro_en']
        service_text_en = request.form['service_text_en']

        service_title_ru = request.form['service_title_ru']
        service_intro_ru = request.form['service_intro_ru']
        service_text_ru = request.form['service_text_ru']


        try:
            service = Service(img_link = img_link, service_title_de = service_title_de, service_intro_de = service_intro_de, service_text_de = service_text_de, service_title_en = service_title_en, service_intro_en = service_intro_en, service_text_en = service_text_en, service_title_ru = service_title_ru, service_intro_ru = service_intro_ru, service_text_ru = service_text_ru)
            db.session.add(service)
            db.session.commit()


        except:
            print ("Ошибка")


        return redirect(url_for('services_ru'))

    
    form = ServiceForm()
    return render_template('create_service.html', form = form)


@app.route('/create-about', methods = ['POST', 'GET'])
@login_required
def create_about():
    if request.method == "POST":
        img_link = request.form['img_link']

        about_heading_de = request.form['about_heading_de']
        about_text_de = request.form['about_text_de']

        about_heading_en = request.form['about_heading_en']
        about_text_en = request.form['about_text_en']

        about_heading_ru = request.form['about_heading_ru']
        about_text_ru = request.form['about_text_ru']


        try:
            about =  About (img_link = img_link, about_heading_de = about_heading_de, about_text_de = about_text_de, about_heading_en = about_heading_en, about_text_en = about_text_en, about_heading_ru = about_heading_ru, about_text_ru = about_text_ru)
            db.session.add(about)
            db.session.commit()


        except:
            print ("Ошибка")

        return redirect(url_for('about_ru'))

    
    form = AboutForm()
    return render_template('create_about.html', form = form)


@app.route('/create-contact', methods = ['GET', 'POST'])
@login_required
def create_contact():
    if request.method == "POST":
        fa_link = request.form['fa_link']

        link = request.form['link']

        contacts_text_de = request.form['contacts_text_de']

        contacts_text_en = request.form['contacts_text_en']

        contacts_text_ru = request.form['contacts_text_ru']


        try:
            contact = Contacts(link = link, fa_link = fa_link, contacts_text_de = contacts_text_de, contacts_text_en = contacts_text_en, contacts_text_ru = contacts_text_ru)
            db.session.add(contact)
            db.session.commit()


        except:
            print("Ошибка")

        
        return redirect(url_for('contacts_ru'))


    form = ContactForm()
    return render_template('create_contact.html', form = form)


@app.route('/create-cargo-service/', methods = ['GET', 'POST'])
@login_required
def create_cargo_service():
    if request.method == "POST":
        img_link = request.form['img_link']

        cargo_title_de = request.form['cargo_title_de']
        cargo_amount_de = request.form['cargo_amount_de']

        cargo_title_en = request.form['cargo_title_en']
        cargo_amount_en = request.form['cargo_amount_en']
        
        cargo_title_ru = request.form['cargo_title_ru']
        cargo_amount_ru = request.form['cargo_amount_ru']


        try:
            cargo = CargoTransport(img_link = img_link, cargo_title_de = cargo_title_de, cargo_amount_de = cargo_amount_de,  cargo_title_en = cargo_title_en, cargo_amount_en = cargo_amount_en,  cargo_title_ru = cargo_title_ru, cargo_amount_ru = cargo_amount_ru)
            db.session.add(cargo)
            db.session.commit()


        except:
            print ("Ошибка")


        return redirect(url_for('services_ru'))


    form = CargoForm()
    return render_template('create_cargo.html', form = form)


@app.route('/create-people-service/', methods = ['GET', 'POST'])
@login_required
def create_people_service():
    if request.method == "POST":
        img_link = request.form['img_link']

        transport_title_de = request.form['transport_title_de']

        transport_title_en = request.form['transport_title_en']

        transport_title_ru = request.form['transport_title_ru']


        try:
            transport = PeopleTransport(img_link = img_link, transport_title_de = transport_title_de, transport_title_en = transport_title_en, transport_title_ru = transport_title_ru)
            db.session.add(transport)
            db.session.commit()


        except:
            print("Ошибка")

        return redirect(url_for('services_ru'))


    form = PeopleForm()
    return render_template('create_people_service.html', form = form)

        


@app.route('/create-tech-gadget/', methods = ['GET', 'POST'])
@login_required
def create_tech_gadget():
    if request.method == "POST":
        img_link = request.form['img_link']


        try:
            tg = TechGadgets(img_link = img_link,)
            db.session.add(tg)
            db.session.commit()


        except:
            print ("Ошибка")


        return redirect(url_for('services_ru'))

    
    form = TechGadgetForm()
    return render_template('create_tg.html', form = form)


@app.route('/create-home-item/', methods = ['GET', 'POST'])
@login_required
def create_home_item():
    if request.method == "POST":
        img_link = request.form['img_link']


        try:
            hi = HomeItems(img_link = img_link,)
            db.session.add(hi)
            db.session.commit()


        except:
            print ("Ошибка")


        return redirect(url_for('services_ru'))

    
    form = HomeItemForm()
    return render_template('create_hi.html', form = form)

@app.route('/')
def index_de():
    services = Service.query.all()
    return render_template('index_de.html', services = services)


@app.route('/en/')
def index_en():
    services = Service.query.all()
    return render_template('index_en.html', services = services)


@app.route('/ru/')
def index_ru():
    services = Service.query.all()
    return render_template('index_ru.html', services = services)


@app.route('/services/')
def services_de():    
    services = Service.query.all()
    return render_template('services_de.html', services=services)
    

@app.route('/en/services/')
def services_en():
    services = Service.query.all()
    return render_template('services_en.html', services = services)
    

@app.route('/ru/services/')
def services_ru():
    services = Service.query.all()
    return render_template('services_ru.html', services = services)


@app.route('/services/<slug>/')
def service_detail_de(slug):
    service = Service.query.filter(Service.slug == slug).first()
    cargo = CargoTransport.query.all()
    people = PeopleTransport.query.all()
    tech_gadgets = TechGadgets.query.all()
    home_items = HomeItems.query.all()
    return render_template('service_detail_de.html', service = service, cargo = cargo, people = people, tech_gadgets = tech_gadgets, home_items = home_items)


@app.route('/en/services/<slug>/')
def service_detail_en(slug):
    service = Service.query.filter(Service.slug == slug).first()
    cargo = CargoTransport.query.all()
    people = PeopleTransport.query.all()
    tech_gadgets = TechGadgets.query.all()
    home_items = HomeItems.query.all()
    return render_template('service_detail_en.html', service = service, cargo = cargo, people = people, tech_gadgets = tech_gadgets, home_items = home_items)


@app.route('/ru/services/<slug>/')
def service_detail_ru(slug):
    service = Service.query.filter(Service.slug == slug).first()
    cargo = CargoTransport.query.all()
    people = PeopleTransport.query.all()
    tech_gadgets = TechGadgets.query.all()
    home_items = HomeItems.query.all()
    return render_template('service_detail_ru.html', service = service, cargo = cargo, people = people, tech_gadgets = tech_gadgets, home_items = home_items)


@app.route('/services/<slug>/edit', methods = ['GET',  'POST'])
def service_edit(slug):
    service = Service.query.filter(Service.slug == slug).first()


    if request.method == 'POST':
        form = ServiceForm(formdata= request.form, obj = service)
        form.populate_obj(service)
        db.session.commit()
        return redirect(url_for('services_de', slug = service.slug))


    form = ServiceForm(obj=service)
    return render_template('service_edit.html', service = service, form = form)

      
@app.route('/services/<slug>/del')
def service_delete(slug):
    service = Service.query.filter(Service.slug == slug).first()


    try:
        db.session.delete(service)
        db.session.commit()
        return redirect('/ru/services')


    except:
        return render_template('404.html')


@app.route('/services/Cargo-transportation/<int:id>/edit', methods = ['GET', 'POST'])
def cargo_edit(id):
    cargo = CargoTransport.query.filter(CargoTransport.id == id).first()

    if request.method == 'POST':
        form = CargoForm(formdata = request.form, obj = cargo)
        form.populate_obj(cargo)
        db.session.commit()
        return redirect('/ru/services/Cargo-transportation/')


    form = CargoForm(obj = cargo)
    return render_template('cargo_edit.html', cargo = cargo, form = form)



@app.route('/services/Cargo-transportation/<int:id>/del')
def cargo_delete(id):
    cargo = CargoTransport.query.filter(CargoTransport.id == id).first()


    try:
        db.session.delete(cargo)
        db.session.commit()
        return redirect('/ru/services/Cargo-transportation/')


    except:
        return render_template('404.html')


@app.route('/services/People-transportation/<int:id>/edit', methods = ['GET', 'POST'])
def people_edit(id):
    people = PeopleTransport.query.filter(PeopleTransport.id == id).first()

    if request.method == 'POST':
        form = PeopleForm(formdata = request.form, obj = people)
        form.populate_obj(people)
        db.session.commit()
        return redirect('/ru/services/People-transportation/')


    form = PeopleForm(obj = people)
    return render_template('people_edit.html', people = people, form = form)



@app.route('/services/People-transportation/<int:id>/del')
def people_delete(id):
    people = PeopleTransport.query.filter(PeopleTransport.id == id).first()


    try:
        db.session.delete(people)
        db.session.commit()
        return redirect('/ru/services/People-transportation/')


    except:
        return render_template('404.html')


@app.route('/services/Purchase-and-sale-of-goods/tech-gadgets/<int:id>/del')
def gadget_delete(id):
    tech_gadgets = TechGadgets.query.filter(TechGadgets.id == id).first()


    try:
        db.session.delete(tech_gadgets)
        db.session.commit()
        return redirect('/ru/services/Purchase-and-sale-of-goods/')


    except:
        return render_template('404.html')


@app.route('/services/Purchase-and-sale-of-goods/home-items/<int:id>/del')
def dom_delete(id):
    home_items = HomeItems.query.filter(HomeItems.id == id).first()


    try:
        db.session.delete(home_items)
        db.session.commit()
        return redirect('/ru/services/Purchase-and-sale-of-goods/')


    except:
        return render_template('404.html')


@app.route('/about-us/')
def about_de():
    about = About.query.all()
    return render_template('about_de.html', about = about)


@app.route('/en/about/')
def about_en():
    about = About.query.all()
    return render_template('about_en.html', about = about)


@app.route('/ru/about/')
def about_ru():
    about = About.query.all()
    return render_template('about_ru.html', about = about)


@app.route('/about/<int:id>/edit', methods = ['GET',  'POST'])
@app.route('/about-us/<int:id>/edit', methods = ['GET',  'POST'])
def about_edit(id):
    about = About.query.filter(About.id == id).first()


    if request.method == 'POST':
        form = AboutForm(formdata= request.form, obj = about)
        form.populate_obj(about)
        db.session.commit()
        return redirect(url_for('about_de', id = about.id))


    form = AboutForm(obj=about)
    return render_template('about_edit.html', about = about, form = form)


@app.route('/about-us/<int:id>/del')
def about_delete_de(id):
    about = About.query.filter(About.id == id).first()

    
    try:
        db.session.delete(about)
        db.session.commit()
        return redirect('/about-us')


    except:
        return render_template('404.html')


@app.route('/contact-us/')
def contacts_de():
    contacts = Contacts.query.all()
    return render_template('contacts_de.html', contacts = contacts)


@app.route('/en/contacts/')
def contacts_en():
    contacts = Contacts.query.all()
    return render_template('contacts_en.html', contacts = contacts)


@app.route('/ru/contacts/')
def contacts_ru():
    contacts = Contacts.query.all()
    return render_template('contacts_ru.html', contacts = contacts)


@app.route('/contact-us/<int:id>/edit', methods = ['GET',  'POST'])
@app.route('/contacts/<int:id>/edit', methods = ['GET',  'POST'])
def contact_edit(id):
    contact = Contacts.query.filter(Contacts.id == id).first()


    if request.method == 'POST':
        form = ContactForm(formdata= request.form, obj = contact)
        form.populate_obj(contact)
        db.session.commit()
        return redirect(url_for('contacts_de', id = contact.id))


    form = ContactForm(obj=contact)
    return render_template('contacts_edit.html', contact = contact, form = form)


@app.route('/contacts/<int:id>/del')
def contact_delete_de(id):
    contacts = Contacts.query.filter(Contacts.id == id).first()
    
    try:
        db.session.delete(contacts)
        db.session.commit()
        return redirect('/contact-us')


    except:
        return render_template('404.html')


@app.route('/rights')
def rights():
    return render_template ('rights.html')


@app.route('/privacy')
def privacy_de():
    return render_template ('privacy_de.html')


@app.route('/en/privacy')
def privacy_en():
    return render_template ('privacy_en.html')


@app.route('/ru/privacy')
def privacy_ru():
    return render_template ('privacy_ru.html')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
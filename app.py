import os
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///itplus.db'
app.secret_key = "itplus112"
db = SQLAlchemy(app)

class Design(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(64), unique=False, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Image: {self.image}"
    
class Ecommerce(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(64), unique=False, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Image: {self.image}"

class Booking(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(64), unique=False, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Image: {self.image}"

class Social(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(64), unique=False, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Image: {self.image}"
    
class Apps(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    image = db.Column(db.String(64), unique=False, nullable=False)
    link = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"Name : {self.name}, Image: {self.image}"
    
class Home(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(64), unique=False, nullable=False)

    def __repr__(self):
        return f"Text : {self.text}"

@app.route('/design_delete/<int:id>', methods=['POST'])
def design_delete(id):
    design = Design.query.get_or_404(id)
    db.session.delete(design)
    db.session.commit()
    flash(f"Page '{design.name}' has been deleted.", "success")

    return redirect(url_for('design'))

@app.route('/eco_delete/<int:id>', methods=['POST'])
def eco_delete(id):
    ecommerce = Ecommerce.query.get_or_404(id)
    db.session.delete(ecommerce)
    db.session.commit()
    flash(f"Page '{ecommerce.name}' has been deleted.", "success")
    return redirect(url_for('eco'))

@app.route('/app_delete/<int:id>', methods=['POST'])
def app_delete(id):
    apps = Apps.query.get_or_404(id)
    db.session.delete(apps)
    db.session.commit()
    flash(f"Page '{apps.name}' has been deleted.", "success")
    return redirect(url_for('apps'))

@app.route('/social_delete/<int:id>', methods=['POST'])
def social_delete(id):
    social = Social.query.get_or_404(id)
    db.session.delete(social)
    db.session.commit()
    flash(f"Page '{social.name}' has been deleted.", "success")

    return redirect(url_for('social'))
@app.route('/home_delete/<int:id>', methods=['POST'])
def home_delete(id):
    home = Home.query.get_or_404(id)
    db.session.delete(home)
    db.session.commit()
    flash(f"Page '{home.name}' has been deleted.", "success")
    return redirect(url_for('home'))

@app.route('/book_delete/<int:id>', methods=['POST'])
def book_delete(id):
    booking = Booking.query.get_or_404(id)
    db.session.delete(booking)
    db.session.commit()
    flash(f"Page '{booking.name}' has been deleted.", "success")
    return redirect(url_for('book'))

@app.route('/design_edit/<int:id>', methods=['POST'])
def design_edit(id):
    design = Design.query.get_or_404(id)

    # Update the fields from the form
    design.name = request.form['name']
    design.link = request.form['link']

    # Handle the optional image update
    if 'image' in request.files:
        image = request.files['image']
        if image.filename:
            # Save new image
            upload_folder = os.path.join(app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)
            design.image = f"static/uploads/{image.filename}"

    db.session.commit()
    flash(f"Page '{design.name}' has been updated successfully.", "success")
    return redirect(url_for('design'))


@app.route('/home_edit/<int:id>', methods=['GET', 'POST'])
def home_edit(id):
    home = Home.query.get_or_404(id)
    if request.method == 'POST':
        home.name = request.form['name']
        db.session.commit()
        flash(f"Page '{home.name}' has been updated.", "success")
        return redirect(url_for('view_entries'))
    return render_template('edit_page.html', design=design)
    
@app.route('/ecommerce_edit/<int:id>', methods=['POST'])
def ecommerce_edit(id):
    ecommerce = Ecommerce.query.get_or_404(id)

    # Update the fields from the form
    ecommerce.name = request.form['name']
    ecommerce.link = request.form['link']

    # Handle the optional image update
    if 'image' in request.files:
        image = request.files['image']
        if image.filename:
            # Save new image
            upload_folder = os.path.join(app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)
            ecommerce.image = f"static/uploads/{image.filename}"

    db.session.commit()
    flash(f"Page '{ecommerce.name}' has been updated successfully.", "success")
    return redirect(url_for('eco'))


@app.route('/app_edit/<int:id>', methods=['POST'])
def app_edit(id):
    apps = Apps.query.get_or_404(id)

    # Update the fields from the form
    apps.name = request.form['name']
    apps.link = request.form['link']

    # Handle the optional image update
    if 'image' in request.files:
        image = request.files['image']
        if image.filename:
            # Save new image
            upload_folder = os.path.join(app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)
            apps.image = f"static/uploads/{image.filename}"

    db.session.commit()
    flash(f"Page '{apps.name}' has been updated successfully.", "success")
    return redirect(url_for('apps'))

@app.route('/book_edit/<int:id>', methods=['POST'])
def book_edit(id):
    booking = Booking.query.get_or_404(id)

    # Update the fields from the form
    booking.name = request.form['name']
    booking.link = request.form['link']

    # Handle the optional image update
    if 'image' in request.files:
        image = request.files['image']
        if image.filename:
            # Save new image
            upload_folder = os.path.join(app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)
            booking.image = f"static/uploads/{image.filename}"

    db.session.commit()
    flash(f"Page '{booking.name}' has been updated successfully.", "success")
    return redirect(url_for('book'))


@app.route('/social_edit/<int:id>', methods=['POST'])
def social_edit(id):
    social = Social.query.get_or_404(id)

    # Update the fields from the form
    social.name = request.form['name']
    social.link = request.form['link']

    # Handle the optional image update
    if 'image' in request.files:
        image = request.files['image']
        if image.filename:
            # Save new image
            upload_folder = os.path.join(app.root_path, 'static/uploads')
            os.makedirs(upload_folder, exist_ok=True)
            image_path = os.path.join(upload_folder, image.filename)
            image.save(image_path)
            social.image = f"static/uploads/{image.filename}"

    db.session.commit()
    flash(f"Page '{social.name}' has been updated successfully.", "success")
    return redirect(url_for('social'))


@app.route('/')
def home():
   design = Design.query.all()
   apps = Apps.query.all()
   ecos = Ecommerce.query.all()
   books = Booking.query.all()
   social = Social.query.all()
   home = Home.query.all()
   return render_template('index.html', design=design, apps=apps, ecos=ecos,  books=books, socials=social, homes=home)

@app.route("/design")
def design():
   
   design = Design.query.all()
   return render_template('design.html', design=design)

@app.route("/home_view")
def home_view():
   
   home = Home.query.all()
   return render_template('home_view.html', homes=home)

@app.route("/app")
def apps():
   
   apps = Apps.query.all()
   return render_template('app.html', apps=apps)

@app.route("/eco")
def eco():
   
   ecos = Ecommerce.query.all()
   return render_template('eco.html', ecos=ecos)

@app.route("/book")
def book():
   
   books = Booking.query.all()
   return render_template('booking.html', books=books)

@app.route("/social")
def social():
   
   social = Social.query.all()
   return render_template('social.html', socials=social)

@app.route("/design_form", methods=['POST', 'GET'])
def design_form():
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        image = request.files.get('image')

        if not name or not link or not image:
            flash("All fields are required.", "danger")
            return redirect(url_for('design_form'))

        # Save the image to a static/uploads folder
        upload_folder = os.path.join(app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)  # Save the image to the server

        # Save data to the database
        design = Design(name=name, link=link, image=f"static/uploads/{image.filename}")
        db.session.add(design)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('design_form'))

    return render_template('design_form.html')

@app.route("/eco_form", methods=['POST', 'GET'])
def eco_form():
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        image = request.files.get('image')

        if not name or not link or not image:
            flash("All fields are required.", "danger")
            return redirect(url_for('eco_form'))

        # Save the image to a static/uploads folder
        upload_folder = os.path.join(app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)  # Save the image to the server

        # Save data to the database
        eco = Ecommerce(name=name, link=link, image=f"static/uploads/{image.filename}")
        db.session.add(eco)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('eco_form'))

    return render_template('eco_form.html')

@app.route("/book_form", methods=['POST', 'GET'])
def book_form():
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        image = request.files.get('image')

        if not name or not link or not image:
            flash("All fields are required.", "danger")
            return redirect(url_for('book_form'))

        # Save the image to a static/uploads folder
        upload_folder = os.path.join(app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)  # Save the image to the server

        # Save data to the database
        book = Booking(name=name, link=link, image=f"static/uploads/{image.filename}")
        db.session.add(book)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('book_form'))

    return render_template('booking_form.html')

@app.route("/app_form", methods=['POST', 'GET'])
def app_form():
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        image = request.files.get('image')

        if not name or not link or not image:
            flash("All fields are required.", "danger")
            return redirect(url_for('app_form'))

        # Save the image to a static/uploads folder
        upload_folder = os.path.join(app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)  # Save the image to the server

        # Save data to the database
        apps = Apps(name=name, link=link, image=f"static/uploads/{image.filename}")
        db.session.add(apps)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('app_form'))

    return render_template('app_form.html')

@app.route("/social_form", methods=['POST', 'GET'])
def social_form():
    if request.method == 'POST':
        name = request.form.get('name')
        link = request.form.get('link')
        image = request.files.get('image')

        if not name or not link or not image:
            flash("All fields are required.", "danger")
            return redirect(url_for('social_form'))

        # Save the image to a static/uploads folder
        upload_folder = os.path.join(app.root_path, 'static/uploads')
        os.makedirs(upload_folder, exist_ok=True)
        image_path = os.path.join(upload_folder, image.filename)
        image.save(image_path)  # Save the image to the server

        # Save data to the database
        social = Social(name=name, link=link, image=f"static/uploads/{image.filename}")
        db.session.add(social)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('social_form'))

    return render_template('social_form.html')

@app.route("/home_form", methods=['POST', 'GET'])
def home_form():
    if request.method == 'POST':
        text = request.form.get('text')

        if not text:
            flash("All fields are required.", "danger")
            return redirect(url_for('home_form'))

        # Save data to the database
        home = Home(text=text)
        db.session.add(home)
        db.session.commit()

        flash("Page added successfully!", "success")
        return redirect(url_for('home_form'))

    return render_template('home_form.html')

if __name__ == '__main__':
   with app.app_context():
        db.create_all()
   app.run(debug=True)
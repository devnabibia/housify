from . import db
from datetime import date, time
from . import login_manager
from flask_login import UserMixin, current_user
from werkzeug.security import generate_password_hash,check_password_hash



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    '''
    '''
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    profile_pic_path = db.Column(db.String())
    contact = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    pass_secure = db.Column(db.String(255))
    listing = db.relationship('Listing', backref = 'user', lazy = 'dynamic')
    booking = db.relationship('Booking', backref = 'user', lazy = 'dynamic')

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'


class Listing(db.Model):
    '''
    '''


    __tablename__ = 'listings'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    location = db.Column(db.String(255))
    description = db.Column(db.String(255))
    category = db.Column(db.String(255))
    bedrooms = db.Column(db.String(255))
    pricing = db.Column(db.Integer)
    featured_pic_path = db.Column(db.String())
    lister_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
    image  = db.relationship('Image', backref = 'listing', lazy = 'dynamic')
    timeslot = db.relationship('Timeslot', backref = 'listing', lazy = 'dynamic')
    booking = db.relationship('Booking', backref = 'listing', lazy = 'dynamic')



    @classmethod
    def get_all_listings(cls):
        listings = Listing.query.order_by('id').all()
        return listings

    def save_listing(self):
        db.session.add(self)
        db.session.commit()



    def __repr__(self):
        return f'Listing : id : {self.id}'



class Image(db.Model):
    '''
    '''

    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255))
    image_path = db.Column(db.String)
    listing_id = db.Column(db.Integer, db.ForeignKey("listings.id"))


    @classmethod
    def get_all_images(cls):
        images = Image.query.order_by('id').all()
        return images


class Timeslot(db.Model):
    '''
    '''

    __tablename__ = 'timeslots'

    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.Date)
    start_time = db.Column(db.Time)
    end_time = db.Column(db.Time)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    booking = db.relationship('Booking', backref = 'timeslot', lazy = 'dynamic')



    @classmethod
    def get_all_timeslots(cls):
        timeslots = Timeslot.query.order_by('id').all()
        return timeslots

    def save_timeslot(self):
        db.session.add(self)
        db.session.commit()


class Booking(db.Model):
    '''
    '''
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255))
    email = db.Column(db.String(255))
    contact = db.Column(db.Integer)
    listing_id = db.Column(db.Integer, db.ForeignKey('listings.id'))
    lister_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    timeslot_id = db.Column(db.Integer, db.ForeignKey('timeslots.id'), nullable = False)


    @classmethod
    def get_all_bookings(cls):
        bookings = Booking.query.order_by('id').all()
        return bookings

    def save_booking(self):
        db.session.add(self)
        db.session.commit()

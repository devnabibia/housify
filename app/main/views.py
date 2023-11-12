from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import Listing, User, Image, Timeslot, Booking
from .forms import ListingForm, BookingForm, UpdateProfile, TestForm
from flask_login import login_required, current_user
from .. import db, photos

# Views
@main.route('/', methods = ['GET', 'POST'])
def index():
    '''
    View home function that returns the home page
    '''
    apartment =  Listing.query.filter_by(category = 'apartment').all()
    bungalow = Listing.query.filter_by(category="bungalow").all()
    maisonette = Listing.query.filter_by(category="maisonete")
    listing = Listing.query.filter_by().all()



    title = 'Home | Boma Listing'
    return render_template('index.html', title = title, apartment = apartment, bungalow = bungalow, maisonette = maisonette, listing = listing)


@main.route('/user/<uname>')
@login_required
def profile(uname):
    '''
    View profile page function that returns the profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()

    title = f"{uname.capitalize()}'s Profile"

    get_all_listings = Listing.query.filter_by(lister_id=current_user.id).all()
    listing = Listing.query.filter_by(lister_id=current_user.id).all()
    bookings = Booking.query.filter_by(lister_id=current_user.id).all()


    if user is None:
        abort (404)

    return render_template("profile/profile.html", user = user, title=title, listings = get_all_listings, bookings=bookings)





@main.route('/listing/new',methods = ['GET','POST'])
@login_required
def listing():
    '''
    View listing function that returns the listing page and data
    '''


    list_form = ListingForm()

    if list_form.validate_on_submit():
        date = request.form.get("party-date"),
        start = request.form.get("party-time")
        stop = request.form.get("party-time2")

        new_listing = Listing( title=list_form.title.data, location=list_form.location.data, category = list_form.category.data, pricing = list_form.pricing.data, bedrooms = list_form.bedrooms.data, description = list_form.description.data,user = current_user)

        new_listing.save_listing()

        # new_timeslot = Timeslot (date = date, start_time = start, end_time = stop,listing_id=new_listing.id)
        # new_timeslot.save_timeslot()
        return redirect(url_for('main.listing_times',listing_id=new_listing.id))

    title = 'New Listing'
    return render_template('listing.html', list_form = list_form)


@main.route('/listing/<int:listing_id>/times',methods = ['GET','POST'])
@login_required
def listing_times(listing_id):
    '''
    View listing function that returns the listing page and data
    '''
    # if current_user.is_authenticated:
    listing = Listing.query.get(listing_id)


    if listing.user!= current_user:
        abort(403)

    list_form = TestForm()
    if list_form.validate_on_submit():
        date = request.form.get("party-date"),
        start = request.form.get("party-time")
        stop = request.form.get("party-time2")
        new_timeslot = Timeslot (date = date, start_time = start, end_time = stop,listing_id=listing.id)
        new_timeslot.save_timeslot()
        # return redirect(url_for('.listing_times', listing_id = listing_id))

    list = Listing.query.filter_by(id = listing_id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        list.featured_pic_path = path
        db.session.commit()
        # return redirect(url_for('main.index'))

    title = 'New Listing'
    return render_template('listing_times.html', list_form = list_form, listing=listing)






@main.route('/listing/<int:listing_id>')
def single_listing(listing_id):
    """View home function that returns the single listing page"""

    # booking_form = BookingForm()
    listing = Listing.query.get_or_404(listing_id)
    timeslots = Timeslot.query.filter_by(listing_id=listing.id).all()
    user = User.query.filter_by(id=listing.lister_id).first()


    # if booking_form.validate_on_submit():
    #     new_booking = Booking(name=booking_form.name.data, email=booking_form.email.data, contact=booking_form.contact.data, listing_id=listing.id, timeslot_id=timeslots.id)
    #     new_booking.save_booking()


    title = 'Home | Boma Listing'
    return render_template('single-listing.html', title = title, listing=listing, timeslots=timeslots, user=user)

@main.route('/listing/<int:listing_id>/book/<int:timeslot_id>',methods = ['GET','POST'])
def booktime(listing_id,timeslot_id):
    """View home function that returns the single listing page"""

    booking_form = BookingForm()
    # listing = Listing.query.get_or_404(listing_id)
    timeslots = Timeslot.query.filter_by(id=timeslot_id).all()
    listing = Listing.query.get_or_404(listing_id)
    user = User.query.filter_by(id=listing.lister_id).first()

    if booking_form.validate_on_submit():
        new_booking = Booking(name=booking_form.name.data, email=booking_form.email.data, contact=booking_form.contact.data, listing_id=listing_id, timeslot_id=timeslot_id, lister_id=user.id)
        new_booking.save_booking()
        return redirect(url_for('main.index'))

    title = 'Home | Boma Listing'
    return render_template('booking.html', title = title, booking_form = booking_form, listing=listing, timeslots=timeslots)











@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    '''
    View update profile page function that returns the update profile page and its data
    '''
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)



@main.route('/user/<uname>/update/pic',methods=['POST'])
@login_required
def update_pic(uname):
    '''
    View update pic profile function that returns the uppdate profile pic page
    '''
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile', uname=uname))







@main.route('/user/profile/booking/',methods = ['GET', 'POST'])
def booking():
    '''
    View booking function that returns the booking page and data
    '''
    get_all_bookings = Timeslot.query.filter_by(listing = listing.id).all()
    # booking_form = BookingForm()

    # if booking_form.validate_on_submit():
    #     new_booking = Booking(email=booking_form.email.data, name=booking_form.name.data, contact = booking_form.contact.data)
    #     new_booking.save_booking()


    return render_template('booking.html', booking = get_all_bookings)

from sqlalchemy import Column, String, Integer, Boolean, DateTime, ARRAY, ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
db = SQLAlchemy()


# TODO: connect to a local postgresql database
def db_setup(app):
    app.config.from_object('config')
    db.app = app
    db.init_app(app)
    migrate = Migrate(app, db)
    return db

#----------------------------------------------------------------------------#
# Models.
#----------------------------------------------------------------------------#

class Venue(db.Model):
    __tablename__ = 'Venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    address = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    description = db.Column(db.String(500))
    seeking_talent = db.Column(Boolean)
    website = db.Column(String(120))
    genres = db.Column(ARRAY(String))
    shows = db.relationship('Show', backref='Venue', lazy=True)

    def __init__(self, name, genres, city, state, address, phone, image_link, facebook_link, description = "", seeking_talent= False, website ):
        self.name = name
        self.genres = genres
        self.city = city
        self.state = state
        self.address = address
        self.phone = phone
        self.image_link = image_link
        self.facebook_link = facebook_link
        self.website = website
        self.description = description

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    
    def short(self):
        print(self)
        return{
            'id' = self.id,
            'name' = self.name
        }
    
    def long(self):
        print(self)
        return{
            'id' = self.id,
            'name' = self.name,
            'city' = self.city,
            'state' = self.state
        }
    
    def detail(self):
        return{
            'id' = self.id,
            'name' = self.name,
            'genres' = self.genres,
            'address' = self.address,
            'city' = self.city,
            'phone' = self.phone,
            'website' = self.website,
            'facebook_link'= self.facebook_link,
            'seeking_talent' = self.seeking_talent,
            'description' = self.description,
            'image-link' = self.image_link
        }


        


    # TODO: implement any missing fields, as a database migration using Flask-Migrate

class Artist(db.Model):
    __tablename__ = 'Artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    genres = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    facebook_link = db.Column(db.String(120))
    shows = db.relationship(Show, backref='Artist', lazy='dynamics')

    # TODO: implement any missing fields, as a database migration using Flask-Migrate

# TODO Implement Show and Artist models, and complete all model relationships and properties, as a database migration.

#show model
class Show(db.Model):

    __tablename__ = 'Show'
    id = db.Column(Integer,promary_key=True)
    venue_id = db.Column(Integer, ForeignKey(Venue.id), nullable=False)
    artist_id = db.Column(Integer, ForeignKey(Artist.id), nullable=False)
    start_time = db.Column(String(), nullable=False)


    def __init__(self, venue_id,artist_id,start_time):
        self.venue_id = venue_id
        self.artist_id = artist_id
        self.start_time = start_time

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def detail(self):
        return{
            'venue_id' = self.venue_id,
            'venue_name' = self.Venue.name,
            'artist_id' = self.artist_id,
            'artist_name' = self.Artist.name,
            'artist_image_link' = self.Artist.image_link,
            'start_time' = self.start_time
        }

    def artist_details(self):
        return{
            'artist_id' = self.venue_id,
            'artist_name' = self.Artist.name,
            'artist_image_link' = self.Artist.image_link,
            'start_time' = self.start_time

        }
 
    
    def venue_details(self):
        return{
            'venue_id' = self.venue_id,
            'venue_name' = self.Venue.name,
            'venue_image_link' = self.Venue.image_link,
            'start_time' = self.start_time
            
        }

        
  


 
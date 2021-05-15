from datetime import datetime
from analyzer import db, login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Hashtag(db.Model):

	__tablename__ = 'hashtag'
	id = db.Column(db.Integer, primary_key=True)
	hashtag = db.Column(db.String(64), index = False, unique=True, nullable= False)


	def __repr__(self):
		return f"Hashtag('{self.hashtag}')"

class Tweet(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    search_val = db.Column(db.String(64), nullable=False)
    classification_result = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.String(64), nullable=True)
    tweet_id = db.Column(db.String(64), nullable=True, index=True)
    text = db.Column(db.String(64), nullable=True)
    source = db.Column(db.String(64), nullable=True)
    in_reply_to_status_id = db.Column(db.String(64), nullable=True)
    in_reply_to_user_id = db.Column(db.String(64), nullable=True)
    in_reply_to_screen_name = db.Column(db.String(64), nullable=True)
    user_name = db.Column(db.String(64), nullable=True)
    user_screen_name = db.Column(db.String(64), nullable=True)
    user_location = db.Column(db.String(64), nullable=True)
    user_url = db.Column(db.String(64), nullable=True)
    user_description = db.Column(db.String(64), nullable=True)
    user_verified = db.Column(db.String(64), nullable=True)
    user_followers_count = db.Column(db.String(64), nullable=True)
    user_friends_count = db.Column(db.String(64), nullable=True)
    user_listed_count = db.Column(db.String(64), nullable=True)
    user_favourites_count = db.Column(db.String(64), nullable=True)
    user_created_at = db.Column(db.String(64), nullable=True)
    user_id = db.Column(db.String(64), nullable=True)
    user_profile_image_url_https = db.Column(db.String(64), nullable=True)
    coordinates_lat = db.Column(db.String(64), nullable=True)
    coordinates_lon = db.Column(db.String(64), nullable=True)
    place_country = db.Column(db.String(64), nullable=True)
    place_country_code = db.Column(db.String(64), nullable=True)
    place_full_name = db.Column(db.String(64), nullable=True)
    place_id = db.Column(db.String(64), nullable=True)
    place_type = db.Column(db.String(64), nullable=True)
    quoted_status_id = db.Column(db.String(64), nullable=True)
    quoted_status = db.Column(db.String(64), nullable=True)
    retweeted_status = db.Column(db.String(64), nullable=True)
    quote_count = db.Column(db.String(64), nullable=True)
    reply_count = db.Column(db.String(64), nullable=True)
    retweet_count = db.Column(db.String(64), nullable=True)
    favorite_count = db.Column(db.String(64), nullable=True)
    retweeted = db.Column(db.String(64), nullable=True)
    entities = db.Column(db.String(64), nullable=True)
    lang = db.Column(db.String(64), nullable=True)
    feeds_link = db.Column(db.String(64), nullable=True)
    feeds_video = db.Column(db.String(64), nullable=True)
    feeds_image = db.Column(db.String(64), nullable=True)


    def __repr__(self):
        return f"Hashtag('{self.text}')"
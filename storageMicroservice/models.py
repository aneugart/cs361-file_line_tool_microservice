from storageMicroservice import db


class date_keywords(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    date = db.Column(db.Date, index=True, unique=True)
    keyword = db.Column(db.String(1000), index=False)
from . import db

class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    title = db.Column(db.String(64), index=True)
    lessons = db.relationship('Lessons', backref='series')

    def __repr__(self):
        return '%r. %s' % (self.id, self.title)

class Lessons(db.Model):
    __tablename__ = 'lessons'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    title = db.Column(db.String(64), index=True)
    lecturer = db.Column(db.String(64), index=True)
    time = db.Column(db.DateTime)
    notes = db.relationship('Notes', backref='lesson')
    slides = db.relationship('Slides', backref='lesson')

    def __repr__(self):
        return '<Material %r>' % (self.topic)

class Notes(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    url = db.Column(db.String(200))
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))

class Slides(db.Model):
    __tablename__ = 'slides'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    url = db.Column(db.String(200))
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.id'))
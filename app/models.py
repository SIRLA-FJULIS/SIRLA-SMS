from . import db

class Series(db.Model):
    __tablename__ = 'series'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    name = db.Column(db.String(64), index=True)
    materials = db.relationship('Material', backref='series')

    def __repr__(self):
        return '%r. %s' % (self.id, self.name)

class Material(db.Model):
    __tablename__ = 'materials'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    topic = db.Column(db.String(64), index=True)
    series_id = db.Column(db.Integer, db.ForeignKey('series.id'))
    notes = db.relationship('Note', backref='material')
    slides = db.relationship('Slides', backref='material')

    def __repr__(self):
        return '<Material %r>' % (self.topic)

class Note(db.Model):
    __tablename__ = 'notes'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    url = db.Column(db.String(200), index=True)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))

class Slides(db.Model):
    __tablename__ = 'slides'
    id = db.Column(db.Integer, primary_key=True, unique=True, index=True)
    url = db.Column(db.String(200), index=True)
    material_id = db.Column(db.Integer, db.ForeignKey('materials.id'))
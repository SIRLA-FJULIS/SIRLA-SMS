from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.html5 import URLField
from wtforms.validators import DataRequired, url
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Series

class New_Material_Form(FlaskForm):
    series = QuerySelectField(
        "Series", 
        query_factory=lambda: Series.query.all(),
        validators=[DataRequired()]
    )
    note_url = URLField("Note URL", validators=[url()])
    slides_url = URLField("Slides URL", validators=[url()])

    submit = SubmitField("New")


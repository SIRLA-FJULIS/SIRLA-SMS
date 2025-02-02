from flask import render_template, redirect, url_for
from app.main.forms import New_Material_Form
from app.main import bp
from app.models import Lessons, Series
from app import db

@bp.route('/')
def index():
   return render_template("main/index.html")

@bp.route('/new_material', methods = ['GET', 'POST'])
def new_material():
      form = New_Material_Form()
      if form.validate_on_submit():
         series = form.series.data
         new_material = Lessons(series_id=series.id)
         note_url = form.note_url.data
         slides_url = form.slides_url.data
         db.session.add(new_material)
         db.session.commit()
         return redirect(url_for('main.new_material'))

      return render_template("main/new_material.html", form=form)

@bp.route('/material_list')
def material_list():
   materials = Lessons.query.all()
   
   return render_template('main/material_list.html', materials=materials)
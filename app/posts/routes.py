from flask import Blueprint, render_template, redirect, url_for, flash, abort, request
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PitchForm


posts = Blueprint('posts', __name__)

@posts.route('/pitch/new', methods=['GET', 'POST'])
@login_required
def new_pitch():
  form = PitchForm()
  if form.validate_on_submit():
    post = Post(title=form.title.data, content=form.content.data, author=current_user)
    db.session.add(post)
    db.session.commit()
    flash('Your pitch has been posted!', 'success')
    return redirect(url_for('main.index'))
  return render_template('create_pitch.html', title='New Pitch', form=form, legend='New Post')

@posts.route('/pitch/<int:pitch_id>')
def pitch(pitch_id):
  pitch = Post.query.get_or_404(pitch_id)
  return render_template('pitch.html', title=pitch.title, post=pitch)

@posts.route('/pitch/<int:pitch_id>/update', methods=['GET', 'POST'])
@login_required
def update_pitch(pitch_id):
  pitch = Post.query.get_or_404(pitch_id)
  if pitch.author != current_user:
    abort(403)
  form = PitchForm()
  if form.validate_on_submit():
    pitch.title = form.title.data
    pitch.content = form.content.data
    db.session.commit()
    flash('Your post has been updated', 'success')
    return redirect(url_for('posts.pitch', pitch_id=pitch_id))
  elif request.method == 'GET':
    form.title.data = pitch.title
    form.content.data = pitch.content
  return render_template('create_pitch.html', title='Update Pitch', form=form, legend='Update Post')

@posts.route('/pitch/<int:pitch_id>/delete', methods=['POST'])
@login_required
def delete_pitch(pitch_id):
  pitch = Post.query.get_or_404(pitch_id)
  if pitch.author != current_user:
    abort(403)
  db.session.delete(pitch)
  db.session.commit()
  flash('Your post has been deleted', 'success')
  return redirect(url_for('main.index'))






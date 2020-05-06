import unittest
from datetime import datetime
from app.models import Pitch, User, Comment
from app import db

class TestPitchModel(unittest.TestCase):

  def setUp(self):
    self.current_user = User(username = 'James', password = 'potato', email = 'james@ms.com')
    self.new_pitch = Pitch(title="cheesy", pub_date=datetime.utcnow, content="test pitch", category="product")
    self.new_comment = Comment(content = "nice post", pitch=self.new_pitch, date_posted=datetime.utcnow)

  def tearDown(self):
    db.session.delete(self)
    User.query.commit()

  def test_instance(self):
    self.assertTrue(isinstance(self.new_comment,Comment))

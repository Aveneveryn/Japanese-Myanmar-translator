from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Translation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    input_text = db.Column(db.Text, nullable=False)
    input_type = db.Column(db.String(20), default='text')
    result_mm = db.Column(db.Text)
    created_at = db.Column(db.DateTime, server_default=db.func.now())

class SavedWord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word_jp = db.Column(db.String(200), nullable=False)
    reading = db.Column(db.String(200))
    meanings_json = db.Column(db.Text)
    jlpt = db.Column(db.String(10))
    pos = db.Column(db.String(50))
    created_at = db.Column(db.DateTime, server_default=db.func.now())

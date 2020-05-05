from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    institution_name = db.Column(db.String, nullable=False)
    educational_level = db.Column(db.String, nullable=False)


class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key=True)
    experience_description = db.Column(db.Text, nullable=False)
    education_id = db.Column(db.Integer,
                             db.ForeignKey('education.id'),
                             nullable=True)

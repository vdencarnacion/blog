from application import db


class Education(db.Model):
    __tablename__ = 'education'
    id = db.Column(db.Integer, primary_key=True)
    institution_name = db.Column(db.String, nullable=False)
    educational_level = db.Column(db.String, nullable=False)

    def __init__(self, institution_name, educational_level):
        self.institution_name = institution_name
        self.educational_level = educational_level

    def __repr__(self):
        return f'id {self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'institution_name': self.institution_name,
            'educational_level': self.educational_level
        }


class Experience(db.Model):
    __tablename__ = 'experience'
    id = db.Column(db.Integer, primary_key=True)
    experience_description = db.Column(db.Text, nullable=False)
    education_id = db.Column(db.Integer,
                             db.ForeignKey('education.id'),
                             nullable=True)

    def __init__(self, experience_description, education_id):
        self.experience_description = experience_description
        self.education_id = education_id

    def __repr__(self):
        return f'id {self.id}'

    def serialize(self):
        return {
            'id': self.id,
            'experience_description': experience_description,
            'education_id', education_id
        }

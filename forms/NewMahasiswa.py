from wtforms.validators import InputRequired
from flask_wtf import FlaskForm
from wtforms import FileField, StringField
from flask_wtf.file import FileField, FileAllowed, FileRequired

class NewMahasiswa(FlaskForm):
    name = StringField('name',validators=[InputRequired()])
    npm = StringField('npm',validators=[InputRequired()])
    profile_picture = FileField("Profile Picture",validators=[
        FileRequired(), FileAllowed(["png","jpg"],"file Wajib JPG Atau PNG")
    ])
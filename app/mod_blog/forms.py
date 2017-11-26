from flask_wtf import Form
from wtforms import StringField,BooleanField,PasswordField,SubmitField,TextAreaField,SelectField,DateField,HiddenField
from wtforms.validators import DataRequired,Email,Length,EqualTo,optional
from app.mod_user.models import User,Blog


class BlogForm(Form):

	title = StringField('Title',validators=[DataRequired(),Length(1,128)])
	content =TextAreaField('Content',validators=[DataRequired()])
	publication_date = DateField('publicaion_date',format='%m/%d/%Y',validators=[optional()])
	submit = SubmitField('Post')

class CommentForm(Form):
	content=TextAreaField('Content',validators=[DataRequired()])
	parent_id = HiddenField("",validators=[optional()])
	submit = SubmitField('comment')

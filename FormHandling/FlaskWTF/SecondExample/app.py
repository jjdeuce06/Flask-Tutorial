from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField
from wtforms.validators import InputRequired, Length

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secret'

# Using StringField, PasswordField andSubmitField from Flask-WTForms library 
# for username,password fields and submit button..  
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired('Username required!'), 
            Length(min=5, max=25, message='Username must be in 5 to 25 characters')])
    password = PasswordField('Password',validators=[InputRequired('Password required')])
    submit = SubmitField('Submit')
    
@app.route('/Signup', methods=['GET', 'POST'])
def form():
    form = LoginForm()
    if form.validate_on_submit():
        return '<h1>Hi {}!!. Your form is submitted successfully!!'.format(form.username.data)
    return render_template('Signup.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
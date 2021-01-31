from flask import Flask,redirect,url_for,render_template,flash
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField

app = Flask(__name__)

app.config['SECRET_KEY']="my  kkkk key"

class SimpleForm(FlaskForm):
    name = StringField("enter your name")
    submit = SubmitField("click me")


@app.route("/",methods=["GET", "POST"])
def home():
    form=SimpleForm()

    if form.validate_on_submit():
        name=form.name.data
        flash("name is {}".format(name))

        return redirect(url_for('home'))
    return render_template("home.html",form=form)

if __name__ =='__main__':
    app.run(debug=True)
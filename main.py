from flask import Flask, url_for, render_template
from data.access_form import AccessForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'INFORMATION_SECURITY'


@app.route('/')
@app.route('/index')
def main_page():
    title = 'Test Title'
    return render_template('base.html', title=title)


@app.route('/training/<prof>}')
def training_func(prof):
    title = str(prof)

    return render_template('profession.html', title=title)


@app.route('/login')
def access_func():
    form = AccessForm()

    return render_template('access_template.html', form=form)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')

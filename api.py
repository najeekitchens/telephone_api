from flask import Flask, flash, render_template, request, redirect
from flask_restful import Api, Resource, reqparse
import formatnumbers
import searchform

app = Flask(__name__)
api = Api(app)

telephone_numbers = formatnumbers.get_telephone_book()

@app.route('/', methods=['GET', 'POST'])
def index():
    search = TelphoneSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']
    if search.data['search'] == '':
        results = telephone_numbers
    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)

if __name__ == '__main__':
    app.run()

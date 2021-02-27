from flask import Flask, render_template, request, redirect, url_for
from webscrapper import scraper
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get the index page 
    """
    if request.method == 'GET':
        return render_template('index.html')
    else:
        company = request.form['company']
        
        if company is not None:
            print('Searching for company: %s' % company)
            # Gather information on the stock for this company here 
        else:
            print("Could not find that company")
        
        return redirect(url_for('display'))

@app.route('/display', methods=['POST', 'GET'])
def display():
    """
    Display findings on the stock on this page 
    """
    
    if request.method == 'GET':
        return render_template('results.html')
    else:
        company = request.form['company']
        links = scraper(company, 10)
        # perform action with the new company 
        
        return render_template('results.html')


app.run()
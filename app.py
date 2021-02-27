from flask import Flask, render_template, request, redirect, url_for
from webscrapper import scraper
from models.StockPrediction import predict_price

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get the index page 
    """
    if request.method == 'GET':
        return render_template('index.html')
    else:
        company = request.form.get('company')
        titles = scraper(company, 10)

        if company is not None:
            print('Searching for company: %s' % company)
            # Gather information on the stock for this company here
            expected_price = -1
            try:
                expected_price = predict_price(company)
            except Exception:
                print('Could not predict price')
                 
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
        print(company)
        links = scraper(company, 10)
        # perform action with the new company 
        
        return render_template('results.html')


app.run()
from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from webscrapper import scraper
from models.StockPrediction import predict_price
import numpy as np
import json

app = Flask(__name__)
app.secret_key = 'S3CR3TK3Y'

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get the index page 
    """
    err = None
    if 'error' in session.keys():
        err = session['error']
        session.pop('error')
    if request.method == 'GET':
        # get request for the index page
        if err is None: 
            return render_template('index.html')
        else:
            return render_template('index.html', error=err)
    else:
        # post request for the index page 
        company = request.form.get('company')
        
        if len(company) < 1:
            # if the submit contained no information 
            return render_template('index.html')
        company = company.upper()
        session['company_name'] = company
        return redirect(url_for('load'))

@app.route('/load', methods=['GET', 'POST'])
def load():
    company = ''
    
    if 'company_name' in session.keys():
        # get the company to check for 
        company = session['company_name']
    
    if request.method == 'GET':
        return render_template('load_page.html', company=company)
    else:
        if company is not None:
            
            # ensure the company is exists 
            
            titles = scraper(company, 10)
            titles = np.array(list(titles))
            print('Searching for company: %s' % company)
            # Gather information on the stock for this company here
            expected_price = -1
            try:
                # get the predicted price 
                expected_price = predict_price(company)
                session['search_company'] = company
                session['expected_price'] = str(expected_price)
                print('Predicted Price:', expected_price)
                    
            except Exception:
                # if the company could not be found 
                print('Could not predict price')
                
                
                msgs = 'Could not predict price - stock could not be found'
                session['error'] = msgs
                return url_for('index')   
        else:
            print("Could not find that company")
        
        print('redirect to display')
        # show the results page 
        return json.dumps({'success':True}), 200, {'ContentType':'application/json'} 
        
@app.route('/display', methods=['POST', 'GET'])
def display():
    """
    Display findings on the stock on this page 
    """
    expected_price = '-1'
    search_company = ''
    if 'expected_price' in session.keys():
        # get the expected price of the company 
        expected_price = session['expected_price']
        
    if 'search_company' in session.keys():
        # get the company being searched 
        search_company = session['search_company']
    
    
    if request.method == 'GET':
        # get request for the results page 
        return render_template('results.html', expected_price=expected_price, company=search_company)
    else:
        # post request for the results page 
        company = request.form['company']
        print(company)
        links = scraper(company, 10)
        # perform action with the new company 
        
        return render_template('results.html', expected_price=expected_price, company=search_company)


if __name__ == '__main__':
    app.run()
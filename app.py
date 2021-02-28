from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from webscrapper import scraper
from models.StockPrediction import predict_price
import numpy as np
import json
from preprocesser import process
from models.newspaper_review import analyze
import os

WHITE_LIST = ['AAPL', 'FB', 'GOOG', 'GME', 'AMZN']

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './vthacks8-b9a997455cc6.json'

app = Flask(__name__)
app.secret_key = 'S3CR3TK3Y'

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get the index page 
    """
    err = None
    
    vals = []
    

    if 'error' in session.keys():
        err = session['error']
        session.pop('error', None)
    
    size = 0
    if 'size' in session.keys():
        size = session['size']
    
    company_names = ['val'] * size
    price_predictions = [ 'val'] * size
    score_predicitions = [ 'val'] * size
    for i in session.keys():
        if 'company' in i:
            if '1' in i:
                company_names[0] = session[i]
            elif '2' in i:
                company_names[1] = session[i]
            else:
                company_names[2] = session[i]
        elif 'price' in i:
            if '1' in i:
                price_predictions[0] = session[i]
            elif '2' in i:
                price_predictions[1] = session[i]
            else:
                price_predictions[2] = session[i]
        elif 'newspaper' in i:
            if '1' in i:
                score_predicitions[0] = session[i]
            elif '2' in i:
                score_predicitions[1] = session[i]
            else:
                score_predicitions[2] = session[i]
    if len(company_names) > 0:
        vals = list(zip(company_names, price_predictions, score_predicitions))
    
    if request.method == 'GET':
        # get request for the index page
        if err is None:
            return render_template('index.html', vals=vals)
        else:
            return render_template('index.html', error=err, vals=vals)
    else:
        # post request for the index page
        company = request.form.get('company')

        if len(company) < 1:
            # if the submit contained no information
            return render_template('index.html', vals=vals)
        company = company.upper()
        key_val = 'company'
        count = 1
        while (key_val + str(count) in session.keys()):
            # track all 3 values 
            count += 1
            
        session['search_name'] = company
        return redirect(url_for('load'))

@app.route('/load', methods=['GET', 'POST'])
def load():
    company = ''
    
    if 'search_name' in session.keys():
        # get the company to check for 
        company = session['search_name']
    if request.method == 'GET':
        return render_template('load_page.html', company=company)
    else:
        
        if company != '':
            session.pop('search_name', None)
        
        if company not in WHITE_LIST:
            msg = 'Stocks must be one of the following: '
            for i in WHITE_LIST:
                msg = msg + i
                if i != WHITE_LIST[-1]:
                    msg = msg + ', '
            session['error']  = msg
            return url_for('index')
        
        if company is not None:
            
            # ensure the company is exists 
            
            titles = scraper(company, 1)
            titles = np.array(list(titles))
            process(titles)
            score = analyze("models/testfile.txt")
            print('score: ', score)
            # Gather information on the stock for this company here
            expected_price = -1
            try:
                # get the predicted price 
                print('Searching for company: %s' % company)
                
                expected_price = predict_price(company)
                
                count = 1
                key = 'expected_price'
                
                while key + str(count) in session:
                    count += 1
                
                if count <= 3:
                    
                    session['search_company' + str(count)] = company
                    session['expected_price' + str(count)] = str(expected_price)
                    session['newspaper_review' + str(count)] = str(score)
                    session['size'] = count
                    
                else:
                    
                    for i in range(2):
                        session['search_company' + str(i + 1)] = session['search_company' + str(i + 2)]
                        session['expected_price' + str(i + 1)] = session['expected_price' + str(i + 2)]
                        session['newspaper_review' + str(i + 1)] = session['newspaper_review' + str(i + 2)]
                        
                    session['search_company3'] = company
                    session['expected_price3'] = str(expected_price)
                    session['newspaper_review3'] = str(score)
                print('Predicted Price:', expected_price)
                    
            except Exception as e:
                # if the company could not be found 
                print(str(e))
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

    if 'newspaper_review' in session.keys():
        # get the company being searched 
        newspaper_review = session['newspaper_review']
    
    
    if request.method == 'GET':
        # get request for the results page 
        return render_template('results.html', expected_price=expected_price, company=search_company, newspaper_review=round(newspaper_review, 1))
    else:
        # post request for the results page 
        company = request.form['company']
        print(company)
        links = scraper(company, 1)
        # perform action with the new company 
        
        return render_template('results.html', expected_price=expected_price, company=search_company, newspaper_review=round(newspaper_review, 1))



if __name__ == '__main__':
    app.run()

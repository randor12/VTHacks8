from flask import Flask, render_template, request, redirect, url_for, session, flash, get_flashed_messages
from webscrapper import scraper
from models.StockPrediction import predict_price

app = Flask(__name__)
app.secret_key = 'S3CR3TK3Y'

@app.route('/', methods=['POST', 'GET'])
def index():
    """
    Get the index page 
    """
    if request.method == 'GET':
        # get request for the index page 
        return render_template('index.html')
    else:
        # post request for the index page 
        company = request.form.get('company')

        if company is not None:
            
            # ensure the company is exists 
            
            company = company.upper()
            titles = scraper(company, 10)
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
                
                return render_template('index.html', error=msgs)   
        else:
            print("Could not find that company")
        # show the results page 
        return redirect(url_for('display'))

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


app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
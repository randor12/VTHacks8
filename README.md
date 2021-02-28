# VTHacks8
This is the code for VT Hacks 8

## Hackathon Team Name: StackOverflow
## Project Name: StockOverflow
## About:

This website allows users to search up stocks by their ticker (ex: AAPL, AMZN, FB, etc..), in order to make a prediction on the 
expected price of the stock in 15 days. This also uses Google API for sentiment analysis on newspapers which are scraped from the internet 
in live time and analyzed with the machine learning model, in order to help predict the future stock price. 

Since analyzing a company takes a decent amount of time, go ahead a play the Dino Game while waiting for your analysis to load. 
This was put on our page using open source code created by Google, that allows the user to play the Dino Game while the AI 
works on predicting the stocks. 

## Tools:
- Python (Flask, Jupyter Notebook, Tensorflow)
- HTML, JavaScript, CSS 

## Creating the Web Page:
The web page was created with Flask. This allows for Python to handle 
requests for traffic to the web page on the server side. HTML, CSS, and JavaScript 
is then used to display the actual web page itself for the front end. 

In the beginning, you are greeted to a search bar. This allows you to input the 
stock you are interested in searching more on. 

While you are waiting for the predictions, (they take a while as we collect the first
10 pages of news from Google on that company in order to analyze the stock), 
you can play the Dino Game created by Google as a the machine learning 
analyzes the data for you.

Finally, you are brought back to the home page where you are able to see the results. 
This will give you the 3 most recently searched stocks, their predicted prices, and 
a score related to the sentiment value from the analyzed news papers. This will then be 
indicated with a green, yellow, or red background. Green backgrounds typically indicate 
the sentiment expects "bullish" results for the stock to increase, yellow expects more 
neutral results and means the stock can most likely be held, and red indicates a "bearish" 
result, which means the stock should probably be sold. 

## About the Models:
There were 2 Machine Learning models used in our project. The first model is the 
sentiment analysis. We used Google API in order to use their Sentiment Analysis 
model to get a score related to news articles in order to get a general sense of 
what way the most recent news believes the stock will trend over a short period of time. 

The second model was a Stock Price predictor. This would predict the future price 
of the stock, predicting the price in 15 days from today. We used TensorFlow in order 
to train the model, using a Sequential model to get a relative idea at where the expected 
price will be in 15 days. While it is unlikely to get the exact price of the stock, it 
typically was around 20% off of the actual price on average, allowing for a rough 
idea on the stock price after that period of time. 


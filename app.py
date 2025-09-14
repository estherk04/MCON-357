#!/usr/bin/env python3
"""
MCON 357 - Flask Web Application
A simple Flask web app that extends the hello world concept.
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    """Main route that displays the interactive index page."""
    return render_template('index.html')

@app.route('/hello')
def hello_world():
    """Simple hello world route."""
    return '''
    <html>
        <head>
            <title>MCON 357 - Hello World</title>
            <style>
                body { 
                    font-family: Arial, sans-serif; 
                    text-align: center; 
                    margin-top: 100px;
                    background-color: #f0f0f0;
                }
                h1 { color: #333; }
                p { color: #666; font-size: 18px; }
                .container {
                    background-color: white;
                    padding: 40px;
                    border-radius: 10px;
                    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                    max-width: 600px;
                    margin: 0 auto;
                }
                a { color: #007bff; text-decoration: none; }
                a:hover { text-decoration: underline; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, World!</h1>
                <p>Welcome to MCON 357!</p>
                <p>This is a Flask web application.</p>
                <p>Your Python project is now running on the web! 🚀</p>
                <p><a href="/">← Back to Interactive Page</a></p>
            </div>
        </body>
    </html>
    '''

@app.route('/api/hello')
def api_hello():
    """API endpoint that returns JSON response."""
    return {
        'message': 'Hello, World!',
        'project': 'MCON 357',
        'framework': 'Flask',
        'status': 'success'
    }

if __name__ == '__main__':
    print("Starting MCON 357 Flask application...")
    print("Visit http://localhost:5000 to see your app!")
    app.run(debug=True, host='0.0.0.0', port=5000)


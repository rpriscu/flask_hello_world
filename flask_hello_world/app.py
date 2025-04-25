from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <html>
        <head>
            <title>My First Flask App</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 40px;
                    text-align: center;
                }
                h1 {
                    color: #333;
                }
            </style>
        </head>
        <body>
            <h1>Hello, World!</h1>
            <p>This is my first Flask web application!</p>
        </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True)

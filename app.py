from flask import Flask



@app.route('/')
def hello():
    return "Hello World! Test"

if __name__ == '__main__':
    app.run()
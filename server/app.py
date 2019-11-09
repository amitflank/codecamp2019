from flask import Flask, request, json
app = Flask(__name__)
 
@app.route("/")
def hello():
    return "Welcome to Python Flask!"

@app.route('/test', methods=['POST'])
def test():
    print(request.form['tempo'])
    
    return "square"
 
if __name__ == "__main__":
    app.run()
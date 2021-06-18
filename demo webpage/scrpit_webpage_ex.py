from flask import Flask,render_template

app=Flask(__name__)
@app.route('/')
def home():
    return render_template(template_name_or_list='home.html')

@app.route('/about/')
def about():
    return "about content goes here"

if __name__ == '__main__':
    app.run(debug=True)
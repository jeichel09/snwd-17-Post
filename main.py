from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contact", methods=["POST"])
def contact():
    print(request.form.get('contact_name'))
    print(request.form.get('contact_email'))
    print(request.form.get('contact_message'))
    return render_template("success.html")



if __name__ == '__main__':
    app.run()
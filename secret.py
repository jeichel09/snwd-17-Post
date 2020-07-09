import random
from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    secret_num = request.cookies.get("secret_number")

    response = make_response(render_template("secret_index.html"))
    if not secret_num:
        sec_num = random.randint(1, 30)
        response.set_cookie("secret_number", str(sec_num))

    return response

@app.route("/answer", methods=["POST"])
def answer():
    your_guess = int(request.form.get("guess"))
    secret_num = int(request.cookies.get("secret_number"))

    if your_guess == secret_num:
        message = "Correct! The secret number is {0}".format(str(secret_num))
        response = make_response(render_template("answer.html", message=message))
        response.set_cookie("secret_number", str(random.randint(1, 30)))
        return response
    elif your_guess > secret_num:
        message = "Your guess is not correct... try something smaller."
        return render_template("answer.html", message=message)
    else:
        message = "Your guess is not correct... try something bigger."
        return render_template("answer.html", message=message)

if __name__ == '__main__':
    app.run(debug=True)
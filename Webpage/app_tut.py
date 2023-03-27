from flask import Flask,render_template
 
app=Flask(__name__)

@app.route("/")
def home():
    return render_template("bob1.html")




# @app.route("/<name>")
# def user(name):
#     return f"Hello! <h1>{name}<h1>"


# @app.route("/admin")
# def admin():
#     return redirect(url_for("user",name="Admin"))

if __name__=="__main__":
    app.run()




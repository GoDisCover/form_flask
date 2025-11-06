from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
list_mahasiswa = []

@app.route("/")
def index():
    return render_template(
        "index.html", title="Welcome Page", name="Jessen", npm="2428250039",list_mahasiswa = list_mahasiswa
    )


@app.route("/add-new-mahasiswa", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name = request.form['name']
        npm = request.form['npm']
        print(name)
        print(npm)
        list_mahasiswa.append({
            "name" : name,
            "npm" : npm
        })
        return redirect(url_for("index"))
    return render_template("add_new_mahasiswa.html", title="Add New Mahasiswa")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

import os
from flask import Flask, redirect, render_template, request, send_from_directory, url_for
from werkzeug.utils import secure_filename
from forms.NewMahasiswa import NewMahasiswa


app = Flask(__name__)
UPLOUD_FOLDER = "uplouds"
app.config["SECRET_KEY"] = "SECRET_KEY"
app.config["UPLOUD_FILE"] = UPLOUD_FOLDER
app.config["MAX_CONTENT_LENGHT"] = 1 * 1024 * 1024
list_mahasiswa = []

@app.route("/")
def index():
    return render_template(
        "index.html", title="Welcome Page", name="Jessen", npm="2428250039",list_mahasiswa = list_mahasiswa
    )


@app.route("/add-new-mahasiswa", methods=["GET", "POST"])
def add():
    form = NewMahasiswa()
    if form.validate_on_submit():
        nama = form.name.data
        npm = form.npm.data
        profile_picture = form.profile_picture.data
        file_name = secure_filename(profile_picture.filename)
        save_dir = os.path.join(UPLOUD_FOLDER,"media")
        os.makedirs(save_dir,exist_ok=True)
        profile_picture.save(os.path.join(save_dir,file_name))
        list_mahasiswa.insert(0, {
            "nama" : nama,
            "npm" : npm,
            "profile_picture" : file_name
        })
        return redirect(url_for("index"))

    return render_template("add_new_mahasiswa.html", title="Add New Mahasiswa", form=form)

@app.route("/uploads/<path>:filename")
def uploud_file(filename):
    return send_from_directory(app.config["UPLOUD_FILE"],filename)

if __name__ == "__main__":
    app.run(debug=True, port=5000)

from flask import Flask, send_from_directory, request, redirect

app = Flask(__name__)


@app.route("/login/<path:path>", methods=["GET"])
def login_(path):
    return send_from_directory("login", path)


@app.route("/description/<path:path>", methods=["GET"])
def description_(path):
    return send_from_directory("description", path)


@app.route("/animation/<path:path>", methods=["GET"])
def animation_(path):
    return send_from_directory("animation", path)


@app.route("/login/", methods=["GET"])
def login_meta():
    return redirect("/login/index.hrepositiontml")


@app.route("/description/", methods=["GET"])
def description_meta():
    return redirect("/description/index.html")


@app.route("/animation/", methods=["GET"])
def animation_meta():
    return redirect("/animation/index.html")


@app.route("/login/index.html", methods=["POST"])
def login_action():
    login = request.form.get("username", "noname")
    pwd = request.form.get("password", "1234")

    if (login, pwd) == ("aboba", "42"):
        return redirect("/description/index.html")
    else:
        return redirect("/login/index.html")


@app.route("/", methods=["POST"])
def general_action():
    return redirect("/login/index.html")


@app.route("/", methods=["GET"])
def general():
    return f"""
    <html>
    <body>
        <h4>url: {request.url_root}</h4>
        <h4>Client IP address: {request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)}</h4>
        <form method="post">
            <input type="submit" value="reposition: Login">
        </form>
    </body>
    </html>
    """

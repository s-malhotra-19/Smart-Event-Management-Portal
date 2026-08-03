from flask import Flask, render_template, request, redirect, url_for
events = [
    {
        "id": 1,
        "name": "AI Workshop",
        "date": "10 Aug 2026",
        "location": "LPU Auditorium"
    },
    {
        "id": 2,
        "name": "Hackathon",
        "date": "18 Aug 2026",
        "location": "Block 38"
    },
    {
        "id": 3,
        "name": "Sports Meet",
        "date": "25 Aug 2026",
        "location": "Sports Complex"
    }
]

bookings = []
app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def check_login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "admin" and password == "admin":
        return redirect(url_for("admin"))

    elif username == "user" and password == "123":
        return redirect(url_for("index"))

    else:
        return "Invalid Username or Password"


@app.route("/index")
def index():
    return render_template("index.html", events=events)


@app.route("/admin")
def admin():
    return render_template("admin.html", events=events)
@app.route("/add", methods=["POST"])
def add():

    new_event = {
        "id": len(events) + 1,
        "name": request.form["name"],
        "date": request.form["date"],
        "location": request.form["location"]
    }

    events.append(new_event)

    return redirect(url_for("admin"))

@app.route("/book/<int:event_id>", methods=["POST"])
def book(event_id):

    for event in events:
        if event["id"] == event_id:
            bookings.append(event)
            break

    return redirect(url_for("history"))

@app.route("/delete/<int:event_id>", methods=["POST"])
def delete(event_id):

    global events

    events = [event for event in events if event["id"] != event_id]

    return redirect(url_for("admin"))

@app.route("/history")
def history():
    return render_template("history.html", bookings=bookings)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


texts = ["1st Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem nemo, suscipit perspiciatis aperiam id nihil fugit asperiores alias exercitationem quisquam. Deleniti quasi nostrum repellat, commodi ut esse ad tempore possimus?",
"2nd Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem nemo, suscipit perspiciatis aperiam id nihil fugit asperiores alias exercitationem quisquam. Deleniti quasi nostrum repellat, commodi ut esse ad tempore possimus?",
"3rd Lorem ipsum dolor sit amet consectetur adipisicing elit. Voluptatem nemo, suscipit perspiciatis aperiam id nihil fugit asperiores alias exercitationem quisquam. Deleniti quasi nostrum repellat, commodi ut esse ad tempore possimus?"]


@app.route("/first")
def first():
    return texts[0]


@app.route("/second")
def second():
    return texts[1]


@app.route("/third")
def third():
    return texts[2]


from flask import Flask, render_template
import requests

app = Flask(__name__)

blog_posts = requests.get("https://api.npoint.io/9310476ceb6796fd6f91").json()

@app.route('/')
def home():
    return render_template("index.html",blogs=blog_posts)


@app.route('/blog/<int:id>')
def get_blog(id):
    for blogg in blog_posts:
        if id==blogg['id']:
            my_blog=blogg
            return render_template("post.html",blog=my_blog)


if __name__ == "__main__":
    app.run(debug=True)

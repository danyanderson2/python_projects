from flask import Flask, render_template
import requests
app=Flask(__name__)

API_ENDPOINT= "https://api.npoint.io/674f5423f73deab1e9a7"

response=requests.get(API_ENDPOINT).json()

@app.route('/')
def home():
   return render_template('index.html',blog_posts=response)


@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<int:id>')
def post(id):
    for blog in response:
        if blog['id'] == id:
            title=blog['title']
            subtitle=blog['subtitle']

            return render_template('post.html',id=id,title=title,subtitle=subtitle)

if __name__=='__main__':
    app.run()

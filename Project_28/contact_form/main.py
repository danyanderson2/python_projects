from flask import Flask, render_template,request
import smtplib
import requests
USER='danyanderson2222@gmail.com'
PASSWORD='klcwvzxzvmzxbhfq'
# USE YOUR OWN npoint LINK! ADD AN IMAGE URL FOR YOUR POST. 👇
posts = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()

app = Flask(__name__)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact",methods=['POST','GET']) # Add methods parameter and set GET and POST as possible methods
def contact():  # need to trigger contact method once submit button is clicked
    if request.method=='GET':
        return render_template("contact.html")
    elif request.method=='POST':
        name=request.form['name']
        tel=request.form['phone']
        email=request.form['email']
        message=request.form['message']
        # the function executes once the submit button is clicked, hence I can use that to my advantage and send my mail
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=USER, password=PASSWORD)
            connection.sendmail(from_addr=USER,
                                to_addrs=USER,
                                msg=f"Subject:Hello Dany! \n\n {message}\n\n\n Sent by: {name}\nPhone: {tel}\nEmail: {email}")
        return render_template('contact.html',msg="Successfully sent message")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=False, port=5001)

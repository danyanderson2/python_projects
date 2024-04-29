from flask import Flask
import random
app=Flask(__name__)

# random number between 0 and 9
number = random.randint(0,9)

@app.route('/')
def display():
    return '<h1>Guess a number between 0 and 9</h1>'\
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMGQxbWZ3OGtwbXlxdXQxYWxrem5ibDRieHd6Y215a3dmYnkxYzh5NCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OK914NO5d8ey9sSNAQ/giphy.gif" width ="200">'


@app.route('/<int:num>')
def guess_number(num):
    if number<num:
        return '<h1> Ooops!!! Wrong one. The number is smaller than your guess :( </h1>'\
                '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExejFqY3FhcXZnczF2enJzMXRibnF3dmxkemZrb2Y5MzZnODQ2ajhldCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/9JLOGsEfPjpR1179HE/giphy.gif" width=200>'
    elif number>num:

        return '<h1 color="green"> Your number is lower than the right one :( </h1>' \
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjM3ZDg1YTFqM21odzljZm0xM3c5amxyZWs5ZTVzdTR1YWluOG0xayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3ohA2ZD9EkeK2AyfdK/giphy.gif" width=200>'
    else:
        return '<h1 color="red"> You got it !!! :)</h1>' \
               '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNTZjdDFvcjFraDZpbHJ1Y3N2d3RiOXhvMnoyYjFzcWcwYnRkYnBmaCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/l1J3pZOnBQ1qeBwZ2/giphy.gif" width=200>'

print(number)
if __name__=='__main__':
    app.run(debug=False)
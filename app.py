from flask import Flask
from flask import send_file, request
app = Flask(__name__)

template = """
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <title>Lab 3: Images and Flask</title>
    <link rel="icon" type="image/png" href="/mars.png">
  </head>

  <body>
    {content}
  </body>
</html>
""".strip()

# root route to show different content, with added sunset.jpg
@app.route('/')
def home():
  content = """
  <h1>Welcome!</h1>
    <img src='/sunset.jpg' alt='Sunset over the mountains' width='400'>
  """
  return template.replace("{content}", content)

# add route that requires two int value with its path. if /add/2/3 it will return 2+3=5
@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    result = f"{a} + {b} = {a + b}"
    return template.replace("{content}", result)
    
# reverse route that displayes the reverse of q GET parameter. /reverse?q=abcd returns a page with abcd reversed is dcba
@app.route("/reverse")
def reverse():
    word = request.args.get("q","")
    reversed_word = word[::-1]
    result = f"{word} reversed is {reversed_word}"
    return template.replace("{content}", result)

# route called sunset.jpg that returns sunset.jpg. uses send_file function
@app.route("/sunset.jpg")
def sunset():
    return send_file("sunset.jpg")

# route to server mars.png 
@app.route("/mars.png")
def mars():
    return send_file("mars.png")

if __name__ == '__main__':
    app.run(debug=True)

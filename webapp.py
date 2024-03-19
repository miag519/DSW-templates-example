from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route("/")
def render_main():
    return render_template('home.html')

@app.route("/p1")
def render_page1():
    return render_template('page1.html')
    
@app.route("/response")  
def render_response():
    word = request.args["word"]
    word1 = request.args["word2"]
    word2 = request.args["word3"]
    number = request.args["number"]
    if len(word) > 3:
     username = (word[0:3] + word1)
    else:
     username = (word + word1)
    if len(word2) > 4:
     usernames = (number + word2[0:4] + number)
    else:
     usernames = (word2 + number)
    reverse = (word2[::-1] + word)
    if len(word) > 6 and len(word1) > 2:
     half = (word[2:6] + number + word1[0:2])
    else:
     half = (word + number)
    if len(word2) > 5 and len(number) > 3: 
     mixed = (number[0:1] + word2[2:5] + number[2:3])
    else:
     mixed = (number + word2[::-1] + number)
    return render_template('page1.html', a = username, b = usernames, c = reverse, d = half, e = mixed)
    



    
if __name__=="__main__":
    app.run(debug=True)

from flask import Flask
app=Flask(__name__)

@app.route('/') #装饰器： route函数将URL和一个视图函数绑定
def hello_world():
    return 'Hello,World!'

if __name__=='main.py':
    app.run()
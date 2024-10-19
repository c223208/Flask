from flask import Flask

# インスタンス生成
app = Flask(__name__)

# ルーティング
@app.route('/')
def shouw_index():
    return'indexページ'

@app.route('/hello/')
@app.route('/hello/<name>')
def show_hello(name=None):
    return f'Hello, {name}'

# 実行
if __name__ == '__main__'
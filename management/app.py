from flask import Flask, render_template

# インスタンス生成
app = Flask(__name__)

# ルーティング
# TOPページ
@app.route('/')
def index():
    return render_template('jinja/top.html')

# 一覧
class member:
    # コンストラクタ
    def __init__(self, id, name):
        self.id = id

@app.route('/list')
def member_list():
    return render_template

# 詳細

# 実行
if __name__ == '__main__':
    app.run()

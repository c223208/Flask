from flask import Flask, render_template

# インスタンス生成
app = Flask(__name__)


# ルーティング
# TOPページ
@app.route('/')
def index():
    return render_template('top.html')

# 一覧
@app.route('/list')
def item_list():
    return render_template('list.html')

# 詳細
@app.route('/detail/<int:id>')
def item_detail(id):
    return render_template('detail.html', show_id=id)

# render_templateで値を渡す
@app.route("/multiple")
def show_jinja_multiple():
    word1 = "テンプレートエンジン"
    word2 = "神社"
    return render_template('jinja/show1.html', temp = word1, jinja = word2)

# render_templateで値を渡す「辞書型」
@app.route("/dict")
def show_jinja_dict():
    words = {
        'temp':"てんぷれーとえんじん",
        'jinja':"ジンジャ"
    }
    return render_template('jinja/show2.html', key = words)

# render_templateで値を渡す「リスト型」
@app.route("/list2")
def show_jinja_list():
    hero_list = ['桃太郎','金太郎','浦島タロウ']
    return render_template('jinja/show3.html', users = hero_list)

# render_templateで値を渡す「クラス」
class Hero:
    # コンストラクタ
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # 表示用関数
    def __str__(self):
        return f'名前：{self.name} 年齢：{self.age}'
    
@app.route("/class")
def show_jinja_class():
    hana = Hero('花咲かじいさん', 99)
    return render_template('jinja/show4.html', user = hana)

#▼▼▼▼▼ここから【制御文】▼▼▼▼▼
# 「商品」クラス
class item:
    # コンストラクタ
    def __init__(self, id, name):
        self.id = id
        self.name = name
    # 表示用関数
    def __str__(self):
        return f'商品ID：{self.id} 商品名：{self.name}'

# 繰り返し
@app.route("/for_list")
def show_for_list():
    item_list = [item(1,"ダンゴ"), item(2,"にくまん"), item(3,"ドラ焼き")]
    return render_template('for_list.html', items = item_list)

# 条件分岐
@app.route('/if_detail/<int:id>')
def show_if_detail(id):
    item_list = [item(1,"ダンゴ"), item(2,"にくまん"), item(3,"ドラ焼き")]
    return render_template('if_detail.html', show_id=id, items = item_list)

# 条件分岐２
@app.route('/if/')
@app.route('/if/<target>')
def show_jinja_if(target="colorless"):
    print(target)
    return render_template('jinja/if_else.html', color=target)


# 実行
if __name__ == '__main__':
    app.run()
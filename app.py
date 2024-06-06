from flask import Flask, render_template, request,jsonify,make_response
import os

app = Flask(__name__, static_folder='static', template_folder='templates')

save_dir = './static/mdfiles'

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/resume/')
def resume():
    return render_template('resume.html')

@app.route('/signin/')
def signin():
    return render_template('signin.html')

@app.route('/xls/<filename>')
def xls(filename):
    path = save_dir+'/'+filename+'.md'
    print(path)
    if os.path.exists(path):
        with open(file=path,mode='r',encoding='utf-8') as mdf:
            content = mdf.read()
    else:
        content = '# 默认内容（未找到文件）'
    return render_template('xls.html',content = content,filename = filename)

@app.route('/xzmm/')
def xzmm():
    return render_template('xzmm.html')

@app.route('/save', methods=['POST'])
def savemd():
    content = request.form['content']
    print(content)
    filename = request.form['filename']
    print(filename)
    path = save_dir+'/'+filename+'.md'
    with open(path, 'w',encoding='utf-8') as f:
        f.write(content)

    return 'Saved successfully!' 

@app.route('/picture/<picname>')
def getpic(picname):
    return save_dir+'/images/'+ picname

@app.route('/get/<filename>')
def getmd(filename):
    path = save_dir+'/'+filename+'.md'
    if os.path.exists(path):
        with open(file=path,mode='r',encoding='utf-8') as mdf:
            content = mdf.read()
    else:
        content = '# 默认内容（未找到文件）'
    return make_response(jsonify(content))

if __name__ == '__main__':
    app.run(debug=True)

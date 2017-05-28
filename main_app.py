from flask import Flask
from flask import request
from flask import render_template

from decimal import Decimal

import silverRobot.guloso.guloso as guloso
import silverRobot.genetico.genetico as genetico


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

# ====================================================
#       Exemplos
# ====================================================
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/hello2/')
@app.route('/hello2/<name>')
def hello2(name=None):
    return render_template('hello2.html', name=name)
# ====================================================
#       Fim Exemplos
# ====================================================

def lerArquivo():
    qtd_classes = int(request.form['qtd_classes'])

    f = request.files['the_file']
    f_bytes = f.read()
    f_str = f_bytes.decode()
    f_str = f_str.replace('\n', '')

    nums = []
    for n in f_str.split(";"):
        if n.isnumeric():
            nums.append(Decimal(n))

    return qtd_classes, nums

# ====================================================

@app.route('/guloso', methods=['GET', 'POST'])
def route_guloso():
    if request.method == 'POST':
        return guloso_post()
    else:
        return render_template('upload.html', action='guloso')
def guloso_post():
    qtd_classes, nums = lerArquivo()
    return guloso.guloso_run(nums, qtd_classes)

# ====================================================

@app.route('/genetico', methods=['GET', 'POST'])
def route_genetico():
    if request.method == 'POST':
        return genetico_post()
    else:
        return render_template('upload.html', action='genetico')
def genetico_post():
    classes, numeros = lerArquivo()

    qtdIteracoes = int(request.form['qtdIteracoes'])
    geracoes = int(request.form['geracoes'])
    tamanhoPopulacao = int(request.form['tamanhoPopulacao'])
    qtdIndividuosElitismo = int(request.form['qtdIndividuosElitismo'])
    taxaCruzamento = Decimal(request.form['taxaCruzamento'])
    taxaMutacao = Decimal(request.form['taxaMutacao'])

    solucao = genetico.genetico_run(classes, numeros, geracoes, tamanhoPopulacao, qtdIteracoes, qtdIndividuosElitismo, taxaCruzamento, taxaMutacao)
    return render_template('genetico_solucao.html', request=request, solucao=str(solucao))
    return str(solucao)

# ==================================================
#       LOCAL
# ==================================================
if __name__ == "__main__":
    app.run(debug=True)
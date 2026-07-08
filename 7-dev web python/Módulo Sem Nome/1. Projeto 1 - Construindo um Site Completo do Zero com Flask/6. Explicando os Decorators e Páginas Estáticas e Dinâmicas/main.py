from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Coe Lira, meu 1º site ta no ar!!!!! To sabendo muito</h1><p>Esse site ta ficando legal</p>'


@app.route('/contato')
def contato():
    return 'Qualquer dúvida mande um e-mail para listavip@hashtagtreinamentos.com'


if __name__ == '__main__':
    app.run(debug=True)


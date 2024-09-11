from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Halaman utama dengan konten default
    return render_template('index.html', section='home')

@app.route('/beranda')
def beranda():
    # Mengarahkan ke halaman dengan konten Beranda
    return render_template('beranda.html', section='beranda')

@app.route('/finish')
def finish():
    # Mengarahkan ke halaman dengan konten Finish
    return render_template('finish.html', section='finish')

if __name__ == '__main__':
    app.run(debug=True)

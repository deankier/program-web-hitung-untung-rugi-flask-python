from flask import Flask, render_template, request
app = Flask(__name__)

namaR = ""
rincianR = ""
modalR = 0
biayaR = 0
penjualanR = 0
kotorR = 0
bersihR = 0
untungR = 0
persen = 0

def cabang(per):
    if per<0:
        untungrugi = "Usaha Anda Rugi Mencapai"
    elif per>0:
        untungrugi = "Keuntungan Usaha Anda Mencapai"
    return untungrugi

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/panduan')
def panduan():
    return render_template('panduan.html')

@app.route('/tentang')
def tentang():
    return render_template('tentang.html')

@app.route('/',methods=['POST'])
def getValue():
    namaR = request.form['nama']
    rincianR = request.form['bulan']
    modalR = request.form['modal']
    biayaR = request.form['biaya']
    penjualanR = request.form['penjualan']
    kotorR = int(penjualanR) - int(modalR)
    bersihR = int(kotorR) - int(biayaR)
    persen = round((bersihR/(int(modalR)+int(biayaR)))*100,2)
    return render_template('index.html', nm=namaR, rin=rincianR, md=modalR, 
    biy=biayaR, pen=penjualanR, ktr=kotorR, brs=bersihR, prs=persen, PnL=cabang(persen))


app.run(debug=True)
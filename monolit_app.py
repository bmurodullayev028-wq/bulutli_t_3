from flask import Flask, jsonify, request, render_template_string
import os
from serverless_moduli import hisob_funksiya

app = Flask(__name__)

HTML_SHABLON = """
<!DOCTYPE html>
<html lang="uz">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>3-mustaqil ish — Modernizatsiya</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', Tahoma, sans-serif; }
        body {
            background: linear-gradient(135deg, #090d16, #172033, #0f172a);
            color: #f8fafc;
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 24px;
        }
        .card {
            background: rgba(23, 32, 51, 0.94);
            border: 1px solid #334155;
            border-radius: 18px;
            padding: 36px;
            max-width: 740px;
            width: 100%;
            box-shadow: 0 24px 50px rgba(0, 0, 0, 0.55);
        }
        .badge {
            display: inline-block;
            background: rgba(168, 85, 247, 0.16);
            color: #d8b4fe;
            border: 1px solid #9333ea;
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            margin-bottom: 18px;
        }
        .title {
            font-size: 20px;
            color: #cbd5e1;
            line-height: 1.5;
            margin-bottom: 20px;
        }
        .big {
            font-size: 28px;
            font-weight: 800;
            color: #38bdf8;
            white-space: nowrap;
        }
        .box {
            background: #0b1120;
            border: 1px solid #1e293b;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 18px;
        }
        .row { display: flex; gap: 10px; flex-wrap: wrap; margin-top: 10px; }
        input {
            flex: 1;
            min-width: 160px;
            padding: 10px 12px;
            border-radius: 8px;
            border: 1px solid #475569;
            background: #111827;
            color: #fff;
        }
        button {
            background: #7e22ce;
            color: #fff;
            border: none;
            padding: 10px 18px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
        }
        button:hover { background: #6b21a8; }
        #natija { margin-top: 14px; color: #34d399; font-size: 14px; line-height: 1.6; }
    </style>
</head>
<body>
    <div class="card">
        <div class="badge">● Arxitektura: Monolit + Serverless / Microservice moduli</div>
        <h1 class="title">
            Murodullayev Bekzodning bulutli texnologiyalar fanidan <span class="big">3-mustaqil ishi</span>
        </h1>

        <div class="box">
            <strong>Serverless / Microservice hisob-kitob funksiyasini sinash</strong>
            <div class="row">
                <input type="number" id="son" value="10" placeholder="Son kiriting">
                <button onclick="hisobla()">Funksiyani chaqirish</button>
            </div>
            <div id="natija">Natija shu yerda ko‘rinadi...</div>
        </div>
    </div>

    <script>
        async function hisobla() {
            const son = document.getElementById('son').value || 0;
            const res = await fetch(`/api/serverless/hisob?son=${encodeURIComponent(son)}`);
            const data = await res.json();
            document.getElementById('natija').innerHTML =
                `<strong>Rejim:</strong> ${data.rejim}<br>` +
                `<strong>Kiruvchi qiymat:</strong> ${data.son} → <strong>Kvadrati:</strong> ${data.kvadrat}, <strong>2x:</strong> ${data.ikki_barobar}<br>` +
                `<strong>Holat:</strong> ${data.xabar}`;
        }
        hisobla();
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML_SHABLON)

@app.route('/api/serverless/hisob', methods=['GET'])
def serverless_endpoint():
    son_str = request.args.get('son', '0')
    try:
        son = float(son_str)
    except ValueError:
        return jsonify({"xato": "Noto‘g‘ri son kiritildi"}), 400
    return jsonify(hisob_funksiya(son))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
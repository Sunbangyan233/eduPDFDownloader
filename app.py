from flask import Flask, request, send_file
import requests
import io

app = Flask(__name__)

@app.route('/prpr', methods=['GET'])
def proxy_download():
    file_url = request.args.get('file_url')
    auth_header = request.args.get('auth_header')

    if not file_url or not auth_header:
        return "无法下载：URL字段中缺失文件链接或请求头", 400

    headers = {
        'X-ND-AUTH': auth_header
    }

    try:
        response = requests.get(file_url, headers=headers)
        if response.status_code == 200:
            pdf_file = io.BytesIO(response.content)
            return send_file(pdf_file, mimetype='application/pdf')
        else:
            return f"无法下载：服务器（PDF提供方）返回状态码 {response.status_code}", response.status_code
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
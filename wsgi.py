from dashapp import app
from dashapp.tabindex import layout


app.layout = layout


if __name__ == '__main__':
    public = True  # 24.212.252.134:33
    if public:
        ip = '192.168.0.129'  # essayer 0.0.0.0 c'est peut-etre un wildcard
        port = 33
        app.run_server(debug=False, host=ip, port=port)
    else:
        app.run_server(debug=True)



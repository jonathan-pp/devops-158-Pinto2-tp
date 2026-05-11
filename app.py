from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "test test 2 Hello EPSIC - DevOps - ALED"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

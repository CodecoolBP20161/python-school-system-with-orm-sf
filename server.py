from flask import Flask, render_template, request, url_for, redirect, g

app = Flask(__name__)


@app.route('/')
def main():
    return 'YEAHH!!!!'


if __name__ == '__main__':
    app.run()

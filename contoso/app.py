from re import L
from flask import Flask, redirect, url_for, render_template,session,request
import requests, os, uuid, json
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')
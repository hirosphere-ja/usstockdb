from django.shortcuts import render, redirect
from django.views import generic
from .models import Market

class IndexView(generic.ListView):
    model = Market

"""
汎用ビューを使う場合
templates以下のフォルダ名はアプリ名と同じ名前⇒usstockmarket
フォルダ以下のhtml名はモデルのクラス名_list.htmlとする⇒market_list.html
"""

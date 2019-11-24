from django.shortcuts import render, redirect
from django.views import generic
from .models import Usstock

class IndexView(generic.ListView):
    model = Usstock

"""
汎用ビューを使う場合
templates以下のフォルダ名はアプリ名と同じ名前⇒usstocklist
フォルダ以下のhtml名はモデルのクラス名_list.htmlとする⇒usstock_list.html
"""

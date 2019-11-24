from django.shortcuts import render, redirect
from django.views import generic
from django.urls import reverse_lazy
from .models import Usstock

"""
汎用ビュー(ListView)を使う場合
templates以下のフォルダ名はアプリ名と同じ名前⇒usstocklist
フォルダ以下のhtml名はモデルのクラス名_list.htmlとする⇒usstock_list.html
"""
class IndexView(generic.ListView):
  model = Usstock

"""
汎用ビュー(CreateView)を使う場合
フォルダ以下のhtml名はモデルのクラス名_form.htmlとする⇒usstock_form.html
"""
class AddView(generic.CreateView):
  model = Usstock
  fields = '__all__'
  success_url = reverse_lazy('index')

"""
汎用ビュー(UpdateView)を使う場合
フォルダ以下のhtml名はモデルのクラス名_list.htmlとする⇒usstock_form.htmlとすべきだが
登録画面と同じになるので新たに変更画面(usstock_form.html)を作成しtemplate_nameで指定する 
"""
class EditView(generic.UpdateView):
  model = Usstock
  fields = '__all__'
  success_url = reverse_lazy('index')
  template_name = 'usstocklist/usstock_edit.html'

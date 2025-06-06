from django.db import models
from django.contrib.auth.models import User # Userモデルをインポート
from django.urls import reverse #reverse関数をインポート

class Article(models.Model):#継承元を()の中に書く
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    # 投稿完了したあとのリダイレクト処理！
    # モデルのデータを保存した後、勝手に実行してくれる
    def get_absolute_url(self):
        return reverse("bbs:detail", kwargs={"pk": self.pk})
    
    
    def __str__(self):
        return self.content
    
    # self.contentじゃなくてもよい。管理画面でどう表示したいかによってカスタマイズする。今回は投稿内容のみ

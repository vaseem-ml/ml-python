from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    # path('analyzetweets', views.analyzetweets, name="analyzetweets"),
	# path('sentiment', views.sentiment, name="sentiment")
]

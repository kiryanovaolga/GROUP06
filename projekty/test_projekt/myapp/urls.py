from django.urls import path
from myapp import views

# 127.0.0.1:8000/
# 127.0.0.1:8000/admin/

urlpatterns = [
    path('', views.index_page),
    # path('time/', ), # zde přidejte time_page

    # http://127.0.0.1:8000/url-paths/
    path('url-paths/', views.url_paths),

    path('calculate/', views.my_math),

    path('calculator/', views.calculator),

    # path('jmeno/jana/', views.my_page),
    # path('jmeno/petr/', views.my_page),
    # path('jmeno/karel/', views.my_page),
    
    # jmeno/ales/
    # instagram.com/suche.cz/
    # instagram.com/uzivatel/
    # zpravy.cz/clanky/top-mista-na-bydleni-109282/
    # zpravy.cz/clanky/top-mista-na-sport-28273/
    # slug 'Top místa na bydlení' -> 'top-mista-na-bydleni'

    # toto udělá validaci pro /clanky/<slug>-<id>/
    # máme vzor
    # zpravy.cz/clanky/top-mista-na-bydleni-109282/

    # toto udělá validaci pouze pro /clanky/
    # zpravy.cz/clanky/?id=109282
    
    path('jmeno/<str:name>/', views.my_page),
    # todo: ukazat url cesty pomocí regex
    
    # clanky/jak-nasbirat-houby-1093283/
    # clanky/nejlespi-mista-na-prochazku-762873/
    # clanky/asaj_-162651-762873/

    path('clanky/<slug:name>-<int:number>/uuu/', views.article),

    # pages/
    # pages/65276523/
    # pages/65276523/edit/
    # pages/65276523/komentare/
    
    # pages/7268723/abc-xyz/
    # pages/727/alskja-asda-sada/
    # pages/727/askdjalks/

    path('pages/<int:number>/<slug:text>/', views.pages),


    # http://127.0.0.1:8000/login/
    path('login/', views.login),

    path('test-template/', views.test_template),
]

"""
youtube.com/watch?v=JKAHDAS8
youtube.com/playlist/ZGAUSZD

/
/pages/
/pages/my-page-1/
/pages/new-page/asklaksjdak/aksdlajs/

slug
str
int
uuid
"""
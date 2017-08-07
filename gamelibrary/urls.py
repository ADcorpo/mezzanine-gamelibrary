from django.conf.urls import url

from gamelibrary.views import GameDetailView


urlpatterns = \
              [
                  url(r'^(?P<slug>[-\w]+)/$',
                      GameDetailView.as_view(),
                      name="game-detail"),
              ]

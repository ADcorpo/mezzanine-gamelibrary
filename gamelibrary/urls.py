from django.conf.urls import url

from gamelibrary.views import (GameDetailView,
                               DevelopperRelatedListView,
                               EditorRelatedListView,
                               GenreRelatedListView)


urlpatterns = \
              [
                  url(r'^editor/(?P<slug>[-\w]+)/$',
                      EditorRelatedListView.as_view(),
                      name="game-list-editor"),

                  url(r'^developper/(?P<slug>[-\w]+)/$',
                      DevelopperRelatedListView.as_view(),
                      name="game-list-dev"),

                  url(r'^genre/(?P<slug>[-\w]+)/$',
                      GenreRelatedListView.as_view(),
                      name="game-list-genre"),

                  url(r'^(?P<slug>[-\w]+)/$',
                      GameDetailView.as_view(),
                      name="game-detail"),
              ]

from copy import deepcopy

from django.contrib import admin

from mezzanine.core.admin import (DisplayableAdmin,
                                  BaseTranslationModelAdmin)
from mezzanine.conf import settings

from gamelibrary.models import (Game,
                                GameDevelopper,
                                GameEditor,
                                GameGenre)


game_fieldsets = deepcopy(DisplayableAdmin.fieldsets)
game_fieldsets[0][1]["fields"].insert(1, "editor")
game_fieldsets[0][1]["fields"].insert(1, "developper")
game_fieldsets[0][1]["fields"].insert(1, "genres")


class GameAdmin(DisplayableAdmin):
    """
    Administration class for Games
    """

    fieldsets = game_fieldsets
    list_display = ["title", "status", "editor", "developper", "admin_link"]
    list_filter = deepcopy(DisplayableAdmin.list_filter) + ("editor",
                                                            "developper",
                                                            "genres",)
    filter_horizontal = ("genres",)


class GameDevelopperAdmin(BaseTranslationModelAdmin):
    """
    Admin class for game developpers. Not displayed in the
    admin panel by default.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "gamelibrary.GameDevelopper" in items:
                return True
        return False


class GameEditorAdmin(BaseTranslationModelAdmin):
    """
    Admin class for game editors. Not displayed in the
    admin panel by default.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "gamelibrary.GameEditor" in items:
                return True
        return False


class GameGenreAdmin(BaseTranslationModelAdmin):
    """
    Admin class for game genres. Not displayed in the
    admin panel by default.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def has_module_permission(self, request):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "gamelibrary.GameGenre" in items:
                return True
        return False


admin.site.register(Game, GameAdmin)
admin.site.register(GameDevelopper, GameDevelopperAdmin)
admin.site.register(GameEditor, GameEditorAdmin)
admin.site.register(GameGenre, GameGenreAdmin)

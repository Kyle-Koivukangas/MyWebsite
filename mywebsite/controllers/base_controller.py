import pyramid.renderers
import pyramid.httpexceptions as exc

import mywebsite.infrastructure.static_cache as static_cache
from mywebsite.infrastructure.suppressor import suppress
import mywebsite.infrastructure.cookie_auth as cookie_auth
from mywebsite.services.account_service import AccountService


class BaseController:

    def __init__(self, request):
        self.request = request

        self.build_cache_id = static_cache.build_cache_id

        #grab layout and make available to all controllers
        layout_render = pyramid.renderers.get_renderer('mywebsite:templates/shared/_layout.pt')
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        if not self.logged_in_user_id:
            return False
        return True

    @property
    def dev_mode_on(self):
        return False


    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)

    @property
    def data_dict(self):
        data = dict()
        data.update(self.request.GET)
        data.update(self.request.POST)
        data.update(self.request.matchdict)

        return data

    @property
    def logged_in_user_id(self):
        return cookie_auth.get_user_id_from_cookie(self.request)

    @property
    def logged_in_user(self):
        """accesses the database and returns user account details via user ID in auth cookie."""
        user_id = self.logged_in_user_id
        if not user_id:
            return None

        return AccountService.find_account_by_id(user_id)

    @property
    def active_page(self):
        """Shows the current 'active' page being displayed, used for lighting up navbar on active page"""


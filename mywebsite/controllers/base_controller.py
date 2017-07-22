import mywebsite.infrastructure.static_cache as static_cache
from mywebsite.infrastructure.suppressor import suppress
import pyramid.renderers
import pyramid.httpexceptions as exc


class BaseController:

    def __init__(self, request):
        self.request = request

        self.build_cache_id = static_cache.build_cache_id

        #grab layout and make available to all controllers
        layout_render = pyramid.renderers.get_renderer('mywebsite:templates/shared/_bootstrap_layout.pt')
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

    @property
    def is_logged_in(self):
        return False

    @property
    def dev_mode_on(self):
        return False


    def redirect(self, to_url, permanent=False):
        if permanent:
            raise exc.HTTPMovedPermanently(to_url)
        raise exc.HTTPFound(to_url)

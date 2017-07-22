import pyramid.renderers


class BaseController:

    def __init__(self, request):
        self.request = request

        #self.build_cache_id = static_cache.build_cache_id

        #grab layout and make available to all controllers
        layout_render = pyramid.renderers.get_renderer('mywebsite:templates/shared/_layout.pt')
        impl = layout_render.implementation()
        self.layout = impl.macros['layout']

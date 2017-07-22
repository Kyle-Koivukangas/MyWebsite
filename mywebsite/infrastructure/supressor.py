import pyramid_handlers

class suppress(pyramid_handlers.action):
    def __init__(self, _, **kw):
        kw['request_method'] = ["RanDoM_BuLLsHiT_ThAt_iS_noT_aN_HTTP_VeRb_oR_ReQuEsT"]
        super().__init__(**kw)

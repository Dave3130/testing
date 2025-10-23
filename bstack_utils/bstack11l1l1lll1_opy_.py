# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
class bstack1l11ll1l1_opy_:
    def __init__(self, handler):
        self._11l11ll1111_opy_ = None
        self.handler = handler
        self._11l11ll111l_opy_ = self.bstack11l11l1llll_opy_()
        self.patch()
    def patch(self):
        self._11l11ll1111_opy_ = self._11l11ll111l_opy_.execute
        self._11l11ll111l_opy_.execute = self.bstack11l11ll11l1_opy_()
    def bstack11l11ll11l1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack111111l_opy_ (u"ࠧࡨࡥࡧࡱࡵࡩࠧ᫘"), driver_command, None, this, args)
            response = self._11l11ll1111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack111111l_opy_ (u"ࠨࡡࡧࡶࡨࡶࠧ᫙"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll111l_opy_.execute = self._11l11ll1111_opy_
    @staticmethod
    def bstack11l11l1llll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
class bstack111ll1ll1l_opy_:
    def __init__(self, handler):
        self._11l11l1l111_opy_ = None
        self.handler = handler
        self._11l11l11lll_opy_ = self.bstack11l11l11ll1_opy_()
        self.patch()
    def patch(self):
        self._11l11l1l111_opy_ = self._11l11l11lll_opy_.execute
        self._11l11l11lll_opy_.execute = self.bstack11l11l11l1l_opy_()
    def bstack11l11l11l1l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11lll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᫿"), driver_command, None, this, args)
            response = self._11l11l1l111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11lll1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᬀ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l11lll_opy_.execute = self._11l11l1l111_opy_
    @staticmethod
    def bstack11l11l11ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
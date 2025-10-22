# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
class bstack11l11l1ll1_opy_:
    def __init__(self, handler):
        self._11l11l11lll_opy_ = None
        self.handler = handler
        self._11l11l11l1l_opy_ = self.bstack11l11l11ll1_opy_()
        self.patch()
    def patch(self):
        self._11l11l11lll_opy_ = self._11l11l11l1l_opy_.execute
        self._11l11l11l1l_opy_.execute = self.bstack11l11l11l11_opy_()
    def bstack11l11l11l11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l1l11_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᫿"), driver_command, None, this, args)
            response = self._11l11l11lll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l1l11_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᬀ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l11l1l_opy_.execute = self._11l11l11lll_opy_
    @staticmethod
    def bstack11l11l11ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
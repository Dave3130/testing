# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
class bstack1l111l11l_opy_:
    def __init__(self, handler):
        self._11l11l1l111_opy_ = None
        self.handler = handler
        self._11l11l1l1l1_opy_ = self.bstack11l11l1l1ll_opy_()
        self.patch()
    def patch(self):
        self._11l11l1l111_opy_ = self._11l11l1l1l1_opy_.execute
        self._11l11l1l1l1_opy_.execute = self.bstack11l11l1l11l_opy_()
    def bstack11l11l1l11l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᫸"), driver_command, None, this, args)
            response = self._11l11l1l111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤ᫹"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1l1l1_opy_.execute = self._11l11l1l111_opy_
    @staticmethod
    def bstack11l11l1l1ll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
class bstack1l1ll1ll11_opy_:
    def __init__(self, handler):
        self._11l11l1l11l_opy_ = None
        self.handler = handler
        self._11l11l1l111_opy_ = self.bstack11l11l1l1l1_opy_()
        self.patch()
    def patch(self):
        self._11l11l1l11l_opy_ = self._11l11l1l111_opy_.execute
        self._11l11l1l111_opy_.execute = self.bstack11l11l1l1ll_opy_()
    def bstack11l11l1l1ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l11l1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᫸"), driver_command, None, this, args)
            response = self._11l11l1l11l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l11l1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤ᫹"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1l111_opy_.execute = self._11l11l1l11l_opy_
    @staticmethod
    def bstack11l11l1l1l1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
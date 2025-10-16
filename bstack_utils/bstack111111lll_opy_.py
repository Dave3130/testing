# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
class bstack11ll11l111_opy_:
    def __init__(self, handler):
        self._11l11ll1l11_opy_ = None
        self.handler = handler
        self._11l11ll11l1_opy_ = self.bstack11l11ll111l_opy_()
        self.patch()
    def patch(self):
        self._11l11ll1l11_opy_ = self._11l11ll11l1_opy_.execute
        self._11l11ll11l1_opy_.execute = self.bstack11l11ll11ll_opy_()
    def bstack11l11ll11ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1lllll1_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤ᫣"), driver_command, None, this, args)
            response = self._11l11ll1l11_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1lllll1_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤ᫤"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll11l1_opy_.execute = self._11l11ll1l11_opy_
    @staticmethod
    def bstack11l11ll111l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
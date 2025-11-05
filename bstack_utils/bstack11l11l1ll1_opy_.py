# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
class bstack11ll1l111l_opy_:
    def __init__(self, handler):
        self._11l11l111l1_opy_ = None
        self.handler = handler
        self._11l11l1111l_opy_ = self.bstack11l11l111ll_opy_()
        self.patch()
    def patch(self):
        self._11l11l111l1_opy_ = self._11l11l1111l_opy_.execute
        self._11l11l1111l_opy_.execute = self.bstack11l11l11l11_opy_()
    def bstack11l11l11l11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1lll11l_opy_ (u"ࠤࡥࡩ࡫ࡵࡲࡦࠤᬔ"), driver_command, None, this, args)
            response = self._11l11l111l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1lll11l_opy_ (u"ࠥࡥ࡫ࡺࡥࡳࠤᬕ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1111l_opy_.execute = self._11l11l111l1_opy_
    @staticmethod
    def bstack11l11l111ll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
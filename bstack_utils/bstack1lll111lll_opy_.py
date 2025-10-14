# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
class bstack1l1lll1ll_opy_:
    def __init__(self, handler):
        self._11l11ll11l1_opy_ = None
        self.handler = handler
        self._11l11l1llll_opy_ = self.bstack11l11ll111l_opy_()
        self.patch()
    def patch(self):
        self._11l11ll11l1_opy_ = self._11l11l1llll_opy_.execute
        self._11l11l1llll_opy_.execute = self.bstack11l11ll1111_opy_()
    def bstack11l11ll1111_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l1l11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣ᫛"), driver_command, None, this, args)
            response = self._11l11ll11l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l1l11_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣ᫜"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1llll_opy_.execute = self._11l11ll11l1_opy_
    @staticmethod
    def bstack11l11ll111l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
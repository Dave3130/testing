# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
class bstack1l111111ll_opy_:
    def __init__(self, handler):
        self._11l11ll11l1_opy_ = None
        self.handler = handler
        self._11l11ll11ll_opy_ = self.bstack11l11ll111l_opy_()
        self.patch()
    def patch(self):
        self._11l11ll11l1_opy_ = self._11l11ll11ll_opy_.execute
        self._11l11ll11ll_opy_.execute = self.bstack11l11ll1l11_opy_()
    def bstack11l11ll1l11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1ll11_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣ᫢"), driver_command, None, this, args)
            response = self._11l11ll11l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1ll11_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣ᫣"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll11ll_opy_.execute = self._11l11ll11l1_opy_
    @staticmethod
    def bstack11l11ll111l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
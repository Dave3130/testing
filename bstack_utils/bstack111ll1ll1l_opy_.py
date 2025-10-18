# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
class bstack111l11l111_opy_:
    def __init__(self, handler):
        self._11l11l1l111_opy_ = None
        self.handler = handler
        self._11l11l11lll_opy_ = self.bstack11l11l11ll1_opy_()
        self.patch()
    def patch(self):
        self._11l11l1l111_opy_ = self._11l11l11lll_opy_.execute
        self._11l11l11lll_opy_.execute = self.bstack11l11l1l11l_opy_()
    def bstack11l11l1l11l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l111_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᬅ"), driver_command, None, this, args)
            response = self._11l11l1l111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l111_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᬆ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l11lll_opy_.execute = self._11l11l1l111_opy_
    @staticmethod
    def bstack11l11l11ll1_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
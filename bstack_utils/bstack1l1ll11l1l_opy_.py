# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
class bstack11ll11llll_opy_:
    def __init__(self, handler):
        self._11l111lllll_opy_ = None
        self.handler = handler
        self._11l11l11111_opy_ = self.bstack11l111lll1l_opy_()
        self.patch()
    def patch(self):
        self._11l111lllll_opy_ = self._11l11l11111_opy_.execute
        self._11l11l11111_opy_.execute = self.bstack11l111llll1_opy_()
    def bstack11l111llll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11ll1ll_opy_ (u"ࠣࡤࡨࡪࡴࡸࡥࠣᬯ"), driver_command, None, this, args)
            response = self._11l111lllll_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11ll1ll_opy_ (u"ࠤࡤࡪࡹ࡫ࡲࠣᬰ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l11111_opy_.execute = self._11l111lllll_opy_
    @staticmethod
    def bstack11l111lll1l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
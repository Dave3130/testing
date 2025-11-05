# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
class bstack1lll11l111_opy_:
    def __init__(self, handler):
        self._11l111llll1_opy_ = None
        self.handler = handler
        self._11l111lll1l_opy_ = self.bstack11l11l11111_opy_()
        self.patch()
    def patch(self):
        self._11l111llll1_opy_ = self._11l111lll1l_opy_.execute
        self._11l111lll1l_opy_.execute = self.bstack11l111lllll_opy_()
    def bstack11l111lllll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫ࠢᬮ"), driver_command, None, this, args)
            response = self._11l111llll1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11111_opy_ (u"ࠣࡣࡩࡸࡪࡸࠢᬯ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l111lll1l_opy_.execute = self._11l111llll1_opy_
    @staticmethod
    def bstack11l11l11111_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
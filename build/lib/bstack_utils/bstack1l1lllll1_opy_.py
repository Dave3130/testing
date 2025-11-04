# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
class bstack111111llll_opy_:
    def __init__(self, handler):
        self._11l111llll1_opy_ = None
        self.handler = handler
        self._11l111lll1l_opy_ = self.bstack11l111lllll_opy_()
        self.patch()
    def patch(self):
        self._11l111llll1_opy_ = self._11l111lll1l_opy_.execute
        self._11l111lll1l_opy_.execute = self.bstack11l11l11111_opy_()
    def bstack11l11l11111_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l1111_opy_ (u"ࠢࡣࡧࡩࡳࡷ࡫ࠢᬮ"), driver_command, None, this, args)
            response = self._11l111llll1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l1111_opy_ (u"ࠣࡣࡩࡸࡪࡸࠢᬯ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l111lll1l_opy_.execute = self._11l111llll1_opy_
    @staticmethod
    def bstack11l111lllll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
class bstack11ll1ll11_opy_:
    def __init__(self, handler):
        self._11l11l1l11l_opy_ = None
        self.handler = handler
        self._11l11l1l111_opy_ = self.bstack11l11l11lll_opy_()
        self.patch()
    def patch(self):
        self._11l11l1l11l_opy_ = self._11l11l1l111_opy_.execute
        self._11l11l1l111_opy_.execute = self.bstack11l11l11ll1_opy_()
    def bstack11l11l11ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1lllll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨᬃ"), driver_command, None, this, args)
            response = self._11l11l1l11l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1lllll1l_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨᬄ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1l111_opy_.execute = self._11l11l1l11l_opy_
    @staticmethod
    def bstack11l11l11lll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
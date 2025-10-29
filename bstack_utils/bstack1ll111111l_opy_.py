# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
class bstack11l1lll1l1_opy_:
    def __init__(self, handler):
        self._11l11l11l1l_opy_ = None
        self.handler = handler
        self._11l11l111l1_opy_ = self.bstack11l11l11l11_opy_()
        self.patch()
    def patch(self):
        self._11l11l11l1l_opy_ = self._11l11l111l1_opy_.execute
        self._11l11l111l1_opy_.execute = self.bstack11l11l111ll_opy_()
    def bstack11l11l111ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l11ll_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨᬟ"), driver_command, None, this, args)
            response = self._11l11l11l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l11ll_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨᬠ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l111l1_opy_.execute = self._11l11l11l1l_opy_
    @staticmethod
    def bstack11l11l11l11_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
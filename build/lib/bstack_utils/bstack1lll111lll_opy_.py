# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
class bstack1l111l1ll1_opy_:
    def __init__(self, handler):
        self._11l11ll1111_opy_ = None
        self.handler = handler
        self._11l11l1lll1_opy_ = self.bstack11l11l1llll_opy_()
        self.patch()
    def patch(self):
        self._11l11ll1111_opy_ = self._11l11l1lll1_opy_.execute
        self._11l11l1lll1_opy_.execute = self.bstack11l11ll111l_opy_()
    def bstack11l11ll111l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨ᫒"), driver_command, None, this, args)
            response = self._11l11ll1111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11111_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨ᫓"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1lll1_opy_.execute = self._11l11ll1111_opy_
    @staticmethod
    def bstack11l11l1llll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
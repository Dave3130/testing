# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
class bstack111l1lll1l_opy_:
    def __init__(self, handler):
        self._11l11l1ll1l_opy_ = None
        self.handler = handler
        self._11l11l1llll_opy_ = self.bstack11l11ll1111_opy_()
        self.patch()
    def patch(self):
        self._11l11l1ll1l_opy_ = self._11l11l1llll_opy_.execute
        self._11l11l1llll_opy_.execute = self.bstack11l11l1lll1_opy_()
    def bstack11l11l1lll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11l111_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨ᫒"), driver_command, None, this, args)
            response = self._11l11l1ll1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11l111_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨ᫓"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1llll_opy_.execute = self._11l11l1ll1l_opy_
    @staticmethod
    def bstack11l11ll1111_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
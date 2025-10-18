# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
class bstack1lll1l111l_opy_:
    def __init__(self, handler):
        self._11l11ll1111_opy_ = None
        self.handler = handler
        self._11l11ll111l_opy_ = self.bstack11l11l1llll_opy_()
        self.patch()
    def patch(self):
        self._11l11ll1111_opy_ = self._11l11ll111l_opy_.execute
        self._11l11ll111l_opy_.execute = self.bstack11l11l1lll1_opy_()
    def bstack11l11l1lll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l1lll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࠦ᫞"), driver_command, None, this, args)
            response = self._11l11ll1111_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l1lll1_opy_ (u"ࠧࡧࡦࡵࡧࡵࠦ᫟"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll111l_opy_.execute = self._11l11ll1111_opy_
    @staticmethod
    def bstack11l11l1llll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
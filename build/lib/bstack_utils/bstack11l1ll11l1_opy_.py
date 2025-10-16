# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
class bstack111l11111_opy_:
    def __init__(self, handler):
        self._11l11ll111l_opy_ = None
        self.handler = handler
        self._11l11ll11l1_opy_ = self.bstack11l11ll1l11_opy_()
        self.patch()
    def patch(self):
        self._11l11ll111l_opy_ = self._11l11ll11l1_opy_.execute
        self._11l11ll11l1_opy_.execute = self.bstack11l11ll11ll_opy_()
    def bstack11l11ll11ll_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࠦ᫥"), driver_command, None, this, args)
            response = self._11l11ll111l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l_opy_ (u"ࠧࡧࡦࡵࡧࡵࠦ᫦"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll11l1_opy_.execute = self._11l11ll111l_opy_
    @staticmethod
    def bstack11l11ll1l11_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
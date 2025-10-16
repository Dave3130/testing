# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
class bstack11lll11l11_opy_:
    def __init__(self, handler):
        self._11l11ll11l1_opy_ = None
        self.handler = handler
        self._11l11ll1l11_opy_ = self.bstack11l11ll11ll_opy_()
        self.patch()
    def patch(self):
        self._11l11ll11l1_opy_ = self._11l11ll1l11_opy_.execute
        self._11l11ll1l11_opy_.execute = self.bstack11l11ll111l_opy_()
    def bstack11l11ll111l_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1ll1ll1_opy_ (u"ࠦࡧ࡫ࡦࡰࡴࡨࠦ᫥"), driver_command, None, this, args)
            response = self._11l11ll11l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1ll1ll1_opy_ (u"ࠧࡧࡦࡵࡧࡵࠦ᫦"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll1l11_opy_.execute = self._11l11ll11l1_opy_
    @staticmethod
    def bstack11l11ll11ll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
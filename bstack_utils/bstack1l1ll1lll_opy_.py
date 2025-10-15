# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
class bstack1llllll11l_opy_:
    def __init__(self, handler):
        self._11l11ll11l1_opy_ = None
        self.handler = handler
        self._11l11ll111l_opy_ = self.bstack11l11l1llll_opy_()
        self.patch()
    def patch(self):
        self._11l11ll11l1_opy_ = self._11l11ll111l_opy_.execute
        self._11l11ll111l_opy_.execute = self.bstack11l11ll1111_opy_()
    def bstack11l11ll1111_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1ll1l_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࠥ᫝"), driver_command, None, this, args)
            response = self._11l11ll11l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1ll1l_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࠥ᫞"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11ll111l_opy_.execute = self._11l11ll11l1_opy_
    @staticmethod
    def bstack11l11l1llll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
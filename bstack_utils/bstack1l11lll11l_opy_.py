# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
class bstack1111l1l11_opy_:
    def __init__(self, handler):
        self._11l11l11l1l_opy_ = None
        self.handler = handler
        self._11l11l11l11_opy_ = self.bstack11l11l11lll_opy_()
        self.patch()
    def patch(self):
        self._11l11l11l1l_opy_ = self._11l11l11l11_opy_.execute
        self._11l11l11l11_opy_.execute = self.bstack11l11l11ll1_opy_()
    def bstack11l11l11ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack1l111ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࠥᬀ"), driver_command, None, this, args)
            response = self._11l11l11l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack1l111ll_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࠥᬁ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l11l11_opy_.execute = self._11l11l11l1l_opy_
    @staticmethod
    def bstack11l11l11lll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
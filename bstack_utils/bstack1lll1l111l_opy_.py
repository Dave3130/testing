# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
class bstack11l111ll11_opy_:
    def __init__(self, handler):
        self._11l11l11l1l_opy_ = None
        self.handler = handler
        self._11l11l1l111_opy_ = self.bstack11l11l11lll_opy_()
        self.patch()
    def patch(self):
        self._11l11l11l1l_opy_ = self._11l11l1l111_opy_.execute
        self._11l11l1l111_opy_.execute = self.bstack11l11l11ll1_opy_()
    def bstack11l11l11ll1_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11ll_opy_ (u"ࠥࡦࡪ࡬࡯ࡳࡧࠥᬇ"), driver_command, None, this, args)
            response = self._11l11l11l1l_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11ll_opy_ (u"ࠦࡦ࡬ࡴࡦࡴࠥᬈ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l1l111_opy_.execute = self._11l11l11l1l_opy_
    @staticmethod
    def bstack11l11l11lll_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
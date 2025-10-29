# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
class bstack11l1llll11_opy_:
    def __init__(self, handler):
        self._11l11l111l1_opy_ = None
        self.handler = handler
        self._11l11l111ll_opy_ = self.bstack11l11l11l1l_opy_()
        self.patch()
    def patch(self):
        self._11l11l111l1_opy_ = self._11l11l111ll_opy_.execute
        self._11l11l111ll_opy_.execute = self.bstack11l11l11l11_opy_()
    def bstack11l11l11l11_opy_(self):
        def execute(this, driver_command, *args, **kwargs):
            self.handler(bstack11ll1l_opy_ (u"ࠨࡢࡦࡨࡲࡶࡪࠨᬟ"), driver_command, None, this, args)
            response = self._11l11l111l1_opy_(this, driver_command, *args, **kwargs)
            self.handler(bstack11ll1l_opy_ (u"ࠢࡢࡨࡷࡩࡷࠨᬠ"), driver_command, response)
            return response
        return execute
    def reset(self):
        self._11l11l111ll_opy_.execute = self._11l11l111l1_opy_
    @staticmethod
    def bstack11l11l11l1l_opy_():
        from selenium.webdriver.remote.webdriver import WebDriver
        return WebDriver
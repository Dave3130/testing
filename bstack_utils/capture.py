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
import builtins
import logging
class bstack1l111l11_opy_:
    def __init__(self, handler):
        self._111lll11111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1ll1ll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l1lll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩ᮷"), bstack1l1lll1_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫ᮸"), bstack1l1lll1_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧ᮹"), bstack1l1lll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᮺ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1llll1_opy_
        self._111ll1lll1l_opy_()
    def _111ll1llll1_opy_(self, *args, **kwargs):
        self._111lll11111_opy_(*args, **kwargs)
        message = bstack1l1lll1_opy_ (u"ࠨࠢࠪᮻ").join(map(str, args)) + bstack1l1lll1_opy_ (u"ࠩ࡟ࡲࠬᮼ")
        self._log_message(bstack1l1lll1_opy_ (u"ࠪࡍࡓࡌࡏࠨᮽ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l1lll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᮾ"): level, bstack1l1lll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᮿ"): msg})
    def _111ll1lll1l_opy_(self):
        for level, bstack111ll1lll11_opy_ in self._111ll1ll1ll_opy_.items():
            setattr(logging, level, self._111ll1lllll_opy_(level, bstack111ll1lll11_opy_))
    def _111ll1lllll_opy_(self, level, bstack111ll1lll11_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1lll11_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll11111_opy_
        for level, bstack111ll1lll11_opy_ in self._111ll1ll1ll_opy_.items():
            setattr(logging, level, bstack111ll1lll11_opy_)
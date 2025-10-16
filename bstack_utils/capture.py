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
import builtins
import logging
class bstack1ll111l1_opy_:
    def __init__(self, handler):
        self._111lll111l1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111lll1111l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1ll1ll1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᮾ"), bstack1ll1ll1_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᮿ"), bstack1ll1ll1_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᯀ"), bstack1ll1ll1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᯁ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1llll1_opy_
        self._111lll111ll_opy_()
    def _111ll1llll1_opy_(self, *args, **kwargs):
        self._111lll111l1_opy_(*args, **kwargs)
        message = bstack1ll1ll1_opy_ (u"ࠨࠢࠪᯂ").join(map(str, args)) + bstack1ll1ll1_opy_ (u"ࠩ࡟ࡲࠬᯃ")
        self._log_message(bstack1ll1ll1_opy_ (u"ࠪࡍࡓࡌࡏࠨᯄ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1ll1ll1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᯅ"): level, bstack1ll1ll1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᯆ"): msg})
    def _111lll111ll_opy_(self):
        for level, bstack111ll1lllll_opy_ in self._111lll1111l_opy_.items():
            setattr(logging, level, self._111lll11111_opy_(level, bstack111ll1lllll_opy_))
    def _111lll11111_opy_(self, level, bstack111ll1lllll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1lllll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll111l1_opy_
        for level, bstack111ll1lllll_opy_ in self._111lll1111l_opy_.items():
            setattr(logging, level, bstack111ll1lllll_opy_)
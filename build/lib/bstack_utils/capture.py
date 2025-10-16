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
import builtins
import logging
class bstack11llll11_opy_:
    def __init__(self, handler):
        self._111ll1lllll_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111lll111l1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᮾ"), bstack1l_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᮿ"), bstack1l_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᯀ"), bstack1l_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᯁ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111lll11111_opy_
        self._111lll1111l_opy_()
    def _111lll11111_opy_(self, *args, **kwargs):
        self._111ll1lllll_opy_(*args, **kwargs)
        message = bstack1l_opy_ (u"ࠨࠢࠪᯂ").join(map(str, args)) + bstack1l_opy_ (u"ࠩ࡟ࡲࠬᯃ")
        self._log_message(bstack1l_opy_ (u"ࠪࡍࡓࡌࡏࠨᯄ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᯅ"): level, bstack1l_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᯆ"): msg})
    def _111lll1111l_opy_(self):
        for level, bstack111ll1llll1_opy_ in self._111lll111l1_opy_.items():
            setattr(logging, level, self._111lll111ll_opy_(level, bstack111ll1llll1_opy_))
    def _111lll111ll_opy_(self, level, bstack111ll1llll1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1llll1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1lllll_opy_
        for level, bstack111ll1llll1_opy_ in self._111lll111l1_opy_.items():
            setattr(logging, level, bstack111ll1llll1_opy_)
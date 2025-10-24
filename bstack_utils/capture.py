# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import builtins
import logging
class bstack1ll1llll_opy_:
    def __init__(self, handler):
        self._111ll1l1l11_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l1l1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1l1_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᯓ"), bstack1l1_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᯔ"), bstack1l1_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᯕ"), bstack1l1_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᯖ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l1ll1_opy_
        self._111ll1ll11l_opy_()
    def _111ll1l1ll1_opy_(self, *args, **kwargs):
        self._111ll1l1l11_opy_(*args, **kwargs)
        message = bstack1l1_opy_ (u"ࠨࠢࠪᯗ").join(map(str, args)) + bstack1l1_opy_ (u"ࠩ࡟ࡲࠬᯘ")
        self._log_message(bstack1l1_opy_ (u"ࠪࡍࡓࡌࡏࠨᯙ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1l1_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᯚ"): level, bstack1l1_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᯛ"): msg})
    def _111ll1ll11l_opy_(self):
        for level, bstack111ll1l1lll_opy_ in self._111ll1l1l1l_opy_.items():
            setattr(logging, level, self._111ll1ll111_opy_(level, bstack111ll1l1lll_opy_))
    def _111ll1ll111_opy_(self, level, bstack111ll1l1lll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l1lll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1l11_opy_
        for level, bstack111ll1l1lll_opy_ in self._111ll1l1l1l_opy_.items():
            setattr(logging, level, bstack111ll1l1lll_opy_)
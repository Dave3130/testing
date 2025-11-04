# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import builtins
import logging
class bstack1ll11l11_opy_:
    def __init__(self, handler):
        self._111ll11l11l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll11ll1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l1111_opy_ (u"ࠫ࡮ࡴࡦࡰࠩᰋ"), bstack11l1111_opy_ (u"ࠬࡪࡥࡣࡷࡪࠫᰌ"), bstack11l1111_opy_ (u"࠭ࡷࡢࡴࡱ࡭ࡳ࡭ࠧᰍ"), bstack11l1111_opy_ (u"ࠧࡦࡴࡵࡳࡷ࠭ᰎ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll11ll11_opy_
        self._111ll11l1l1_opy_()
    def _111ll11ll11_opy_(self, *args, **kwargs):
        self._111ll11l11l_opy_(*args, **kwargs)
        message = bstack11l1111_opy_ (u"ࠨࠢࠪᰏ").join(map(str, args)) + bstack11l1111_opy_ (u"ࠩ࡟ࡲࠬᰐ")
        self._log_message(bstack11l1111_opy_ (u"ࠪࡍࡓࡌࡏࠨᰑ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l1111_opy_ (u"ࠫࡱ࡫ࡶࡦ࡮ࠪᰒ"): level, bstack11l1111_opy_ (u"ࠬࡳࡥࡴࡵࡤ࡫ࡪ࠭ᰓ"): msg})
    def _111ll11l1l1_opy_(self):
        for level, bstack111ll11l1ll_opy_ in self._111ll11ll1l_opy_.items():
            setattr(logging, level, self._111ll11l111_opy_(level, bstack111ll11l1ll_opy_))
    def _111ll11l111_opy_(self, level, bstack111ll11l1ll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll11l1ll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll11l11l_opy_
        for level, bstack111ll11l1ll_opy_ in self._111ll11ll1l_opy_.items():
            setattr(logging, level, bstack111ll11l1ll_opy_)
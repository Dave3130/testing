# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import builtins
import logging
class bstack1l1l111l_opy_:
    def __init__(self, handler):
        self._111ll11l1ll_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll11ll1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11111_opy_ (u"ࠬ࡯࡮ࡧࡱࠪᰌ"), bstack11111_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬᰍ"), bstack11111_opy_ (u"ࠧࡸࡣࡵࡲ࡮ࡴࡧࠨᰎ"), bstack11111_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧᰏ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll11l1l1_opy_
        self._111ll11ll11_opy_()
    def _111ll11l1l1_opy_(self, *args, **kwargs):
        self._111ll11l1ll_opy_(*args, **kwargs)
        message = bstack11111_opy_ (u"ࠩࠣࠫᰐ").join(map(str, args)) + bstack11111_opy_ (u"ࠪࡠࡳ࠭ᰑ")
        self._log_message(bstack11111_opy_ (u"ࠫࡎࡔࡆࡐࠩᰒ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11111_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫᰓ"): level, bstack11111_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧᰔ"): msg})
    def _111ll11ll11_opy_(self):
        for level, bstack111ll11lll1_opy_ in self._111ll11ll1l_opy_.items():
            setattr(logging, level, self._111ll11l11l_opy_(level, bstack111ll11lll1_opy_))
    def _111ll11l11l_opy_(self, level, bstack111ll11lll1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll11lll1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll11l1ll_opy_
        for level, bstack111ll11lll1_opy_ in self._111ll11ll1l_opy_.items():
            setattr(logging, level, bstack111ll11lll1_opy_)
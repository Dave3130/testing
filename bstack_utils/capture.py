# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import builtins
import logging
class bstack1ll1l1ll_opy_:
    def __init__(self, handler):
        self._111ll11l1l1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll11l11l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11ll1ll_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᰍ"), bstack11ll1ll_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᰎ"), bstack11ll1ll_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᰏ"), bstack11ll1ll_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᰐ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll11l1ll_opy_
        self._111ll11ll1l_opy_()
    def _111ll11l1ll_opy_(self, *args, **kwargs):
        self._111ll11l1l1_opy_(*args, **kwargs)
        message = bstack11ll1ll_opy_ (u"ࠪࠤࠬᰑ").join(map(str, args)) + bstack11ll1ll_opy_ (u"ࠫࡡࡴࠧᰒ")
        self._log_message(bstack11ll1ll_opy_ (u"ࠬࡏࡎࡇࡑࠪᰓ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11ll1ll_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᰔ"): level, bstack11ll1ll_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᰕ"): msg})
    def _111ll11ll1l_opy_(self):
        for level, bstack111ll11lll1_opy_ in self._111ll11l11l_opy_.items():
            setattr(logging, level, self._111ll11ll11_opy_(level, bstack111ll11lll1_opy_))
    def _111ll11ll11_opy_(self, level, bstack111ll11lll1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll11lll1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll11l1l1_opy_
        for level, bstack111ll11lll1_opy_ in self._111ll11l11l_opy_.items():
            setattr(logging, level, bstack111ll11lll1_opy_)
# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import builtins
import logging
class bstack1lll1ll1_opy_:
    def __init__(self, handler):
        self._111ll11ll1l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l1111_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1lll11l_opy_ (u"ࠧࡪࡰࡩࡳ᯲ࠬ"), bstack1lll11l_opy_ (u"ࠨࡦࡨࡦࡺ࡭᯳ࠧ"), bstack1lll11l_opy_ (u"ࠩࡺࡥࡷࡴࡩ࡯ࡩࠪ᯴"), bstack1lll11l_opy_ (u"ࠪࡩࡷࡸ࡯ࡳࠩ᯵")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l11l1_opy_
        self._111ll11lll1_opy_()
    def _111ll1l11l1_opy_(self, *args, **kwargs):
        self._111ll11ll1l_opy_(*args, **kwargs)
        message = bstack1lll11l_opy_ (u"ࠫࠥ࠭᯶").join(map(str, args)) + bstack1lll11l_opy_ (u"ࠬࡢ࡮ࠨ᯷")
        self._log_message(bstack1lll11l_opy_ (u"࠭ࡉࡏࡈࡒࠫ᯸"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1lll11l_opy_ (u"ࠧ࡭ࡧࡹࡩࡱ࠭᯹"): level, bstack1lll11l_opy_ (u"ࠨ࡯ࡨࡷࡸࡧࡧࡦࠩ᯺"): msg})
    def _111ll11lll1_opy_(self):
        for level, bstack111ll11llll_opy_ in self._111ll1l1111_opy_.items():
            setattr(logging, level, self._111ll1l111l_opy_(level, bstack111ll11llll_opy_))
    def _111ll1l111l_opy_(self, level, bstack111ll11llll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll11llll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll11ll1l_opy_
        for level, bstack111ll11llll_opy_ in self._111ll1l1111_opy_.items():
            setattr(logging, level, bstack111ll11llll_opy_)
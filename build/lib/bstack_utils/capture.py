# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import builtins
import logging
class bstack1lll11ll_opy_:
    def __init__(self, handler):
        self._111ll1l1l1l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l11ll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11lll1_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᯘ"), bstack11lll1_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᯙ"), bstack11lll1_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬᯚ"), bstack11lll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᯛ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l11l1_opy_
        self._111ll1l1ll1_opy_()
    def _111ll1l11l1_opy_(self, *args, **kwargs):
        self._111ll1l1l1l_opy_(*args, **kwargs)
        message = bstack11lll1_opy_ (u"࠭ࠠࠨᯜ").join(map(str, args)) + bstack11lll1_opy_ (u"ࠧ࡝ࡰࠪᯝ")
        self._log_message(bstack11lll1_opy_ (u"ࠨࡋࡑࡊࡔ࠭ᯞ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11lll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᯟ"): level, bstack11lll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᯠ"): msg})
    def _111ll1l1ll1_opy_(self):
        for level, bstack111ll1l1l11_opy_ in self._111ll1l11ll_opy_.items():
            setattr(logging, level, self._111ll1l1lll_opy_(level, bstack111ll1l1l11_opy_))
    def _111ll1l1lll_opy_(self, level, bstack111ll1l1l11_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l1l11_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1l1l_opy_
        for level, bstack111ll1l1l11_opy_ in self._111ll1l11ll_opy_.items():
            setattr(logging, level, bstack111ll1l1l11_opy_)
# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import builtins
import logging
class bstack1l1ll111_opy_:
    def __init__(self, handler):
        self._111ll1l1ll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l1l11_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l1l11_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᯘ"), bstack11l1l11_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᯙ"), bstack11l1l11_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬᯚ"), bstack11l1l11_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᯛ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l111l_opy_
        self._111ll1l1l1l_opy_()
    def _111ll1l111l_opy_(self, *args, **kwargs):
        self._111ll1l1ll1_opy_(*args, **kwargs)
        message = bstack11l1l11_opy_ (u"࠭ࠠࠨᯜ").join(map(str, args)) + bstack11l1l11_opy_ (u"ࠧ࡝ࡰࠪᯝ")
        self._log_message(bstack11l1l11_opy_ (u"ࠨࡋࡑࡊࡔ࠭ᯞ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l1l11_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᯟ"): level, bstack11l1l11_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᯠ"): msg})
    def _111ll1l1l1l_opy_(self):
        for level, bstack111ll1l11ll_opy_ in self._111ll1l1l11_opy_.items():
            setattr(logging, level, self._111ll1l11l1_opy_(level, bstack111ll1l11ll_opy_))
    def _111ll1l11l1_opy_(self, level, bstack111ll1l11ll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l11ll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1ll1_opy_
        for level, bstack111ll1l11ll_opy_ in self._111ll1l1l11_opy_.items():
            setattr(logging, level, bstack111ll1l11ll_opy_)
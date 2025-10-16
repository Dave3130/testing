# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import builtins
import logging
class bstack1ll111l1_opy_:
    def __init__(self, handler):
        self._111lll1111l_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1lllll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1lllll1_opy_ (u"ࠩ࡬ࡲ࡫ࡵࠧᮼ"), bstack1lllll1_opy_ (u"ࠪࡨࡪࡨࡵࡨࠩᮽ"), bstack1lllll1_opy_ (u"ࠫࡼࡧࡲ࡯࡫ࡱ࡫ࠬᮾ"), bstack1lllll1_opy_ (u"ࠬ࡫ࡲࡳࡱࡵࠫᮿ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111lll111ll_opy_
        self._111ll1llll1_opy_()
    def _111lll111ll_opy_(self, *args, **kwargs):
        self._111lll1111l_opy_(*args, **kwargs)
        message = bstack1lllll1_opy_ (u"࠭ࠠࠨᯀ").join(map(str, args)) + bstack1lllll1_opy_ (u"ࠧ࡝ࡰࠪᯁ")
        self._log_message(bstack1lllll1_opy_ (u"ࠨࡋࡑࡊࡔ࠭ᯂ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1lllll1_opy_ (u"ࠩ࡯ࡩࡻ࡫࡬ࠨᯃ"): level, bstack1lllll1_opy_ (u"ࠪࡱࡪࡹࡳࡢࡩࡨࠫᯄ"): msg})
    def _111ll1llll1_opy_(self):
        for level, bstack111lll11111_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, self._111lll111l1_opy_(level, bstack111lll11111_opy_))
    def _111lll111l1_opy_(self, level, bstack111lll11111_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111lll11111_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll1111l_opy_
        for level, bstack111lll11111_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, bstack111lll11111_opy_)
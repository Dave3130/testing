# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import builtins
import logging
class bstack1ll1lll1_opy_:
    def __init__(self, handler):
        self._111lll11111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1llll1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1ll1l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨ᮶"), bstack1ll1l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪ᮷"), bstack1ll1l_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭᮸"), bstack1ll1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬ᮹")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1lll11_opy_
        self._111ll1lllll_opy_()
    def _111ll1lll11_opy_(self, *args, **kwargs):
        self._111lll11111_opy_(*args, **kwargs)
        message = bstack1ll1l_opy_ (u"ࠧࠡࠩᮺ").join(map(str, args)) + bstack1ll1l_opy_ (u"ࠨ࡞ࡱࠫᮻ")
        self._log_message(bstack1ll1l_opy_ (u"ࠩࡌࡒࡋࡕࠧᮼ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1ll1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᮽ"): level, bstack1ll1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᮾ"): msg})
    def _111ll1lllll_opy_(self):
        for level, bstack111ll1lll1l_opy_ in self._111ll1llll1_opy_.items():
            setattr(logging, level, self._111lll1111l_opy_(level, bstack111ll1lll1l_opy_))
    def _111lll1111l_opy_(self, level, bstack111ll1lll1l_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1lll1l_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll11111_opy_
        for level, bstack111ll1lll1l_opy_ in self._111ll1llll1_opy_.items():
            setattr(logging, level, bstack111ll1lll1l_opy_)
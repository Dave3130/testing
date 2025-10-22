# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import builtins
import logging
class bstack1l1ll1ll_opy_:
    def __init__(self, handler):
        self._111ll1l1ll1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l111l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack111l1l_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᯙ"), bstack111l1l_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪᯚ"), bstack111l1l_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ᯛ"), bstack111l1l_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᯜ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l11ll_opy_
        self._111ll1l1l1l_opy_()
    def _111ll1l11ll_opy_(self, *args, **kwargs):
        self._111ll1l1ll1_opy_(*args, **kwargs)
        message = bstack111l1l_opy_ (u"ࠧࠡࠩᯝ").join(map(str, args)) + bstack111l1l_opy_ (u"ࠨ࡞ࡱࠫᯞ")
        self._log_message(bstack111l1l_opy_ (u"ࠩࡌࡒࡋࡕࠧᯟ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack111l1l_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᯠ"): level, bstack111l1l_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᯡ"): msg})
    def _111ll1l1l1l_opy_(self):
        for level, bstack111ll1l11l1_opy_ in self._111ll1l111l_opy_.items():
            setattr(logging, level, self._111ll1l1l11_opy_(level, bstack111ll1l11l1_opy_))
    def _111ll1l1l11_opy_(self, level, bstack111ll1l11l1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l11l1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1ll1_opy_
        for level, bstack111ll1l11l1_opy_ in self._111ll1l111l_opy_.items():
            setattr(logging, level, bstack111ll1l11l1_opy_)
# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import builtins
import logging
class bstack1ll1ll1l_opy_:
    def __init__(self, handler):
        self._111ll1l1l11_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l11l1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11ll_opy_ (u"ࠪ࡭ࡳ࡬࡯ࠨᯠ"), bstack11ll_opy_ (u"ࠫࡩ࡫ࡢࡶࡩࠪᯡ"), bstack11ll_opy_ (u"ࠬࡽࡡࡳࡰ࡬ࡲ࡬࠭ᯢ"), bstack11ll_opy_ (u"࠭ࡥࡳࡴࡲࡶࠬᯣ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l11ll_opy_
        self._111ll1l1l1l_opy_()
    def _111ll1l11ll_opy_(self, *args, **kwargs):
        self._111ll1l1l11_opy_(*args, **kwargs)
        message = bstack11ll_opy_ (u"ࠧࠡࠩᯤ").join(map(str, args)) + bstack11ll_opy_ (u"ࠨ࡞ࡱࠫᯥ")
        self._log_message(bstack11ll_opy_ (u"ࠩࡌࡒࡋࡕ᯦ࠧ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11ll_opy_ (u"ࠪࡰࡪࡼࡥ࡭ࠩᯧ"): level, bstack11ll_opy_ (u"ࠫࡲ࡫ࡳࡴࡣࡪࡩࠬᯨ"): msg})
    def _111ll1l1l1l_opy_(self):
        for level, bstack111ll1l1lll_opy_ in self._111ll1l11l1_opy_.items():
            setattr(logging, level, self._111ll1l1ll1_opy_(level, bstack111ll1l1lll_opy_))
    def _111ll1l1ll1_opy_(self, level, bstack111ll1l1lll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l1lll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1l11_opy_
        for level, bstack111ll1l1lll_opy_ in self._111ll1l11l1_opy_.items():
            setattr(logging, level, bstack111ll1l1lll_opy_)
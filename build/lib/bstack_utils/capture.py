# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import builtins
import logging
class bstack1lllll11_opy_:
    def __init__(self, handler):
        self._111lll11111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1ll1ll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11111_opy_ (u"࠭ࡩ࡯ࡨࡲ᮫ࠫ"), bstack11111_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᮬ"), bstack11111_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᮭ"), bstack11111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᮮ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1llll1_opy_
        self._111ll1lllll_opy_()
    def _111ll1llll1_opy_(self, *args, **kwargs):
        self._111lll11111_opy_(*args, **kwargs)
        message = bstack11111_opy_ (u"ࠪࠤࠬᮯ").join(map(str, args)) + bstack11111_opy_ (u"ࠫࡡࡴࠧ᮰")
        self._log_message(bstack11111_opy_ (u"ࠬࡏࡎࡇࡑࠪ᮱"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᮲"): level, bstack11111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᮳"): msg})
    def _111ll1lllll_opy_(self):
        for level, bstack111ll1lll1l_opy_ in self._111ll1ll1ll_opy_.items():
            setattr(logging, level, self._111ll1lll11_opy_(level, bstack111ll1lll1l_opy_))
    def _111ll1lll11_opy_(self, level, bstack111ll1lll1l_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1lll1l_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll11111_opy_
        for level, bstack111ll1lll1l_opy_ in self._111ll1ll1ll_opy_.items():
            setattr(logging, level, bstack111ll1lll1l_opy_)
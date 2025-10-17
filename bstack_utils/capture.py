# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import builtins
import logging
class bstack1lll111l_opy_:
    def __init__(self, handler):
        self._111ll1ll1l1_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1lll1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l111_opy_ (u"࠭ࡩ࡯ࡨࡲ᮫ࠫ"), bstack11l111_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᮬ"), bstack11l111_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᮭ"), bstack11l111_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᮮ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1lll11_opy_
        self._111ll1ll1ll_opy_()
    def _111ll1lll11_opy_(self, *args, **kwargs):
        self._111ll1ll1l1_opy_(*args, **kwargs)
        message = bstack11l111_opy_ (u"ࠪࠤࠬᮯ").join(map(str, args)) + bstack11l111_opy_ (u"ࠫࡡࡴࠧ᮰")
        self._log_message(bstack11l111_opy_ (u"ࠬࡏࡎࡇࡑࠪ᮱"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l111_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬ᮲"): level, bstack11l111_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨ᮳"): msg})
    def _111ll1ll1ll_opy_(self):
        for level, bstack111ll1lllll_opy_ in self._111ll1lll1l_opy_.items():
            setattr(logging, level, self._111ll1llll1_opy_(level, bstack111ll1lllll_opy_))
    def _111ll1llll1_opy_(self, level, bstack111ll1lllll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1lllll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1ll1l1_opy_
        for level, bstack111ll1lllll_opy_ in self._111ll1lll1l_opy_.items():
            setattr(logging, level, bstack111ll1lllll_opy_)
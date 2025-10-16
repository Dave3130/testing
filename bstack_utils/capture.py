# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import builtins
import logging
class bstack1l1l11ll_opy_:
    def __init__(self, handler):
        self._111lll11111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1lllll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1ll11_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᮻ"), bstack1ll11_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᮼ"), bstack1ll11_opy_ (u"ࠪࡻࡦࡸ࡮ࡪࡰࡪࠫᮽ"), bstack1ll11_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᮾ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1llll1_opy_
        self._111lll111l1_opy_()
    def _111ll1llll1_opy_(self, *args, **kwargs):
        self._111lll11111_opy_(*args, **kwargs)
        message = bstack1ll11_opy_ (u"ࠬࠦࠧᮿ").join(map(str, args)) + bstack1ll11_opy_ (u"࠭࡜࡯ࠩᯀ")
        self._log_message(bstack1ll11_opy_ (u"ࠧࡊࡐࡉࡓࠬᯁ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1ll11_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᯂ"): level, bstack1ll11_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᯃ"): msg})
    def _111lll111l1_opy_(self):
        for level, bstack111lll111ll_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, self._111lll1111l_opy_(level, bstack111lll111ll_opy_))
    def _111lll1111l_opy_(self, level, bstack111lll111ll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111lll111ll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll11111_opy_
        for level, bstack111lll111ll_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, bstack111lll111ll_opy_)
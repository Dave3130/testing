# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import builtins
import logging
class bstack1l111lll_opy_:
    def __init__(self, handler):
        self._111ll1l11ll_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll11lll1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l11ll_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭᯺"), bstack11l11ll_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨ᯻"), bstack11l11ll_opy_ (u"ࠪࡻࡦࡸ࡮ࡪࡰࡪࠫ᯼"), bstack11l11ll_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪ᯽")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l111l_opy_
        self._111ll1l1111_opy_()
    def _111ll1l111l_opy_(self, *args, **kwargs):
        self._111ll1l11ll_opy_(*args, **kwargs)
        message = bstack11l11ll_opy_ (u"ࠬࠦࠧ᯾").join(map(str, args)) + bstack11l11ll_opy_ (u"࠭࡜࡯ࠩ᯿")
        self._log_message(bstack11l11ll_opy_ (u"ࠧࡊࡐࡉࡓࠬᰀ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l11ll_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᰁ"): level, bstack11l11ll_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧࠪᰂ"): msg})
    def _111ll1l1111_opy_(self):
        for level, bstack111ll11llll_opy_ in self._111ll11lll1_opy_.items():
            setattr(logging, level, self._111ll1l11l1_opy_(level, bstack111ll11llll_opy_))
    def _111ll1l11l1_opy_(self, level, bstack111ll11llll_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll11llll_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l11ll_opy_
        for level, bstack111ll11llll_opy_ in self._111ll11lll1_opy_.items():
            setattr(logging, level, bstack111ll11llll_opy_)
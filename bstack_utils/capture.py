# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import builtins
import logging
class bstack1lll1l1l_opy_:
    def __init__(self, handler):
        self._111ll1ll111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l1l1l_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack11l111_opy_ (u"ࠨ࡫ࡱࡪࡴ࠭ᯞ"), bstack11l111_opy_ (u"ࠩࡧࡩࡧࡻࡧࠨᯟ"), bstack11l111_opy_ (u"ࠪࡻࡦࡸ࡮ࡪࡰࡪࠫᯠ"), bstack11l111_opy_ (u"ࠫࡪࡸࡲࡰࡴࠪᯡ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l1l11_opy_
        self._111ll1l1lll_opy_()
    def _111ll1l1l11_opy_(self, *args, **kwargs):
        self._111ll1ll111_opy_(*args, **kwargs)
        message = bstack11l111_opy_ (u"ࠬࠦࠧᯢ").join(map(str, args)) + bstack11l111_opy_ (u"࠭࡜࡯ࠩᯣ")
        self._log_message(bstack11l111_opy_ (u"ࠧࡊࡐࡉࡓࠬᯤ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack11l111_opy_ (u"ࠨ࡮ࡨࡺࡪࡲࠧᯥ"): level, bstack11l111_opy_ (u"ࠩࡰࡩࡸࡹࡡࡨࡧ᯦ࠪ"): msg})
    def _111ll1l1lll_opy_(self):
        for level, bstack111ll1l1ll1_opy_ in self._111ll1l1l1l_opy_.items():
            setattr(logging, level, self._111ll1l11ll_opy_(level, bstack111ll1l1ll1_opy_))
    def _111ll1l11ll_opy_(self, level, bstack111ll1l1ll1_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l1ll1_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1ll111_opy_
        for level, bstack111ll1l1ll1_opy_ in self._111ll1l1l1l_opy_.items():
            setattr(logging, level, bstack111ll1l1ll1_opy_)
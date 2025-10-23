# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import builtins
import logging
class bstack1l1lll1l_opy_:
    def __init__(self, handler):
        self._111lll11111_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1lllll_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack111111l_opy_ (u"ࠬ࡯࡮ࡧࡱࠪ᮱"), bstack111111l_opy_ (u"࠭ࡤࡦࡤࡸ࡫ࠬ᮲"), bstack111111l_opy_ (u"ࠧࡸࡣࡵࡲ࡮ࡴࡧࠨ᮳"), bstack111111l_opy_ (u"ࠨࡧࡵࡶࡴࡸࠧ᮴")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1llll1_opy_
        self._111ll1lll11_opy_()
    def _111ll1llll1_opy_(self, *args, **kwargs):
        self._111lll11111_opy_(*args, **kwargs)
        message = bstack111111l_opy_ (u"ࠩࠣࠫ᮵").join(map(str, args)) + bstack111111l_opy_ (u"ࠪࡠࡳ࠭᮶")
        self._log_message(bstack111111l_opy_ (u"ࠫࡎࡔࡆࡐࠩ᮷"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack111111l_opy_ (u"ࠬࡲࡥࡷࡧ࡯ࠫ᮸"): level, bstack111111l_opy_ (u"࠭࡭ࡦࡵࡶࡥ࡬࡫ࠧ᮹"): msg})
    def _111ll1lll11_opy_(self):
        for level, bstack111lll1111l_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, self._111ll1lll1l_opy_(level, bstack111lll1111l_opy_))
    def _111ll1lll1l_opy_(self, level, bstack111lll1111l_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111lll1111l_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111lll11111_opy_
        for level, bstack111lll1111l_opy_ in self._111ll1lllll_opy_.items():
            setattr(logging, level, bstack111lll1111l_opy_)
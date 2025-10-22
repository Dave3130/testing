# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import builtins
import logging
class bstack1l1l1lll_opy_:
    def __init__(self, handler):
        self._111ll1l1lll_opy_ = builtins.print
        self.handler = handler
        self._started = False
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)
        self._111ll1l1ll1_opy_ = {
            level: getattr(self.logger, level)
            for level in [bstack1lllll1l_opy_ (u"࠭ࡩ࡯ࡨࡲࠫᯜ"), bstack1lllll1l_opy_ (u"ࠧࡥࡧࡥࡹ࡬࠭ᯝ"), bstack1lllll1l_opy_ (u"ࠨࡹࡤࡶࡳ࡯࡮ࡨࠩᯞ"), bstack1lllll1l_opy_ (u"ࠩࡨࡶࡷࡵࡲࠨᯟ")]
        }
    def start(self):
        if self._started:
            return
        self._started = True
        builtins.print = self._111ll1l1l1l_opy_
        self._111ll1l11ll_opy_()
    def _111ll1l1l1l_opy_(self, *args, **kwargs):
        self._111ll1l1lll_opy_(*args, **kwargs)
        message = bstack1lllll1l_opy_ (u"ࠪࠤࠬᯠ").join(map(str, args)) + bstack1lllll1l_opy_ (u"ࠫࡡࡴࠧᯡ")
        self._log_message(bstack1lllll1l_opy_ (u"ࠬࡏࡎࡇࡑࠪᯢ"), message)
    def _log_message(self, level, msg, *args, **kwargs):
        if self.handler:
            self.handler({bstack1lllll1l_opy_ (u"࠭࡬ࡦࡸࡨࡰࠬᯣ"): level, bstack1lllll1l_opy_ (u"ࠧ࡮ࡧࡶࡷࡦ࡭ࡥࠨᯤ"): msg})
    def _111ll1l11ll_opy_(self):
        for level, bstack111ll1l1l11_opy_ in self._111ll1l1ll1_opy_.items():
            setattr(logging, level, self._111ll1ll111_opy_(level, bstack111ll1l1l11_opy_))
    def _111ll1ll111_opy_(self, level, bstack111ll1l1l11_opy_):
        def wrapper(msg, *args, **kwargs):
            bstack111ll1l1l11_opy_(msg, *args, **kwargs)
            self._log_message(level.upper(), msg)
        return wrapper
    def reset(self):
        if not self._started:
            return
        self._started = False
        builtins.print = self._111ll1l1lll_opy_
        for level, bstack111ll1l1l11_opy_ in self._111ll1l1ll1_opy_.items():
            setattr(logging, level, bstack111ll1l1l11_opy_)
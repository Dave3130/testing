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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l11111_opy_
class bstack1llll1lll1l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lllll_opy_: bstack1lll1l11111_opy_
    def __init__(self):
        self.bstack1llll1l1ll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lllll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11llll1_opy_(self):
        return (self.bstack1llll1l1ll1_opy_ != None and self.bin_session_id != None and self.bstack1lll11lllll_opy_ != None)
    def configure(self, bstack1llll1l1ll1_opy_, config, bin_session_id: str, bstack1lll11lllll_opy_: bstack1lll1l11111_opy_):
        self.bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1ll1l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢࡰࡳࡩࡻ࡬ࡦࠢࡾࡷࡪࡲࡦ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢ࠲ࡤࡥ࡮ࡢ࡯ࡨࡣࡤࢃ࠺ࠡࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥᅕ") + str(self.bin_session_id) + bstack1ll1l_opy_ (u"ࠢࠣᅖ"))
    def bstack1lllll1l111_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1ll1l_opy_ (u"ࠣࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡔ࡯࡯ࡧࠥᅗ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
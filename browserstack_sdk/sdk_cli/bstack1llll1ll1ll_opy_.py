# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
class bstack1llllllll11_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    def __init__(self):
        self.bstack1lllll1lll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll1l11111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l1111l_opy_(self):
        return (self.bstack1lllll1lll1_opy_ != None and self.bin_session_id != None and self.bstack1lll1l11111_opy_ != None)
    def configure(self, bstack1lllll1lll1_opy_, config, bin_session_id: str, bstack1lll1l11111_opy_: bstack1lll11lllll_opy_):
        self.bstack1lllll1lll1_opy_ = bstack1lllll1lll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1ll1ll1_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢࡰࡳࡩࡻ࡬ࡦࠢࡾࡷࡪࡲࡦ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢ࠲ࡤࡥ࡮ࡢ࡯ࡨࡣࡤࢃ࠺ࠡࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥᅜ") + str(self.bin_session_id) + bstack1ll1ll1_opy_ (u"ࠢࠣᅝ"))
    def bstack1llllll111l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1ll1ll1_opy_ (u"ࠣࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡔ࡯࡯ࡧࠥᅞ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
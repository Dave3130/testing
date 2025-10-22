# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l11ll_opy_ import bstack1lll11l11l1_opy_
class bstack1lllll111l1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l11ll_opy_: bstack1lll11l11l1_opy_
    def __init__(self):
        self.bstack1lllll1lll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l11ll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1l11_opy_(self):
        return (self.bstack1lllll1lll1_opy_ != None and self.bin_session_id != None and self.bstack1lll11l11ll_opy_ != None)
    def configure(self, bstack1lllll1lll1_opy_, config, bin_session_id: str, bstack1lll11l11ll_opy_: bstack1lll11l11l1_opy_):
        self.bstack1lllll1lll1_opy_ = bstack1lllll1lll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l11ll_opy_ = bstack1lll11l11ll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l111ll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢࡰࡳࡩࡻ࡬ࡦࠢࡾࡷࡪࡲࡦ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢ࠲ࡤࡥ࡮ࡢ࡯ࡨࡣࡤࢃ࠺ࠡࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥᅸ") + str(self.bin_session_id) + bstack1l111ll_opy_ (u"ࠢࠣᅹ"))
    def bstack1lllll1111l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l111ll_opy_ (u"ࠣࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡔ࡯࡯ࡧࠥᅺ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
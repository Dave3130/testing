# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l11ll_opy_
class bstack1lllll11lll_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l11_opy_: bstack1lll11l11ll_opy_
    def __init__(self):
        self.bstack1llll11ll11_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l11_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l11l1_opy_(self):
        return (self.bstack1llll11ll11_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l11_opy_ != None)
    def configure(self, bstack1llll11ll11_opy_, config, bin_session_id: str, bstack1lll11l1l11_opy_: bstack1lll11l11ll_opy_):
        self.bstack1llll11ll11_opy_ = bstack1llll11ll11_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l11_opy_ = bstack1lll11l1l11_opy_
        if self.bin_session_id:
            self.logger.debug(bstack111l1l_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢࡰࡳࡩࡻ࡬ࡦࠢࡾࡷࡪࡲࡦ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢ࠲ࡤࡥ࡮ࡢ࡯ࡨࡣࡤࢃ࠺ࠡࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥᅸ") + str(self.bin_session_id) + bstack111l1l_opy_ (u"ࠢࠣᅹ"))
    def bstack1llllll11l1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack111l1l_opy_ (u"ࠣࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡔ࡯࡯ࡧࠥᅺ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
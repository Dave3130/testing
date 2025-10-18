# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
class bstack1lllllllll1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_
    def __init__(self):
        self.bstack1lllll11111_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l11ll_opy_(self):
        return (self.bstack1lllll11111_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l1l_opy_ != None)
    def configure(self, bstack1lllll11111_opy_, config, bin_session_id: str, bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_):
        self.bstack1lllll11111_opy_ = bstack1lllll11111_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11ll_opy_ (u"ࠨ࡛ࡼ࡫ࡧࠬࡸ࡫࡬ࡧࠫࢀࡡࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡥࡥࠢࡰࡳࡩࡻ࡬ࡦࠢࡾࡷࡪࡲࡦ࠯ࡡࡢࡧࡱࡧࡳࡴࡡࡢ࠲ࡤࡥ࡮ࡢ࡯ࡨࡣࡤࢃ࠺ࠡࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥ࠿ࠥᅿ") + str(self.bin_session_id) + bstack11ll_opy_ (u"ࠢࠣᆀ"))
    def bstack1lllll111ll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11ll_opy_ (u"ࠣࡤ࡬ࡲࡤࡹࡥࡴࡵ࡬ࡳࡳࡥࡩࡥࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡔ࡯࡯ࡧࠥᆁ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11ll111_opy_ import bstack1lll11l1lll_opy_
class bstack1llllll1111_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11ll111_opy_: bstack1lll11l1lll_opy_
    def __init__(self):
        self.bstack1lllllll1ll_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11ll111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1ll1_opy_(self):
        return (self.bstack1lllllll1ll_opy_ != None and self.bin_session_id != None and self.bstack1lll11ll111_opy_ != None)
    def configure(self, bstack1lllllll1ll_opy_, config, bin_session_id: str, bstack1lll11ll111_opy_: bstack1lll11l1lll_opy_):
        self.bstack1lllllll1ll_opy_ = bstack1lllllll1ll_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11ll111_opy_ = bstack1lll11ll111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l11l1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤࠡ࡯ࡲࡨࡺࡲࡥࠡࡽࡶࡩࡱ࡬࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡ࠱ࡣࡤࡴࡡ࡮ࡧࡢࡣࢂࡀࠠࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤᅰ") + str(self.bin_session_id) + bstack11l11l1_opy_ (u"ࠨࠢᅱ"))
    def bstack1llll1lllll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l11l1_opy_ (u"ࠢࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡓࡵ࡮ࡦࠤᅲ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
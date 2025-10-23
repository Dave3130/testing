# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l11ll_opy_
class bstack1llllll111l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l1l_opy_: bstack1lll11l11ll_opy_
    def __init__(self):
        self.bstack1llll11lll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1l11_opy_(self):
        return (self.bstack1llll11lll1_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l1l_opy_ != None)
    def configure(self, bstack1llll11lll1_opy_, config, bin_session_id: str, bstack1lll11l1l1l_opy_: bstack1lll11l11ll_opy_):
        self.bstack1llll11lll1_opy_ = bstack1llll11lll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11lll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤࠡ࡯ࡲࡨࡺࡲࡥࠡࡽࡶࡩࡱ࡬࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡ࠱ࡣࡤࡴࡡ࡮ࡧࡢࡣࢂࡀࠠࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤᅷ") + str(self.bin_session_id) + bstack11lll1_opy_ (u"ࠨࠢᅸ"))
    def bstack1llll1ll1ll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11lll1_opy_ (u"ࠢࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡓࡵ࡮ࡦࠤᅹ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
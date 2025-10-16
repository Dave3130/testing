# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll1l1111l_opy_
class bstack1llll1ll11l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_
    def __init__(self):
        self.bstack1111111l1l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lllll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l11111_opy_(self):
        return (self.bstack1111111l1l_opy_ != None and self.bin_session_id != None and self.bstack1lll11lllll_opy_ != None)
    def configure(self, bstack1111111l1l_opy_, config, bin_session_id: str, bstack1lll11lllll_opy_: bstack1lll1l1111l_opy_):
        self.bstack1111111l1l_opy_ = bstack1111111l1l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1lllll1_opy_ (u"ࠧࡡࡻࡪࡦࠫࡷࡪࡲࡦࠪࡿࡠࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷ࡫ࡤࠡ࡯ࡲࡨࡺࡲࡥࠡࡽࡶࡩࡱ࡬࠮ࡠࡡࡦࡰࡦࡹࡳࡠࡡ࠱ࡣࡤࡴࡡ࡮ࡧࡢࡣࢂࡀࠠࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤ࠾ࠤᅛ") + str(self.bin_session_id) + bstack1lllll1_opy_ (u"ࠨࠢᅜ"))
    def bstack1llll1lllll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1lllll1_opy_ (u"ࠢࡣ࡫ࡱࡣࡸ࡫ࡳࡴ࡫ࡲࡲࡤ࡯ࡤࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡓࡵ࡮ࡦࠤᅝ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
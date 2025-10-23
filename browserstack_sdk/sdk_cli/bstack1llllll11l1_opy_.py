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
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lllll_opy_ import bstack1lll11llll1_opy_
class bstack1llllll111l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lllll_opy_: bstack1lll11llll1_opy_
    def __init__(self):
        self.bstack111111111l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lllll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l11111_opy_(self):
        return (self.bstack111111111l_opy_ != None and self.bin_session_id != None and self.bstack1lll11lllll_opy_ != None)
    def configure(self, bstack111111111l_opy_, config, bin_session_id: str, bstack1lll11lllll_opy_: bstack1lll11llll1_opy_):
        self.bstack111111111l_opy_ = bstack111111111l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lllll_opy_ = bstack1lll11lllll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack111111l_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࡧࠤࡲࡵࡤࡶ࡮ࡨࠤࢀࡹࡥ࡭ࡨ࠱ࡣࡤࡩ࡬ࡢࡵࡶࡣࡤ࠴࡟ࡠࡰࡤࡱࡪࡥ࡟ࡾ࠼ࠣࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧᅐ") + str(self.bin_session_id) + bstack111111l_opy_ (u"ࠤࠥᅑ"))
    def bstack1llll1l1ll1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack111111l_opy_ (u"ࠥࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡏࡱࡱࡩࠧᅒ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
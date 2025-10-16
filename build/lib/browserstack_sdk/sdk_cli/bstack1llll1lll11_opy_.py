# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll1l1111l_opy_
class bstack1llll1llll1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_
    def __init__(self):
        self.bstack1llll1lll1l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll1l11111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11lllll_opy_(self):
        return (self.bstack1llll1lll1l_opy_ != None and self.bin_session_id != None and self.bstack1lll1l11111_opy_ != None)
    def configure(self, bstack1llll1lll1l_opy_, config, bin_session_id: str, bstack1lll1l11111_opy_: bstack1lll1l1111l_opy_):
        self.bstack1llll1lll1l_opy_ = bstack1llll1lll1l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦࠣࡱࡴࡪࡵ࡭ࡧࠣࡿࡸ࡫࡬ࡧ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣ࠳ࡥ࡟࡯ࡣࡰࡩࡤࡥࡽ࠻ࠢࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦᅝ") + str(self.bin_session_id) + bstack1l_opy_ (u"ࠣࠤᅞ"))
    def bstack1lllll1l111_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l_opy_ (u"ࠤࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡎࡰࡰࡨࠦᅟ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
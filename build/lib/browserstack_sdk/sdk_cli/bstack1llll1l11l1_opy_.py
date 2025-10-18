# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
class bstack1111111ll1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_
    def __init__(self):
        self.bstack1lllll1ll11_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lll1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11lll11_opy_(self):
        return (self.bstack1lllll1ll11_opy_ != None and self.bin_session_id != None and self.bstack1lll11lll1l_opy_ != None)
    def configure(self, bstack1lllll1ll11_opy_, config, bin_session_id: str, bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_):
        self.bstack1lllll1ll11_opy_ = bstack1lllll1ll11_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lll1l_opy_ = bstack1lll11lll1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦࠣࡱࡴࡪࡵ࡭ࡧࠣࡿࡸ࡫࡬ࡧ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣ࠳ࡥ࡟࡯ࡣࡰࡩࡤࡥࡽ࠻ࠢࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦᅖ") + str(self.bin_session_id) + bstack1l1lll1_opy_ (u"ࠣࠤᅗ"))
    def bstack1llll1llll1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1l1lll1_opy_ (u"ࠤࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡎࡰࡰࡨࠦᅘ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
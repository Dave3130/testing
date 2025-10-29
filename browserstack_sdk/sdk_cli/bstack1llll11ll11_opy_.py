# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l1111_opy_
class bstack1lllll11111_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_
    def __init__(self):
        self.bstack1llll1l1ll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l11l1_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l111l_opy_(self):
        return (self.bstack1llll1l1ll1_opy_ != None and self.bin_session_id != None and self.bstack1lll11l11l1_opy_ != None)
    def configure(self, bstack1llll1l1ll1_opy_, config, bin_session_id: str, bstack1lll11l11l1_opy_: bstack1lll11l1111_opy_):
        self.bstack1llll1l1ll1_opy_ = bstack1llll1l1ll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l11l1_opy_ = bstack1lll11l11l1_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l11ll_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡩࡩࠦ࡭ࡰࡦࡸࡰࡪࠦࡻࡴࡧ࡯ࡪ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟࠯ࡡࡢࡲࡦࡳࡥࡠࡡࢀ࠾ࠥࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢᆊ") + str(self.bin_session_id) + bstack11l11ll_opy_ (u"ࠦࠧᆋ"))
    def bstack1llll11l1l1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l11ll_opy_ (u"ࠧࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠦࡣࡢࡰࡱࡳࡹࠦࡢࡦࠢࡑࡳࡳ࡫ࠢᆌ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
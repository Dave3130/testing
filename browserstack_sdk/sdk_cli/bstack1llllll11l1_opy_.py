# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l11l1_opy_ import bstack1lll11l111l_opy_
class bstack1lllll1l111_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l11l1_opy_: bstack1lll11l111l_opy_
    def __init__(self):
        self.bstack1lllll111l1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l11l1_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1111_opy_(self):
        return (self.bstack1lllll111l1_opy_ != None and self.bin_session_id != None and self.bstack1lll11l11l1_opy_ != None)
    def configure(self, bstack1lllll111l1_opy_, config, bin_session_id: str, bstack1lll11l11l1_opy_: bstack1lll11l111l_opy_):
        self.bstack1lllll111l1_opy_ = bstack1lllll111l1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l11l1_opy_ = bstack1lll11l11l1_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11ll1l_opy_ (u"ࠥ࡟ࢀ࡯ࡤࠩࡵࡨࡰ࡫࠯ࡽ࡞ࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡩࡩࠦ࡭ࡰࡦࡸࡰࡪࠦࡻࡴࡧ࡯ࡪ࠳ࡥ࡟ࡤ࡮ࡤࡷࡸࡥ࡟࠯ࡡࡢࡲࡦࡳࡥࡠࡡࢀ࠾ࠥࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࡃࠢᆊ") + str(self.bin_session_id) + bstack11ll1l_opy_ (u"ࠦࠧᆋ"))
    def bstack1llll1l11l1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11ll1l_opy_ (u"ࠧࡨࡩ࡯ࡡࡶࡩࡸࡹࡩࡰࡰࡢ࡭ࡩࠦࡣࡢࡰࡱࡳࡹࠦࡢࡦࠢࡑࡳࡳ࡫ࠢᆌ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
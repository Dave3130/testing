# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
class bstack111111ll11_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    def __init__(self):
        self.bstack1llllll111l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll1l11111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll1l1111l_opy_(self):
        return (self.bstack1llllll111l_opy_ != None and self.bin_session_id != None and self.bstack1lll1l11111_opy_ != None)
    def configure(self, bstack1llllll111l_opy_, config, bin_session_id: str, bstack1lll1l11111_opy_: bstack1lll11lllll_opy_):
        self.bstack1llllll111l_opy_ = bstack1llllll111l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1ll11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࡪࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡼࡵࡨࡰ࡫࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠ࠰ࡢࡣࡳࡧ࡭ࡦࡡࡢࢁ࠿ࠦࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣᅚ") + str(self.bin_session_id) + bstack1ll11_opy_ (u"ࠧࠨᅛ"))
    def bstack1111111l1l_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1ll11_opy_ (u"ࠨࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡒࡴࡴࡥࠣᅜ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
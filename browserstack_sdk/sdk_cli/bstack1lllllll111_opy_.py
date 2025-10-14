# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll1l11111_opy_ import bstack1lll11lllll_opy_
class bstack1lllll1l111_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll1l11111_opy_: bstack1lll11lllll_opy_
    def __init__(self):
        self.bstack1llll1ll11l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll1l11111_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11llll1_opy_(self):
        return (self.bstack1llll1ll11l_opy_ != None and self.bin_session_id != None and self.bstack1lll1l11111_opy_ != None)
    def configure(self, bstack1llll1ll11l_opy_, config, bin_session_id: str, bstack1lll1l11111_opy_: bstack1lll11lllll_opy_):
        self.bstack1llll1ll11l_opy_ = bstack1llll1ll11l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll1l11111_opy_ = bstack1lll1l11111_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࡪࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡼࡵࡨࡰ࡫࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠ࠰ࡢࡣࡳࡧ࡭ࡦࡡࡢࢁ࠿ࠦࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣᅓ") + str(self.bin_session_id) + bstack11l1l11_opy_ (u"ࠧࠨᅔ"))
    def bstack1llllllll11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l1l11_opy_ (u"ࠨࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡒࡴࡴࡥࠣᅕ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
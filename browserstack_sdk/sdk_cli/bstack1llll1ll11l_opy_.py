# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
class bstack1llll1l1l11_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_
    def __init__(self):
        self.bstack1llllll1l11_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1ll1_opy_(self):
        return (self.bstack1llllll1l11_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l1l_opy_ != None)
    def configure(self, bstack1llllll1l11_opy_, config, bin_session_id: str, bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_):
        self.bstack1llllll1l11_opy_ = bstack1llllll1l11_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡠࢁࡩࡥࠪࡶࡩࡱ࡬ࠩࡾ࡟ࠣࡧࡴࡴࡦࡪࡩࡸࡶࡪࡪࠠ࡮ࡱࡧࡹࡱ࡫ࠠࡼࡵࡨࡰ࡫࠴࡟ࡠࡥ࡯ࡥࡸࡹ࡟ࡠ࠰ࡢࡣࡳࡧ࡭ࡦࡡࡢࢁ࠿ࠦࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪ࠽ࠣᅽ") + str(self.bin_session_id) + bstack11l111_opy_ (u"ࠧࠨᅾ"))
    def bstack1llll1lll11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l111_opy_ (u"ࠨࡢࡪࡰࡢࡷࡪࡹࡳࡪࡱࡱࡣ࡮ࡪࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡒࡴࡴࡥࠣᅿ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
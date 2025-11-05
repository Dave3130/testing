# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll111llll_opy_ import bstack1lll11l111l_opy_
class bstack1lllll111l1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll111llll_opy_: bstack1lll11l111l_opy_
    def __init__(self):
        self.bstack1llllll1l1l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll111llll_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1111_opy_(self):
        return (self.bstack1llllll1l1l_opy_ != None and self.bin_session_id != None and self.bstack1lll111llll_opy_ != None)
    def configure(self, bstack1llllll1l1l_opy_, config, bin_session_id: str, bstack1lll111llll_opy_: bstack1lll11l111l_opy_):
        self.bstack1llllll1l1l_opy_ = bstack1llllll1l1l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll111llll_opy_ = bstack1lll111llll_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣ࡝ࡾ࡭ࡩ࠮ࡳࡦ࡮ࡩ࠭ࢂࡣࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡧࡧࠤࡲࡵࡤࡶ࡮ࡨࠤࢀࡹࡥ࡭ࡨ࠱ࡣࡤࡩ࡬ࡢࡵࡶࡣࡤ࠴࡟ࡠࡰࡤࡱࡪࡥ࡟ࡾ࠼ࠣࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࡁࠧᆏ") + str(self.bin_session_id) + bstack11ll1ll_opy_ (u"ࠤࠥᆐ"))
    def bstack1llllll1ll1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11ll1ll_opy_ (u"ࠥࡦ࡮ࡴ࡟ࡴࡧࡶࡷ࡮ࡵ࡮ࡠ࡫ࡧࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡏࡱࡱࡩࠧᆑ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lll11_opy_ import bstack1lll11ll1ll_opy_
class bstack1llll1l1l1l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_
    def __init__(self):
        self.bstack1lllllllll1_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lll11_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11lll1l_opy_(self):
        return (self.bstack1lllllllll1_opy_ != None and self.bin_session_id != None and self.bstack1lll11lll11_opy_ != None)
    def configure(self, bstack1lllllllll1_opy_, config, bin_session_id: str, bstack1lll11lll11_opy_: bstack1lll11ll1ll_opy_):
        self.bstack1lllllllll1_opy_ = bstack1lllllllll1_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lll11_opy_ = bstack1lll11lll11_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11l111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨࠥࡳ࡯ࡥࡷ࡯ࡩࠥࢁࡳࡦ࡮ࡩ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥ࠮ࡠࡡࡱࡥࡲ࡫࡟ࡠࡿ࠽ࠤࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨᅊ") + str(self.bin_session_id) + bstack11l111_opy_ (u"ࠥࠦᅋ"))
    def bstack1llllll1l11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11l111_opy_ (u"ࠦࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡐࡲࡲࡪࠨᅌ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
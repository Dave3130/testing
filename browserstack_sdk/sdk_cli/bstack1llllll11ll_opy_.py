# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11lll1l_opy_ import bstack1lll11llll1_opy_
class bstack1lllll1l1l1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_
    def __init__(self):
        self.bstack1llll1lll11_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11lll1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11lll11_opy_(self):
        return (self.bstack1llll1lll11_opy_ != None and self.bin_session_id != None and self.bstack1lll11lll1l_opy_ != None)
    def configure(self, bstack1llll1lll11_opy_, config, bin_session_id: str, bstack1lll11lll1l_opy_: bstack1lll11llll1_opy_):
        self.bstack1llll1lll11_opy_ = bstack1llll1lll11_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11lll1l_opy_ = bstack1lll11lll1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨࠥࡳ࡯ࡥࡷ࡯ࡩࠥࢁࡳࡦ࡮ࡩ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥ࠮ࡠࡡࡱࡥࡲ࡫࡟ࡠࡿ࠽ࠤࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨᅊ") + str(self.bin_session_id) + bstack11111_opy_ (u"ࠥࠦᅋ"))
    def bstack1lllll1lll1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11111_opy_ (u"ࠦࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡐࡲࡲࡪࠨᅌ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
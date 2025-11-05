# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l1l_opy_ import bstack1lll11l1l11_opy_
class bstack1lllllll1l1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_
    def __init__(self):
        self.bstack1llll11l11l_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l1l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l11ll_opy_(self):
        return (self.bstack1llll11l11l_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l1l_opy_ != None)
    def configure(self, bstack1llll11l11l_opy_, config, bin_session_id: str, bstack1lll11l1l1l_opy_: bstack1lll11l1l11_opy_):
        self.bstack1llll11l11l_opy_ = bstack1llll11l11l_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l1l_opy_ = bstack1lll11l1l1l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨࠥࡳ࡯ࡥࡷ࡯ࡩࠥࢁࡳࡦ࡮ࡩ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥ࠮ࡠࡡࡱࡥࡲ࡫࡟ࡠࡿ࠽ࠤࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨᅴ") + str(self.bin_session_id) + bstack1lll11l_opy_ (u"ࠥࠦᅵ"))
    def bstack1llllll1lll_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1lll11l_opy_ (u"ࠦࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡐࡲࡲࡪࠨᅶ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
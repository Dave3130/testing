# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l1l11_opy_ import bstack1lll11l1l1l_opy_
class bstack1lllll1111l_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_
    def __init__(self):
        self.bstack1lllllll111_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l1l11_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1ll1_opy_(self):
        return (self.bstack1lllllll111_opy_ != None and self.bin_session_id != None and self.bstack1lll11l1l11_opy_ != None)
    def configure(self, bstack1lllllll111_opy_, config, bin_session_id: str, bstack1lll11l1l11_opy_: bstack1lll11l1l1l_opy_):
        self.bstack1lllllll111_opy_ = bstack1lllllll111_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l1l11_opy_ = bstack1lll11l1l11_opy_
        if self.bin_session_id:
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠤ࡞ࡿ࡮ࡪࠨࡴࡧ࡯ࡪ࠮ࢃ࡝ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡨࡨࠥࡳ࡯ࡥࡷ࡯ࡩࠥࢁࡳࡦ࡮ࡩ࠲ࡤࡥࡣ࡭ࡣࡶࡷࡤࡥ࠮ࡠࡡࡱࡥࡲ࡫࡟ࡠࡿ࠽ࠤࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࡂࠨᅻ") + str(self.bin_session_id) + bstack1lllll1l_opy_ (u"ࠥࠦᅼ"))
    def bstack1llll1lll11_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack1lllll1l_opy_ (u"ࠦࡧ࡯࡮ࡠࡵࡨࡷࡸ࡯࡯࡯ࡡ࡬ࡨࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡐࡲࡲࡪࠨᅽ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
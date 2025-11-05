# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import logging
import abc
from browserstack_sdk.sdk_cli.bstack1lll11l111l_opy_ import bstack1lll111llll_opy_
class bstack1llll111ll1_opy_(abc.ABC):
    bin_session_id: str
    bstack1lll11l111l_opy_: bstack1lll111llll_opy_
    def __init__(self):
        self.bstack1llll1ll1ll_opy_ = None
        self.config = None
        self.bin_session_id = None
        self.bstack1lll11l111l_opy_ = None
        self.logger = logging.getLogger(self.__class__.__name__)
        self.logger.setLevel(logging.INFO)
    def bstack1lll11l1111_opy_(self):
        return (self.bstack1llll1ll1ll_opy_ != None and self.bin_session_id != None and self.bstack1lll11l111l_opy_ != None)
    def configure(self, bstack1llll1ll1ll_opy_, config, bin_session_id: str, bstack1lll11l111l_opy_: bstack1lll111llll_opy_):
        self.bstack1llll1ll1ll_opy_ = bstack1llll1ll1ll_opy_
        self.config = config
        self.bin_session_id = bin_session_id
        self.bstack1lll11l111l_opy_ = bstack1lll11l111l_opy_
        if self.bin_session_id:
            self.logger.debug(bstack11111_opy_ (u"ࠢ࡜ࡽ࡬ࡨ࠭ࡹࡥ࡭ࡨࠬࢁࡢࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡦࡦࠣࡱࡴࡪࡵ࡭ࡧࠣࡿࡸ࡫࡬ࡧ࠰ࡢࡣࡨࡲࡡࡴࡵࡢࡣ࠳ࡥ࡟࡯ࡣࡰࡩࡤࡥࡽ࠻ࠢࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࡀࠦᆎ") + str(self.bin_session_id) + bstack11111_opy_ (u"ࠣࠤᆏ"))
    def bstack1llllll11l1_opy_(self):
        if not self.bin_session_id:
            raise ValueError(bstack11111_opy_ (u"ࠤࡥ࡭ࡳࡥࡳࡦࡵࡶ࡭ࡴࡴ࡟ࡪࡦࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡎࡰࡰࡨࠦᆐ"))
    @abc.abstractmethod
    def is_enabled(self) -> bool:
        return False
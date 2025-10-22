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
import os
import tempfile
import math
from bstack_utils import bstack11llll111l_opy_
from bstack_utils.constants import bstack1l11llll1_opy_, bstack11l11l1ll1l_opy_
from bstack_utils.helper import bstack11ll1l1l1ll_opy_, get_host_info
from bstack_utils.bstack11ll1ll1lll_opy_ import bstack11ll1l1llll_opy_
import json
import re
import sys
bstack111lll1l1ll_opy_ = bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡴࡳࡻࡗࡩࡸࡺࡳࡐࡰࡉࡥ࡮ࡲࡵࡳࡧࠥ᭣")
bstack111lll1llll_opy_ = bstack1lllll1l_opy_ (u"ࠧࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦ᭤")
bstack111lll1ll1l_opy_ = bstack1lllll1l_opy_ (u"ࠨࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࡋ࡯ࡲࡴࡶࠥ᭥")
bstack111lll111ll_opy_ = bstack1lllll1l_opy_ (u"ࠢࡳࡧࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࠣ᭦")
bstack111llllll1l_opy_ = bstack1lllll1l_opy_ (u"ࠣࡵ࡮࡭ࡵࡌ࡬ࡢ࡭ࡼࡥࡳࡪࡆࡢ࡫࡯ࡩࡩࠨ᭧")
bstack111llll111l_opy_ = bstack1lllll1l_opy_ (u"ࠤࡵࡹࡳ࡙࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࠨ᭨")
bstack11l1111l1ll_opy_ = {
    bstack111lll1l1ll_opy_,
    bstack111lll1llll_opy_,
    bstack111lll1ll1l_opy_,
    bstack111lll111ll_opy_,
    bstack111llllll1l_opy_,
    bstack111llll111l_opy_
}
bstack11l1111l1l1_opy_ = {bstack1lllll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪ᭩")}
logger = bstack11llll111l_opy_.get_logger(__name__, bstack1l11llll1_opy_)
class bstack111llll1ll1_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l11111ll1_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack111l11ll_opy_:
    _1ll1l1llll1_opy_ = None
    def __init__(self, config):
        self.bstack11l11111111_opy_ = False
        self.bstack111lll11ll1_opy_ = False
        self.bstack111lll1111l_opy_ = False
        self.bstack111lll111l1_opy_ = False
        self.bstack111llll1l1l_opy_ = None
        self.bstack11l1111l111_opy_ = bstack111llll1ll1_opy_()
        self.bstack11l1111lll1_opy_ = None
        opts = config.get(bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭪"), {})
        self.bstack11l11111l1l_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡅࡏࡘࠪ᭫"), bstack1lllll1l_opy_ (u"ࠨ᭬ࠢ"))
        self.bstack111ll1ll1l1_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡅࡏࡍࠬ᭭"), bstack1lllll1l_opy_ (u"ࠣࠤ᭮"))
        bstack111lll1l111_opy_ = opts.get(bstack111llll111l_opy_, {})
        bstack11l11111l11_opy_ = None
        if bstack1lllll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩ᭯") in bstack111lll1l111_opy_:
            bstack11l11111l11_opy_ = bstack111lll1l111_opy_[bstack1lllll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ᭰")]
            if bstack11l11111l11_opy_ is None:
                bstack11l11111l11_opy_ = []
        self.__111ll1ll1ll_opy_(
            bstack111lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᭱"), False),
            bstack111lll1l111_opy_.get(bstack1lllll1l_opy_ (u"ࠬࡳ࡯ࡥࡧࠪ᭲"), bstack1lllll1l_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭᭳")),
            bstack11l11111l11_opy_
        )
        self.__111lllll1l1_opy_(opts.get(bstack111lll1ll1l_opy_, False))
        self.__11l1111llll_opy_(opts.get(bstack111lll111ll_opy_, False))
        self.__111llllll11_opy_(opts.get(bstack111llllll1l_opy_, False))
    @classmethod
    def bstack1111l1ll_opy_(cls, config=None):
        if cls._1ll1l1llll1_opy_ is None and config is not None:
            cls._1ll1l1llll1_opy_ = bstack111l11ll_opy_(config)
        return cls._1ll1l1llll1_opy_
    @staticmethod
    def bstack1111lll1_opy_(config: dict) -> bool:
        bstack111ll1lll1l_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭴"), {}).get(bstack111lll1l1ll_opy_, {})
        return bstack111ll1lll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩ᭵"), False)
    @staticmethod
    def bstack1llllllll_opy_(config: dict) -> int:
        bstack111ll1lll1l_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭶"), {}).get(bstack111lll1l1ll_opy_, {})
        retries = 0
        if bstack111l11ll_opy_.bstack1111lll1_opy_(config):
            retries = bstack111ll1lll1l_opy_.get(bstack1lllll1l_opy_ (u"ࠪࡱࡦࡾࡒࡦࡶࡵ࡭ࡪࡹࠧ᭷"), 1)
        return retries
    @staticmethod
    def bstack11lll11ll_opy_(config: dict) -> dict:
        bstack111lll1l1l1_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭸"), {})
        return {
            key: value for key, value in bstack111lll1l1l1_opy_.items() if key in bstack11l1111l1ll_opy_
        }
    @staticmethod
    def bstack111llll11ll_opy_():
        bstack1lllll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭹")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠨࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࢀࢃࠢ᭺").format(os.getenv(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ᭻")))))
    @staticmethod
    def bstack111ll1lllll_opy_(test_name: str):
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᭼")
        bstack11l111l1111_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1l_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡽࢀ࠲ࡹࡾࡴࠣ᭽").format(os.getenv(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᭾"))))
        with open(bstack11l111l1111_opy_, bstack1lllll1l_opy_ (u"ࠫࡦ࠭᭿")) as file:
            file.write(bstack1lllll1l_opy_ (u"ࠧࢁࡽ࡝ࡰࠥᮀ").format(test_name))
    @staticmethod
    def bstack111lllll111_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l1111l1l1_opy_
    @staticmethod
    def bstack11l1ll1lll1_opy_(config: dict) -> bool:
        bstack111lll1lll1_opy_ = config.get(bstack1lllll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮁ"), {}).get(bstack111lll1llll_opy_, {})
        return bstack111lll1lll1_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮂ"), False)
    @staticmethod
    def bstack11l1llllll1_opy_(config: dict, bstack11l1lllll11_opy_: int = 0) -> int:
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠯ࠤࡼ࡮ࡩࡤࡪࠣࡧࡦࡴࠠࡣࡧࠣࡥࡳࠦࡡࡣࡵࡲࡰࡺࡺࡥࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡵࠤࡦࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳ࡬ࡩࡨࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡴࡺࡡ࡭ࡡࡷࡩࡸࡺࡳࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࠨࡳࡧࡴࡹ࡮ࡸࡥࡥࠢࡩࡳࡷࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠰ࡦࡦࡹࡥࡥࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࡸ࠯࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮃ")
        bstack111lll1lll1_opy_ = config.get(bstack1lllll1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᮄ"), {}).get(bstack1lllll1l_opy_ (u"ࠪࡥࡧࡵࡲࡵࡄࡸ࡭ࡱࡪࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠩᮅ"), {})
        bstack11l111111l1_opy_ = 0
        bstack111llll11l1_opy_ = 0
        if bstack111l11ll_opy_.bstack11l1ll1lll1_opy_(config):
            bstack111llll11l1_opy_ = bstack111lll1lll1_opy_.get(bstack1lllll1l_opy_ (u"ࠫࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴࠩᮆ"), 5)
            if isinstance(bstack111llll11l1_opy_, str) and bstack111llll11l1_opy_.endswith(bstack1lllll1l_opy_ (u"ࠬࠫࠧᮇ")):
                try:
                    percentage = int(bstack111llll11l1_opy_.strip(bstack1lllll1l_opy_ (u"࠭ࠥࠨᮈ")))
                    if bstack11l1lllll11_opy_ > 0:
                        bstack11l111111l1_opy_ = math.ceil((percentage * bstack11l1lllll11_opy_) / 100)
                    else:
                        raise ValueError(bstack1lllll1l_opy_ (u"ࠢࡕࡱࡷࡥࡱࠦࡴࡦࡵࡷࡷࠥࡳࡵࡴࡶࠣࡦࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡨࡲࡶࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠯ࡥࡥࡸ࡫ࡤࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࡷ࠳ࠨᮉ"))
                except ValueError as e:
                    raise ValueError(bstack1lllll1l_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪࠦࡶࡢ࡮ࡸࡩࠥ࡬࡯ࡳࠢࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹ࠺ࠡࡽࢀࠦᮊ").format(bstack111llll11l1_opy_)) from e
            else:
                bstack11l111111l1_opy_ = int(bstack111llll11l1_opy_)
        logger.info(bstack1lllll1l_opy_ (u"ࠤࡐࡥࡽࠦࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡸ࡫ࡴࠡࡶࡲ࠾ࠥࢁࡽࠡࠪࡩࡶࡴࡳࠠࡤࡱࡱࡪ࡮࡭࠺ࠡࡽࢀ࠭ࠧᮋ").format(bstack11l111111l1_opy_, bstack111llll11l1_opy_))
        return bstack11l111111l1_opy_
    def bstack111lll11l11_opy_(self):
        return self.bstack111lll111l1_opy_
    def bstack111lll11l1l_opy_(self):
        return self.bstack111llll1l1l_opy_
    def bstack111lll11lll_opy_(self):
        return self.bstack11l1111lll1_opy_
    def __111ll1ll1ll_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111lll111l1_opy_ = bool(enabled)
            if mode not in [bstack1lllll1l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪᮌ"), bstack1lllll1l_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡕ࡮࡭ࡻࠪᮍ")]:
                logger.warning(bstack1lllll1l_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡ࡯ࡲࡨࡪࠦࠧࡼࡿࠪࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡪࡰࡪࠤࡹࡵࠠࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ࠰ࠥᮎ").format(mode))
                mode = bstack1lllll1l_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭ᮏ")
            self.bstack111llll1l1l_opy_ = mode
            if source is None:
                self.bstack11l1111lll1_opy_ = None
            elif isinstance(source, list):
                self.bstack11l1111lll1_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1lllll1l_opy_ (u"ࠧ࠯࡬ࡶࡳࡳ࠭ᮐ")):
                self.bstack11l1111lll1_opy_ = self._111llll1111_opy_(source)
            self.__111ll1lll11_opy_()
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣ࠱ࠥ࡫࡮ࡢࡤ࡯ࡩࡩࡀࠠࡼࡿ࠯ࠤࡲࡵࡤࡦ࠼ࠣࡿࢂ࠲ࠠࡴࡱࡸࡶࡨ࡫࠺ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣᮑ").format(enabled, mode, source, e))
    def bstack11l1111ll1l_opy_(self):
        return self.bstack11l11111111_opy_
    def __111lllll1l1_opy_(self, value):
        self.bstack11l11111111_opy_ = bool(value)
        self.__111ll1lll11_opy_()
    def bstack11l11111lll_opy_(self):
        return self.bstack111lll11ll1_opy_
    def __11l1111llll_opy_(self, value):
        self.bstack111lll11ll1_opy_ = bool(value)
        self.__111ll1lll11_opy_()
    def bstack111lllll1ll_opy_(self):
        return self.bstack111lll1111l_opy_
    def __111llllll11_opy_(self, value):
        self.bstack111lll1111l_opy_ = bool(value)
        self.__111ll1lll11_opy_()
    def __111ll1lll11_opy_(self):
        if self.bstack111lll111l1_opy_:
            self.bstack11l11111111_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack111lll1111l_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111llll111l_opy_)
        elif self.bstack11l11111111_opy_:
            self.bstack111lll11ll1_opy_ = False
            self.bstack111lll1111l_opy_ = False
            self.bstack111lll111l1_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111lll1ll1l_opy_)
        elif self.bstack111lll11ll1_opy_:
            self.bstack11l11111111_opy_ = False
            self.bstack111lll1111l_opy_ = False
            self.bstack111lll111l1_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111lll111ll_opy_)
        elif self.bstack111lll1111l_opy_:
            self.bstack11l11111111_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack111lll111l1_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111llllll1l_opy_)
        else:
            self.bstack11l1111l111_opy_.disable()
    def bstack1llll11ll_opy_(self):
        return self.bstack11l1111l111_opy_.bstack11l11111ll1_opy_()
    def bstack11l1l1ll1_opy_(self):
        if self.bstack11l1111l111_opy_.bstack11l11111ll1_opy_():
            return self.bstack11l1111l111_opy_.get_name()
        return None
    def _111llll1111_opy_(self, bstack111llll1lll_opy_):
        bstack1lllll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡷࡴࡻࡲࡤࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠡࡣࡱࡨࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡯ࡴࠡࡨࡲࡶࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡰࡷࡵࡧࡪࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠢࠫࡷࡹࡸࠩ࠻ࠢࡓࡥࡹ࡮ࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡕࡒࡒࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡊࡴࡸ࡭ࡢࡶࡷࡩࡩࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡳࡧࡳࡳࡸ࡯ࡴࡰࡴࡼࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᮒ")
        if not os.path.isfile(bstack111llll1lll_opy_):
            logger.error(bstack1lllll1l_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠮ࠣᮓ").format(bstack111llll1lll_opy_))
            return []
        data = None
        try:
            with open(bstack111llll1lll_opy_, bstack1lllll1l_opy_ (u"ࠦࡷࠨᮔ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡐࡓࡐࡐࠣࡪࡷࡵ࡭ࠡࡵࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮕ").format(bstack111llll1lll_opy_, e))
            return []
        _11l1111l11l_opy_ = None
        _11l1111ll11_opy_ = None
        def _11l111111ll_opy_():
            bstack111llll1l11_opy_ = {}
            bstack111ll1llll1_opy_ = {}
            try:
                if self.bstack11l11111l1l_opy_.startswith(bstack1lllll1l_opy_ (u"࠭ࡻࠨᮖ")) and self.bstack11l11111l1l_opy_.endswith(bstack1lllll1l_opy_ (u"ࠧࡾࠩᮗ")):
                    bstack111llll1l11_opy_ = json.loads(self.bstack11l11111l1l_opy_)
                else:
                    bstack111llll1l11_opy_ = dict(item.split(bstack1lllll1l_opy_ (u"ࠨ࠼ࠪᮘ")) for item in self.bstack11l11111l1l_opy_.split(bstack1lllll1l_opy_ (u"ࠩ࠯ࠫᮙ")) if bstack1lllll1l_opy_ (u"ࠪ࠾ࠬᮚ") in item) if self.bstack11l11111l1l_opy_ else {}
                if self.bstack111ll1ll1l1_opy_.startswith(bstack1lllll1l_opy_ (u"ࠫࢀ࠭ᮛ")) and self.bstack111ll1ll1l1_opy_.endswith(bstack1lllll1l_opy_ (u"ࠬࢃࠧᮜ")):
                    bstack111ll1llll1_opy_ = json.loads(self.bstack111ll1ll1l1_opy_)
                else:
                    bstack111ll1llll1_opy_ = dict(item.split(bstack1lllll1l_opy_ (u"࠭࠺ࠨᮝ")) for item in self.bstack111ll1ll1l1_opy_.split(bstack1lllll1l_opy_ (u"ࠧ࠭ࠩᮞ")) if bstack1lllll1l_opy_ (u"ࠨ࠼ࠪᮟ") in item) if self.bstack111ll1ll1l1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1lllll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡩࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡱࡦࡶࡰࡪࡰࡪࡷ࠿ࠦࡻࡾࠤᮠ").format(e))
            logger.debug(bstack1lllll1l_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡲࡧࡰࡱ࡫ࡱ࡫ࡸࠦࡦࡳࡱࡰࠤࡪࡴࡶ࠻ࠢࡾࢁ࠱ࠦࡃࡍࡋ࠽ࠤࢀࢃࠢᮡ").format(bstack111llll1l11_opy_, bstack111ll1llll1_opy_))
            return bstack111llll1l11_opy_, bstack111ll1llll1_opy_
        if _11l1111l11l_opy_ is None or _11l1111ll11_opy_ is None:
            _11l1111l11l_opy_, _11l1111ll11_opy_ = _11l111111ll_opy_()
        def bstack111lllllll1_opy_(name, bstack111lll1l11l_opy_):
            if name in _11l1111ll11_opy_:
                return _11l1111ll11_opy_[name]
            if name in _11l1111l11l_opy_:
                return _11l1111l11l_opy_[name]
            if bstack111lll1l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮢ")):
                return bstack111lll1l11l_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᮣ")]
            return None
        if isinstance(data, dict):
            bstack11l1111111l_opy_ = []
            bstack111llllllll_opy_ = re.compile(bstack1lllll1l_opy_ (u"ࡸࠧ࡟࡝ࡄ࠱࡟࠶࠭࠺ࡡࡠ࠯ࠩ࠭ᮤ"))
            for name, bstack111lll1l11l_opy_ in data.items():
                if not isinstance(bstack111lll1l11l_opy_, dict):
                    continue
                if not bstack111lll1l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡶࡴ࡯ࠫᮥ")):
                    logger.warning(bstack1lllll1l_opy_ (u"ࠣࡔࡨࡴࡴࡹࡩࡵࡱࡵࡽ࡛ࠥࡒࡍࠢ࡬ࡷࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮦ").format(name, bstack111lll1l11l_opy_))
                    continue
                if not bstack111llllllll_opy_.match(name):
                    logger.warning(bstack1lllll1l_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࡧࡱࡵࡱࡦࡺࠠࡧࡱࡵࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮧ").format(name, bstack111lll1l11l_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1lllll1l_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࠨࡽࢀࠫࠥࡳࡵࡴࡶࠣ࡬ࡦࡼࡥࠡࡣࠣࡰࡪࡴࡧࡵࡪࠣࡦࡪࡺࡷࡦࡧࡱࠤ࠶ࠦࡡ࡯ࡦࠣ࠷࠵ࠦࡣࡩࡣࡵࡥࡨࡺࡥࡳࡵ࠱ࠦᮨ").format(name))
                    continue
                bstack111lll1l11l_opy_ = bstack111lll1l11l_opy_.copy()
                bstack111lll1l11l_opy_[bstack1lllll1l_opy_ (u"ࠫࡳࡧ࡭ࡦࠩᮩ")] = name
                bstack111lll1l11l_opy_[bstack1lllll1l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬᮪ࠬ")] = bstack111lllllll1_opy_(name, bstack111lll1l11l_opy_)
                if not bstack111lll1l11l_opy_.get(bstack1lllll1l_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭᮫࠭")):
                    logger.warning(bstack1lllll1l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡰࡲࡸࠥࡹࡰࡦࡥ࡬ࡪ࡮࡫ࡤࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᮬ").format(name, bstack111lll1l11l_opy_))
                    continue
                if bstack111lll1l11l_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬᮭ")) and bstack111lll1l11l_opy_[bstack1lllll1l_opy_ (u"ࠩࡥࡥࡸ࡫ࡂࡳࡣࡱࡧ࡭࠭ᮮ")] == bstack111lll1l11l_opy_[bstack1lllll1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮯ")]:
                    logger.warning(bstack1lllll1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡧ࡮ࡥࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᮰").format(name, bstack111lll1l11l_opy_))
                    continue
                bstack11l1111111l_opy_.append(bstack111lll1l11l_opy_)
            return bstack11l1111111l_opy_
        return data
    def bstack111lllll11l_opy_(self):
        data = {
            bstack1lllll1l_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫ᮱"): {
                bstack1lllll1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮲"): self.bstack111lll11l11_opy_(),
                bstack1lllll1l_opy_ (u"ࠧ࡮ࡱࡧࡩࠬ᮳"): self.bstack111lll11l1l_opy_(),
                bstack1lllll1l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ᮴"): self.bstack111lll11lll_opy_()
            }
        }
        return data
    def bstack111lll1ll11_opy_(self, config):
        bstack111ll1ll11l_opy_ = {}
        bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨ᮵")] = {
            bstack1lllll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᮶"): self.bstack111lll11l11_opy_(),
            bstack1lllll1l_opy_ (u"ࠫࡲࡵࡤࡦࠩ᮷"): self.bstack111lll11l1l_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࠨ᮸")] = {
            bstack1lllll1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮹"): self.bstack11l11111lll_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠧࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡨ࡬ࡶࡸࡺࠧᮺ")] = {
            bstack1lllll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮻ"): self.bstack11l1111ll1l_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠩࡶ࡯࡮ࡶ࡟ࡧࡣ࡬ࡰ࡮ࡴࡧࡠࡣࡱࡨࡤ࡬࡬ࡢ࡭ࡼࠫᮼ")] = {
            bstack1lllll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮽ"): self.bstack111lllll1ll_opy_()
        }
        if self.bstack1111lll1_opy_(config):
            bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠫࡷ࡫ࡴࡳࡻࡢࡸࡪࡹࡴࡴࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᮾ")] = {
                bstack1lllll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮿ"): True,
                bstack1lllll1l_opy_ (u"࠭࡭ࡢࡺࡢࡶࡪࡺࡲࡪࡧࡶࠫᯀ"): self.bstack1llllllll_opy_(config)
            }
        if self.bstack11l1ll1lll1_opy_(config):
            bstack111ll1ll11l_opy_[bstack1lllll1l_opy_ (u"ࠧࡢࡤࡲࡶࡹࡥࡢࡶ࡫࡯ࡨࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦࠩᯁ")] = {
                bstack1lllll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯂ"): True,
                bstack1lllll1l_opy_ (u"ࠩࡰࡥࡽࡥࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠨᯃ"): self.bstack11l1llllll1_opy_(config)
            }
        return bstack111ll1ll11l_opy_
    def bstack11l1111l1l_opy_(self, config):
        bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡱ࡯ࡰࡪࡩࡴࡴࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡢࡺࠢࡰࡥࡰ࡯࡮ࡨࠢࡤࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠥ࠮ࡳࡵࡴࠬ࠾࡚ࠥࡨࡦࠢࡘ࡙ࡎࡊࠠࡰࡨࠣࡸ࡭࡫ࠠࡣࡷ࡬ࡰࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᯄ")
        if not (config.get(bstack1lllll1l_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᯅ"), None) in bstack11l11l1ll1l_opy_ and self.bstack111lll11l11_opy_()):
            return None
        bstack111lll11111_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᯆ"), None)
        logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥᯇ").format(bstack111lll11111_opy_))
        try:
            bstack11ll11l1111_opy_ = bstack1lllll1l_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠧᯈ").format(bstack111lll11111_opy_)
            payload = {
                bstack1lllll1l_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨᯉ"): config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᯊ"), bstack1lllll1l_opy_ (u"ࠪࠫᯋ")),
                bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᯌ"): config.get(bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᯍ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᯎ"): os.environ.get(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᯏ"), bstack1lllll1l_opy_ (u"ࠣࠤᯐ")),
                bstack1lllll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᯑ"): int(os.environ.get(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᯒ")) or bstack1lllll1l_opy_ (u"ࠦ࠵ࠨᯓ")),
                bstack1lllll1l_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᯔ"): int(os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᯕ")) or bstack1lllll1l_opy_ (u"ࠢ࠲ࠤᯖ")),
                bstack1lllll1l_opy_ (u"ࠣࡪࡲࡷࡹࡏ࡮ࡧࡱࠥᯗ"): get_host_info(),
            }
            logger.debug(bstack1lllll1l_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡶࡡࡺ࡮ࡲࡥࡩࡀࠠࡼࡿࠥᯘ").format(payload))
            response = bstack11ll1l1llll_opy_.bstack11ll111ll1l_opy_(bstack11ll11l1111_opy_, payload)
            if response:
                logger.debug(bstack1lllll1l_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡄࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᯙ").format(response))
                return response
            else:
                logger.error(bstack1lllll1l_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᯚ").format(bstack111lll11111_opy_))
                return None
        except Exception as e:
            logger.error(bstack1lllll1l_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇࠤࢀࢃ࠺ࠡࡽࢀࠦᯛ").format(bstack111lll11111_opy_, e))
            return None
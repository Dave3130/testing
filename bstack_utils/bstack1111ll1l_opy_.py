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
import os
import tempfile
import math
from bstack_utils import bstack11l111l1ll_opy_
from bstack_utils.constants import bstack1111l1lll_opy_, bstack11l11llll1l_opy_
from bstack_utils.helper import bstack11ll1ll11l1_opy_, get_host_info
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11ll1l1l11l_opy_
import json
import re
import sys
bstack111lll1lll1_opy_ = bstack11l111_opy_ (u"ࠨࡲࡦࡶࡵࡽ࡙࡫ࡳࡵࡵࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧ᭥")
bstack111llllll11_opy_ = bstack11l111_opy_ (u"ࠢࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨ᭦")
bstack11l1111l1l1_opy_ = bstack11l111_opy_ (u"ࠣࡴࡸࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡇࡣ࡬ࡰࡪࡪࡆࡪࡴࡶࡸࠧ᭧")
bstack11l11111111_opy_ = bstack11l111_opy_ (u"ࠤࡵࡩࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࠥ᭨")
bstack111lllll1l1_opy_ = bstack11l111_opy_ (u"ࠥࡷࡰ࡯ࡰࡇ࡮ࡤ࡯ࡾࡧ࡮ࡥࡈࡤ࡭ࡱ࡫ࡤࠣ᭩")
bstack11l11111ll1_opy_ = bstack11l111_opy_ (u"ࠦࡷࡻ࡮ࡔ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠣ᭪")
bstack11l1111lll1_opy_ = {
    bstack111lll1lll1_opy_,
    bstack111llllll11_opy_,
    bstack11l1111l1l1_opy_,
    bstack11l11111111_opy_,
    bstack111lllll1l1_opy_,
    bstack11l11111ll1_opy_
}
bstack11l1111l111_opy_ = {bstack11l111_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬ᭫")}
logger = bstack11l111l1ll_opy_.get_logger(__name__, bstack1111l1lll_opy_)
class bstack111lll1l1ll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111lllll1ll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1lll1l1ll_opy_:
    _1ll1ll111ll_opy_ = None
    def __init__(self, config):
        self.bstack111ll1ll1ll_opy_ = False
        self.bstack111ll1lll11_opy_ = False
        self.bstack11l1111111l_opy_ = False
        self.bstack111llll1l11_opy_ = False
        self.bstack111llll111l_opy_ = None
        self.bstack11l1111llll_opy_ = bstack111lll1l1ll_opy_()
        self.bstack11l11111l11_opy_ = None
        opts = config.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵ᭬ࠪ"), {})
        self.bstack111lll1111l_opy_ = config.get(bstack11l111_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡇࡑ࡚ࠬ᭭"), bstack11l111_opy_ (u"ࠣࠤ᭮"))
        self.bstack111lll1ll1l_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠧ᭯"), bstack11l111_opy_ (u"ࠥࠦ᭰"))
        bstack111ll1ll1l1_opy_ = opts.get(bstack11l11111ll1_opy_, {})
        bstack111llllll1l_opy_ = None
        if bstack11l111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ᭱") in bstack111ll1ll1l1_opy_:
            bstack111llllll1l_opy_ = bstack111ll1ll1l1_opy_[bstack11l111_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᭲")]
            if bstack111llllll1l_opy_ is None:
                bstack111llllll1l_opy_ = []
        self.__11l1111ll11_opy_(
            bstack111ll1ll1l1_opy_.get(bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᭳"), False),
            bstack111ll1ll1l1_opy_.get(bstack11l111_opy_ (u"ࠧ࡮ࡱࡧࡩࠬ᭴"), bstack11l111_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭵")),
            bstack111llllll1l_opy_
        )
        self.__11l1111l1ll_opy_(opts.get(bstack11l1111l1l1_opy_, False))
        self.__111lll11lll_opy_(opts.get(bstack11l11111111_opy_, False))
        self.__111lll11111_opy_(opts.get(bstack111lllll1l1_opy_, False))
    @classmethod
    def bstack111l11l1_opy_(cls, config=None):
        if cls._1ll1ll111ll_opy_ is None and config is not None:
            cls._1ll1ll111ll_opy_ = bstack1lll1l1ll_opy_(config)
        return cls._1ll1ll111ll_opy_
    @staticmethod
    def bstack1lll111l1_opy_(config: dict) -> bool:
        bstack111lll11l11_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭶"), {}).get(bstack111lll1lll1_opy_, {})
        return bstack111lll11l11_opy_.get(bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᭷"), False)
    @staticmethod
    def bstack1lllll1l1_opy_(config: dict) -> int:
        bstack111lll11l11_opy_ = config.get(bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭸"), {}).get(bstack111lll1lll1_opy_, {})
        retries = 0
        if bstack1lll1l1ll_opy_.bstack1lll111l1_opy_(config):
            retries = bstack111lll11l11_opy_.get(bstack11l111_opy_ (u"ࠬࡳࡡࡹࡔࡨࡸࡷ࡯ࡥࡴࠩ᭹"), 1)
        return retries
    @staticmethod
    def bstack1l1llll1l_opy_(config: dict) -> dict:
        bstack111llll1lll_opy_ = config.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭺"), {})
        return {
            key: value for key, value in bstack111llll1lll_opy_.items() if key in bstack11l1111lll1_opy_
        }
    @staticmethod
    def bstack111ll1lll1l_opy_():
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭻")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤ᭼").format(os.getenv(bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ᭽")))))
    @staticmethod
    def bstack11l1111ll1l_opy_(test_name: str):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭾")
        bstack111llll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥ᭿").format(os.getenv(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᮀ"))))
        with open(bstack111llll11l1_opy_, bstack11l111_opy_ (u"࠭ࡡࠨᮁ")) as file:
            file.write(bstack11l111_opy_ (u"ࠢࡼࡿ࡟ࡲࠧᮂ").format(test_name))
    @staticmethod
    def bstack11l111111l1_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l1111l111_opy_
    @staticmethod
    def bstack11l1lllll1l_opy_(config: dict) -> bool:
        bstack111lll11ll1_opy_ = config.get(bstack11l111_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬᮃ"), {}).get(bstack111llllll11_opy_, {})
        return bstack111lll11ll1_opy_.get(bstack11l111_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮄ"), False)
    @staticmethod
    def bstack11l1lllllll_opy_(config: dict, bstack11ll1111111_opy_: int = 0) -> int:
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠱ࠦࡷࡩ࡫ࡦ࡬ࠥࡩࡡ࡯ࠢࡥࡩࠥࡧ࡮ࠡࡣࡥࡷࡴࡲࡵࡵࡧࠣࡲࡺࡳࡢࡦࡴࠣࡳࡷࠦࡡࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࠭ࡪࡩࡤࡶࠬ࠾࡚ࠥࡨࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺ࡯ࡵࡣ࡯ࡣࡹ࡫ࡳࡵࡵࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࠪࡵࡩࡶࡻࡩࡳࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳࠪ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮅ")
        bstack111lll11ll1_opy_ = config.get(bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮆ"), {}).get(bstack11l111_opy_ (u"ࠬࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠫᮇ"), {})
        bstack111ll1ll11l_opy_ = 0
        bstack11l111111ll_opy_ = 0
        if bstack1lll1l1ll_opy_.bstack11l1lllll1l_opy_(config):
            bstack11l111111ll_opy_ = bstack111lll11ll1_opy_.get(bstack11l111_opy_ (u"࠭࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶࠫᮈ"), 5)
            if isinstance(bstack11l111111ll_opy_, str) and bstack11l111111ll_opy_.endswith(bstack11l111_opy_ (u"ࠧࠦࠩᮉ")):
                try:
                    percentage = int(bstack11l111111ll_opy_.strip(bstack11l111_opy_ (u"ࠨࠧࠪᮊ")))
                    if bstack11ll1111111_opy_ > 0:
                        bstack111ll1ll11l_opy_ = math.ceil((percentage * bstack11ll1111111_opy_) / 100)
                    else:
                        raise ValueError(bstack11l111_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨ࠱ࡧࡧࡳࡦࡦࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࡹ࠮ࠣᮋ"))
                except ValueError as e:
                    raise ValueError(bstack11l111_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥࠡࡸࡤࡰࡺ࡫ࠠࡧࡱࡵࠤࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴ࠼ࠣࡿࢂࠨᮌ").format(bstack11l111111ll_opy_)) from e
            else:
                bstack111ll1ll11l_opy_ = int(bstack11l111111ll_opy_)
        logger.info(bstack11l111_opy_ (u"ࠦࡒࡧࡸࠡࡨࡤ࡭ࡱࡻࡲࡦࡵࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡳࡦࡶࠣࡸࡴࡀࠠࡼࡿࠣࠬ࡫ࡸ࡯࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠯ࠢᮍ").format(bstack111ll1ll11l_opy_, bstack11l111111ll_opy_))
        return bstack111ll1ll11l_opy_
    def bstack111llll11ll_opy_(self):
        return self.bstack111llll1l11_opy_
    def bstack111lllllll1_opy_(self):
        return self.bstack111llll111l_opy_
    def bstack111lllll111_opy_(self):
        return self.bstack11l11111l11_opy_
    def __11l1111ll11_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll1l11_opy_ = bool(enabled)
            if mode not in [bstack11l111_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬᮎ"), bstack11l111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡐࡰ࡯ࡽࠬᮏ")]:
                logger.warning(bstack11l111_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡱࡴࡪࡥࠡࠩࡾࢁࠬࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡴࡰࠢࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ࠲ࠧᮐ").format(mode))
                mode = bstack11l111_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᮑ")
            self.bstack111llll111l_opy_ = mode
            if source is None:
                self.bstack11l11111l11_opy_ = None
            elif isinstance(source, list):
                self.bstack11l11111l11_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l111_opy_ (u"ࠩ࠱࡮ࡸࡵ࡮ࠨᮒ")):
                self.bstack11l11111l11_opy_ = self._111llll1111_opy_(source)
            self.__111lll111ll_opy_()
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࠳ࠠࡦࡰࡤࡦࡱ࡫ࡤ࠻ࠢࡾࢁ࠱ࠦ࡭ࡰࡦࡨ࠾ࠥࢁࡽ࠭ࠢࡶࡳࡺࡸࡣࡦ࠼ࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᮓ").format(enabled, mode, source, e))
    def bstack111lllll11l_opy_(self):
        return self.bstack111ll1ll1ll_opy_
    def __11l1111l1ll_opy_(self, value):
        self.bstack111ll1ll1ll_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def bstack111llll1ll1_opy_(self):
        return self.bstack111ll1lll11_opy_
    def __111lll11lll_opy_(self, value):
        self.bstack111ll1lll11_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def bstack111lll11l1l_opy_(self):
        return self.bstack11l1111111l_opy_
    def __111lll11111_opy_(self, value):
        self.bstack11l1111111l_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def __111lll111ll_opy_(self):
        if self.bstack111llll1l11_opy_:
            self.bstack111ll1ll1ll_opy_ = False
            self.bstack111ll1lll11_opy_ = False
            self.bstack11l1111111l_opy_ = False
            self.bstack11l1111llll_opy_.enable(bstack11l11111ll1_opy_)
        elif self.bstack111ll1ll1ll_opy_:
            self.bstack111ll1lll11_opy_ = False
            self.bstack11l1111111l_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack11l1111llll_opy_.enable(bstack11l1111l1l1_opy_)
        elif self.bstack111ll1lll11_opy_:
            self.bstack111ll1ll1ll_opy_ = False
            self.bstack11l1111111l_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack11l1111llll_opy_.enable(bstack11l11111111_opy_)
        elif self.bstack11l1111111l_opy_:
            self.bstack111ll1ll1ll_opy_ = False
            self.bstack111ll1lll11_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack11l1111llll_opy_.enable(bstack111lllll1l1_opy_)
        else:
            self.bstack11l1111llll_opy_.disable()
    def bstack1llllll11_opy_(self):
        return self.bstack11l1111llll_opy_.bstack111lllll1ll_opy_()
    def bstack11ll1l11ll_opy_(self):
        if self.bstack11l1111llll_opy_.bstack111lllll1ll_opy_():
            return self.bstack11l1111llll_opy_.get_name()
        return None
    def _111llll1111_opy_(self, bstack111lll1l1l1_opy_):
        bstack11l111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡹ࡯ࡶࡴࡦࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠣࡥࡳࡪࠠࡧࡱࡵࡱࡦࡺࠠࡪࡶࠣࡪࡴࡸࠠࡴ࡯ࡤࡶࡹࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡲࡹࡷࡩࡥࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡕࡧࡴࡩࠢࡷࡳࠥࡺࡨࡦࠢࡍࡗࡔࡔࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡌ࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡵࡩࡵࡵࡳࡪࡶࡲࡶࡾࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮔ")
        if not os.path.isfile(bstack111lll1l1l1_opy_):
            logger.error(bstack11l111_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠥᮕ").format(bstack111lll1l1l1_opy_))
            return []
        data = None
        try:
            with open(bstack111lll1l1l1_opy_, bstack11l111_opy_ (u"ࠨࡲࠣᮖ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l111_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡋࡕࡒࡒࠥ࡬ࡲࡰ࡯ࠣࡷࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮗ").format(bstack111lll1l1l1_opy_, e))
            return []
        _111llll1l1l_opy_ = None
        _111lll1ll11_opy_ = None
        def _111lll1l111_opy_():
            bstack11l111l1111_opy_ = {}
            bstack111lll1l11l_opy_ = {}
            try:
                if self.bstack111lll1111l_opy_.startswith(bstack11l111_opy_ (u"ࠨࡽࠪᮘ")) and self.bstack111lll1111l_opy_.endswith(bstack11l111_opy_ (u"ࠩࢀࠫᮙ")):
                    bstack11l111l1111_opy_ = json.loads(self.bstack111lll1111l_opy_)
                else:
                    bstack11l111l1111_opy_ = dict(item.split(bstack11l111_opy_ (u"ࠪ࠾ࠬᮚ")) for item in self.bstack111lll1111l_opy_.split(bstack11l111_opy_ (u"ࠫ࠱࠭ᮛ")) if bstack11l111_opy_ (u"ࠬࡀࠧᮜ") in item) if self.bstack111lll1111l_opy_ else {}
                if self.bstack111lll1ll1l_opy_.startswith(bstack11l111_opy_ (u"࠭ࡻࠨᮝ")) and self.bstack111lll1ll1l_opy_.endswith(bstack11l111_opy_ (u"ࠧࡾࠩᮞ")):
                    bstack111lll1l11l_opy_ = json.loads(self.bstack111lll1ll1l_opy_)
                else:
                    bstack111lll1l11l_opy_ = dict(item.split(bstack11l111_opy_ (u"ࠨ࠼ࠪᮟ")) for item in self.bstack111lll1ll1l_opy_.split(bstack11l111_opy_ (u"ࠩ࠯ࠫᮠ")) if bstack11l111_opy_ (u"ࠪ࠾ࠬᮡ") in item) if self.bstack111lll1ll1l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l111_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡦࡸࡳࡪࡰࡪࠤ࡫࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡳࡡࡱࡲ࡬ࡲ࡬ࡹ࠺ࠡࡽࢀࠦᮢ").format(e))
            logger.debug(bstack11l111_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࠽ࠤࢀࢃࠬࠡࡅࡏࡍ࠿ࠦࡻࡾࠤᮣ").format(bstack11l111l1111_opy_, bstack111lll1l11l_opy_))
            return bstack11l111l1111_opy_, bstack111lll1l11l_opy_
        if _111llll1l1l_opy_ is None or _111lll1ll11_opy_ is None:
            _111llll1l1l_opy_, _111lll1ll11_opy_ = _111lll1l111_opy_()
        def bstack111lll1llll_opy_(name, bstack111ll1llll1_opy_):
            if name in _111lll1ll11_opy_:
                return _111lll1ll11_opy_[name]
            if name in _111llll1l1l_opy_:
                return _111llll1l1l_opy_[name]
            if bstack111ll1llll1_opy_.get(bstack11l111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭ᮤ")):
                return bstack111ll1llll1_opy_[bstack11l111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮥ")]
            return None
        if isinstance(data, dict):
            bstack11l11111lll_opy_ = []
            bstack111ll1lllll_opy_ = re.compile(bstack11l111_opy_ (u"ࡳࠩࡡ࡟ࡆ࠳࡚࠱࠯࠼ࡣࡢ࠱ࠤࠨᮦ"))
            for name, bstack111ll1llll1_opy_ in data.items():
                if not isinstance(bstack111ll1llll1_opy_, dict):
                    continue
                if not bstack111ll1llll1_opy_.get(bstack11l111_opy_ (u"ࠩࡸࡶࡱ࠭ᮧ")):
                    logger.warning(bstack11l111_opy_ (u"ࠥࡖࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡖࡔࡏࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᮨ").format(name, bstack111ll1llll1_opy_))
                    continue
                if not bstack111ll1lllll_opy_.match(name):
                    logger.warning(bstack11l111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࡩࡳࡷࡳࡡࡵࠢࡩࡳࡷࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮩ").format(name, bstack111ll1llll1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l111_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࠪࡿࢂ࠭ࠠ࡮ࡷࡶࡸࠥ࡮ࡡࡷࡧࠣࡥࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡨࡥࡵࡹࡨࡩࡳࠦ࠱ࠡࡣࡱࡨࠥ࠹࠰ࠡࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࡷ࠳ࠨ᮪").format(name))
                    continue
                bstack111ll1llll1_opy_ = bstack111ll1llll1_opy_.copy()
                bstack111ll1llll1_opy_[bstack11l111_opy_ (u"࠭࡮ࡢ࡯ࡨ᮫ࠫ")] = name
                bstack111ll1llll1_opy_[bstack11l111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮬ")] = bstack111lll1llll_opy_(name, bstack111ll1llll1_opy_)
                if not bstack111ll1llll1_opy_.get(bstack11l111_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮭ")):
                    logger.warning(bstack11l111_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡲࡴࡺࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮮ").format(name, bstack111ll1llll1_opy_))
                    continue
                if bstack111ll1llll1_opy_.get(bstack11l111_opy_ (u"ࠪࡦࡦࡹࡥࡃࡴࡤࡲࡨ࡮ࠧᮯ")) and bstack111ll1llll1_opy_[bstack11l111_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨ᮰")] == bstack111ll1llll1_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬ᮱")]:
                    logger.warning(bstack11l111_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡢࡰࡧࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡺࡨࡦࠢࡶࡥࡲ࡫ࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨ᮲").format(name, bstack111ll1llll1_opy_))
                    continue
                bstack11l11111lll_opy_.append(bstack111ll1llll1_opy_)
            return bstack11l11111lll_opy_
        return data
    def bstack11l1111l11l_opy_(self):
        data = {
            bstack11l111_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭᮳"): {
                bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩ᮴"): self.bstack111llll11ll_opy_(),
                bstack11l111_opy_ (u"ࠩࡰࡳࡩ࡫ࠧ᮵"): self.bstack111lllllll1_opy_(),
                bstack11l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪ᮶"): self.bstack111lllll111_opy_()
            }
        }
        return data
    def bstack111lll111l1_opy_(self, config):
        bstack111llllllll_opy_ = {}
        bstack111llllllll_opy_[bstack11l111_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪ᮷")] = {
            bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᮸"): self.bstack111llll11ll_opy_(),
            bstack11l111_opy_ (u"࠭࡭ࡰࡦࡨࠫ᮹"): self.bstack111lllllll1_opy_()
        }
        bstack111llllllll_opy_[bstack11l111_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࠪᮺ")] = {
            bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮻ"): self.bstack111llll1ll1_opy_()
        }
        bstack111llllllll_opy_[bstack11l111_opy_ (u"ࠩࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࡢࡪ࡮ࡸࡳࡵࠩᮼ")] = {
            bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮽ"): self.bstack111lllll11l_opy_()
        }
        bstack111llllllll_opy_[bstack11l111_opy_ (u"ࠫࡸࡱࡩࡱࡡࡩࡥ࡮ࡲࡩ࡯ࡩࡢࡥࡳࡪ࡟ࡧ࡮ࡤ࡯ࡾ࠭ᮾ")] = {
            bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮿ"): self.bstack111lll11l1l_opy_()
        }
        if self.bstack1lll111l1_opy_(config):
            bstack111llllllll_opy_[bstack11l111_opy_ (u"࠭ࡲࡦࡶࡵࡽࡤࡺࡥࡴࡶࡶࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᯀ")] = {
                bstack11l111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯁ"): True,
                bstack11l111_opy_ (u"ࠨ࡯ࡤࡼࡤࡸࡥࡵࡴ࡬ࡩࡸ࠭ᯂ"): self.bstack1lllll1l1_opy_(config)
            }
        if self.bstack11l1lllll1l_opy_(config):
            bstack111llllllll_opy_[bstack11l111_opy_ (u"ࠩࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᯃ")] = {
                bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯄ"): True,
                bstack11l111_opy_ (u"ࠫࡲࡧࡸࡠࡨࡤ࡭ࡱࡻࡲࡦࡵࠪᯅ"): self.bstack11l1lllllll_opy_(config)
            }
        return bstack111llllllll_opy_
    def bstack111llll1l1_opy_(self, config):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡳࡱࡲࡥࡤࡶࡶࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡤࡼࠤࡲࡧ࡫ࡪࡰࡪࠤࡦࠦࡣࡢ࡮࡯ࠤࡹࡵࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤ࡚࡛ࡉࡅࠢࡲࡪࠥࡺࡨࡦࠢࡥࡹ࡮ࡲࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡪࡡࡵࡣࠣࡪࡴࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᯆ")
        if not (config.get(bstack11l111_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᯇ"), None) in bstack11l11llll1l_opy_ and self.bstack111llll11ll_opy_()):
            return None
        bstack11l11111l1l_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᯈ"), None)
        logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡃࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᯉ").format(bstack11l11111l1l_opy_))
        try:
            bstack11ll111ll11_opy_ = bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠢᯊ").format(bstack11l11111l1l_opy_)
            payload = {
                bstack11l111_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᯋ"): config.get(bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᯌ"), bstack11l111_opy_ (u"ࠬ࠭ᯍ")),
                bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᯎ"): config.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᯏ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᯐ"): os.environ.get(bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᯑ"), bstack11l111_opy_ (u"ࠥࠦᯒ")),
                bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᯓ"): int(os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᯔ")) or bstack11l111_opy_ (u"ࠨ࠰ࠣᯕ")),
                bstack11l111_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᯖ"): int(os.environ.get(bstack11l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᯗ")) or bstack11l111_opy_ (u"ࠤ࠴ࠦᯘ")),
                bstack11l111_opy_ (u"ࠥ࡬ࡴࡹࡴࡊࡰࡩࡳࠧᯙ"): get_host_info(),
            }
            logger.debug(bstack11l111_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡱࡣࡼࡰࡴࡧࡤ࠻ࠢࡾࢁࠧᯚ").format(payload))
            response = bstack11ll1l1l11l_opy_.bstack11ll111llll_opy_(bstack11ll111ll11_opy_, payload)
            if response:
                logger.debug(bstack11l111_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡆࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᯛ").format(response))
                return response
            else:
                logger.error(bstack11l111_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥᯜ").format(bstack11l11111l1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࠦࡻࡾ࠼ࠣࡿࢂࠨᯝ").format(bstack11l11111l1l_opy_, e))
            return None
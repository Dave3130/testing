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
import os
import tempfile
import math
from bstack_utils import bstack11ll1111l_opy_
from bstack_utils.constants import bstack11l11ll11_opy_, bstack11l11llll11_opy_
from bstack_utils.helper import bstack11ll1l1ll11_opy_, get_host_info
from bstack_utils.bstack11ll1ll1l1l_opy_ import bstack11ll1ll11ll_opy_
import json
import re
import sys
bstack111lll1llll_opy_ = bstack1lll11l_opy_ (u"ࠢࡳࡧࡷࡶࡾ࡚ࡥࡴࡶࡶࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨ᭴")
bstack11l1111l1l1_opy_ = bstack1lll11l_opy_ (u"ࠣࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢ᭵")
bstack111ll1ll1ll_opy_ = bstack1lll11l_opy_ (u"ࠤࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࡇ࡫ࡵࡷࡹࠨ᭶")
bstack111lllll11l_opy_ = bstack1lll11l_opy_ (u"ࠥࡶࡪࡸࡵ࡯ࡒࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡋࡧࡩ࡭ࡧࡧࠦ᭷")
bstack111lll11111_opy_ = bstack1lll11l_opy_ (u"ࠦࡸࡱࡩࡱࡈ࡯ࡥࡰࡿࡡ࡯ࡦࡉࡥ࡮ࡲࡥࡥࠤ᭸")
bstack11l11111l1l_opy_ = bstack1lll11l_opy_ (u"ࠧࡸࡵ࡯ࡕࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠤ᭹")
bstack111lll1ll11_opy_ = {
    bstack111lll1llll_opy_,
    bstack11l1111l1l1_opy_,
    bstack111ll1ll1ll_opy_,
    bstack111lllll11l_opy_,
    bstack111lll11111_opy_,
    bstack11l11111l1l_opy_
}
bstack111ll1l1ll1_opy_ = {bstack1lll11l_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᭺")}
logger = bstack11ll1111l_opy_.get_logger(__name__, bstack11l11ll11_opy_)
class bstack111llll1111_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111lll11l1l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack111l1l1l_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config):
        self.bstack111llll1l1l_opy_ = False
        self.bstack111llll11ll_opy_ = False
        self.bstack111ll1ll111_opy_ = False
        self.bstack11l111111ll_opy_ = False
        self.bstack111ll1llll1_opy_ = None
        self.bstack111lll1111l_opy_ = bstack111llll1111_opy_()
        self.bstack111llllllll_opy_ = None
        opts = config.get(bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭻"), {})
        self.bstack111llll1lll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡈࡒ࡛࠭᭼"), bstack1lll11l_opy_ (u"ࠤࠥ᭽"))
        self.bstack11l1111111l_opy_ = config.get(bstack1lll11l_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡈࡒࡉࠨ᭾"), bstack1lll11l_opy_ (u"ࠦࠧ᭿"))
        bstack111ll1lll1l_opy_ = opts.get(bstack11l11111l1l_opy_, {})
        bstack111lll11ll1_opy_ = None
        if bstack1lll11l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᮀ") in bstack111ll1lll1l_opy_:
            bstack111lll1l11l_opy_ = bstack111ll1lll1l_opy_[bstack1lll11l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᮁ")]
            if bstack111lll1l11l_opy_ is None or (isinstance(bstack111lll1l11l_opy_, str) and bstack111lll1l11l_opy_.strip() == bstack1lll11l_opy_ (u"ࠧࠨᮂ")) or (isinstance(bstack111lll1l11l_opy_, list) and len(bstack111lll1l11l_opy_) == 0):
                bstack111lll11ll1_opy_ = []
            elif isinstance(bstack111lll1l11l_opy_, list):
                bstack111lll11ll1_opy_ = bstack111lll1l11l_opy_
            elif isinstance(bstack111lll1l11l_opy_, str) and bstack111lll1l11l_opy_.strip():
                bstack111lll11ll1_opy_ = bstack111lll1l11l_opy_
            else:
                logger.warning(bstack1lll11l_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡳࡺࡸࡣࡦࠢࡹࡥࡱࡻࡥࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡴࡰࠢࡨࡱࡵࡺࡹࠡ࡮࡬ࡷࡹ࠴ࠢᮃ").format(bstack111lll1l11l_opy_))
                bstack111lll11ll1_opy_ = []
        self.__111lll111l1_opy_(
            bstack111ll1lll1l_opy_.get(bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮄ"), False),
            bstack111ll1lll1l_opy_.get(bstack1lll11l_opy_ (u"ࠪࡱࡴࡪࡥࠨᮅ"), bstack1lll11l_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫᮆ")),
            bstack111lll11ll1_opy_
        )
        self.__111lll11lll_opy_(opts.get(bstack111ll1ll1ll_opy_, False))
        self.__11l11111lll_opy_(opts.get(bstack111lllll11l_opy_, False))
        self.__111llll11l1_opy_(opts.get(bstack111lll11111_opy_, False))
    @classmethod
    def bstack111l1111_opy_(cls, config=None):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack111l1l1l_opy_(config)
        return cls._1ll1l1lll11_opy_
    @staticmethod
    def bstack11111lll_opy_(config: dict) -> bool:
        bstack111llllll11_opy_ = config.get(bstack1lll11l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮇ"), {}).get(bstack111lll1llll_opy_, {})
        return bstack111llllll11_opy_.get(bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮈ"), False)
    @staticmethod
    def bstack111l11ll_opy_(config: dict) -> int:
        bstack111llllll11_opy_ = config.get(bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᮉ"), {}).get(bstack111lll1llll_opy_, {})
        retries = 0
        if bstack111l1l1l_opy_.bstack11111lll_opy_(config):
            retries = bstack111llllll11_opy_.get(bstack1lll11l_opy_ (u"ࠨ࡯ࡤࡼࡗ࡫ࡴࡳ࡫ࡨࡷࠬᮊ"), 1)
        return retries
    @staticmethod
    def bstack11ll1ll1l_opy_(config: dict) -> dict:
        bstack111ll1l1l1l_opy_ = config.get(bstack1lll11l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᮋ"), {})
        return {
            key: value for key, value in bstack111ll1l1l1l_opy_.items() if key in bstack111lll1ll11_opy_
        }
    @staticmethod
    def bstack111lll1ll1l_opy_():
        bstack1lll11l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᮌ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧᮍ").format(os.getenv(bstack1lll11l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᮎ")))))
    @staticmethod
    def bstack111ll1lllll_opy_(test_name: str):
        bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᮏ")
        bstack111ll1l11ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lll11l_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨᮐ").format(os.getenv(bstack1lll11l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨᮑ"))))
        with open(bstack111ll1l11ll_opy_, bstack1lll11l_opy_ (u"ࠩࡤࠫᮒ")) as file:
            file.write(bstack1lll11l_opy_ (u"ࠥࡿࢂࡢ࡮ࠣᮓ").format(test_name))
    @staticmethod
    def bstack11l11111l11_opy_(framework: str) -> bool:
       return framework.lower() in bstack111ll1l1ll1_opy_
    @staticmethod
    def bstack11l1llll11l_opy_(config: dict) -> bool:
        bstack11l1111l1ll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮔ"), {}).get(bstack11l1111l1l1_opy_, {})
        return bstack11l1111l1ll_opy_.get(bstack1lll11l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮕ"), False)
    @staticmethod
    def bstack11l1ll1ll11_opy_(config: dict, bstack11l1ll1llll_opy_: int = 0) -> int:
        bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠭ࠢࡺ࡬࡮ࡩࡨࠡࡥࡤࡲࠥࡨࡥࠡࡣࡱࠤࡦࡨࡳࡰ࡮ࡸࡸࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡳࠢࡤࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡪ࡮࡭ࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡲࡸࡦࡲ࡟ࡵࡧࡶࡸࡸࠦࠨࡪࡰࡷ࠭࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤ࠭ࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮖ")
        bstack11l1111l1ll_opy_ = config.get(bstack1lll11l_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᮗ"), {}).get(bstack1lll11l_opy_ (u"ࠨࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠧᮘ"), {})
        bstack111llll111l_opy_ = 0
        bstack111lll1l1l1_opy_ = 0
        if bstack111l1l1l_opy_.bstack11l1llll11l_opy_(config):
            bstack111lll1l1l1_opy_ = bstack11l1111l1ll_opy_.get(bstack1lll11l_opy_ (u"ࠩࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹࠧᮙ"), 5)
            if isinstance(bstack111lll1l1l1_opy_, str) and bstack111lll1l1l1_opy_.endswith(bstack1lll11l_opy_ (u"ࠪࠩࠬᮚ")):
                try:
                    percentage = int(bstack111lll1l1l1_opy_.strip(bstack1lll11l_opy_ (u"ࠫࠪ࠭ᮛ")))
                    if bstack11l1ll1llll_opy_ > 0:
                        bstack111llll111l_opy_ = math.ceil((percentage * bstack11l1ll1llll_opy_) / 100)
                    else:
                        raise ValueError(bstack1lll11l_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡱࡺࡹࡴࠡࡤࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵ࠱ࠦᮜ"))
                except ValueError as e:
                    raise ValueError(bstack1lll11l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨࠤࡻࡧ࡬ࡶࡧࠣࡪࡴࡸࠠ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷ࠿ࠦࡻࡾࠤᮝ").format(bstack111lll1l1l1_opy_)) from e
            else:
                bstack111llll111l_opy_ = int(bstack111lll1l1l1_opy_)
        logger.info(bstack1lll11l_opy_ (u"ࠢࡎࡣࡻࠤ࡫ࡧࡩ࡭ࡷࡵࡩࡸࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡶࡩࡹࠦࡴࡰ࠼ࠣࡿࢂࠦࠨࡧࡴࡲࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡻࡾࠫࠥᮞ").format(bstack111llll111l_opy_, bstack111lll1l1l1_opy_))
        return bstack111llll111l_opy_
    def bstack111lll11l11_opy_(self):
        return self.bstack11l111111ll_opy_
    def bstack111lll1lll1_opy_(self):
        return self.bstack111ll1llll1_opy_
    def bstack111ll1ll1l1_opy_(self):
        return self.bstack111llllllll_opy_
    def __111lll111l1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l111111ll_opy_ = bool(enabled)
            if mode not in [bstack1lll11l_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᮟ"), bstack1lll11l_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡓࡳࡲࡹࠨᮠ")]:
                logger.warning(bstack1lll11l_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࡭ࡰࡦࡨࠤࠬࢁࡽࠨࠢࡳࡶࡴࡼࡩࡥࡧࡧ࠲ࠥࡊࡥࡧࡣࡸࡰࡹ࡯࡮ࡨࠢࡷࡳࠥ࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭࠮ࠣᮡ").format(mode))
                mode = bstack1lll11l_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫᮢ")
            self.bstack111ll1llll1_opy_ = mode
            if source is None:
                self.bstack111llllllll_opy_ = None
            elif isinstance(source, list):
                self.bstack111llllllll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1lll11l_opy_ (u"ࠬ࠴ࡪࡴࡱࡱࠫᮣ")):
                self.bstack111llllllll_opy_ = self._111llllll1l_opy_(source)
            self.__11l11111ll1_opy_()
        except Exception as e:
            logger.error(bstack1lll11l_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡ࠯ࠣࡩࡳࡧࡢ࡭ࡧࡧ࠾ࠥࢁࡽ࠭ࠢࡰࡳࡩ࡫࠺ࠡࡽࢀ࠰ࠥࡹ࡯ࡶࡴࡦࡩ࠿ࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᮤ").format(enabled, mode, source, e))
    def bstack111llll1l11_opy_(self):
        return self.bstack111llll1l1l_opy_
    def __111lll11lll_opy_(self, value):
        self.bstack111llll1l1l_opy_ = bool(value)
        self.__11l11111ll1_opy_()
    def bstack11l1111l11l_opy_(self):
        return self.bstack111llll11ll_opy_
    def __11l11111lll_opy_(self, value):
        self.bstack111llll11ll_opy_ = bool(value)
        self.__11l11111ll1_opy_()
    def bstack111lllllll1_opy_(self):
        return self.bstack111ll1ll111_opy_
    def __111llll11l1_opy_(self, value):
        self.bstack111ll1ll111_opy_ = bool(value)
        self.__11l11111ll1_opy_()
    def __11l11111ll1_opy_(self):
        if self.bstack11l111111ll_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111llll11ll_opy_ = False
            self.bstack111ll1ll111_opy_ = False
            self.bstack111lll1111l_opy_.enable(bstack11l11111l1l_opy_)
        elif self.bstack111llll1l1l_opy_:
            self.bstack111llll11ll_opy_ = False
            self.bstack111ll1ll111_opy_ = False
            self.bstack11l111111ll_opy_ = False
            self.bstack111lll1111l_opy_.enable(bstack111ll1ll1ll_opy_)
        elif self.bstack111llll11ll_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111ll1ll111_opy_ = False
            self.bstack11l111111ll_opy_ = False
            self.bstack111lll1111l_opy_.enable(bstack111lllll11l_opy_)
        elif self.bstack111ll1ll111_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111llll11ll_opy_ = False
            self.bstack11l111111ll_opy_ = False
            self.bstack111lll1111l_opy_.enable(bstack111lll11111_opy_)
        else:
            self.bstack111lll1111l_opy_.disable()
    def bstack1111llll_opy_(self):
        return self.bstack111lll1111l_opy_.bstack111lll11l1l_opy_()
    def bstack11l11l11l1_opy_(self):
        if self.bstack111lll1111l_opy_.bstack111lll11l1l_opy_():
            return self.bstack111lll1111l_opy_.get_name()
        return None
    def _111llllll1l_opy_(self, bstack111lll111ll_opy_):
        bstack1lll11l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡵࡲࡹࡷࡩࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠦࡡ࡯ࡦࠣࡪࡴࡸ࡭ࡢࡶࠣ࡭ࡹࠦࡦࡰࡴࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸࡵࡵࡳࡥࡨࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠠࠩࡵࡷࡶ࠮ࡀࠠࡑࡣࡷ࡬ࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡓࡐࡐࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡈࡲࡶࡲࡧࡴࡵࡧࡧࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡸࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᮥ")
        if not os.path.isfile(bstack111lll111ll_opy_):
            logger.error(bstack1lll11l_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠨᮦ").format(bstack111lll111ll_opy_))
            return []
        data = None
        try:
            with open(bstack111lll111ll_opy_, bstack1lll11l_opy_ (u"ࠤࡵࠦᮧ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1lll11l_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡎࡘࡕࡎࠡࡨࡵࡳࡲࠦࡳࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮨ").format(bstack111lll111ll_opy_, e))
            return []
        _111lll1l1ll_opy_ = None
        _111ll1lll11_opy_ = None
        def _111lllll111_opy_():
            bstack11l1111l111_opy_ = {}
            bstack111lllll1ll_opy_ = {}
            try:
                if self.bstack111llll1lll_opy_.startswith(bstack1lll11l_opy_ (u"ࠫࢀ࠭ᮩ")) and self.bstack111llll1lll_opy_.endswith(bstack1lll11l_opy_ (u"ࠬࢃ᮪ࠧ")):
                    bstack11l1111l111_opy_ = json.loads(self.bstack111llll1lll_opy_)
                else:
                    bstack11l1111l111_opy_ = dict(item.split(bstack1lll11l_opy_ (u"࠭࠺ࠨ᮫")) for item in self.bstack111llll1lll_opy_.split(bstack1lll11l_opy_ (u"ࠧ࠭ࠩᮬ")) if bstack1lll11l_opy_ (u"ࠨ࠼ࠪᮭ") in item) if self.bstack111llll1lll_opy_ else {}
                if self.bstack11l1111111l_opy_.startswith(bstack1lll11l_opy_ (u"ࠩࡾࠫᮮ")) and self.bstack11l1111111l_opy_.endswith(bstack1lll11l_opy_ (u"ࠪࢁࠬᮯ")):
                    bstack111lllll1ll_opy_ = json.loads(self.bstack11l1111111l_opy_)
                else:
                    bstack111lllll1ll_opy_ = dict(item.split(bstack1lll11l_opy_ (u"ࠫ࠿࠭᮰")) for item in self.bstack11l1111111l_opy_.split(bstack1lll11l_opy_ (u"ࠬ࠲ࠧ᮱")) if bstack1lll11l_opy_ (u"࠭࠺ࠨ᮲") in item) if self.bstack11l1111111l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1lll11l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡧࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵ࠽ࠤࢀࢃࠢ᮳").format(e))
            logger.debug(bstack1lll11l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡰࡥࡵࡶࡩ࡯ࡩࡶࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻࡀࠠࡼࡿ࠯ࠤࡈࡒࡉ࠻ࠢࡾࢁࠧ᮴").format(bstack11l1111l111_opy_, bstack111lllll1ll_opy_))
            return bstack11l1111l111_opy_, bstack111lllll1ll_opy_
        if _111lll1l1ll_opy_ is None or _111ll1lll11_opy_ is None:
            _111lll1l1ll_opy_, _111ll1lll11_opy_ = _111lllll111_opy_()
        def bstack11l11111111_opy_(name, bstack11l111111l1_opy_):
            if name in _111ll1lll11_opy_:
                return _111ll1lll11_opy_[name]
            if name in _111lll1l1ll_opy_:
                return _111lll1l1ll_opy_[name]
            if bstack11l111111l1_opy_.get(bstack1lll11l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩ᮵")):
                return bstack11l111111l1_opy_[bstack1lll11l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪ᮶")]
            return None
        if isinstance(data, dict):
            bstack111ll1l1lll_opy_ = []
            bstack111ll1l1l11_opy_ = re.compile(bstack1lll11l_opy_ (u"ࡶࠬࡤ࡛ࡂ࠯࡝࠴࠲࠿࡟࡞࠭ࠧࠫ᮷"))
            for name, bstack11l111111l1_opy_ in data.items():
                if not isinstance(bstack11l111111l1_opy_, dict):
                    continue
                url = bstack11l111111l1_opy_.get(bstack1lll11l_opy_ (u"ࠬࡻࡲ࡭ࠩ᮸"))
                if url is None or (isinstance(url, str) and url.strip() == bstack1lll11l_opy_ (u"࠭ࠧ᮹")):
                    logger.warning(bstack1lll11l_opy_ (u"ࠢࡓࡧࡳࡳࡸ࡯ࡴࡰࡴࡼࠤ࡚ࡘࡌࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮺ").format(name, bstack11l111111l1_opy_))
                    continue
                if not bstack111ll1l1l11_opy_.match(name):
                    logger.warning(bstack1lll11l_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡳࡺࡸࡣࡦࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠦࡦࡰࡴࡰࡥࡹࠦࡦࡰࡴࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮻ").format(name, bstack11l111111l1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1lll11l_opy_ (u"ࠤࡖࡳࡺࡸࡣࡦࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠦࠧࡼࡿࠪࠤࡲࡻࡳࡵࠢ࡫ࡥࡻ࡫ࠠࡢࠢ࡯ࡩࡳ࡭ࡴࡩࠢࡥࡩࡹࡽࡥࡦࡰࠣ࠵ࠥࡧ࡮ࡥࠢ࠶࠴ࠥࡩࡨࡢࡴࡤࡧࡹ࡫ࡲࡴ࠰ࠥᮼ").format(name))
                    continue
                bstack11l111111l1_opy_ = bstack11l111111l1_opy_.copy()
                bstack11l111111l1_opy_[bstack1lll11l_opy_ (u"ࠪࡲࡦࡳࡥࠨᮽ")] = name
                bstack11l111111l1_opy_[bstack1lll11l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮾ")] = bstack11l11111111_opy_(name, bstack11l111111l1_opy_)
                if not bstack11l111111l1_opy_.get(bstack1lll11l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᮿ")) or bstack11l111111l1_opy_.get(bstack1lll11l_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭ᯀ")) == bstack1lll11l_opy_ (u"ࠧࠨᯁ"):
                    logger.warning(bstack1lll11l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡱࡳࡹࠦࡳࡱࡧࡦ࡭࡫࡯ࡥࡥࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᯂ").format(name, bstack11l111111l1_opy_))
                    continue
                if bstack11l111111l1_opy_.get(bstack1lll11l_opy_ (u"ࠩࡥࡥࡸ࡫ࡂࡳࡣࡱࡧ࡭࠭ᯃ")) and bstack11l111111l1_opy_[bstack1lll11l_opy_ (u"ࠪࡦࡦࡹࡥࡃࡴࡤࡲࡨ࡮ࠧᯄ")] == bstack11l111111l1_opy_[bstack1lll11l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᯅ")]:
                    logger.warning(bstack1lll11l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡡ࡯ࡦࠣࡦࡦࡹࡥࠡࡤࡵࡥࡳࡩࡨࠡࡥࡤࡲࡳࡵࡴࠡࡤࡨࠤࡹ࡮ࡥࠡࡵࡤࡱࡪࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᯆ").format(name, bstack11l111111l1_opy_))
                    continue
                bstack111ll1l1lll_opy_.append(bstack11l111111l1_opy_)
            return bstack111ll1l1lll_opy_
        return data
    def bstack111lllll1l1_opy_(self):
        data = {
            bstack1lll11l_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᯇ"): {
                bstack1lll11l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯈ"): self.bstack111lll11l11_opy_(),
                bstack1lll11l_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭ᯉ"): self.bstack111lll1lll1_opy_(),
                bstack1lll11l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᯊ"): self.bstack111ll1ll1l1_opy_()
            }
        }
        return data
    def bstack111lll1l111_opy_(self, config):
        bstack111ll1ll11l_opy_ = {}
        bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᯋ")] = {
            bstack1lll11l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᯌ"): self.bstack111lll11l11_opy_(),
            bstack1lll11l_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᯍ"): self.bstack111lll1lll1_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"࠭ࡲࡦࡴࡸࡲࡤࡶࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡡࡩࡥ࡮ࡲࡥࡥࠩᯎ")] = {
            bstack1lll11l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯏ"): self.bstack11l1111l11l_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"ࠨࡴࡸࡲࡤࡶࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡡࡩࡥ࡮ࡲࡥࡥࡡࡩ࡭ࡷࡹࡴࠨᯐ")] = {
            bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᯑ"): self.bstack111llll1l11_opy_()
        }
        bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"ࠪࡷࡰ࡯ࡰࡠࡨࡤ࡭ࡱ࡯࡮ࡨࡡࡤࡲࡩࡥࡦ࡭ࡣ࡮ࡽࠬᯒ")] = {
            bstack1lll11l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᯓ"): self.bstack111lllllll1_opy_()
        }
        if self.bstack11111lll_opy_(config):
            bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"ࠬࡸࡥࡵࡴࡼࡣࡹ࡫ࡳࡵࡵࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧᯔ")] = {
                bstack1lll11l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᯕ"): True,
                bstack1lll11l_opy_ (u"ࠧ࡮ࡣࡻࡣࡷ࡫ࡴࡳ࡫ࡨࡷࠬᯖ"): self.bstack111l11ll_opy_(config)
            }
        if self.bstack11l1llll11l_opy_(config):
            bstack111ll1ll11l_opy_[bstack1lll11l_opy_ (u"ࠨࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥ࡯࡯ࡡࡩࡥ࡮ࡲࡵࡳࡧࠪᯗ")] = {
                bstack1lll11l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᯘ"): True,
                bstack1lll11l_opy_ (u"ࠪࡱࡦࡾ࡟ࡧࡣ࡬ࡰࡺࡸࡥࡴࠩᯙ"): self.bstack11l1ll1ll11_opy_(config)
            }
        return bstack111ll1ll11l_opy_
    def bstack11111l11l1_opy_(self, config):
        bstack1lll11l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅࡲࡰࡱ࡫ࡣࡵࡵࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡣࡻࠣࡱࡦࡱࡩ࡯ࡩࠣࡥࠥࡩࡡ࡭࡮ࠣࡸࡴࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡹ࡮ࡲࡤࡠࡷࡸ࡭ࡩࠦࠨࡴࡶࡵ࠭࠿ࠦࡔࡩࡧ࡙࡚ࠣࡏࡄࠡࡱࡩࠤࡹ࡮ࡥࠡࡤࡸ࡭ࡱࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡩࡧࡴࡢࠢࡩࡳࡷ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡦ࡬ࡧࡹࡀࠠࡓࡧࡶࡴࡴࡴࡳࡦࠢࡩࡶࡴࡳࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠰ࠥࡵࡲࠡࡐࡲࡲࡪࠦࡩࡧࠢࡩࡥ࡮ࡲࡥࡥ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᯚ")
        if not (config.get(bstack1lll11l_opy_ (u"ࠬ࡬ࡲࡢ࡯ࡨࡻࡴࡸ࡫ࠨᯛ"), None) in bstack11l11llll11_opy_ and self.bstack111lll11l11_opy_()):
            return None
        bstack111llll1ll1_opy_ = os.environ.get(bstack1lll11l_opy_ (u"࠭ࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠫᯜ"), None)
        logger.debug(bstack1lll11l_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡉ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡘ࡙ࡎࡊ࠺ࠡࡽࢀࠦᯝ").format(bstack111llll1ll1_opy_))
        try:
            bstack11ll111l1ll_opy_ = bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࡨࡵࡪ࡮ࡧࡷ࠴ࢁࡽ࠰ࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠨᯞ").format(bstack111llll1ll1_opy_)
            payload = {
                bstack1lll11l_opy_ (u"ࠤࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠢᯟ"): config.get(bstack1lll11l_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᯠ"), bstack1lll11l_opy_ (u"ࠫࠬᯡ")),
                bstack1lll11l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠣᯢ"): config.get(bstack1lll11l_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩᯣ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lll11l_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧᯤ"): os.environ.get(bstack1lll11l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠢᯥ"), bstack1lll11l_opy_ (u"ࠤ᯦ࠥ")),
                bstack1lll11l_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨᯧ"): int(os.environ.get(bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢᯨ")) or bstack1lll11l_opy_ (u"ࠧ࠶ࠢᯩ")),
                bstack1lll11l_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵࠥᯪ"): int(os.environ.get(bstack1lll11l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᯫ")) or bstack1lll11l_opy_ (u"ࠣ࠳ࠥᯬ")),
                bstack1lll11l_opy_ (u"ࠤ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠦᯭ"): get_host_info(),
            }
            logger.debug(bstack1lll11l_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡕࡨࡲࡩ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡰࡢࡻ࡯ࡳࡦࡪ࠺ࠡࡽࢀࠦᯮ").format(payload))
            response = bstack11ll1ll11ll_opy_.bstack11ll111ll11_opy_(bstack11ll111l1ll_opy_, payload)
            if response:
                logger.debug(bstack1lll11l_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡅࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡣࡰ࡮࡯ࡩࡨࡺࡩࡰࡰࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᯯ").format(response))
                return response
            else:
                logger.error(bstack1lll11l_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡤࡸ࡭ࡱࡪࠠࡖࡗࡌࡈ࠿ࠦࡻࡾࠤᯰ").format(bstack111llll1ll1_opy_))
                return None
        except Exception as e:
            logger.error(bstack1lll11l_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡤࡸ࡭ࡱࡪࠠࡖࡗࡌࡈࠥࢁࡽ࠻ࠢࡾࢁࠧᯱ").format(bstack111llll1ll1_opy_, e))
            return None
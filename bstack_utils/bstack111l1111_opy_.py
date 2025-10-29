# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1l11111111_opy_
from bstack_utils.constants import bstack1l1l11l11_opy_, bstack11l11ll1l11_opy_
from bstack_utils.helper import bstack11ll1l11ll1_opy_, get_host_info
from bstack_utils.bstack11ll1l1lll1_opy_ import bstack11ll1l1ll11_opy_
import json
import re
import sys
bstack111llll1ll1_opy_ = bstack11ll1l_opy_ (u"ࠦࡷ࡫ࡴࡳࡻࡗࡩࡸࡺࡳࡐࡰࡉࡥ࡮ࡲࡵࡳࡧࠥ᭿")
bstack111lllll111_opy_ = bstack11ll1l_opy_ (u"ࠧࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦᮀ")
bstack111lll1l111_opy_ = bstack11ll1l_opy_ (u"ࠨࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࡋ࡯ࡲࡴࡶࠥᮁ")
bstack111llll1l11_opy_ = bstack11ll1l_opy_ (u"ࠢࡳࡧࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࠣᮂ")
bstack111lll1llll_opy_ = bstack11ll1l_opy_ (u"ࠣࡵ࡮࡭ࡵࡌ࡬ࡢ࡭ࡼࡥࡳࡪࡆࡢ࡫࡯ࡩࡩࠨᮃ")
bstack11l1111111l_opy_ = bstack11ll1l_opy_ (u"ࠤࡵࡹࡳ࡙࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࠨᮄ")
bstack11l1111l1ll_opy_ = {
    bstack111llll1ll1_opy_,
    bstack111lllll111_opy_,
    bstack111lll1l111_opy_,
    bstack111llll1l11_opy_,
    bstack111lll1llll_opy_,
    bstack11l1111111l_opy_
}
bstack111llllll1l_opy_ = {bstack11ll1l_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᮅ")}
logger = bstack1l11111111_opy_.get_logger(__name__, bstack1l1l11l11_opy_)
class bstack11l11111l11_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111lll1lll1_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1llllll11_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config):
        self.bstack111ll1lll1l_opy_ = False
        self.bstack111llll11l1_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack111llll111l_opy_ = False
        self.bstack11l11111111_opy_ = None
        self.bstack111lll111ll_opy_ = bstack11l11111l11_opy_()
        self.bstack111lllllll1_opy_ = None
        opts = config.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮆ"), {})
        self.bstack111lllll11l_opy_ = config.get(bstack11ll1l_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡅࡏࡘࠪᮇ"), bstack11ll1l_opy_ (u"ࠨࠢᮈ"))
        self.bstack11l111111l1_opy_ = config.get(bstack11ll1l_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡅࡏࡍࠬᮉ"), bstack11ll1l_opy_ (u"ࠣࠤᮊ"))
        bstack111llll1lll_opy_ = opts.get(bstack11l1111111l_opy_, {})
        bstack111ll1ll11l_opy_ = None
        if bstack11ll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᮋ") in bstack111llll1lll_opy_:
            bstack11l1111ll11_opy_ = bstack111llll1lll_opy_[bstack11ll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᮌ")]
            if bstack11l1111ll11_opy_ is None or bstack11l1111ll11_opy_ == bstack11ll1l_opy_ (u"ࠫࠬᮍ") or (isinstance(bstack11l1111ll11_opy_, list) and len(bstack11l1111ll11_opy_) == 0):
                bstack111ll1ll11l_opy_ = []
            elif isinstance(bstack11l1111ll11_opy_, list):
                bstack111ll1ll11l_opy_ = bstack11l1111ll11_opy_
            elif isinstance(bstack11l1111ll11_opy_, str) and bstack11l1111ll11_opy_.strip():
                bstack111ll1ll11l_opy_ = bstack11l1111ll11_opy_
            else:
                logger.warning(bstack11ll1l_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳࡰࡷࡵࡧࡪࠦࡶࡢ࡮ࡸࡩࠥ࡯࡮ࠡࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡾࢁ࠳ࠦࡄࡦࡨࡤࡹࡱࡺࡩ࡯ࡩࠣࡸࡴࠦࡥ࡮ࡲࡷࡽࠥࡲࡩࡴࡶ࠱ࠦᮎ").format(bstack11l1111ll11_opy_))
                bstack111ll1ll11l_opy_ = []
        self.__11l111111ll_opy_(
            bstack111llll1lll_opy_.get(bstack11ll1l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮏ"), False),
            bstack111llll1lll_opy_.get(bstack11ll1l_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᮐ"), bstack11ll1l_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᮑ")),
            bstack111ll1ll11l_opy_
        )
        self.__111ll1llll1_opy_(opts.get(bstack111lll1l111_opy_, False))
        self.__11l1111l11l_opy_(opts.get(bstack111llll1l11_opy_, False))
        self.__111lll11lll_opy_(opts.get(bstack111lll1llll_opy_, False))
    @classmethod
    def bstack111111ll_opy_(cls, config=None):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack1llllll11_opy_(config)
        return cls._1ll1l1lll11_opy_
    @staticmethod
    def bstack1lllll111_opy_(config: dict) -> bool:
        bstack111ll1l1lll_opy_ = config.get(bstack11ll1l_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᮒ"), {}).get(bstack111llll1ll1_opy_, {})
        return bstack111ll1l1lll_opy_.get(bstack11ll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮓ"), False)
    @staticmethod
    def bstack1lllllll1_opy_(config: dict) -> int:
        bstack111ll1l1lll_opy_ = config.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮔ"), {}).get(bstack111llll1ll1_opy_, {})
        retries = 0
        if bstack1llllll11_opy_.bstack1lllll111_opy_(config):
            retries = bstack111ll1l1lll_opy_.get(bstack11ll1l_opy_ (u"ࠬࡳࡡࡹࡔࡨࡸࡷ࡯ࡥࡴࠩᮕ"), 1)
        return retries
    @staticmethod
    def bstack11l1ll11ll_opy_(config: dict) -> dict:
        bstack111lllll1l1_opy_ = config.get(bstack11ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮖ"), {})
        return {
            key: value for key, value in bstack111lllll1l1_opy_.items() if key in bstack11l1111l1ll_opy_
        }
    @staticmethod
    def bstack111lll1111l_opy_():
        bstack11ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮗ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤᮘ").format(os.getenv(bstack11ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢᮙ")))))
    @staticmethod
    def bstack111ll1l1ll1_opy_(test_name: str):
        bstack11ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᮚ")
        bstack111lll111l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1l_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥᮛ").format(os.getenv(bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥᮜ"))))
        with open(bstack111lll111l1_opy_, bstack11ll1l_opy_ (u"࠭ࡡࠨᮝ")) as file:
            file.write(bstack11ll1l_opy_ (u"ࠢࡼࡿ࡟ࡲࠧᮞ").format(test_name))
    @staticmethod
    def bstack111ll1l1l11_opy_(framework: str) -> bool:
       return framework.lower() in bstack111llllll1l_opy_
    @staticmethod
    def bstack11l1llll1l1_opy_(config: dict) -> bool:
        bstack11l11111l1l_opy_ = config.get(bstack11ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬᮟ"), {}).get(bstack111lllll111_opy_, {})
        return bstack11l11111l1l_opy_.get(bstack11ll1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮠ"), False)
    @staticmethod
    def bstack11l1llll1ll_opy_(config: dict, bstack11l1lllll1l_opy_: int = 0) -> int:
        bstack11ll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠱ࠦࡷࡩ࡫ࡦ࡬ࠥࡩࡡ࡯ࠢࡥࡩࠥࡧ࡮ࠡࡣࡥࡷࡴࡲࡵࡵࡧࠣࡲࡺࡳࡢࡦࡴࠣࡳࡷࠦࡡࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࠭ࡪࡩࡤࡶࠬ࠾࡚ࠥࡨࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺ࡯ࡵࡣ࡯ࡣࡹ࡫ࡳࡵࡵࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࠪࡵࡩࡶࡻࡩࡳࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳࠪ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮡ")
        bstack11l11111l1l_opy_ = config.get(bstack11ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮢ"), {}).get(bstack11ll1l_opy_ (u"ࠬࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠫᮣ"), {})
        bstack111ll1lllll_opy_ = 0
        bstack111llllll11_opy_ = 0
        if bstack1llllll11_opy_.bstack11l1llll1l1_opy_(config):
            bstack111llllll11_opy_ = bstack11l11111l1l_opy_.get(bstack11ll1l_opy_ (u"࠭࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶࠫᮤ"), 5)
            if isinstance(bstack111llllll11_opy_, str) and bstack111llllll11_opy_.endswith(bstack11ll1l_opy_ (u"ࠧࠦࠩᮥ")):
                try:
                    percentage = int(bstack111llllll11_opy_.strip(bstack11ll1l_opy_ (u"ࠨࠧࠪᮦ")))
                    if bstack11l1lllll1l_opy_ > 0:
                        bstack111ll1lllll_opy_ = math.ceil((percentage * bstack11l1lllll1l_opy_) / 100)
                    else:
                        raise ValueError(bstack11ll1l_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨ࠱ࡧࡧࡳࡦࡦࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࡹ࠮ࠣᮧ"))
                except ValueError as e:
                    raise ValueError(bstack11ll1l_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥࠡࡸࡤࡰࡺ࡫ࠠࡧࡱࡵࠤࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴ࠼ࠣࡿࢂࠨᮨ").format(bstack111llllll11_opy_)) from e
            else:
                bstack111ll1lllll_opy_ = int(bstack111llllll11_opy_)
        logger.info(bstack11ll1l_opy_ (u"ࠦࡒࡧࡸࠡࡨࡤ࡭ࡱࡻࡲࡦࡵࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡳࡦࡶࠣࡸࡴࡀࠠࡼࡿࠣࠬ࡫ࡸ࡯࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠯ࠢᮩ").format(bstack111ll1lllll_opy_, bstack111llllll11_opy_))
        return bstack111ll1lllll_opy_
    def bstack111lllll1ll_opy_(self):
        return self.bstack111llll111l_opy_
    def bstack111ll1ll1ll_opy_(self):
        return self.bstack11l11111111_opy_
    def bstack11l11111ll1_opy_(self):
        return self.bstack111lllllll1_opy_
    def __11l111111ll_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll111l_opy_ = bool(enabled)
            if mode not in [bstack11ll1l_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸ᮪ࠬ"), bstack11ll1l_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡐࡰ࡯ࡽ᮫ࠬ")]:
                logger.warning(bstack11ll1l_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡱࡴࡪࡥࠡࠩࡾࢁࠬࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡴࡰࠢࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ࠲ࠧᮬ").format(mode))
                mode = bstack11ll1l_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᮭ")
            self.bstack11l11111111_opy_ = mode
            if source is None:
                self.bstack111lllllll1_opy_ = None
            elif isinstance(source, list):
                self.bstack111lllllll1_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11ll1l_opy_ (u"ࠩ࠱࡮ࡸࡵ࡮ࠨᮮ")):
                self.bstack111lllllll1_opy_ = self._11l1111l1l1_opy_(source)
            self.__111lll1ll11_opy_()
        except Exception as e:
            logger.error(bstack11ll1l_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࠳ࠠࡦࡰࡤࡦࡱ࡫ࡤ࠻ࠢࡾࢁ࠱ࠦ࡭ࡰࡦࡨ࠾ࠥࢁࡽ࠭ࠢࡶࡳࡺࡸࡣࡦ࠼ࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥᮯ").format(enabled, mode, source, e))
    def bstack111llll11ll_opy_(self):
        return self.bstack111ll1lll1l_opy_
    def __111ll1llll1_opy_(self, value):
        self.bstack111ll1lll1l_opy_ = bool(value)
        self.__111lll1ll11_opy_()
    def bstack111ll1l1l1l_opy_(self):
        return self.bstack111llll11l1_opy_
    def __11l1111l11l_opy_(self, value):
        self.bstack111llll11l1_opy_ = bool(value)
        self.__111lll1ll11_opy_()
    def bstack111ll1lll11_opy_(self):
        return self.bstack111llll1111_opy_
    def __111lll11lll_opy_(self, value):
        self.bstack111llll1111_opy_ = bool(value)
        self.__111lll1ll11_opy_()
    def __111lll1ll11_opy_(self):
        if self.bstack111llll111l_opy_:
            self.bstack111ll1lll1l_opy_ = False
            self.bstack111llll11l1_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll111ll_opy_.enable(bstack11l1111111l_opy_)
        elif self.bstack111ll1lll1l_opy_:
            self.bstack111llll11l1_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll111ll_opy_.enable(bstack111lll1l111_opy_)
        elif self.bstack111llll11l1_opy_:
            self.bstack111ll1lll1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll111ll_opy_.enable(bstack111llll1l11_opy_)
        elif self.bstack111llll1111_opy_:
            self.bstack111ll1lll1l_opy_ = False
            self.bstack111llll11l1_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll111ll_opy_.enable(bstack111lll1llll_opy_)
        else:
            self.bstack111lll111ll_opy_.disable()
    def bstack1lll11l1l_opy_(self):
        return self.bstack111lll111ll_opy_.bstack111lll1lll1_opy_()
    def bstack1l1lllll1_opy_(self):
        if self.bstack111lll111ll_opy_.bstack111lll1lll1_opy_():
            return self.bstack111lll111ll_opy_.get_name()
        return None
    def _11l1111l1l1_opy_(self, bstack111lll11l1l_opy_):
        bstack11ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡹ࡯ࡶࡴࡦࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠣࡥࡳࡪࠠࡧࡱࡵࡱࡦࡺࠠࡪࡶࠣࡪࡴࡸࠠࡴ࡯ࡤࡶࡹࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡲࡹࡷࡩࡥࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡕࡧࡴࡩࠢࡷࡳࠥࡺࡨࡦࠢࡍࡗࡔࡔࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡌ࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡵࡩࡵࡵࡳࡪࡶࡲࡶࡾࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᮰")
        if not os.path.isfile(bstack111lll11l1l_opy_):
            logger.error(bstack11ll1l_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠥ᮱").format(bstack111lll11l1l_opy_))
            return []
        data = None
        try:
            with open(bstack111lll11l1l_opy_, bstack11ll1l_opy_ (u"ࠨࡲࠣ᮲")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11ll1l_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡋࡕࡒࡒࠥ࡬ࡲࡰ࡯ࠣࡷࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥ᮳").format(bstack111lll11l1l_opy_, e))
            return []
        _111ll1ll1l1_opy_ = None
        _111llllllll_opy_ = None
        def _11l11111lll_opy_():
            bstack111lll11ll1_opy_ = {}
            bstack11l1111l111_opy_ = {}
            try:
                if self.bstack111lllll11l_opy_.startswith(bstack11ll1l_opy_ (u"ࠨࡽࠪ᮴")) and self.bstack111lllll11l_opy_.endswith(bstack11ll1l_opy_ (u"ࠩࢀࠫ᮵")):
                    bstack111lll11ll1_opy_ = json.loads(self.bstack111lllll11l_opy_)
                else:
                    bstack111lll11ll1_opy_ = dict(item.split(bstack11ll1l_opy_ (u"ࠪ࠾ࠬ᮶")) for item in self.bstack111lllll11l_opy_.split(bstack11ll1l_opy_ (u"ࠫ࠱࠭᮷")) if bstack11ll1l_opy_ (u"ࠬࡀࠧ᮸") in item) if self.bstack111lllll11l_opy_ else {}
                if self.bstack11l111111l1_opy_.startswith(bstack11ll1l_opy_ (u"࠭ࡻࠨ᮹")) and self.bstack11l111111l1_opy_.endswith(bstack11ll1l_opy_ (u"ࠧࡾࠩᮺ")):
                    bstack11l1111l111_opy_ = json.loads(self.bstack11l111111l1_opy_)
                else:
                    bstack11l1111l111_opy_ = dict(item.split(bstack11ll1l_opy_ (u"ࠨ࠼ࠪᮻ")) for item in self.bstack11l111111l1_opy_.split(bstack11ll1l_opy_ (u"ࠩ࠯ࠫᮼ")) if bstack11ll1l_opy_ (u"ࠪ࠾ࠬᮽ") in item) if self.bstack11l111111l1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11ll1l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡦࡸࡳࡪࡰࡪࠤ࡫࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡳࡡࡱࡲ࡬ࡲ࡬ࡹ࠺ࠡࡽࢀࠦᮾ").format(e))
            logger.debug(bstack11ll1l_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࠽ࠤࢀࢃࠬࠡࡅࡏࡍ࠿ࠦࡻࡾࠤᮿ").format(bstack111lll11ll1_opy_, bstack11l1111l111_opy_))
            return bstack111lll11ll1_opy_, bstack11l1111l111_opy_
        if _111ll1ll1l1_opy_ is None or _111llllllll_opy_ is None:
            _111ll1ll1l1_opy_, _111llllllll_opy_ = _11l11111lll_opy_()
        def bstack111lll11l11_opy_(name, bstack111lll1ll1l_opy_):
            if name in _111llllllll_opy_:
                return _111llllllll_opy_[name]
            if name in _111ll1ll1l1_opy_:
                return _111ll1ll1l1_opy_[name]
            if bstack111lll1ll1l_opy_.get(bstack11ll1l_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭ᯀ")):
                return bstack111lll1ll1l_opy_[bstack11ll1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᯁ")]
            return None
        if isinstance(data, dict):
            bstack111lll1l1ll_opy_ = []
            bstack111lll1l1l1_opy_ = re.compile(bstack11ll1l_opy_ (u"ࡳࠩࡡ࡟ࡆ࠳࡚࠱࠯࠼ࡣࡢ࠱ࠤࠨᯂ"))
            for name, bstack111lll1ll1l_opy_ in data.items():
                if not isinstance(bstack111lll1ll1l_opy_, dict):
                    continue
                if not bstack111lll1ll1l_opy_.get(bstack11ll1l_opy_ (u"ࠩࡸࡶࡱ࠭ᯃ")):
                    logger.warning(bstack11ll1l_opy_ (u"ࠥࡖࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡖࡔࡏࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᯄ").format(name, bstack111lll1ll1l_opy_))
                    continue
                if not bstack111lll1l1l1_opy_.match(name):
                    logger.warning(bstack11ll1l_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࡩࡳࡷࡳࡡࡵࠢࡩࡳࡷࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᯅ").format(name, bstack111lll1ll1l_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11ll1l_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࠪࡿࢂ࠭ࠠ࡮ࡷࡶࡸࠥ࡮ࡡࡷࡧࠣࡥࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡨࡥࡵࡹࡨࡩࡳࠦ࠱ࠡࡣࡱࡨࠥ࠹࠰ࠡࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࡷ࠳ࠨᯆ").format(name))
                    continue
                bstack111lll1ll1l_opy_ = bstack111lll1ll1l_opy_.copy()
                bstack111lll1ll1l_opy_[bstack11ll1l_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᯇ")] = name
                bstack111lll1ll1l_opy_[bstack11ll1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᯈ")] = bstack111lll11l11_opy_(name, bstack111lll1ll1l_opy_)
                if not bstack111lll1ll1l_opy_.get(bstack11ll1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᯉ")):
                    logger.warning(bstack11ll1l_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡲࡴࡺࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᯊ").format(name, bstack111lll1ll1l_opy_))
                    continue
                if bstack111lll1ll1l_opy_.get(bstack11ll1l_opy_ (u"ࠪࡦࡦࡹࡥࡃࡴࡤࡲࡨ࡮ࠧᯋ")) and bstack111lll1ll1l_opy_[bstack11ll1l_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨᯌ")] == bstack111lll1ll1l_opy_[bstack11ll1l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᯍ")]:
                    logger.warning(bstack11ll1l_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡢࡰࡧࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡺࡨࡦࠢࡶࡥࡲ࡫ࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᯎ").format(name, bstack111lll1ll1l_opy_))
                    continue
                bstack111lll1l1ll_opy_.append(bstack111lll1ll1l_opy_)
            return bstack111lll1l1ll_opy_
        return data
    def bstack111lll11111_opy_(self):
        data = {
            bstack11ll1l_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᯏ"): {
                bstack11ll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯐ"): self.bstack111lllll1ll_opy_(),
                bstack11ll1l_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᯑ"): self.bstack111ll1ll1ll_opy_(),
                bstack11ll1l_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᯒ"): self.bstack11l11111ll1_opy_()
            }
        }
        return data
    def bstack111ll1ll111_opy_(self, config):
        bstack111lll1l11l_opy_ = {}
        bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᯓ")] = {
            bstack11ll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯔ"): self.bstack111lllll1ll_opy_(),
            bstack11ll1l_opy_ (u"࠭࡭ࡰࡦࡨࠫᯕ"): self.bstack111ll1ll1ll_opy_()
        }
        bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࠪᯖ")] = {
            bstack11ll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯗ"): self.bstack111ll1l1l1l_opy_()
        }
        bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࡢࡪ࡮ࡸࡳࡵࠩᯘ")] = {
            bstack11ll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯙ"): self.bstack111llll11ll_opy_()
        }
        bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠫࡸࡱࡩࡱࡡࡩࡥ࡮ࡲࡩ࡯ࡩࡢࡥࡳࡪ࡟ࡧ࡮ࡤ࡯ࡾ࠭ᯚ")] = {
            bstack11ll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯛ"): self.bstack111ll1lll11_opy_()
        }
        if self.bstack1lllll111_opy_(config):
            bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"࠭ࡲࡦࡶࡵࡽࡤࡺࡥࡴࡶࡶࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᯜ")] = {
                bstack11ll1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯝ"): True,
                bstack11ll1l_opy_ (u"ࠨ࡯ࡤࡼࡤࡸࡥࡵࡴ࡬ࡩࡸ࠭ᯞ"): self.bstack1lllllll1_opy_(config)
            }
        if self.bstack11l1llll1l1_opy_(config):
            bstack111lll1l11l_opy_[bstack11ll1l_opy_ (u"ࠩࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᯟ")] = {
                bstack11ll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯠ"): True,
                bstack11ll1l_opy_ (u"ࠫࡲࡧࡸࡠࡨࡤ࡭ࡱࡻࡲࡦࡵࠪᯡ"): self.bstack11l1llll1ll_opy_(config)
            }
        return bstack111lll1l11l_opy_
    def bstack1l1l1l11l_opy_(self, config):
        bstack11ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡳࡱࡲࡥࡤࡶࡶࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡤࡼࠤࡲࡧ࡫ࡪࡰࡪࠤࡦࠦࡣࡢ࡮࡯ࠤࡹࡵࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤ࡚࡛ࡉࡅࠢࡲࡪࠥࡺࡨࡦࠢࡥࡹ࡮ࡲࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡪࡡࡵࡣࠣࡪࡴࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᯢ")
        if not (config.get(bstack11ll1l_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᯣ"), None) in bstack11l11ll1l11_opy_ and self.bstack111lllll1ll_opy_()):
            return None
        bstack111llll1l1l_opy_ = os.environ.get(bstack11ll1l_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᯤ"), None)
        logger.debug(bstack11ll1l_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡃࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᯥ").format(bstack111llll1l1l_opy_))
        try:
            bstack11ll111l11l_opy_ = bstack11ll1l_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧ᯦ࠢ").format(bstack111llll1l1l_opy_)
            payload = {
                bstack11ll1l_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᯧ"): config.get(bstack11ll1l_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᯨ"), bstack11ll1l_opy_ (u"ࠬ࠭ᯩ")),
                bstack11ll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᯪ"): config.get(bstack11ll1l_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᯫ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᯬ"): os.environ.get(bstack11ll1l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᯭ"), bstack11ll1l_opy_ (u"ࠥࠦᯮ")),
                bstack11ll1l_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᯯ"): int(os.environ.get(bstack11ll1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᯰ")) or bstack11ll1l_opy_ (u"ࠨ࠰ࠣᯱ")),
                bstack11ll1l_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶ᯲ࠦ"): int(os.environ.get(bstack11ll1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖ᯳ࠥ")) or bstack11ll1l_opy_ (u"ࠤ࠴ࠦ᯴")),
                bstack11ll1l_opy_ (u"ࠥ࡬ࡴࡹࡴࡊࡰࡩࡳࠧ᯵"): get_host_info(),
            }
            logger.debug(bstack11ll1l_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡱࡣࡼࡰࡴࡧࡤ࠻ࠢࡾࢁࠧ᯶").format(payload))
            response = bstack11ll1l1ll11_opy_.bstack11ll111ll11_opy_(bstack11ll111l11l_opy_, payload)
            if response:
                logger.debug(bstack11ll1l_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡆࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ᯷").format(response))
                return response
            else:
                logger.error(bstack11ll1l_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥ᯸").format(bstack111llll1l1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11ll1l_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࠦࡻࡾ࠼ࠣࡿࢂࠨ᯹").format(bstack111llll1l1l_opy_, e))
            return None
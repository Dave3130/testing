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
import os
import tempfile
import math
from bstack_utils import bstack11111l1ll1_opy_
from bstack_utils.constants import bstack11l111lll_opy_, bstack11l11l1l11l_opy_
from bstack_utils.helper import bstack11ll1l1ll11_opy_, get_host_info
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l111l1_opy_
import json
import re
import sys
bstack111lll111ll_opy_ = bstack11ll1ll_opy_ (u"ࠨࡲࡦࡶࡵࡽ࡙࡫ࡳࡵࡵࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧᮏ")
bstack111llllll1l_opy_ = bstack11ll1ll_opy_ (u"ࠢࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨᮐ")
bstack111lllll1ll_opy_ = bstack11ll1ll_opy_ (u"ࠣࡴࡸࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡇࡣ࡬ࡰࡪࡪࡆࡪࡴࡶࡸࠧᮑ")
bstack111ll1lll1l_opy_ = bstack11ll1ll_opy_ (u"ࠤࡵࡩࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࠥᮒ")
bstack111ll1l1l1l_opy_ = bstack11ll1ll_opy_ (u"ࠥࡷࡰ࡯ࡰࡇ࡮ࡤ࡯ࡾࡧ࡮ࡥࡈࡤ࡭ࡱ࡫ࡤࠣᮓ")
bstack11l11111lll_opy_ = bstack11ll1ll_opy_ (u"ࠦࡷࡻ࡮ࡔ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠣᮔ")
bstack111lll11ll1_opy_ = {
    bstack111lll111ll_opy_,
    bstack111llllll1l_opy_,
    bstack111lllll1ll_opy_,
    bstack111ll1lll1l_opy_,
    bstack111ll1l1l1l_opy_,
    bstack11l11111lll_opy_
}
bstack111ll1l1111_opy_ = {bstack11ll1ll_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᮕ")}
logger = bstack11111l1ll1_opy_.get_logger(__name__, bstack11l111lll_opy_)
class bstack111ll1l1lll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111ll11llll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1llllll11_opy_:
    _1ll1l1lll1l_opy_ = None
    def __init__(self, config):
        self.bstack111lll1ll1l_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack111llll1l11_opy_ = False
        self.bstack111llll111l_opy_ = False
        self.bstack111llll1lll_opy_ = None
        self.bstack111lll1ll11_opy_ = bstack111ll1l1lll_opy_()
        self.bstack11l11111l1l_opy_ = None
        opts = config.get(bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮖ"), {})
        self.bstack111ll1ll111_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡇࡑ࡚ࠬᮗ"), bstack11ll1ll_opy_ (u"ࠣࠤᮘ"))
        self.bstack111ll1lll11_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠧᮙ"), bstack11ll1ll_opy_ (u"ࠥࠦᮚ"))
        bstack111lll11l11_opy_ = opts.get(bstack11l11111lll_opy_, {})
        bstack111ll1l1ll1_opy_ = None
        if bstack11ll1ll_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᮛ") in bstack111lll11l11_opy_:
            bstack111ll1l1l11_opy_ = bstack111lll11l11_opy_[bstack11ll1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᮜ")]
            if bstack111ll1l1l11_opy_ is None or (isinstance(bstack111ll1l1l11_opy_, str) and bstack111ll1l1l11_opy_.strip() == bstack11ll1ll_opy_ (u"࠭ࠧᮝ")) or (isinstance(bstack111ll1l1l11_opy_, list) and len(bstack111ll1l1l11_opy_) == 0):
                bstack111ll1l1ll1_opy_ = []
            elif isinstance(bstack111ll1l1l11_opy_, list):
                bstack111ll1l1ll1_opy_ = bstack111ll1l1l11_opy_
            elif isinstance(bstack111ll1l1l11_opy_, str) and bstack111ll1l1l11_opy_.strip():
                bstack111ll1l1ll1_opy_ = bstack111ll1l1l11_opy_
            else:
                logger.warning(bstack11ll1ll_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡲࡹࡷࡩࡥࠡࡸࡤࡰࡺ࡫ࠠࡪࡰࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࢀࢃ࠮ࠡࡆࡨࡪࡦࡻ࡬ࡵ࡫ࡱ࡫ࠥࡺ࡯ࠡࡧࡰࡴࡹࡿࠠ࡭࡫ࡶࡸ࠳ࠨᮞ").format(bstack111ll1l1l11_opy_))
                bstack111ll1l1ll1_opy_ = []
        self.__111lll1l1l1_opy_(
            bstack111lll11l11_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮟ"), False),
            bstack111lll11l11_opy_.get(bstack11ll1ll_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮠ"), bstack11ll1ll_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪᮡ")),
            bstack111ll1l1ll1_opy_
        )
        self.__111lllll111_opy_(opts.get(bstack111lllll1ll_opy_, False))
        self.__111ll1l111l_opy_(opts.get(bstack111ll1lll1l_opy_, False))
        self.__111ll1ll1ll_opy_(opts.get(bstack111ll1l1l1l_opy_, False))
    @classmethod
    def bstack1lll11ll1_opy_(cls, config=None):
        if cls._1ll1l1lll1l_opy_ is None and config is not None:
            cls._1ll1l1lll1l_opy_ = bstack1llllll11_opy_(config)
        return cls._1ll1l1lll1l_opy_
    @staticmethod
    def bstack1lll1llll_opy_(config: dict) -> bool:
        bstack111llll1l1l_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᮢ"), {}).get(bstack111lll111ll_opy_, {})
        return bstack111llll1l1l_opy_.get(bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮣ"), False)
    @staticmethod
    def bstack111l11ll_opy_(config: dict) -> int:
        bstack111llll1l1l_opy_ = config.get(bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮤ"), {}).get(bstack111lll111ll_opy_, {})
        retries = 0
        if bstack1llllll11_opy_.bstack1lll1llll_opy_(config):
            retries = bstack111llll1l1l_opy_.get(bstack11ll1ll_opy_ (u"ࠧ࡮ࡣࡻࡖࡪࡺࡲࡪࡧࡶࠫᮥ"), 1)
        return retries
    @staticmethod
    def bstack111ll1lll_opy_(config: dict) -> dict:
        bstack111ll1ll11l_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬᮦ"), {})
        return {
            key: value for key, value in bstack111ll1ll11l_opy_.items() if key in bstack111lll11ll1_opy_
        }
    @staticmethod
    def bstack111ll1llll1_opy_():
        bstack11ll1ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮧ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦᮨ").format(os.getenv(bstack11ll1ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤᮩ")))))
    @staticmethod
    def bstack111llllllll_opy_(test_name: str):
        bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᮪")
        bstack111ll1ll1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll1ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸ᮫ࠧ").format(os.getenv(bstack11ll1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᮬ"))))
        with open(bstack111ll1ll1l1_opy_, bstack11ll1ll_opy_ (u"ࠨࡣࠪᮭ")) as file:
            file.write(bstack11ll1ll_opy_ (u"ࠤࡾࢁࡡࡴࠢᮮ").format(test_name))
    @staticmethod
    def bstack111lll1lll1_opy_(framework: str) -> bool:
       return framework.lower() in bstack111ll1l1111_opy_
    @staticmethod
    def bstack11l1ll11ll1_opy_(config: dict) -> bool:
        bstack11l11111111_opy_ = config.get(bstack11ll1ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᮯ"), {}).get(bstack111llllll1l_opy_, {})
        return bstack11l11111111_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᮰"), False)
    @staticmethod
    def bstack11l1lll11ll_opy_(config: dict, bstack11l1lll1111_opy_: int = 0) -> int:
        bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠬࠡࡹ࡫࡭ࡨ࡮ࠠࡤࡣࡱࠤࡧ࡫ࠠࡢࡰࠣࡥࡧࡹ࡯࡭ࡷࡷࡩࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡲࠡࡣࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡩ࡭࡬ࠦࠨࡥ࡫ࡦࡸ࠮ࡀࠠࡕࡪࡨࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡱࡷࡥࡱࡥࡴࡦࡵࡷࡷࠥ࠮ࡩ࡯ࡶࠬ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࠬࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᮱")
        bstack11l11111111_opy_ = config.get(bstack11ll1ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᮲"), {}).get(bstack11ll1ll_opy_ (u"ࠧࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪ࠭᮳"), {})
        bstack111lll1l111_opy_ = 0
        bstack111lllll11l_opy_ = 0
        if bstack1llllll11_opy_.bstack11l1ll11ll1_opy_(config):
            bstack111lllll11l_opy_ = bstack11l11111111_opy_.get(bstack11ll1ll_opy_ (u"ࠨ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸ࠭᮴"), 5)
            if isinstance(bstack111lllll11l_opy_, str) and bstack111lllll11l_opy_.endswith(bstack11ll1ll_opy_ (u"ࠩࠨࠫ᮵")):
                try:
                    percentage = int(bstack111lllll11l_opy_.strip(bstack11ll1ll_opy_ (u"ࠪࠩࠬ᮶")))
                    if bstack11l1lll1111_opy_ > 0:
                        bstack111lll1l111_opy_ = math.ceil((percentage * bstack11l1lll1111_opy_) / 100)
                    else:
                        raise ValueError(bstack11ll1ll_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡰࡹࡸࡺࠠࡣࡧࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴ࠰ࠥ᮷"))
                except ValueError as e:
                    raise ValueError(bstack11ll1ll_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧࠣࡺࡦࡲࡵࡦࠢࡩࡳࡷࠦ࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶ࠾ࠥࢁࡽࠣ᮸").format(bstack111lllll11l_opy_)) from e
            else:
                bstack111lll1l111_opy_ = int(bstack111lllll11l_opy_)
        logger.info(bstack11ll1ll_opy_ (u"ࠨࡍࡢࡺࠣࡪࡦ࡯࡬ࡶࡴࡨࡷࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡵࡨࡸࠥࡺ࡯࠻ࠢࡾࢁࠥ࠮ࡦࡳࡱࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽࠪࠤ᮹").format(bstack111lll1l111_opy_, bstack111lllll11l_opy_))
        return bstack111lll1l111_opy_
    def bstack111lll1l1ll_opy_(self):
        return self.bstack111llll111l_opy_
    def bstack11l11111ll1_opy_(self):
        return self.bstack111llll1lll_opy_
    def bstack111lll1l11l_opy_(self):
        return self.bstack11l11111l1l_opy_
    def __111lll1l1l1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll111l_opy_ = bool(enabled)
            if mode not in [bstack11ll1ll_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡈ࡬ࡶࡸࡺࠧᮺ"), bstack11ll1ll_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡒࡲࡱࡿࠧᮻ")]:
                logger.warning(bstack11ll1ll_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡳ࡯ࡥࡧࠣࠫࢀࢃࠧࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸ࡮ࡴࡧࠡࡶࡲࠤࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ࠴ࠢᮼ").format(mode))
                mode = bstack11ll1ll_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪᮽ")
            self.bstack111llll1lll_opy_ = mode
            if source is None:
                self.bstack11l11111l1l_opy_ = None
            elif isinstance(source, list):
                self.bstack11l11111l1l_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11ll1ll_opy_ (u"ࠫ࠳ࡰࡳࡰࡰࠪᮾ")):
                self.bstack11l11111l1l_opy_ = self._111ll1lllll_opy_(source)
            self.__11l111111l1_opy_()
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠ࠮ࠢࡨࡲࡦࡨ࡬ࡦࡦ࠽ࠤࢀࢃࠬࠡ࡯ࡲࡨࡪࡀࠠࡼࡿ࠯ࠤࡸࡵࡵࡳࡥࡨ࠾ࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᮿ").format(enabled, mode, source, e))
    def bstack111lll11lll_opy_(self):
        return self.bstack111lll1ll1l_opy_
    def __111lllll111_opy_(self, value):
        self.bstack111lll1ll1l_opy_ = bool(value)
        self.__11l111111l1_opy_()
    def bstack111llllll11_opy_(self):
        return self.bstack111llll1111_opy_
    def __111ll1l111l_opy_(self, value):
        self.bstack111llll1111_opy_ = bool(value)
        self.__11l111111l1_opy_()
    def bstack111llll1ll1_opy_(self):
        return self.bstack111llll1l11_opy_
    def __111ll1ll1ll_opy_(self, value):
        self.bstack111llll1l11_opy_ = bool(value)
        self.__11l111111l1_opy_()
    def __11l111111l1_opy_(self):
        if self.bstack111llll111l_opy_:
            self.bstack111lll1ll1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111lll1ll11_opy_.enable(bstack11l11111lll_opy_)
        elif self.bstack111lll1ll1l_opy_:
            self.bstack111llll1111_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll1ll11_opy_.enable(bstack111lllll1ll_opy_)
        elif self.bstack111llll1111_opy_:
            self.bstack111lll1ll1l_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll1ll11_opy_.enable(bstack111ll1lll1l_opy_)
        elif self.bstack111llll1l11_opy_:
            self.bstack111lll1ll1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll1ll11_opy_.enable(bstack111ll1l1l1l_opy_)
        else:
            self.bstack111lll1ll11_opy_.disable()
    def bstack1lll1l11l_opy_(self):
        return self.bstack111lll1ll11_opy_.bstack111ll11llll_opy_()
    def bstack11l1ll1l1_opy_(self):
        if self.bstack111lll1ll11_opy_.bstack111ll11llll_opy_():
            return self.bstack111lll1ll11_opy_.get_name()
        return None
    def _111ll1lllll_opy_(self, bstack111llll11ll_opy_):
        bstack11ll1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡴࡱࡸࡶࡨ࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠥࡧ࡮ࡥࠢࡩࡳࡷࡳࡡࡵࠢ࡬ࡸࠥ࡬࡯ࡳࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡴࡻࡲࡤࡧࡢࡪ࡮ࡲࡥࡠࡲࡤࡸ࡭ࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡵࡪࡨࠤࡏ࡙ࡏࡏࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡇࡱࡵࡱࡦࡺࡴࡦࡦࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡷ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᯀ")
        if not os.path.isfile(bstack111llll11ll_opy_):
            logger.error(bstack11ll1ll_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡾࠩࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠧᯁ").format(bstack111llll11ll_opy_))
            return []
        data = None
        try:
            with open(bstack111llll11ll_opy_, bstack11ll1ll_opy_ (u"ࠣࡴࠥᯂ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡍࡗࡔࡔࠠࡧࡴࡲࡱࠥࡹ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᯃ").format(bstack111llll11ll_opy_, e))
            return []
        _111lll11111_opy_ = None
        _111llll11l1_opy_ = None
        def _111lll1111l_opy_():
            bstack11l111111ll_opy_ = {}
            bstack111ll1l11l1_opy_ = {}
            try:
                if self.bstack111ll1ll111_opy_.startswith(bstack11ll1ll_opy_ (u"ࠪࡿࠬᯄ")) and self.bstack111ll1ll111_opy_.endswith(bstack11ll1ll_opy_ (u"ࠫࢂ࠭ᯅ")):
                    bstack11l111111ll_opy_ = json.loads(self.bstack111ll1ll111_opy_)
                else:
                    bstack11l111111ll_opy_ = dict(item.split(bstack11ll1ll_opy_ (u"ࠬࡀࠧᯆ")) for item in self.bstack111ll1ll111_opy_.split(bstack11ll1ll_opy_ (u"࠭ࠬࠨᯇ")) if bstack11ll1ll_opy_ (u"ࠧ࠻ࠩᯈ") in item) if self.bstack111ll1ll111_opy_ else {}
                if self.bstack111ll1lll11_opy_.startswith(bstack11ll1ll_opy_ (u"ࠨࡽࠪᯉ")) and self.bstack111ll1lll11_opy_.endswith(bstack11ll1ll_opy_ (u"ࠩࢀࠫᯊ")):
                    bstack111ll1l11l1_opy_ = json.loads(self.bstack111ll1lll11_opy_)
                else:
                    bstack111ll1l11l1_opy_ = dict(item.split(bstack11ll1ll_opy_ (u"ࠪ࠾ࠬᯋ")) for item in self.bstack111ll1lll11_opy_.split(bstack11ll1ll_opy_ (u"ࠫ࠱࠭ᯌ")) if bstack11ll1ll_opy_ (u"ࠬࡀࠧᯍ") in item) if self.bstack111ll1lll11_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11ll1ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴ࠼ࠣࡿࢂࠨᯎ").format(e))
            logger.debug(bstack11ll1ll_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࠿ࠦࡻࡾ࠮ࠣࡇࡑࡏ࠺ࠡࡽࢀࠦᯏ").format(bstack11l111111ll_opy_, bstack111ll1l11l1_opy_))
            return bstack11l111111ll_opy_, bstack111ll1l11l1_opy_
        if _111lll11111_opy_ is None or _111llll11l1_opy_ is None:
            _111lll11111_opy_, _111llll11l1_opy_ = _111lll1111l_opy_()
        def bstack111lll11l1l_opy_(name, bstack111lll1llll_opy_):
            if name in _111llll11l1_opy_:
                return _111llll11l1_opy_[name]
            if name in _111lll11111_opy_:
                return _111lll11111_opy_[name]
            if bstack111lll1llll_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᯐ")):
                return bstack111lll1llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᯑ")]
            return None
        if isinstance(data, dict):
            bstack11l11111l11_opy_ = []
            bstack111lllllll1_opy_ = re.compile(bstack11ll1ll_opy_ (u"ࡵࠫࡣࡡࡁ࠮࡜࠳࠱࠾ࡥ࡝ࠬࠦࠪᯒ"))
            for name, bstack111lll1llll_opy_ in data.items():
                if not isinstance(bstack111lll1llll_opy_, dict):
                    continue
                url = bstack111lll1llll_opy_.get(bstack11ll1ll_opy_ (u"ࠫࡺࡸ࡬ࠨᯓ"))
                if url is None or (isinstance(url, str) and url.strip() == bstack11ll1ll_opy_ (u"ࠬ࠭ᯔ")):
                    logger.warning(bstack11ll1ll_opy_ (u"ࠨࡒࡦࡲࡲࡷ࡮ࡺ࡯ࡳࡻ࡙ࠣࡗࡒࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᯕ").format(name, bstack111lll1llll_opy_))
                    continue
                if not bstack111lllllll1_opy_.match(name):
                    logger.warning(bstack11ll1ll_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡬࡯ࡳࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᯖ").format(name, bstack111lll1llll_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11ll1ll_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࠭ࡻࡾࠩࠣࡱࡺࡹࡴࠡࡪࡤࡺࡪࠦࡡࠡ࡮ࡨࡲ࡬ࡺࡨࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢ࠴ࠤࡦࡴࡤࠡ࠵࠳ࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳ࠯ࠤᯗ").format(name))
                    continue
                bstack111lll1llll_opy_ = bstack111lll1llll_opy_.copy()
                bstack111lll1llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᯘ")] = name
                bstack111lll1llll_opy_[bstack11ll1ll_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᯙ")] = bstack111lll11l1l_opy_(name, bstack111lll1llll_opy_)
                if not bstack111lll1llll_opy_.get(bstack11ll1ll_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᯚ")) or bstack111lll1llll_opy_.get(bstack11ll1ll_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᯛ")) == bstack11ll1ll_opy_ (u"࠭ࠧᯜ"):
                    logger.warning(bstack11ll1ll_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡰࡲࡸࠥࡹࡰࡦࡥ࡬ࡪ࡮࡫ࡤࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᯝ").format(name, bstack111lll1llll_opy_))
                    continue
                if bstack111lll1llll_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬᯞ")) and bstack111lll1llll_opy_[bstack11ll1ll_opy_ (u"ࠩࡥࡥࡸ࡫ࡂࡳࡣࡱࡧ࡭࠭ᯟ")] == bstack111lll1llll_opy_[bstack11ll1ll_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᯠ")]:
                    logger.warning(bstack11ll1ll_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡧ࡮ࡥࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᯡ").format(name, bstack111lll1llll_opy_))
                    continue
                bstack11l11111l11_opy_.append(bstack111lll1llll_opy_)
            return bstack11l11111l11_opy_
        return data
    def bstack111lllll1l1_opy_(self):
        data = {
            bstack11ll1ll_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᯢ"): {
                bstack11ll1ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᯣ"): self.bstack111lll1l1ll_opy_(),
                bstack11ll1ll_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᯤ"): self.bstack11l11111ll1_opy_(),
                bstack11ll1ll_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᯥ"): self.bstack111lll1l11l_opy_()
            }
        }
        return data
    def bstack11l1111111l_opy_(self, config):
        bstack111lll111l1_opy_ = {}
        bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨ᯦")] = {
            bstack11ll1ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯧ"): self.bstack111lll1l1ll_opy_(),
            bstack11ll1ll_opy_ (u"ࠫࡲࡵࡤࡦࠩᯨ"): self.bstack11l11111ll1_opy_()
        }
        bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࠨᯩ")] = {
            bstack11ll1ll_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᯪ"): self.bstack111llllll11_opy_()
        }
        bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠧࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡨ࡬ࡶࡸࡺࠧᯫ")] = {
            bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯬ"): self.bstack111lll11lll_opy_()
        }
        bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠩࡶ࡯࡮ࡶ࡟ࡧࡣ࡬ࡰ࡮ࡴࡧࡠࡣࡱࡨࡤ࡬࡬ࡢ࡭ࡼࠫᯭ")] = {
            bstack11ll1ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯮ"): self.bstack111llll1ll1_opy_()
        }
        if self.bstack1lll1llll_opy_(config):
            bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠫࡷ࡫ࡴࡳࡻࡢࡸࡪࡹࡴࡴࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᯯ")] = {
                bstack11ll1ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯰ"): True,
                bstack11ll1ll_opy_ (u"࠭࡭ࡢࡺࡢࡶࡪࡺࡲࡪࡧࡶࠫᯱ"): self.bstack111l11ll_opy_(config)
            }
        if self.bstack11l1ll11ll1_opy_(config):
            bstack111lll111l1_opy_[bstack11ll1ll_opy_ (u"ࠧࡢࡤࡲࡶࡹࡥࡢࡶ࡫࡯ࡨࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦ᯲ࠩ")] = {
                bstack11ll1ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥ᯳ࠩ"): True,
                bstack11ll1ll_opy_ (u"ࠩࡰࡥࡽࡥࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠨ᯴"): self.bstack11l1lll11ll_opy_(config)
            }
        return bstack111lll111l1_opy_
    def bstack1ll11lll1_opy_(self, config):
        bstack11ll1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡱ࡯ࡰࡪࡩࡴࡴࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡢࡺࠢࡰࡥࡰ࡯࡮ࡨࠢࡤࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠥ࠮ࡳࡵࡴࠬ࠾࡚ࠥࡨࡦࠢࡘ࡙ࡎࡊࠠࡰࡨࠣࡸ࡭࡫ࠠࡣࡷ࡬ࡰࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᯵")
        if not (config.get(bstack11ll1ll_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧ᯶"), None) in bstack11l11l1l11l_opy_ and self.bstack111lll1l1ll_opy_()):
            return None
        bstack111ll1l11ll_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪ᯷"), None)
        logger.debug(bstack11ll1ll_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥ᯸").format(bstack111ll1l11ll_opy_))
        try:
            bstack11ll11111ll_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠧ᯹").format(bstack111ll1l11ll_opy_)
            payload = {
                bstack11ll1ll_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨ᯺"): config.get(bstack11ll1ll_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᯻"), bstack11ll1ll_opy_ (u"ࠪࠫ᯼")),
                bstack11ll1ll_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢ᯽"): config.get(bstack11ll1ll_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨ᯾"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11ll1ll_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦ᯿"): os.environ.get(bstack11ll1ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᰀ"), bstack11ll1ll_opy_ (u"ࠣࠤᰁ")),
                bstack11ll1ll_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᰂ"): int(os.environ.get(bstack11ll1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᰃ")) or bstack11ll1ll_opy_ (u"ࠦ࠵ࠨᰄ")),
                bstack11ll1ll_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᰅ"): int(os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᰆ")) or bstack11ll1ll_opy_ (u"ࠢ࠲ࠤᰇ")),
                bstack11ll1ll_opy_ (u"ࠣࡪࡲࡷࡹࡏ࡮ࡧࡱࠥᰈ"): get_host_info(),
            }
            logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡶࡡࡺ࡮ࡲࡥࡩࡀࠠࡼࡿࠥᰉ").format(payload))
            response = bstack11ll1l111l1_opy_.bstack11ll11111l1_opy_(bstack11ll11111ll_opy_, payload)
            if response:
                logger.debug(bstack11ll1ll_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡄࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᰊ").format(response))
                return response
            else:
                logger.error(bstack11ll1ll_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᰋ").format(bstack111ll1l11ll_opy_))
                return None
        except Exception as e:
            logger.error(bstack11ll1ll_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇࠤࢀࢃ࠺ࠡࡽࢀࠦᰌ").format(bstack111ll1l11ll_opy_, e))
            return None
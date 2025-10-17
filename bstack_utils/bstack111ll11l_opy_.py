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
import os
import tempfile
import math
from bstack_utils import bstack111ll1ll1l_opy_
from bstack_utils.constants import bstack1l1ll11lll_opy_, bstack11l11ll1lll_opy_
from bstack_utils.helper import bstack11ll1llll11_opy_, get_host_info
from bstack_utils.bstack11ll1ll1ll1_opy_ import bstack11ll1ll11ll_opy_
import json
import re
import sys
bstack11l111111ll_opy_ = bstack11111_opy_ (u"ࠦࡷ࡫ࡴࡳࡻࡗࡩࡸࡺࡳࡐࡰࡉࡥ࡮ࡲࡵࡳࡧࠥᬲ")
bstack111lllll1ll_opy_ = bstack11111_opy_ (u"ࠧࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦᬳ")
bstack111lllllll1_opy_ = bstack11111_opy_ (u"ࠨࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࡋ࡯ࡲࡴࡶ᬴ࠥ")
bstack111lll11ll1_opy_ = bstack11111_opy_ (u"ࠢࡳࡧࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࠣᬵ")
bstack111lll111ll_opy_ = bstack11111_opy_ (u"ࠣࡵ࡮࡭ࡵࡌ࡬ࡢ࡭ࡼࡥࡳࡪࡆࡢ࡫࡯ࡩࡩࠨᬶ")
bstack111llll11ll_opy_ = bstack11111_opy_ (u"ࠤࡵࡹࡳ࡙࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࠨᬷ")
bstack11l1111l11l_opy_ = {
    bstack11l111111ll_opy_,
    bstack111lllll1ll_opy_,
    bstack111lllllll1_opy_,
    bstack111lll11ll1_opy_,
    bstack111lll111ll_opy_,
    bstack111llll11ll_opy_
}
bstack111lll1ll1l_opy_ = {bstack11111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᬸ")}
logger = bstack111ll1ll1l_opy_.get_logger(__name__, bstack1l1ll11lll_opy_)
class bstack11l111l1l11_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l111ll111_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1lllll1ll_opy_:
    _1ll1ll111ll_opy_ = None
    def __init__(self, config):
        self.bstack11l111l1l1l_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack11l111l11ll_opy_ = False
        self.bstack111lll1l1l1_opy_ = False
        self.bstack111lll1l11l_opy_ = None
        self.bstack111lll11lll_opy_ = bstack11l111l1l11_opy_()
        self.bstack11l1111l1ll_opy_ = None
        opts = config.get(bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᬹ"), {})
        self.bstack111llll1ll1_opy_ = config.get(bstack11111_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡅࡏࡘࠪᬺ"), bstack11111_opy_ (u"ࠨࠢᬻ"))
        self.bstack111llll111l_opy_ = config.get(bstack11111_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡅࡏࡍࠬᬼ"), bstack11111_opy_ (u"ࠣࠤᬽ"))
        bstack111lll11l1l_opy_ = opts.get(bstack111llll11ll_opy_, {})
        bstack11l111111l1_opy_ = None
        if bstack11111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᬾ") in bstack111lll11l1l_opy_:
            bstack11l111111l1_opy_ = bstack111lll11l1l_opy_[bstack11111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᬿ")]
            if bstack11l111111l1_opy_ is None:
                bstack11l111111l1_opy_ = []
        self.__11l1111ll1l_opy_(
            bstack111lll11l1l_opy_.get(bstack11111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᭀ"), False),
            bstack111lll11l1l_opy_.get(bstack11111_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᭁ"), bstack11111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭ᭂ")),
            bstack11l111111l1_opy_
        )
        self.__111llll11l1_opy_(opts.get(bstack111lllllll1_opy_, False))
        self.__111lll1111l_opy_(opts.get(bstack111lll11ll1_opy_, False))
        self.__111llll1lll_opy_(opts.get(bstack111lll111ll_opy_, False))
    @classmethod
    def bstack111111ll_opy_(cls, config=None):
        if cls._1ll1ll111ll_opy_ is None and config is not None:
            cls._1ll1ll111ll_opy_ = bstack1lllll1ll_opy_(config)
        return cls._1ll1ll111ll_opy_
    @staticmethod
    def bstack1111l1ll_opy_(config: dict) -> bool:
        bstack11l111l111l_opy_ = config.get(bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᭃ"), {}).get(bstack11l111111ll_opy_, {})
        return bstack11l111l111l_opy_.get(bstack11111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥ᭄ࠩ"), False)
    @staticmethod
    def bstack1111l1l1_opy_(config: dict) -> int:
        bstack11l111l111l_opy_ = config.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᭅ"), {}).get(bstack11l111111ll_opy_, {})
        retries = 0
        if bstack1lllll1ll_opy_.bstack1111l1ll_opy_(config):
            retries = bstack11l111l111l_opy_.get(bstack11111_opy_ (u"ࠪࡱࡦࡾࡒࡦࡶࡵ࡭ࡪࡹࠧᭆ"), 1)
        return retries
    @staticmethod
    def bstack1111111l1_opy_(config: dict) -> dict:
        bstack11l1111l111_opy_ = config.get(bstack11111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᭇ"), {})
        return {
            key: value for key, value in bstack11l1111l111_opy_.items() if key in bstack11l1111l11l_opy_
        }
    @staticmethod
    def bstack111lll1lll1_opy_():
        bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᭈ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠨࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࢀࢃࠢᭉ").format(os.getenv(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᭊ")))))
    @staticmethod
    def bstack11l1111l1l1_opy_(test_name: str):
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᭋ")
        bstack11l1111111l_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡽࢀ࠲ࡹࡾࡴࠣᭌ").format(os.getenv(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᭍"))))
        with open(bstack11l1111111l_opy_, bstack11111_opy_ (u"ࠫࡦ࠭᭎")) as file:
            file.write(bstack11111_opy_ (u"ࠧࢁࡽ࡝ࡰࠥ᭏").format(test_name))
    @staticmethod
    def bstack111lll1l111_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll1ll1l_opy_
    @staticmethod
    def bstack11ll11111l1_opy_(config: dict) -> bool:
        bstack11l111l11l1_opy_ = config.get(bstack11111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭐"), {}).get(bstack111lllll1ll_opy_, {})
        return bstack11l111l11l1_opy_.get(bstack11111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᭑"), False)
    @staticmethod
    def bstack11ll111111l_opy_(config: dict, bstack11ll1111111_opy_: int = 0) -> int:
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠯ࠤࡼ࡮ࡩࡤࡪࠣࡧࡦࡴࠠࡣࡧࠣࡥࡳࠦࡡࡣࡵࡲࡰࡺࡺࡥࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡵࠤࡦࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳ࡬ࡩࡨࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡴࡺࡡ࡭ࡡࡷࡩࡸࡺࡳࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࠨࡳࡧࡴࡹ࡮ࡸࡥࡥࠢࡩࡳࡷࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠰ࡦࡦࡹࡥࡥࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࡸ࠯࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭒")
        bstack11l111l11l1_opy_ = config.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭓"), {}).get(bstack11111_opy_ (u"ࠪࡥࡧࡵࡲࡵࡄࡸ࡭ࡱࡪࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠩ᭔"), {})
        bstack111lll11l11_opy_ = 0
        bstack11l11111lll_opy_ = 0
        if bstack1lllll1ll_opy_.bstack11ll11111l1_opy_(config):
            bstack11l11111lll_opy_ = bstack11l111l11l1_opy_.get(bstack11111_opy_ (u"ࠫࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴࠩ᭕"), 5)
            if isinstance(bstack11l11111lll_opy_, str) and bstack11l11111lll_opy_.endswith(bstack11111_opy_ (u"ࠬࠫࠧ᭖")):
                try:
                    percentage = int(bstack11l11111lll_opy_.strip(bstack11111_opy_ (u"࠭ࠥࠨ᭗")))
                    if bstack11ll1111111_opy_ > 0:
                        bstack111lll11l11_opy_ = math.ceil((percentage * bstack11ll1111111_opy_) / 100)
                    else:
                        raise ValueError(bstack11111_opy_ (u"ࠢࡕࡱࡷࡥࡱࠦࡴࡦࡵࡷࡷࠥࡳࡵࡴࡶࠣࡦࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡨࡲࡶࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠯ࡥࡥࡸ࡫ࡤࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࡷ࠳ࠨ᭘"))
                except ValueError as e:
                    raise ValueError(bstack11111_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪࠦࡶࡢ࡮ࡸࡩࠥ࡬࡯ࡳࠢࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹ࠺ࠡࡽࢀࠦ᭙").format(bstack11l11111lll_opy_)) from e
            else:
                bstack111lll11l11_opy_ = int(bstack11l11111lll_opy_)
        logger.info(bstack11111_opy_ (u"ࠤࡐࡥࡽࠦࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡸ࡫ࡴࠡࡶࡲ࠾ࠥࢁࡽࠡࠪࡩࡶࡴࡳࠠࡤࡱࡱࡪ࡮࡭࠺ࠡࡽࢀ࠭ࠧ᭚").format(bstack111lll11l11_opy_, bstack11l11111lll_opy_))
        return bstack111lll11l11_opy_
    def bstack111llll1l1l_opy_(self):
        return self.bstack111lll1l1l1_opy_
    def bstack11l1111ll11_opy_(self):
        return self.bstack111lll1l11l_opy_
    def bstack111lll111l1_opy_(self):
        return self.bstack11l1111l1ll_opy_
    def __11l1111ll1l_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111lll1l1l1_opy_ = bool(enabled)
            if mode not in [bstack11111_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭛"), bstack11111_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡕ࡮࡭ࡻࠪ᭜")]:
                logger.warning(bstack11111_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡ࡯ࡲࡨࡪࠦࠧࡼࡿࠪࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡪࡰࡪࠤࡹࡵࠠࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ࠰ࠥ᭝").format(mode))
                mode = bstack11111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭᭞")
            self.bstack111lll1l11l_opy_ = mode
            if source is None:
                self.bstack11l1111l1ll_opy_ = None
            elif isinstance(source, list):
                self.bstack11l1111l1ll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11111_opy_ (u"ࠧ࠯࡬ࡶࡳࡳ࠭᭟")):
                self.bstack11l1111l1ll_opy_ = self._11l111l1111_opy_(source)
            self.__11l11111l11_opy_()
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣ࠱ࠥ࡫࡮ࡢࡤ࡯ࡩࡩࡀࠠࡼࡿ࠯ࠤࡲࡵࡤࡦ࠼ࠣࡿࢂ࠲ࠠࡴࡱࡸࡶࡨ࡫࠺ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ᭠").format(enabled, mode, source, e))
    def bstack111lll1l1ll_opy_(self):
        return self.bstack11l111l1l1l_opy_
    def __111llll11l1_opy_(self, value):
        self.bstack11l111l1l1l_opy_ = bool(value)
        self.__11l11111l11_opy_()
    def bstack11l111l1lll_opy_(self):
        return self.bstack111llll1111_opy_
    def __111lll1111l_opy_(self, value):
        self.bstack111llll1111_opy_ = bool(value)
        self.__11l11111l11_opy_()
    def bstack111lll1ll11_opy_(self):
        return self.bstack11l111l11ll_opy_
    def __111llll1lll_opy_(self, value):
        self.bstack11l111l11ll_opy_ = bool(value)
        self.__11l11111l11_opy_()
    def __11l11111l11_opy_(self):
        if self.bstack111lll1l1l1_opy_:
            self.bstack11l111l1l1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack11l111l11ll_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111llll11ll_opy_)
        elif self.bstack11l111l1l1l_opy_:
            self.bstack111llll1111_opy_ = False
            self.bstack11l111l11ll_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111lllllll1_opy_)
        elif self.bstack111llll1111_opy_:
            self.bstack11l111l1l1l_opy_ = False
            self.bstack11l111l11ll_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111lll11ll1_opy_)
        elif self.bstack11l111l11ll_opy_:
            self.bstack11l111l1l1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111lll111ll_opy_)
        else:
            self.bstack111lll11lll_opy_.disable()
    def bstack1llll1111_opy_(self):
        return self.bstack111lll11lll_opy_.bstack11l111ll111_opy_()
    def bstack1l111ll1ll_opy_(self):
        if self.bstack111lll11lll_opy_.bstack11l111ll111_opy_():
            return self.bstack111lll11lll_opy_.get_name()
        return None
    def _11l111l1111_opy_(self, bstack11l11111111_opy_):
        bstack11111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡷࡴࡻࡲࡤࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠡࡣࡱࡨࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡯ࡴࠡࡨࡲࡶࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡰࡷࡵࡧࡪࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠢࠫࡷࡹࡸࠩ࠻ࠢࡓࡥࡹ࡮ࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡕࡒࡒࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡊࡴࡸ࡭ࡢࡶࡷࡩࡩࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡳࡧࡳࡳࡸ࡯ࡴࡰࡴࡼࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭡")
        if not os.path.isfile(bstack11l11111111_opy_):
            logger.error(bstack11111_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠮ࠣ᭢").format(bstack11l11111111_opy_))
            return []
        data = None
        try:
            with open(bstack11l11111111_opy_, bstack11111_opy_ (u"ࠦࡷࠨ᭣")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡐࡓࡐࡐࠣࡪࡷࡵ࡭ࠡࡵࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣ᭤").format(bstack11l11111111_opy_, e))
            return []
        _11l111l1ll1_opy_ = None
        _11l1111llll_opy_ = None
        def _11l1111lll1_opy_():
            bstack111llll1l11_opy_ = {}
            bstack111llllll11_opy_ = {}
            try:
                if self.bstack111llll1ll1_opy_.startswith(bstack11111_opy_ (u"࠭ࡻࠨ᭥")) and self.bstack111llll1ll1_opy_.endswith(bstack11111_opy_ (u"ࠧࡾࠩ᭦")):
                    bstack111llll1l11_opy_ = json.loads(self.bstack111llll1ll1_opy_)
                else:
                    bstack111llll1l11_opy_ = dict(item.split(bstack11111_opy_ (u"ࠨ࠼ࠪ᭧")) for item in self.bstack111llll1ll1_opy_.split(bstack11111_opy_ (u"ࠩ࠯ࠫ᭨")) if bstack11111_opy_ (u"ࠪ࠾ࠬ᭩") in item) if self.bstack111llll1ll1_opy_ else {}
                if self.bstack111llll111l_opy_.startswith(bstack11111_opy_ (u"ࠫࢀ࠭᭪")) and self.bstack111llll111l_opy_.endswith(bstack11111_opy_ (u"ࠬࢃࠧ᭫")):
                    bstack111llllll11_opy_ = json.loads(self.bstack111llll111l_opy_)
                else:
                    bstack111llllll11_opy_ = dict(item.split(bstack11111_opy_ (u"࠭࠺ࠨ᭬")) for item in self.bstack111llll111l_opy_.split(bstack11111_opy_ (u"ࠧ࠭ࠩ᭭")) if bstack11111_opy_ (u"ࠨ࠼ࠪ᭮") in item) if self.bstack111llll111l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡩࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡱࡦࡶࡰࡪࡰࡪࡷ࠿ࠦࡻࡾࠤ᭯").format(e))
            logger.debug(bstack11111_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡲࡧࡰࡱ࡫ࡱ࡫ࡸࠦࡦࡳࡱࡰࠤࡪࡴࡶ࠻ࠢࡾࢁ࠱ࠦࡃࡍࡋ࠽ࠤࢀࢃࠢ᭰").format(bstack111llll1l11_opy_, bstack111llllll11_opy_))
            return bstack111llll1l11_opy_, bstack111llllll11_opy_
        if _11l111l1ll1_opy_ is None or _11l1111llll_opy_ is None:
            _11l111l1ll1_opy_, _11l1111llll_opy_ = _11l1111lll1_opy_()
        def bstack111lllll11l_opy_(name, bstack111lllll111_opy_):
            if name in _11l1111llll_opy_:
                return _11l1111llll_opy_[name]
            if name in _11l111l1ll1_opy_:
                return _11l111l1ll1_opy_[name]
            if bstack111lllll111_opy_.get(bstack11111_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫ᭱")):
                return bstack111lllll111_opy_[bstack11111_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬ᭲")]
            return None
        if isinstance(data, dict):
            bstack111llllllll_opy_ = []
            bstack111lllll1l1_opy_ = re.compile(bstack11111_opy_ (u"ࡸࠧ࡟࡝ࡄ࠱࡟࠶࠭࠺ࡡࡠ࠯ࠩ࠭᭳"))
            for name, bstack111lllll111_opy_ in data.items():
                if not isinstance(bstack111lllll111_opy_, dict):
                    continue
                if not bstack111lllll111_opy_.get(bstack11111_opy_ (u"ࠧࡶࡴ࡯ࠫ᭴")):
                    logger.warning(bstack11111_opy_ (u"ࠣࡔࡨࡴࡴࡹࡩࡵࡱࡵࡽ࡛ࠥࡒࡍࠢ࡬ࡷࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧ᭵").format(name, bstack111lllll111_opy_))
                    continue
                if not bstack111lllll1l1_opy_.match(name):
                    logger.warning(bstack11111_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࡧࡱࡵࡱࡦࡺࠠࡧࡱࡵࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨ᭶").format(name, bstack111lllll111_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11111_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࠨࡽࢀࠫࠥࡳࡵࡴࡶࠣ࡬ࡦࡼࡥࠡࡣࠣࡰࡪࡴࡧࡵࡪࠣࡦࡪࡺࡷࡦࡧࡱࠤ࠶ࠦࡡ࡯ࡦࠣ࠷࠵ࠦࡣࡩࡣࡵࡥࡨࡺࡥࡳࡵ࠱ࠦ᭷").format(name))
                    continue
                bstack111lllll111_opy_ = bstack111lllll111_opy_.copy()
                bstack111lllll111_opy_[bstack11111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᭸")] = name
                bstack111lllll111_opy_[bstack11111_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬ᭹")] = bstack111lllll11l_opy_(name, bstack111lllll111_opy_)
                if not bstack111lllll111_opy_.get(bstack11111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭᭺")):
                    logger.warning(bstack11111_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡰࡲࡸࠥࡹࡰࡦࡥ࡬ࡪ࡮࡫ࡤࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢ᭻").format(name, bstack111lllll111_opy_))
                    continue
                if bstack111lllll111_opy_.get(bstack11111_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬ᭼")) and bstack111lllll111_opy_[bstack11111_opy_ (u"ࠩࡥࡥࡸ࡫ࡂࡳࡣࡱࡧ࡭࠭᭽")] == bstack111lllll111_opy_[bstack11111_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪ᭾")]:
                    logger.warning(bstack11111_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡧ࡮ࡥࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᭿").format(name, bstack111lllll111_opy_))
                    continue
                bstack111llllllll_opy_.append(bstack111lllll111_opy_)
            return bstack111llllllll_opy_
        return data
    def bstack111lll1llll_opy_(self):
        data = {
            bstack11111_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᮀ"): {
                bstack11111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮁ"): self.bstack111llll1l1l_opy_(),
                bstack11111_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᮂ"): self.bstack11l1111ll11_opy_(),
                bstack11111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᮃ"): self.bstack111lll111l1_opy_()
            }
        }
        return data
    def bstack111llllll1l_opy_(self, config):
        bstack11l11111ll1_opy_ = {}
        bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᮄ")] = {
            bstack11111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮅ"): self.bstack111llll1l1l_opy_(),
            bstack11111_opy_ (u"ࠫࡲࡵࡤࡦࠩᮆ"): self.bstack11l1111ll11_opy_()
        }
        bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࠨᮇ")] = {
            bstack11111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮈ"): self.bstack11l111l1lll_opy_()
        }
        bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠧࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡨ࡬ࡶࡸࡺࠧᮉ")] = {
            bstack11111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮊ"): self.bstack111lll1l1ll_opy_()
        }
        bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠩࡶ࡯࡮ࡶ࡟ࡧࡣ࡬ࡰ࡮ࡴࡧࡠࡣࡱࡨࡤ࡬࡬ࡢ࡭ࡼࠫᮋ")] = {
            bstack11111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮌ"): self.bstack111lll1ll11_opy_()
        }
        if self.bstack1111l1ll_opy_(config):
            bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡴࡳࡻࡢࡸࡪࡹࡴࡴࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᮍ")] = {
                bstack11111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮎ"): True,
                bstack11111_opy_ (u"࠭࡭ࡢࡺࡢࡶࡪࡺࡲࡪࡧࡶࠫᮏ"): self.bstack1111l1l1_opy_(config)
            }
        if self.bstack11ll11111l1_opy_(config):
            bstack11l11111ll1_opy_[bstack11111_opy_ (u"ࠧࡢࡤࡲࡶࡹࡥࡢࡶ࡫࡯ࡨࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦࠩᮐ")] = {
                bstack11111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮑ"): True,
                bstack11111_opy_ (u"ࠩࡰࡥࡽࡥࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠨᮒ"): self.bstack11ll111111l_opy_(config)
            }
        return bstack11l11111ll1_opy_
    def bstack1llll1lll1_opy_(self, config):
        bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡱ࡯ࡰࡪࡩࡴࡴࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡢࡺࠢࡰࡥࡰ࡯࡮ࡨࠢࡤࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠥ࠮ࡳࡵࡴࠬ࠾࡚ࠥࡨࡦࠢࡘ࡙ࡎࡊࠠࡰࡨࠣࡸ࡭࡫ࠠࡣࡷ࡬ࡰࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮓ")
        if not (config.get(bstack11111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᮔ"), None) in bstack11l11ll1lll_opy_ and self.bstack111llll1l1l_opy_()):
            return None
        bstack11l11111l1l_opy_ = os.environ.get(bstack11111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᮕ"), None)
        logger.debug(bstack11111_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥᮖ").format(bstack11l11111l1l_opy_))
        try:
            bstack11ll11ll111_opy_ = bstack11111_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠧᮗ").format(bstack11l11111l1l_opy_)
            payload = {
                bstack11111_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨᮘ"): config.get(bstack11111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᮙ"), bstack11111_opy_ (u"ࠪࠫᮚ")),
                bstack11111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᮛ"): config.get(bstack11111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᮜ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᮝ"): os.environ.get(bstack11111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᮞ"), bstack11111_opy_ (u"ࠣࠤᮟ")),
                bstack11111_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᮠ"): int(os.environ.get(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᮡ")) or bstack11111_opy_ (u"ࠦ࠵ࠨᮢ")),
                bstack11111_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᮣ"): int(os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᮤ")) or bstack11111_opy_ (u"ࠢ࠲ࠤᮥ")),
                bstack11111_opy_ (u"ࠣࡪࡲࡷࡹࡏ࡮ࡧࡱࠥᮦ"): get_host_info(),
            }
            logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡶࡡࡺ࡮ࡲࡥࡩࡀࠠࡼࡿࠥᮧ").format(payload))
            response = bstack11ll1ll11ll_opy_.bstack11ll11ll1ll_opy_(bstack11ll11ll111_opy_, payload)
            if response:
                logger.debug(bstack11111_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡄࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᮨ").format(response))
                return response
            else:
                logger.error(bstack11111_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᮩ").format(bstack11l11111l1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇࠤࢀࢃ࠺ࠡࡽࢀ᮪ࠦ").format(bstack11l11111l1l_opy_, e))
            return None
# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1lll11ll11_opy_
from bstack_utils.constants import bstack1llll11lll_opy_, bstack11l11lllll1_opy_
from bstack_utils.helper import bstack11ll1ll11ll_opy_, get_host_info
from bstack_utils.bstack11lll111lll_opy_ import bstack11lll111111_opy_
import json
import re
import sys
bstack11l1111ll11_opy_ = bstack11l111_opy_ (u"ࠦࡷ࡫ࡴࡳࡻࡗࡩࡸࡺࡳࡐࡰࡉࡥ࡮ࡲࡵࡳࡧࠥᬲ")
bstack111lll11ll1_opy_ = bstack11l111_opy_ (u"ࠧࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦᬳ")
bstack11l111111ll_opy_ = bstack11l111_opy_ (u"ࠨࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࡋ࡯ࡲࡴࡶ᬴ࠥ")
bstack11l11111l1l_opy_ = bstack11l111_opy_ (u"ࠢࡳࡧࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࠣᬵ")
bstack111lllll111_opy_ = bstack11l111_opy_ (u"ࠣࡵ࡮࡭ࡵࡌ࡬ࡢ࡭ࡼࡥࡳࡪࡆࡢ࡫࡯ࡩࡩࠨᬶ")
bstack11l111l1lll_opy_ = bstack11l111_opy_ (u"ࠤࡵࡹࡳ࡙࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࠨᬷ")
bstack111llll1l11_opy_ = {
    bstack11l1111ll11_opy_,
    bstack111lll11ll1_opy_,
    bstack11l111111ll_opy_,
    bstack11l11111l1l_opy_,
    bstack111lllll111_opy_,
    bstack11l111l1lll_opy_
}
bstack111lll1111l_opy_ = {bstack11l111_opy_ (u"ࠪࡴࡾࡺࡥࡴࡶࠪᬸ")}
logger = bstack1lll11ll11_opy_.get_logger(__name__, bstack1llll11lll_opy_)
class bstack11l1111l11l_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111llllllll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1llllllll_opy_:
    _1ll1ll111ll_opy_ = None
    def __init__(self, config):
        self.bstack111lll11l11_opy_ = False
        self.bstack111lllll1l1_opy_ = False
        self.bstack111llll1ll1_opy_ = False
        self.bstack11l1111llll_opy_ = False
        self.bstack111lll1l111_opy_ = None
        self.bstack111lll1l1l1_opy_ = bstack11l1111l11l_opy_()
        self.bstack11l11111lll_opy_ = None
        opts = config.get(bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᬹ"), {})
        self.bstack11l11111111_opy_ = config.get(bstack11l111_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡅࡏࡘࠪᬺ"), bstack11l111_opy_ (u"ࠨࠢᬻ"))
        self.bstack111lll1l1ll_opy_ = config.get(bstack11l111_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡅࡏࡍࠬᬼ"), bstack11l111_opy_ (u"ࠣࠤᬽ"))
        bstack11l111l111l_opy_ = opts.get(bstack11l111l1lll_opy_, {})
        bstack11l1111l111_opy_ = None
        if bstack11l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᬾ") in bstack11l111l111l_opy_:
            bstack11l1111l111_opy_ = bstack11l111l111l_opy_[bstack11l111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᬿ")]
            if bstack11l1111l111_opy_ is None:
                bstack11l1111l111_opy_ = []
        self.__111lll1ll1l_opy_(
            bstack11l111l111l_opy_.get(bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᭀ"), False),
            bstack11l111l111l_opy_.get(bstack11l111_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᭁ"), bstack11l111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭ᭂ")),
            bstack11l1111l111_opy_
        )
        self.__111lll1ll11_opy_(opts.get(bstack11l111111ll_opy_, False))
        self.__111lll111l1_opy_(opts.get(bstack11l11111l1l_opy_, False))
        self.__111llll11l1_opy_(opts.get(bstack111lllll111_opy_, False))
    @classmethod
    def bstack111ll1ll_opy_(cls, config=None):
        if cls._1ll1ll111ll_opy_ is None and config is not None:
            cls._1ll1ll111ll_opy_ = bstack1llllllll_opy_(config)
        return cls._1ll1ll111ll_opy_
    @staticmethod
    def bstack111l111l_opy_(config: dict) -> bool:
        bstack111llll1lll_opy_ = config.get(bstack11l111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᭃ"), {}).get(bstack11l1111ll11_opy_, {})
        return bstack111llll1lll_opy_.get(bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥ᭄ࠩ"), False)
    @staticmethod
    def bstack111lll1l_opy_(config: dict) -> int:
        bstack111llll1lll_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᭅ"), {}).get(bstack11l1111ll11_opy_, {})
        retries = 0
        if bstack1llllllll_opy_.bstack111l111l_opy_(config):
            retries = bstack111llll1lll_opy_.get(bstack11l111_opy_ (u"ࠪࡱࡦࡾࡒࡦࡶࡵ࡭ࡪࡹࠧᭆ"), 1)
        return retries
    @staticmethod
    def bstack11lll1l1l1_opy_(config: dict) -> dict:
        bstack111llll1111_opy_ = config.get(bstack11l111_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨᭇ"), {})
        return {
            key: value for key, value in bstack111llll1111_opy_.items() if key in bstack111llll1l11_opy_
        }
    @staticmethod
    def bstack11l111l11ll_opy_():
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᭈ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠨࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࢀࢃࠢᭉ").format(os.getenv(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᭊ")))))
    @staticmethod
    def bstack11l1111l1l1_opy_(test_name: str):
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᭋ")
        bstack111lll11111_opy_ = os.path.join(tempfile.gettempdir(), bstack11l111_opy_ (u"ࠤࡩࡥ࡮ࡲࡥࡥࡡࡷࡩࡸࡺࡳࡠࡽࢀ࠲ࡹࡾࡴࠣᭌ").format(os.getenv(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᭍"))))
        with open(bstack111lll11111_opy_, bstack11l111_opy_ (u"ࠫࡦ࠭᭎")) as file:
            file.write(bstack11l111_opy_ (u"ࠧࢁࡽ࡝ࡰࠥ᭏").format(test_name))
    @staticmethod
    def bstack11l111l1l11_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll1111l_opy_
    @staticmethod
    def bstack11l1llll1ll_opy_(config: dict) -> bool:
        bstack111lll1llll_opy_ = config.get(bstack11l111_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭐"), {}).get(bstack111lll11ll1_opy_, {})
        return bstack111lll1llll_opy_.get(bstack11l111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᭑"), False)
    @staticmethod
    def bstack11l1llll111_opy_(config: dict, bstack11ll1111l1l_opy_: int = 0) -> int:
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡍࡥࡵࠢࡷ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠯ࠤࡼ࡮ࡩࡤࡪࠣࡧࡦࡴࠠࡣࡧࠣࡥࡳࠦࡡࡣࡵࡲࡰࡺࡺࡥࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡵࠤࡦࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡦࡳࡳ࡬ࡩࡨࠢࠫࡨ࡮ࡩࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴࡼ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡸࡴࡺࡡ࡭ࡡࡷࡩࡸࡺࡳࠡࠪ࡬ࡲࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡺ࡯ࡵࡣ࡯ࠤࡳࡻ࡭ࡣࡧࡵࠤࡴ࡬ࠠࡵࡧࡶࡸࡸࠦࠨࡳࡧࡴࡹ࡮ࡸࡥࡥࠢࡩࡳࡷࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧ࠰ࡦࡦࡹࡥࡥࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨࡸ࠯࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡬ࡲࡹࡀࠠࡕࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭒")
        bstack111lll1llll_opy_ = config.get(bstack11l111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭓"), {}).get(bstack11l111_opy_ (u"ࠪࡥࡧࡵࡲࡵࡄࡸ࡭ࡱࡪࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠩ᭔"), {})
        bstack11l1111l1ll_opy_ = 0
        bstack11l1111111l_opy_ = 0
        if bstack1llllllll_opy_.bstack11l1llll1ll_opy_(config):
            bstack11l1111111l_opy_ = bstack111lll1llll_opy_.get(bstack11l111_opy_ (u"ࠫࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴࠩ᭕"), 5)
            if isinstance(bstack11l1111111l_opy_, str) and bstack11l1111111l_opy_.endswith(bstack11l111_opy_ (u"ࠬࠫࠧ᭖")):
                try:
                    percentage = int(bstack11l1111111l_opy_.strip(bstack11l111_opy_ (u"࠭ࠥࠨ᭗")))
                    if bstack11ll1111l1l_opy_ > 0:
                        bstack11l1111l1ll_opy_ = math.ceil((percentage * bstack11ll1111l1l_opy_) / 100)
                    else:
                        raise ValueError(bstack11l111_opy_ (u"ࠢࡕࡱࡷࡥࡱࠦࡴࡦࡵࡷࡷࠥࡳࡵࡴࡶࠣࡦࡪࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡࡨࡲࡶࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠯ࡥࡥࡸ࡫ࡤࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࡷ࠳ࠨ᭘"))
                except ValueError as e:
                    raise ValueError(bstack11l111_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪࠦࡶࡢ࡮ࡸࡩࠥ࡬࡯ࡳࠢࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹ࠺ࠡࡽࢀࠦ᭙").format(bstack11l1111111l_opy_)) from e
            else:
                bstack11l1111l1ll_opy_ = int(bstack11l1111111l_opy_)
        logger.info(bstack11l111_opy_ (u"ࠤࡐࡥࡽࠦࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࠤࡸ࡫ࡴࠡࡶࡲ࠾ࠥࢁࡽࠡࠪࡩࡶࡴࡳࠠࡤࡱࡱࡪ࡮࡭࠺ࠡࡽࢀ࠭ࠧ᭚").format(bstack11l1111l1ll_opy_, bstack11l1111111l_opy_))
        return bstack11l1111l1ll_opy_
    def bstack111lllllll1_opy_(self):
        return self.bstack11l1111llll_opy_
    def bstack111llllll1l_opy_(self):
        return self.bstack111lll1l111_opy_
    def bstack111lllll1ll_opy_(self):
        return self.bstack11l11111lll_opy_
    def __111lll1ll1l_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l1111llll_opy_ = bool(enabled)
            if mode not in [bstack11l111_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭛"), bstack11l111_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡕ࡮࡭ࡻࠪ᭜")]:
                logger.warning(bstack11l111_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡ࡯ࡲࡨࡪࠦࠧࡼࡿࠪࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡪࡰࡪࠤࡹࡵࠠࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ࠰ࠥ᭝").format(mode))
                mode = bstack11l111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭᭞")
            self.bstack111lll1l111_opy_ = mode
            if source is None:
                self.bstack11l11111lll_opy_ = None
            elif isinstance(source, list):
                self.bstack11l11111lll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l111_opy_ (u"ࠧ࠯࡬ࡶࡳࡳ࠭᭟")):
                self.bstack11l11111lll_opy_ = self._11l11111ll1_opy_(source)
            self.__111lll111ll_opy_()
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠣࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡸ࡫ࡴࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣ࠱ࠥ࡫࡮ࡢࡤ࡯ࡩࡩࡀࠠࡼࡿ࠯ࠤࡲࡵࡤࡦ࠼ࠣࡿࢂ࠲ࠠࡴࡱࡸࡶࡨ࡫࠺ࠡࡽࢀ࠲ࠥࡋࡲࡳࡱࡵ࠾ࠥࢁࡽࠣ᭠").format(enabled, mode, source, e))
    def bstack111llll11ll_opy_(self):
        return self.bstack111lll11l11_opy_
    def __111lll1ll11_opy_(self, value):
        self.bstack111lll11l11_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def bstack111lll11lll_opy_(self):
        return self.bstack111lllll1l1_opy_
    def __111lll111l1_opy_(self, value):
        self.bstack111lllll1l1_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def bstack111lllll11l_opy_(self):
        return self.bstack111llll1ll1_opy_
    def __111llll11l1_opy_(self, value):
        self.bstack111llll1ll1_opy_ = bool(value)
        self.__111lll111ll_opy_()
    def __111lll111ll_opy_(self):
        if self.bstack11l1111llll_opy_:
            self.bstack111lll11l11_opy_ = False
            self.bstack111lllll1l1_opy_ = False
            self.bstack111llll1ll1_opy_ = False
            self.bstack111lll1l1l1_opy_.enable(bstack11l111l1lll_opy_)
        elif self.bstack111lll11l11_opy_:
            self.bstack111lllll1l1_opy_ = False
            self.bstack111llll1ll1_opy_ = False
            self.bstack11l1111llll_opy_ = False
            self.bstack111lll1l1l1_opy_.enable(bstack11l111111ll_opy_)
        elif self.bstack111lllll1l1_opy_:
            self.bstack111lll11l11_opy_ = False
            self.bstack111llll1ll1_opy_ = False
            self.bstack11l1111llll_opy_ = False
            self.bstack111lll1l1l1_opy_.enable(bstack11l11111l1l_opy_)
        elif self.bstack111llll1ll1_opy_:
            self.bstack111lll11l11_opy_ = False
            self.bstack111lllll1l1_opy_ = False
            self.bstack11l1111llll_opy_ = False
            self.bstack111lll1l1l1_opy_.enable(bstack111lllll111_opy_)
        else:
            self.bstack111lll1l1l1_opy_.disable()
    def bstack1llll1lll_opy_(self):
        return self.bstack111lll1l1l1_opy_.bstack111llllllll_opy_()
    def bstack1l1l1l1111_opy_(self):
        if self.bstack111lll1l1l1_opy_.bstack111llllllll_opy_():
            return self.bstack111lll1l1l1_opy_.get_name()
        return None
    def _11l11111ll1_opy_(self, bstack111llllll11_opy_):
        bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡢࡴࡶࡩࠥࡐࡓࡐࡐࠣࡷࡴࡻࡲࡤࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠡࡣࡱࡨࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡯ࡴࠡࡨࡲࡶࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡳࡰࡷࡵࡧࡪࡥࡦࡪ࡮ࡨࡣࡵࡧࡴࡩࠢࠫࡷࡹࡸࠩ࠻ࠢࡓࡥࡹ࡮ࠠࡵࡱࠣࡸ࡭࡫ࠠࡋࡕࡒࡒࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡱ࡯ࡳࡵ࠼ࠣࡊࡴࡸ࡭ࡢࡶࡷࡩࡩࠦ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡳࡧࡳࡳࡸ࡯ࡴࡰࡴࡼࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࡷࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭡")
        if not os.path.isfile(bstack111llllll11_opy_):
            logger.error(bstack11l111_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࠦࡤࡰࡧࡶࠤࡳࡵࡴࠡࡧࡻ࡭ࡸࡺ࠮ࠣ᭢").format(bstack111llllll11_opy_))
            return []
        data = None
        try:
            with open(bstack111llllll11_opy_, bstack11l111_opy_ (u"ࠦࡷࠨ᭣")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥࡐࡓࡐࡐࠣࡪࡷࡵ࡭ࠡࡵࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣ᭤").format(bstack111llllll11_opy_, e))
            return []
        _11l1111ll1l_opy_ = None
        _111lll1l11l_opy_ = None
        def _111lll1lll1_opy_():
            bstack111llll111l_opy_ = {}
            bstack11l111l11l1_opy_ = {}
            try:
                if self.bstack11l11111111_opy_.startswith(bstack11l111_opy_ (u"࠭ࡻࠨ᭥")) and self.bstack11l11111111_opy_.endswith(bstack11l111_opy_ (u"ࠧࡾࠩ᭦")):
                    bstack111llll111l_opy_ = json.loads(self.bstack11l11111111_opy_)
                else:
                    bstack111llll111l_opy_ = dict(item.split(bstack11l111_opy_ (u"ࠨ࠼ࠪ᭧")) for item in self.bstack11l11111111_opy_.split(bstack11l111_opy_ (u"ࠩ࠯ࠫ᭨")) if bstack11l111_opy_ (u"ࠪ࠾ࠬ᭩") in item) if self.bstack11l11111111_opy_ else {}
                if self.bstack111lll1l1ll_opy_.startswith(bstack11l111_opy_ (u"ࠫࢀ࠭᭪")) and self.bstack111lll1l1ll_opy_.endswith(bstack11l111_opy_ (u"ࠬࢃࠧ᭫")):
                    bstack11l111l11l1_opy_ = json.loads(self.bstack111lll1l1ll_opy_)
                else:
                    bstack11l111l11l1_opy_ = dict(item.split(bstack11l111_opy_ (u"࠭࠺ࠨ᭬")) for item in self.bstack111lll1l1ll_opy_.split(bstack11l111_opy_ (u"ࠧ࠭ࠩ᭭")) if bstack11l111_opy_ (u"ࠨ࠼ࠪ᭮") in item) if self.bstack111lll1l1ll_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l111_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡩࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡱࡦࡶࡰࡪࡰࡪࡷ࠿ࠦࡻࡾࠤ᭯").format(e))
            logger.debug(bstack11l111_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡲࡧࡰࡱ࡫ࡱ࡫ࡸࠦࡦࡳࡱࡰࠤࡪࡴࡶ࠻ࠢࡾࢁ࠱ࠦࡃࡍࡋ࠽ࠤࢀࢃࠢ᭰").format(bstack111llll111l_opy_, bstack11l111l11l1_opy_))
            return bstack111llll111l_opy_, bstack11l111l11l1_opy_
        if _11l1111ll1l_opy_ is None or _111lll1l11l_opy_ is None:
            _11l1111ll1l_opy_, _111lll1l11l_opy_ = _111lll1lll1_opy_()
        def bstack111lll11l1l_opy_(name, bstack11l111l1111_opy_):
            if name in _111lll1l11l_opy_:
                return _111lll1l11l_opy_[name]
            if name in _11l1111ll1l_opy_:
                return _11l1111ll1l_opy_[name]
            if bstack11l111l1111_opy_.get(bstack11l111_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫ᭱")):
                return bstack11l111l1111_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬ᭲")]
            return None
        if isinstance(data, dict):
            bstack11l111111l1_opy_ = []
            bstack11l111l1ll1_opy_ = re.compile(bstack11l111_opy_ (u"ࡸࠧ࡟࡝ࡄ࠱࡟࠶࠭࠺ࡡࡠ࠯ࠩ࠭᭳"))
            for name, bstack11l111l1111_opy_ in data.items():
                if not isinstance(bstack11l111l1111_opy_, dict):
                    continue
                if not bstack11l111l1111_opy_.get(bstack11l111_opy_ (u"ࠧࡶࡴ࡯ࠫ᭴")):
                    logger.warning(bstack11l111_opy_ (u"ࠣࡔࡨࡴࡴࡹࡩࡵࡱࡵࡽ࡛ࠥࡒࡍࠢ࡬ࡷࠥࡳࡩࡴࡵ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧ᭵").format(name, bstack11l111l1111_opy_))
                    continue
                if not bstack11l111l1ll1_opy_.match(name):
                    logger.warning(bstack11l111_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࡧࡱࡵࡱࡦࡺࠠࡧࡱࡵࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨ᭶").format(name, bstack11l111l1111_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l111_opy_ (u"ࠥࡗࡴࡻࡲࡤࡧࠣ࡭ࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠠࠨࡽࢀࠫࠥࡳࡵࡴࡶࠣ࡬ࡦࡼࡥࠡࡣࠣࡰࡪࡴࡧࡵࡪࠣࡦࡪࡺࡷࡦࡧࡱࠤ࠶ࠦࡡ࡯ࡦࠣ࠷࠵ࠦࡣࡩࡣࡵࡥࡨࡺࡥࡳࡵ࠱ࠦ᭷").format(name))
                    continue
                bstack11l111l1111_opy_ = bstack11l111l1111_opy_.copy()
                bstack11l111l1111_opy_[bstack11l111_opy_ (u"ࠫࡳࡧ࡭ࡦࠩ᭸")] = name
                bstack11l111l1111_opy_[bstack11l111_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬ᭹")] = bstack111lll11l1l_opy_(name, bstack11l111l1111_opy_)
                if not bstack11l111l1111_opy_.get(bstack11l111_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭᭺")):
                    logger.warning(bstack11l111_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡰࡲࡸࠥࡹࡰࡦࡥ࡬ࡪ࡮࡫ࡤࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢ᭻").format(name, bstack11l111l1111_opy_))
                    continue
                if bstack11l111l1111_opy_.get(bstack11l111_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬ᭼")) and bstack11l111l1111_opy_[bstack11l111_opy_ (u"ࠩࡥࡥࡸ࡫ࡂࡳࡣࡱࡧ࡭࠭᭽")] == bstack11l111l1111_opy_[bstack11l111_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪ᭾")]:
                    logger.warning(bstack11l111_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡧ࡮ࡥࠢࡥࡥࡸ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡤࡣࡱࡲࡴࡺࠠࡣࡧࠣࡸ࡭࡫ࠠࡴࡣࡰࡩࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᭿").format(name, bstack11l111l1111_opy_))
                    continue
                bstack11l111111l1_opy_.append(bstack11l111l1111_opy_)
            return bstack11l111111l1_opy_
        return data
    def bstack11l111l1l1l_opy_(self):
        data = {
            bstack11l111_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᮀ"): {
                bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮁ"): self.bstack111lllllll1_opy_(),
                bstack11l111_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᮂ"): self.bstack111llllll1l_opy_(),
                bstack11l111_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᮃ"): self.bstack111lllll1ll_opy_()
            }
        }
        return data
    def bstack11l1111lll1_opy_(self, config):
        bstack111llll1l1l_opy_ = {}
        bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᮄ")] = {
            bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮅ"): self.bstack111lllllll1_opy_(),
            bstack11l111_opy_ (u"ࠫࡲࡵࡤࡦࠩᮆ"): self.bstack111llllll1l_opy_()
        }
        bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠬࡸࡥࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࠨᮇ")] = {
            bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮈ"): self.bstack111lll11lll_opy_()
        }
        bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠧࡳࡷࡱࡣࡵࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡠࡨࡤ࡭ࡱ࡫ࡤࡠࡨ࡬ࡶࡸࡺࠧᮉ")] = {
            bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮊ"): self.bstack111llll11ll_opy_()
        }
        bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠩࡶ࡯࡮ࡶ࡟ࡧࡣ࡬ࡰ࡮ࡴࡧࡠࡣࡱࡨࡤ࡬࡬ࡢ࡭ࡼࠫᮋ")] = {
            bstack11l111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮌ"): self.bstack111lllll11l_opy_()
        }
        if self.bstack111l111l_opy_(config):
            bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠫࡷ࡫ࡴࡳࡻࡢࡸࡪࡹࡴࡴࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᮍ")] = {
                bstack11l111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮎ"): True,
                bstack11l111_opy_ (u"࠭࡭ࡢࡺࡢࡶࡪࡺࡲࡪࡧࡶࠫᮏ"): self.bstack111lll1l_opy_(config)
            }
        if self.bstack11l1llll1ll_opy_(config):
            bstack111llll1l1l_opy_[bstack11l111_opy_ (u"ࠧࡢࡤࡲࡶࡹࡥࡢࡶ࡫࡯ࡨࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦࠩᮐ")] = {
                bstack11l111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮑ"): True,
                bstack11l111_opy_ (u"ࠩࡰࡥࡽࡥࡦࡢ࡫࡯ࡹࡷ࡫ࡳࠨᮒ"): self.bstack11l1llll111_opy_(config)
            }
        return bstack111llll1l1l_opy_
    def bstack1l111llll_opy_(self, config):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡱ࡯ࡰࡪࡩࡴࡴࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡢࡺࠢࡰࡥࡰ࡯࡮ࡨࠢࡤࠤࡨࡧ࡬࡭ࠢࡷࡳࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡸ࡭ࡱࡪ࡟ࡶࡷ࡬ࡨࠥ࠮ࡳࡵࡴࠬ࠾࡚ࠥࡨࡦࠢࡘ࡙ࡎࡊࠠࡰࡨࠣࡸ࡭࡫ࠠࡣࡷ࡬ࡰࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡨࡦࡺࡡࠡࡨࡲࡶ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡥ࡫ࡦࡸ࠿ࠦࡒࡦࡵࡳࡳࡳࡹࡥࠡࡨࡵࡳࡲࠦࡴࡩࡧࠣࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠡࡧࡱࡨࡵࡵࡩ࡯ࡶ࠯ࠤࡴࡸࠠࡏࡱࡱࡩࠥ࡯ࡦࠡࡨࡤ࡭ࡱ࡫ࡤ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮓ")
        if not (config.get(bstack11l111_opy_ (u"ࠫ࡫ࡸࡡ࡮ࡧࡺࡳࡷࡱࠧᮔ"), None) in bstack11l11lllll1_opy_ and self.bstack111lllllll1_opy_()):
            return None
        bstack11l11111l11_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠬࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠪᮕ"), None)
        logger.debug(bstack11l111_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡈࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥᮖ").format(bstack11l11111l11_opy_))
        try:
            bstack11ll11ll111_opy_ = bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡧࡻࡩ࡭ࡦࡶ࠳ࢀࢃ࠯ࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠧᮗ").format(bstack11l11111l11_opy_)
            payload = {
                bstack11l111_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨᮘ"): config.get(bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᮙ"), bstack11l111_opy_ (u"ࠪࠫᮚ")),
                bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᮛ"): config.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᮜ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᮝ"): os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᮞ"), bstack11l111_opy_ (u"ࠣࠤᮟ")),
                bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᮠ"): int(os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᮡ")) or bstack11l111_opy_ (u"ࠦ࠵ࠨᮢ")),
                bstack11l111_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᮣ"): int(os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᮤ")) or bstack11l111_opy_ (u"ࠢ࠲ࠤᮥ")),
                bstack11l111_opy_ (u"ࠣࡪࡲࡷࡹࡏ࡮ࡧࡱࠥᮦ"): get_host_info(),
            }
            logger.debug(bstack11l111_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡶࡡࡺ࡮ࡲࡥࡩࡀࠠࡼࡿࠥᮧ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll11l1l1l_opy_(bstack11ll11ll111_opy_, payload)
            if response:
                logger.debug(bstack11l111_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡄࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡯࡯ࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᮨ").format(response))
                return response
            else:
                logger.error(bstack11l111_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᮩ").format(bstack11l11111l11_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l111_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇࠤࢀࢃ࠺ࠡࡽࢀ᮪ࠦ").format(bstack11l11111l11_opy_, e))
            return None
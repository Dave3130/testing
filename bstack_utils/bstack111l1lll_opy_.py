# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1l1l1ll111_opy_
from bstack_utils.constants import bstack11ll1lll1l_opy_, bstack11l1l11lll1_opy_
from bstack_utils.helper import bstack11lll11lll1_opy_, get_host_info
from bstack_utils.bstack11lll11ll1l_opy_ import bstack11lll11ll11_opy_
import json
import re
import sys
bstack111lllll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠤࡵࡩࡹࡸࡹࡕࡧࡶࡸࡸࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣᭅ")
bstack111lll1llll_opy_ = bstack1ll1ll1_opy_ (u"ࠥࡥࡧࡵࡲࡵࡄࡸ࡭ࡱࡪࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠤᭆ")
bstack11l1111l111_opy_ = bstack1ll1ll1_opy_ (u"ࠦࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࡉ࡭ࡷࡹࡴࠣᭇ")
bstack111llll1111_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡸࡥࡳࡷࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࡱࡿࡆࡢ࡫࡯ࡩࡩࠨᭈ")
bstack111llll11l1_opy_ = bstack1ll1ll1_opy_ (u"ࠨࡳ࡬࡫ࡳࡊࡱࡧ࡫ࡺࡣࡱࡨࡋࡧࡩ࡭ࡧࡧࠦᭉ")
bstack11l1111ll11_opy_ = bstack1ll1ll1_opy_ (u"ࠢࡳࡷࡱࡗࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࠦᭊ")
bstack11l1111l1ll_opy_ = {
    bstack111lllll11l_opy_,
    bstack111lll1llll_opy_,
    bstack11l1111l111_opy_,
    bstack111llll1111_opy_,
    bstack111llll11l1_opy_,
    bstack11l1111ll11_opy_
}
bstack111llllll11_opy_ = {bstack1ll1ll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨᭋ")}
logger = bstack1l1l1ll111_opy_.get_logger(__name__, bstack11ll1lll1l_opy_)
class bstack111llll1l1l_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l111l111l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1llll111l_opy_:
    _1ll1ll1lll1_opy_ = None
    def __init__(self, config):
        self.bstack111lll11l1l_opy_ = False
        self.bstack111lll1ll11_opy_ = False
        self.bstack11l111ll1l1_opy_ = False
        self.bstack11l11111l11_opy_ = False
        self.bstack111lllll1ll_opy_ = None
        self.bstack11l111l1ll1_opy_ = bstack111llll1l1l_opy_()
        self.bstack11l11111lll_opy_ = None
        opts = config.get(bstack1ll1ll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᭌ"), {})
        self.bstack11l11111l1l_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡊࡔࡖࠨ᭍"), bstack1ll1ll1_opy_ (u"ࠦࠧ᭎"))
        self.bstack111lll1l111_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡃࡍࡋࠪ᭏"), bstack1ll1ll1_opy_ (u"ࠨࠢ᭐"))
        bstack111llll11ll_opy_ = opts.get(bstack11l1111ll11_opy_, {})
        bstack11l11111111_opy_ = None
        if bstack1ll1ll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ᭑") in bstack111llll11ll_opy_:
            bstack11l11111111_opy_ = bstack111llll11ll_opy_[bstack1ll1ll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ᭒")]
            if bstack11l11111111_opy_ is None:
                bstack11l11111111_opy_ = []
        self.__11l11111ll1_opy_(
            bstack111llll11ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪ᭓"), False),
            bstack111llll11ll_opy_.get(bstack1ll1ll1_opy_ (u"ࠪࡱࡴࡪࡥࠨ᭔"), bstack1ll1ll1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ᭕")),
            bstack11l11111111_opy_
        )
        self.__11l1111ll1l_opy_(opts.get(bstack11l1111l111_opy_, False))
        self.__11l1111l1l1_opy_(opts.get(bstack111llll1111_opy_, False))
        self.__111llll1ll1_opy_(opts.get(bstack111llll11l1_opy_, False))
    @classmethod
    def bstack1llllllll_opy_(cls, config=None):
        if cls._1ll1ll1lll1_opy_ is None and config is not None:
            cls._1ll1ll1lll1_opy_ = bstack1llll111l_opy_(config)
        return cls._1ll1ll1lll1_opy_
    @staticmethod
    def bstack11l1l11l_opy_(config: dict) -> bool:
        bstack11l1111lll1_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭖"), {}).get(bstack111lllll11l_opy_, {})
        return bstack11l1111lll1_opy_.get(bstack1ll1ll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᭗"), False)
    @staticmethod
    def bstack111111l1_opy_(config: dict) -> int:
        bstack11l1111lll1_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭘"), {}).get(bstack111lllll11l_opy_, {})
        retries = 0
        if bstack1llll111l_opy_.bstack11l1l11l_opy_(config):
            retries = bstack11l1111lll1_opy_.get(bstack1ll1ll1_opy_ (u"ࠨ࡯ࡤࡼࡗ࡫ࡴࡳ࡫ࡨࡷࠬ᭙"), 1)
        return retries
    @staticmethod
    def bstack1ll1lll11l_opy_(config: dict) -> dict:
        bstack111llll1lll_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭚"), {})
        return {
            key: value for key, value in bstack111llll1lll_opy_.items() if key in bstack11l1111l1ll_opy_
        }
    @staticmethod
    def bstack111lllll1l1_opy_():
        bstack1ll1ll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭛")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧ᭜").format(os.getenv(bstack1ll1ll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᭝")))))
    @staticmethod
    def bstack11l111l1111_opy_(test_name: str):
        bstack1ll1ll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᭞")
        bstack111llll111l_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1ll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨ᭟").format(os.getenv(bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᭠"))))
        with open(bstack111llll111l_opy_, bstack1ll1ll1_opy_ (u"ࠩࡤࠫ᭡")) as file:
            file.write(bstack1ll1ll1_opy_ (u"ࠥࡿࢂࡢ࡮ࠣ᭢").format(test_name))
    @staticmethod
    def bstack11l111ll111_opy_(framework: str) -> bool:
       return framework.lower() in bstack111llllll11_opy_
    @staticmethod
    def bstack11ll111l111_opy_(config: dict) -> bool:
        bstack111lll11l11_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭣"), {}).get(bstack111lll1llll_opy_, {})
        return bstack111lll11l11_opy_.get(bstack1ll1ll1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭤"), False)
    @staticmethod
    def bstack11l1lllll1l_opy_(config: dict, bstack11ll1111l1l_opy_: int = 0) -> int:
        bstack1ll1ll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠭ࠢࡺ࡬࡮ࡩࡨࠡࡥࡤࡲࠥࡨࡥࠡࡣࡱࠤࡦࡨࡳࡰ࡮ࡸࡸࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡳࠢࡤࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡪ࡮࡭ࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡲࡸࡦࡲ࡟ࡵࡧࡶࡸࡸࠦࠨࡪࡰࡷ࠭࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤ࠭ࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭥")
        bstack111lll11l11_opy_ = config.get(bstack1ll1ll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭦"), {}).get(bstack1ll1ll1_opy_ (u"ࠨࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠧ᭧"), {})
        bstack11l111ll11l_opy_ = 0
        bstack11l1111111l_opy_ = 0
        if bstack1llll111l_opy_.bstack11ll111l111_opy_(config):
            bstack11l1111111l_opy_ = bstack111lll11l11_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹࠧ᭨"), 5)
            if isinstance(bstack11l1111111l_opy_, str) and bstack11l1111111l_opy_.endswith(bstack1ll1ll1_opy_ (u"ࠪࠩࠬ᭩")):
                try:
                    percentage = int(bstack11l1111111l_opy_.strip(bstack1ll1ll1_opy_ (u"ࠫࠪ࠭᭪")))
                    if bstack11ll1111l1l_opy_ > 0:
                        bstack11l111ll11l_opy_ = math.ceil((percentage * bstack11ll1111l1l_opy_) / 100)
                    else:
                        raise ValueError(bstack1ll1ll1_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡱࡺࡹࡴࠡࡤࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵ࠱ࠦ᭫"))
                except ValueError as e:
                    raise ValueError(bstack1ll1ll1_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨࠤࡻࡧ࡬ࡶࡧࠣࡪࡴࡸࠠ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷ࠿ࠦࡻࡾࠤ᭬").format(bstack11l1111111l_opy_)) from e
            else:
                bstack11l111ll11l_opy_ = int(bstack11l1111111l_opy_)
        logger.info(bstack1ll1ll1_opy_ (u"ࠢࡎࡣࡻࠤ࡫ࡧࡩ࡭ࡷࡵࡩࡸࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡶࡩࡹࠦࡴࡰ࠼ࠣࡿࢂࠦࠨࡧࡴࡲࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡻࡾࠫࠥ᭭").format(bstack11l111ll11l_opy_, bstack11l1111111l_opy_))
        return bstack11l111ll11l_opy_
    def bstack11l111l11ll_opy_(self):
        return self.bstack11l11111l11_opy_
    def bstack111lll11lll_opy_(self):
        return self.bstack111lllll1ll_opy_
    def bstack11l1111l11l_opy_(self):
        return self.bstack11l11111lll_opy_
    def __11l11111ll1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l11111l11_opy_ = bool(enabled)
            if mode not in [bstack1ll1ll1_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭮"), bstack1ll1ll1_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡓࡳࡲࡹࠨ᭯")]:
                logger.warning(bstack1ll1ll1_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࡭ࡰࡦࡨࠤࠬࢁࡽࠨࠢࡳࡶࡴࡼࡩࡥࡧࡧ࠲ࠥࡊࡥࡧࡣࡸࡰࡹ࡯࡮ࡨࠢࡷࡳࠥ࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭࠮ࠣ᭰").format(mode))
                mode = bstack1ll1ll1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ᭱")
            self.bstack111lllll1ll_opy_ = mode
            if source is None:
                self.bstack11l11111lll_opy_ = None
            elif isinstance(source, list):
                self.bstack11l11111lll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1ll1ll1_opy_ (u"ࠬ࠴ࡪࡴࡱࡱࠫ᭲")):
                self.bstack11l11111lll_opy_ = self._111lll1l1ll_opy_(source)
            self.__111lllllll1_opy_()
        except Exception as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡ࠯ࠣࡩࡳࡧࡢ࡭ࡧࡧ࠾ࠥࢁࡽ࠭ࠢࡰࡳࡩ࡫࠺ࠡࡽࢀ࠰ࠥࡹ࡯ࡶࡴࡦࡩ࠿ࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨ᭳").format(enabled, mode, source, e))
    def bstack11l111111l1_opy_(self):
        return self.bstack111lll11l1l_opy_
    def __11l1111ll1l_opy_(self, value):
        self.bstack111lll11l1l_opy_ = bool(value)
        self.__111lllllll1_opy_()
    def bstack111lll1lll1_opy_(self):
        return self.bstack111lll1ll11_opy_
    def __11l1111l1l1_opy_(self, value):
        self.bstack111lll1ll11_opy_ = bool(value)
        self.__111lllllll1_opy_()
    def bstack11l111111ll_opy_(self):
        return self.bstack11l111ll1l1_opy_
    def __111llll1ll1_opy_(self, value):
        self.bstack11l111ll1l1_opy_ = bool(value)
        self.__111lllllll1_opy_()
    def __111lllllll1_opy_(self):
        if self.bstack11l11111l11_opy_:
            self.bstack111lll11l1l_opy_ = False
            self.bstack111lll1ll11_opy_ = False
            self.bstack11l111ll1l1_opy_ = False
            self.bstack11l111l1ll1_opy_.enable(bstack11l1111ll11_opy_)
        elif self.bstack111lll11l1l_opy_:
            self.bstack111lll1ll11_opy_ = False
            self.bstack11l111ll1l1_opy_ = False
            self.bstack11l11111l11_opy_ = False
            self.bstack11l111l1ll1_opy_.enable(bstack11l1111l111_opy_)
        elif self.bstack111lll1ll11_opy_:
            self.bstack111lll11l1l_opy_ = False
            self.bstack11l111ll1l1_opy_ = False
            self.bstack11l11111l11_opy_ = False
            self.bstack11l111l1ll1_opy_.enable(bstack111llll1111_opy_)
        elif self.bstack11l111ll1l1_opy_:
            self.bstack111lll11l1l_opy_ = False
            self.bstack111lll1ll11_opy_ = False
            self.bstack11l11111l11_opy_ = False
            self.bstack11l111l1ll1_opy_.enable(bstack111llll11l1_opy_)
        else:
            self.bstack11l111l1ll1_opy_.disable()
    def bstack1lllll1ll_opy_(self):
        return self.bstack11l111l1ll1_opy_.bstack11l111l111l_opy_()
    def bstack1lll11ll11_opy_(self):
        if self.bstack11l111l1ll1_opy_.bstack11l111l111l_opy_():
            return self.bstack11l111l1ll1_opy_.get_name()
        return None
    def _111lll1l1ll_opy_(self, bstack11l111ll1ll_opy_):
        bstack1ll1ll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡵࡲࡹࡷࡩࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠦࡡ࡯ࡦࠣࡪࡴࡸ࡭ࡢࡶࠣ࡭ࡹࠦࡦࡰࡴࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸࡵࡵࡳࡥࡨࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠠࠩࡵࡷࡶ࠮ࡀࠠࡑࡣࡷ࡬ࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡓࡐࡐࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡈࡲࡶࡲࡧࡴࡵࡧࡧࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡸࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭴")
        if not os.path.isfile(bstack11l111ll1ll_opy_):
            logger.error(bstack1ll1ll1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠨ᭵").format(bstack11l111ll1ll_opy_))
            return []
        data = None
        try:
            with open(bstack11l111ll1ll_opy_, bstack1ll1ll1_opy_ (u"ࠤࡵࠦ᭶")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡎࡘࡕࡎࠡࡨࡵࡳࡲࠦࡳࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨ᭷").format(bstack11l111ll1ll_opy_, e))
            return []
        _11l1111llll_opy_ = None
        _111lll11ll1_opy_ = None
        def _11l111l1l1l_opy_():
            bstack11l111l1lll_opy_ = {}
            bstack11l111l1l11_opy_ = {}
            try:
                if self.bstack11l11111l1l_opy_.startswith(bstack1ll1ll1_opy_ (u"ࠫࢀ࠭᭸")) and self.bstack11l11111l1l_opy_.endswith(bstack1ll1ll1_opy_ (u"ࠬࢃࠧ᭹")):
                    bstack11l111l1lll_opy_ = json.loads(self.bstack11l11111l1l_opy_)
                else:
                    bstack11l111l1lll_opy_ = dict(item.split(bstack1ll1ll1_opy_ (u"࠭࠺ࠨ᭺")) for item in self.bstack11l11111l1l_opy_.split(bstack1ll1ll1_opy_ (u"ࠧ࠭ࠩ᭻")) if bstack1ll1ll1_opy_ (u"ࠨ࠼ࠪ᭼") in item) if self.bstack11l11111l1l_opy_ else {}
                if self.bstack111lll1l111_opy_.startswith(bstack1ll1ll1_opy_ (u"ࠩࡾࠫ᭽")) and self.bstack111lll1l111_opy_.endswith(bstack1ll1ll1_opy_ (u"ࠪࢁࠬ᭾")):
                    bstack11l111l1l11_opy_ = json.loads(self.bstack111lll1l111_opy_)
                else:
                    bstack11l111l1l11_opy_ = dict(item.split(bstack1ll1ll1_opy_ (u"ࠫ࠿࠭᭿")) for item in self.bstack111lll1l111_opy_.split(bstack1ll1ll1_opy_ (u"ࠬ࠲ࠧᮀ")) if bstack1ll1ll1_opy_ (u"࠭࠺ࠨᮁ") in item) if self.bstack111lll1l111_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1ll1ll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡧࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵ࠽ࠤࢀࢃࠢᮂ").format(e))
            logger.debug(bstack1ll1ll1_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡰࡥࡵࡶࡩ࡯ࡩࡶࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻࡀࠠࡼࡿ࠯ࠤࡈࡒࡉ࠻ࠢࡾࢁࠧᮃ").format(bstack11l111l1lll_opy_, bstack11l111l1l11_opy_))
            return bstack11l111l1lll_opy_, bstack11l111l1l11_opy_
        if _11l1111llll_opy_ is None or _111lll11ll1_opy_ is None:
            _11l1111llll_opy_, _111lll11ll1_opy_ = _11l111l1l1l_opy_()
        def bstack111lllll111_opy_(name, bstack111llllll1l_opy_):
            if name in _111lll11ll1_opy_:
                return _111lll11ll1_opy_[name]
            if name in _11l1111llll_opy_:
                return _11l1111llll_opy_[name]
            if bstack111llllll1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮄ")):
                return bstack111llllll1l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮅ")]
            return None
        if isinstance(data, dict):
            bstack111llll1l11_opy_ = []
            bstack111llllllll_opy_ = re.compile(bstack1ll1ll1_opy_ (u"ࡶࠬࡤ࡛ࡂ࠯࡝࠴࠲࠿࡟࡞࠭ࠧࠫᮆ"))
            for name, bstack111llllll1l_opy_ in data.items():
                if not isinstance(bstack111llllll1l_opy_, dict):
                    continue
                if not bstack111llllll1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠬࡻࡲ࡭ࠩᮇ")):
                    logger.warning(bstack1ll1ll1_opy_ (u"ࠨࡒࡦࡲࡲࡷ࡮ࡺ࡯ࡳࡻ࡙ࠣࡗࡒࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮈ").format(name, bstack111llllll1l_opy_))
                    continue
                if not bstack111llllllll_opy_.match(name):
                    logger.warning(bstack1ll1ll1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡬࡯ࡳࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮉ").format(name, bstack111llllll1l_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1ll1ll1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࠭ࡻࡾࠩࠣࡱࡺࡹࡴࠡࡪࡤࡺࡪࠦࡡࠡ࡮ࡨࡲ࡬ࡺࡨࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢ࠴ࠤࡦࡴࡤࠡ࠵࠳ࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳ࠯ࠤᮊ").format(name))
                    continue
                bstack111llllll1l_opy_ = bstack111llllll1l_opy_.copy()
                bstack111llllll1l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᮋ")] = name
                bstack111llllll1l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮌ")] = bstack111lllll111_opy_(name, bstack111llllll1l_opy_)
                if not bstack111llllll1l_opy_.get(bstack1ll1ll1_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮍ")):
                    logger.warning(bstack1ll1ll1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡮ࡰࡶࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡩࡩࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮎ").format(name, bstack111llllll1l_opy_))
                    continue
                if bstack111llllll1l_opy_.get(bstack1ll1ll1_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪᮏ")) and bstack111llllll1l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮐ")] == bstack111llllll1l_opy_[bstack1ll1ll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮑ")]:
                    logger.warning(bstack1ll1ll1_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡥࡳࡪࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡶ࡫ࡩࠥࡹࡡ࡮ࡧࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮒ").format(name, bstack111llllll1l_opy_))
                    continue
                bstack111llll1l11_opy_.append(bstack111llllll1l_opy_)
            return bstack111llll1l11_opy_
        return data
    def bstack111lll1l1l1_opy_(self):
        data = {
            bstack1ll1ll1_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᮓ"): {
                bstack1ll1ll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮔ"): self.bstack11l111l11ll_opy_(),
                bstack1ll1ll1_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᮕ"): self.bstack111lll11lll_opy_(),
                bstack1ll1ll1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᮖ"): self.bstack11l1111l11l_opy_()
            }
        }
        return data
    def bstack111lll1ll1l_opy_(self, config):
        bstack111lll1l11l_opy_ = {}
        bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᮗ")] = {
            bstack1ll1ll1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮘ"): self.bstack11l111l11ll_opy_(),
            bstack1ll1ll1_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮙ"): self.bstack111lll11lll_opy_()
        }
        bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩ࠭ᮚ")] = {
            bstack1ll1ll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮛ"): self.bstack111lll1lll1_opy_()
        }
        bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠬࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩࡥࡦࡪࡴࡶࡸࠬᮜ")] = {
            bstack1ll1ll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮝ"): self.bstack11l111111l1_opy_()
        }
        bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡤ࡬ࡡࡪ࡮࡬ࡲ࡬ࡥࡡ࡯ࡦࡢࡪࡱࡧ࡫ࡺࠩᮞ")] = {
            bstack1ll1ll1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮟ"): self.bstack11l111111ll_opy_()
        }
        if self.bstack11l1l11l_opy_(config):
            bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠩࡵࡩࡹࡸࡹࡠࡶࡨࡷࡹࡹ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᮠ")] = {
                bstack1ll1ll1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮡ"): True,
                bstack1ll1ll1_opy_ (u"ࠫࡲࡧࡸࡠࡴࡨࡸࡷ࡯ࡥࡴࠩᮢ"): self.bstack111111l1_opy_(config)
            }
        if self.bstack11ll111l111_opy_(config):
            bstack111lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠬࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧᮣ")] = {
                bstack1ll1ll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮤ"): True,
                bstack1ll1ll1_opy_ (u"ࠧ࡮ࡣࡻࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡸ࠭ᮥ"): self.bstack11l1lllll1l_opy_(config)
            }
        return bstack111lll1l11l_opy_
    def bstack111l1l111l_opy_(self, config):
        bstack1ll1ll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉ࡯࡭࡮ࡨࡧࡹࡹࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡧࡿࠠ࡮ࡣ࡮࡭ࡳ࡭ࠠࡢࠢࡦࡥࡱࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡖࡗࡌࡈࠥࡵࡦࠡࡶ࡫ࡩࠥࡨࡵࡪ࡮ࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮦ")
        if not (config.get(bstack1ll1ll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᮧ"), None) in bstack11l1l11lll1_opy_ and self.bstack11l111l11ll_opy_()):
            return None
        bstack11l111l11l1_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᮨ"), None)
        logger.debug(bstack1ll1ll1_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡆࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᮩ").format(bstack11l111l11l1_opy_))
        try:
            bstack11ll11ll11l_opy_ = bstack1ll1ll1_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣ᮪ࠥ").format(bstack11l111l11l1_opy_)
            payload = {
                bstack1ll1ll1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨ᮫ࠦ"): config.get(bstack1ll1ll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᮬ"), bstack1ll1ll1_opy_ (u"ࠨࠩᮭ")),
                bstack1ll1ll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᮮ"): config.get(bstack1ll1ll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᮯ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1ll1ll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ᮰"): os.environ.get(bstack1ll1ll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦ᮱"), bstack1ll1ll1_opy_ (u"ࠨࠢ᮲")),
                bstack1ll1ll1_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥ᮳"): int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦ᮴")) or bstack1ll1ll1_opy_ (u"ࠤ࠳ࠦ᮵")),
                bstack1ll1ll1_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢ᮶"): int(os.environ.get(bstack1ll1ll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨ᮷")) or bstack1ll1ll1_opy_ (u"ࠧ࠷ࠢ᮸")),
                bstack1ll1ll1_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣ᮹"): get_host_info(),
            }
            logger.debug(bstack1ll1ll1_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡴࡦࡿ࡬ࡰࡣࡧ࠾ࠥࢁࡽࠣᮺ").format(payload))
            response = bstack11lll11ll11_opy_.bstack11ll11ll111_opy_(bstack11ll11ll11l_opy_, payload)
            if response:
                logger.debug(bstack1ll1ll1_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡂࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᮻ").format(response))
                return response
            else:
                logger.error(bstack1ll1ll1_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨᮼ").format(bstack11l111l11l1_opy_))
                return None
        except Exception as e:
            logger.error(bstack1ll1ll1_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅࠢࡾࢁ࠿ࠦࡻࡾࠤᮽ").format(bstack11l111l11l1_opy_, e))
            return None
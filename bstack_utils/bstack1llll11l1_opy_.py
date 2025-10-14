# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1ll1111ll_opy_
from bstack_utils.constants import bstack1l11lllll1_opy_, bstack11l1l1111ll_opy_
from bstack_utils.helper import bstack11lll1111ll_opy_, get_host_info
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lllll1_opy_
import json
import re
import sys
bstack11l111l1ll1_opy_ = bstack11l1l11_opy_ (u"ࠨࡲࡦࡶࡵࡽ࡙࡫ࡳࡵࡵࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧᬻ")
bstack11l1111l11l_opy_ = bstack11l1l11_opy_ (u"ࠢࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨᬼ")
bstack11l1111lll1_opy_ = bstack11l1l11_opy_ (u"ࠣࡴࡸࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡇࡣ࡬ࡰࡪࡪࡆࡪࡴࡶࡸࠧᬽ")
bstack111lll1l1ll_opy_ = bstack11l1l11_opy_ (u"ࠤࡵࡩࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࠥᬾ")
bstack111llll1lll_opy_ = bstack11l1l11_opy_ (u"ࠥࡷࡰ࡯ࡰࡇ࡮ࡤ࡯ࡾࡧ࡮ࡥࡈࡤ࡭ࡱ࡫ࡤࠣᬿ")
bstack11l111l1l1l_opy_ = bstack11l1l11_opy_ (u"ࠦࡷࡻ࡮ࡔ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠣᭀ")
bstack111lllll11l_opy_ = {
    bstack11l111l1ll1_opy_,
    bstack11l1111l11l_opy_,
    bstack11l1111lll1_opy_,
    bstack111lll1l1ll_opy_,
    bstack111llll1lll_opy_,
    bstack11l111l1l1l_opy_
}
bstack11l1111ll1l_opy_ = {bstack11l1l11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᭁ")}
logger = bstack1ll1111ll_opy_.get_logger(__name__, bstack1l11lllll1_opy_)
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
    def bstack11l11111ll1_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack11l1l111_opy_:
    _1ll1ll1l111_opy_ = None
    def __init__(self, config):
        self.bstack111lll1l111_opy_ = False
        self.bstack111lllll1l1_opy_ = False
        self.bstack111lll11ll1_opy_ = False
        self.bstack111llllll11_opy_ = False
        self.bstack111lll1llll_opy_ = None
        self.bstack11l1111l111_opy_ = bstack11l111l1l11_opy_()
        self.bstack111lllll111_opy_ = None
        opts = config.get(bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᭂ"), {})
        self.bstack11l11111111_opy_ = config.get(bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡇࡑ࡚ࠬᭃ"), bstack11l1l11_opy_ (u"ࠣࠤ᭄"))
        self.bstack111lll1lll1_opy_ = config.get(bstack11l1l11_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠧᭅ"), bstack11l1l11_opy_ (u"ࠥࠦᭆ"))
        bstack11l111l1lll_opy_ = opts.get(bstack11l111l1l1l_opy_, {})
        bstack11l1111llll_opy_ = None
        if bstack11l1l11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᭇ") in bstack11l111l1lll_opy_:
            bstack11l1111llll_opy_ = bstack11l111l1lll_opy_[bstack11l1l11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᭈ")]
            if bstack11l1111llll_opy_ is None:
                bstack11l1111llll_opy_ = []
        self.__11l111l11l1_opy_(
            bstack11l111l1lll_opy_.get(bstack11l1l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᭉ"), False),
            bstack11l111l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᭊ"), bstack11l1l11_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᭋ")),
            bstack11l1111llll_opy_
        )
        self.__11l1111111l_opy_(opts.get(bstack11l1111lll1_opy_, False))
        self.__111lll11l1l_opy_(opts.get(bstack111lll1l1ll_opy_, False))
        self.__11l1111l1l1_opy_(opts.get(bstack111llll1lll_opy_, False))
    @classmethod
    def bstack1111lll1_opy_(cls, config=None):
        if cls._1ll1ll1l111_opy_ is None and config is not None:
            cls._1ll1ll1l111_opy_ = bstack11l1l111_opy_(config)
        return cls._1ll1ll1l111_opy_
    @staticmethod
    def bstack1lll1l1ll_opy_(config: dict) -> bool:
        bstack111lll1l1l1_opy_ = config.get(bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᭌ"), {}).get(bstack11l111l1ll1_opy_, {})
        return bstack111lll1l1l1_opy_.get(bstack11l1l11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᭍"), False)
    @staticmethod
    def bstack1lllll111_opy_(config: dict) -> int:
        bstack111lll1l1l1_opy_ = config.get(bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭎"), {}).get(bstack11l111l1ll1_opy_, {})
        retries = 0
        if bstack11l1l111_opy_.bstack1lll1l1ll_opy_(config):
            retries = bstack111lll1l1l1_opy_.get(bstack11l1l11_opy_ (u"ࠬࡳࡡࡹࡔࡨࡸࡷ࡯ࡥࡴࠩ᭏"), 1)
        return retries
    @staticmethod
    def bstack11lll1111l_opy_(config: dict) -> dict:
        bstack111llll111l_opy_ = config.get(bstack11l1l11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭐"), {})
        return {
            key: value for key, value in bstack111llll111l_opy_.items() if key in bstack111lllll11l_opy_
        }
    @staticmethod
    def bstack11l111ll11l_opy_():
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭑")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤ᭒").format(os.getenv(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ᭓")))))
    @staticmethod
    def bstack111lll1ll1l_opy_(test_name: str):
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭔")
        bstack111lll111ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥ᭕").format(os.getenv(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᭖"))))
        with open(bstack111lll111ll_opy_, bstack11l1l11_opy_ (u"࠭ࡡࠨ᭗")) as file:
            file.write(bstack11l1l11_opy_ (u"ࠢࡼࡿ࡟ࡲࠧ᭘").format(test_name))
    @staticmethod
    def bstack111lll111l1_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l1111ll1l_opy_
    @staticmethod
    def bstack11ll11111l1_opy_(config: dict) -> bool:
        bstack111llll1l1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭙"), {}).get(bstack11l1111l11l_opy_, {})
        return bstack111llll1l1l_opy_.get(bstack11l1l11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪ᭚"), False)
    @staticmethod
    def bstack11l1llll111_opy_(config: dict, bstack11ll111111l_opy_: int = 0) -> int:
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠱ࠦࡷࡩ࡫ࡦ࡬ࠥࡩࡡ࡯ࠢࡥࡩࠥࡧ࡮ࠡࡣࡥࡷࡴࡲࡵࡵࡧࠣࡲࡺࡳࡢࡦࡴࠣࡳࡷࠦࡡࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࠭ࡪࡩࡤࡶࠬ࠾࡚ࠥࡨࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺ࡯ࡵࡣ࡯ࡣࡹ࡫ࡳࡵࡵࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࠪࡵࡩࡶࡻࡩࡳࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳࠪ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭛")
        bstack111llll1l1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭜"), {}).get(bstack11l1l11_opy_ (u"ࠬࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠫ᭝"), {})
        bstack11l111ll111_opy_ = 0
        bstack11l111111l1_opy_ = 0
        if bstack11l1l111_opy_.bstack11ll11111l1_opy_(config):
            bstack11l111111l1_opy_ = bstack111llll1l1l_opy_.get(bstack11l1l11_opy_ (u"࠭࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶࠫ᭞"), 5)
            if isinstance(bstack11l111111l1_opy_, str) and bstack11l111111l1_opy_.endswith(bstack11l1l11_opy_ (u"ࠧࠦࠩ᭟")):
                try:
                    percentage = int(bstack11l111111l1_opy_.strip(bstack11l1l11_opy_ (u"ࠨࠧࠪ᭠")))
                    if bstack11ll111111l_opy_ > 0:
                        bstack11l111ll111_opy_ = math.ceil((percentage * bstack11ll111111l_opy_) / 100)
                    else:
                        raise ValueError(bstack11l1l11_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨ࠱ࡧࡧࡳࡦࡦࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࡹ࠮ࠣ᭡"))
                except ValueError as e:
                    raise ValueError(bstack11l1l11_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥࠡࡸࡤࡰࡺ࡫ࠠࡧࡱࡵࠤࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴ࠼ࠣࡿࢂࠨ᭢").format(bstack11l111111l1_opy_)) from e
            else:
                bstack11l111ll111_opy_ = int(bstack11l111111l1_opy_)
        logger.info(bstack11l1l11_opy_ (u"ࠦࡒࡧࡸࠡࡨࡤ࡭ࡱࡻࡲࡦࡵࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡳࡦࡶࠣࡸࡴࡀࠠࡼࡿࠣࠬ࡫ࡸ࡯࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠯ࠢ᭣").format(bstack11l111ll111_opy_, bstack11l111111l1_opy_))
        return bstack11l111ll111_opy_
    def bstack11l1111ll11_opy_(self):
        return self.bstack111llllll11_opy_
    def bstack11l1111l1ll_opy_(self):
        return self.bstack111lll1llll_opy_
    def bstack111llll1111_opy_(self):
        return self.bstack111lllll111_opy_
    def __11l111l11l1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llllll11_opy_ = bool(enabled)
            if mode not in [bstack11l1l11_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ᭤"), bstack11l1l11_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡐࡰ࡯ࡽࠬ᭥")]:
                logger.warning(bstack11l1l11_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡱࡴࡪࡥࠡࠩࡾࢁࠬࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡴࡰࠢࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ࠲ࠧ᭦").format(mode))
                mode = bstack11l1l11_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭧")
            self.bstack111lll1llll_opy_ = mode
            if source is None:
                self.bstack111lllll111_opy_ = None
            elif isinstance(source, list):
                self.bstack111lllll111_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l1l11_opy_ (u"ࠩ࠱࡮ࡸࡵ࡮ࠨ᭨")):
                self.bstack111lllll111_opy_ = self._111lll1ll11_opy_(source)
            self.__111lll11lll_opy_()
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࠳ࠠࡦࡰࡤࡦࡱ࡫ࡤ࠻ࠢࡾࢁ࠱ࠦ࡭ࡰࡦࡨ࠾ࠥࢁࡽ࠭ࠢࡶࡳࡺࡸࡣࡦ࠼ࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥ᭩").format(enabled, mode, source, e))
    def bstack11l111l1111_opy_(self):
        return self.bstack111lll1l111_opy_
    def __11l1111111l_opy_(self, value):
        self.bstack111lll1l111_opy_ = bool(value)
        self.__111lll11lll_opy_()
    def bstack111llll11l1_opy_(self):
        return self.bstack111lllll1l1_opy_
    def __111lll11l1l_opy_(self, value):
        self.bstack111lllll1l1_opy_ = bool(value)
        self.__111lll11lll_opy_()
    def bstack11l111l11ll_opy_(self):
        return self.bstack111lll11ll1_opy_
    def __11l1111l1l1_opy_(self, value):
        self.bstack111lll11ll1_opy_ = bool(value)
        self.__111lll11lll_opy_()
    def __111lll11lll_opy_(self):
        if self.bstack111llllll11_opy_:
            self.bstack111lll1l111_opy_ = False
            self.bstack111lllll1l1_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack11l111l1l1l_opy_)
        elif self.bstack111lll1l111_opy_:
            self.bstack111lllll1l1_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack111llllll11_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack11l1111lll1_opy_)
        elif self.bstack111lllll1l1_opy_:
            self.bstack111lll1l111_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack111llllll11_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111lll1l1ll_opy_)
        elif self.bstack111lll11ll1_opy_:
            self.bstack111lll1l111_opy_ = False
            self.bstack111lllll1l1_opy_ = False
            self.bstack111llllll11_opy_ = False
            self.bstack11l1111l111_opy_.enable(bstack111llll1lll_opy_)
        else:
            self.bstack11l1111l111_opy_.disable()
    def bstack1lllll11l_opy_(self):
        return self.bstack11l1111l111_opy_.bstack11l11111ll1_opy_()
    def bstack111l11l1l1_opy_(self):
        if self.bstack11l1111l111_opy_.bstack11l11111ll1_opy_():
            return self.bstack11l1111l111_opy_.get_name()
        return None
    def _111lll1ll11_opy_(self, bstack111lll1l11l_opy_):
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡹ࡯ࡶࡴࡦࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠣࡥࡳࡪࠠࡧࡱࡵࡱࡦࡺࠠࡪࡶࠣࡪࡴࡸࠠࡴ࡯ࡤࡶࡹࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡲࡹࡷࡩࡥࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡕࡧࡴࡩࠢࡷࡳࠥࡺࡨࡦࠢࡍࡗࡔࡔࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡌ࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡵࡩࡵࡵࡳࡪࡶࡲࡶࡾࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭪")
        if not os.path.isfile(bstack111lll1l11l_opy_):
            logger.error(bstack11l1l11_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠥ᭫").format(bstack111lll1l11l_opy_))
            return []
        data = None
        try:
            with open(bstack111lll1l11l_opy_, bstack11l1l11_opy_ (u"ࠨࡲ᭬ࠣ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡋࡕࡒࡒࠥ࡬ࡲࡰ࡯ࠣࡷࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥ᭭").format(bstack111lll1l11l_opy_, e))
            return []
        _11l11111l1l_opy_ = None
        _111llllllll_opy_ = None
        def _11l11111l11_opy_():
            bstack111llll1ll1_opy_ = {}
            bstack111llll1l11_opy_ = {}
            try:
                if self.bstack11l11111111_opy_.startswith(bstack11l1l11_opy_ (u"ࠨࡽࠪ᭮")) and self.bstack11l11111111_opy_.endswith(bstack11l1l11_opy_ (u"ࠩࢀࠫ᭯")):
                    bstack111llll1ll1_opy_ = json.loads(self.bstack11l11111111_opy_)
                else:
                    bstack111llll1ll1_opy_ = dict(item.split(bstack11l1l11_opy_ (u"ࠪ࠾ࠬ᭰")) for item in self.bstack11l11111111_opy_.split(bstack11l1l11_opy_ (u"ࠫ࠱࠭᭱")) if bstack11l1l11_opy_ (u"ࠬࡀࠧ᭲") in item) if self.bstack11l11111111_opy_ else {}
                if self.bstack111lll1lll1_opy_.startswith(bstack11l1l11_opy_ (u"࠭ࡻࠨ᭳")) and self.bstack111lll1lll1_opy_.endswith(bstack11l1l11_opy_ (u"ࠧࡾࠩ᭴")):
                    bstack111llll1l11_opy_ = json.loads(self.bstack111lll1lll1_opy_)
                else:
                    bstack111llll1l11_opy_ = dict(item.split(bstack11l1l11_opy_ (u"ࠨ࠼ࠪ᭵")) for item in self.bstack111lll1lll1_opy_.split(bstack11l1l11_opy_ (u"ࠩ࠯ࠫ᭶")) if bstack11l1l11_opy_ (u"ࠪ࠾ࠬ᭷") in item) if self.bstack111lll1lll1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l1l11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡦࡸࡳࡪࡰࡪࠤ࡫࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡳࡡࡱࡲ࡬ࡲ࡬ࡹ࠺ࠡࡽࢀࠦ᭸").format(e))
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࠽ࠤࢀࢃࠬࠡࡅࡏࡍ࠿ࠦࡻࡾࠤ᭹").format(bstack111llll1ll1_opy_, bstack111llll1l11_opy_))
            return bstack111llll1ll1_opy_, bstack111llll1l11_opy_
        if _11l11111l1l_opy_ is None or _111llllllll_opy_ is None:
            _11l11111l1l_opy_, _111llllllll_opy_ = _11l11111l11_opy_()
        def bstack11l111l111l_opy_(name, bstack111lllllll1_opy_):
            if name in _111llllllll_opy_:
                return _111llllllll_opy_[name]
            if name in _11l11111l1l_opy_:
                return _11l11111l1l_opy_[name]
            if bstack111lllllll1_opy_.get(bstack11l1l11_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭᭺")):
                return bstack111lllllll1_opy_[bstack11l1l11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧ᭻")]
            return None
        if isinstance(data, dict):
            bstack11l111111ll_opy_ = []
            bstack111llllll1l_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡳࠩࡡ࡟ࡆ࠳࡚࠱࠯࠼ࡣࡢ࠱ࠤࠨ᭼"))
            for name, bstack111lllllll1_opy_ in data.items():
                if not isinstance(bstack111lllllll1_opy_, dict):
                    continue
                if not bstack111lllllll1_opy_.get(bstack11l1l11_opy_ (u"ࠩࡸࡶࡱ࠭᭽")):
                    logger.warning(bstack11l1l11_opy_ (u"ࠥࡖࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡖࡔࡏࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢ᭾").format(name, bstack111lllllll1_opy_))
                    continue
                if not bstack111llllll1l_opy_.match(name):
                    logger.warning(bstack11l1l11_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࡩࡳࡷࡳࡡࡵࠢࡩࡳࡷࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣ᭿").format(name, bstack111lllllll1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l1l11_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࠪࡿࢂ࠭ࠠ࡮ࡷࡶࡸࠥ࡮ࡡࡷࡧࠣࡥࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡨࡥࡵࡹࡨࡩࡳࠦ࠱ࠡࡣࡱࡨࠥ࠹࠰ࠡࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࡷ࠳ࠨᮀ").format(name))
                    continue
                bstack111lllllll1_opy_ = bstack111lllllll1_opy_.copy()
                bstack111lllllll1_opy_[bstack11l1l11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᮁ")] = name
                bstack111lllllll1_opy_[bstack11l1l11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮂ")] = bstack11l111l111l_opy_(name, bstack111lllllll1_opy_)
                if not bstack111lllllll1_opy_.get(bstack11l1l11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮃ")):
                    logger.warning(bstack11l1l11_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡲࡴࡺࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮄ").format(name, bstack111lllllll1_opy_))
                    continue
                if bstack111lllllll1_opy_.get(bstack11l1l11_opy_ (u"ࠪࡦࡦࡹࡥࡃࡴࡤࡲࡨ࡮ࠧᮅ")) and bstack111lllllll1_opy_[bstack11l1l11_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨᮆ")] == bstack111lllllll1_opy_[bstack11l1l11_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᮇ")]:
                    logger.warning(bstack11l1l11_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡢࡰࡧࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡺࡨࡦࠢࡶࡥࡲ࡫ࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮈ").format(name, bstack111lllllll1_opy_))
                    continue
                bstack11l111111ll_opy_.append(bstack111lllllll1_opy_)
            return bstack11l111111ll_opy_
        return data
    def bstack11l11111lll_opy_(self):
        data = {
            bstack11l1l11_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᮉ"): {
                bstack11l1l11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮊ"): self.bstack11l1111ll11_opy_(),
                bstack11l1l11_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮋ"): self.bstack11l1111l1ll_opy_(),
                bstack11l1l11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᮌ"): self.bstack111llll1111_opy_()
            }
        }
        return data
    def bstack111lllll1ll_opy_(self, config):
        bstack111llll11ll_opy_ = {}
        bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᮍ")] = {
            bstack11l1l11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮎ"): self.bstack11l1111ll11_opy_(),
            bstack11l1l11_opy_ (u"࠭࡭ࡰࡦࡨࠫᮏ"): self.bstack11l1111l1ll_opy_()
        }
        bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࠪᮐ")] = {
            bstack11l1l11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮑ"): self.bstack111llll11l1_opy_()
        }
        bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"ࠩࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࡢࡪ࡮ࡸࡳࡵࠩᮒ")] = {
            bstack11l1l11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮓ"): self.bstack11l111l1111_opy_()
        }
        bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"ࠫࡸࡱࡩࡱࡡࡩࡥ࡮ࡲࡩ࡯ࡩࡢࡥࡳࡪ࡟ࡧ࡮ࡤ࡯ࡾ࠭ᮔ")] = {
            bstack11l1l11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮕ"): self.bstack11l111l11ll_opy_()
        }
        if self.bstack1lll1l1ll_opy_(config):
            bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"࠭ࡲࡦࡶࡵࡽࡤࡺࡥࡴࡶࡶࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᮖ")] = {
                bstack11l1l11_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮗ"): True,
                bstack11l1l11_opy_ (u"ࠨ࡯ࡤࡼࡤࡸࡥࡵࡴ࡬ࡩࡸ࠭ᮘ"): self.bstack1lllll111_opy_(config)
            }
        if self.bstack11ll11111l1_opy_(config):
            bstack111llll11ll_opy_[bstack11l1l11_opy_ (u"ࠩࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᮙ")] = {
                bstack11l1l11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮚ"): True,
                bstack11l1l11_opy_ (u"ࠫࡲࡧࡸࡠࡨࡤ࡭ࡱࡻࡲࡦࡵࠪᮛ"): self.bstack11l1llll111_opy_(config)
            }
        return bstack111llll11ll_opy_
    def bstack11111lll1l_opy_(self, config):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡳࡱࡲࡥࡤࡶࡶࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡤࡼࠤࡲࡧ࡫ࡪࡰࡪࠤࡦࠦࡣࡢ࡮࡯ࠤࡹࡵࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤ࡚࡛ࡉࡅࠢࡲࡪࠥࡺࡨࡦࠢࡥࡹ࡮ࡲࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡪࡡࡵࡣࠣࡪࡴࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮜ")
        if not (config.get(bstack11l1l11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᮝ"), None) in bstack11l1l1111ll_opy_ and self.bstack11l1111ll11_opy_()):
            return None
        bstack111lll11l11_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᮞ"), None)
        logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡃࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᮟ").format(bstack111lll11l11_opy_))
        try:
            bstack11ll11l1ll1_opy_ = bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠢᮠ").format(bstack111lll11l11_opy_)
            payload = {
                bstack11l1l11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᮡ"): config.get(bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᮢ"), bstack11l1l11_opy_ (u"ࠬ࠭ᮣ")),
                bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᮤ"): config.get(bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᮥ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᮦ"): os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᮧ"), bstack11l1l11_opy_ (u"ࠥࠦᮨ")),
                bstack11l1l11_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᮩ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘ᮪ࠣ")) or bstack11l1l11_opy_ (u"ࠨ࠰᮫ࠣ")),
                bstack11l1l11_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᮬ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᮭ")) or bstack11l1l11_opy_ (u"ࠤ࠴ࠦᮮ")),
                bstack11l1l11_opy_ (u"ࠥ࡬ࡴࡹࡴࡊࡰࡩࡳࠧᮯ"): get_host_info(),
            }
            logger.debug(bstack11l1l11_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡱࡣࡼࡰࡴࡧࡤ࠻ࠢࡾࢁࠧ᮰").format(payload))
            response = bstack11ll1lllll1_opy_.bstack11ll11l11l1_opy_(bstack11ll11l1ll1_opy_, payload)
            if response:
                logger.debug(bstack11l1l11_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡆࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ᮱").format(response))
                return response
            else:
                logger.error(bstack11l1l11_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥ᮲").format(bstack111lll11l11_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࠦࡻࡾ࠼ࠣࡿࢂࠨ᮳").format(bstack111lll11l11_opy_, e))
            return None
# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1l1l1l1111_opy_
from bstack_utils.constants import bstack111lll1l1l_opy_, bstack11l1l11l1l1_opy_
from bstack_utils.helper import bstack11lll11l1l1_opy_, get_host_info
from bstack_utils.bstack11lll1111ll_opy_ import bstack11ll1llllll_opy_
import json
import re
import sys
bstack11l111111l1_opy_ = bstack1ll11_opy_ (u"ࠨࡲࡦࡶࡵࡽ࡙࡫ࡳࡵࡵࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧᭂ")
bstack111lll1ll1l_opy_ = bstack1ll11_opy_ (u"ࠢࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨᭃ")
bstack111lll11l1l_opy_ = bstack1ll11_opy_ (u"ࠣࡴࡸࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡇࡣ࡬ࡰࡪࡪࡆࡪࡴࡶࡸ᭄ࠧ")
bstack111lll1l1l1_opy_ = bstack1ll11_opy_ (u"ࠤࡵࡩࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࠥᭅ")
bstack111lllll1ll_opy_ = bstack1ll11_opy_ (u"ࠥࡷࡰ࡯ࡰࡇ࡮ࡤ࡯ࡾࡧ࡮ࡥࡈࡤ࡭ࡱ࡫ࡤࠣᭆ")
bstack11l111ll1ll_opy_ = bstack1ll11_opy_ (u"ࠦࡷࡻ࡮ࡔ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠣᭇ")
bstack111llll1l11_opy_ = {
    bstack11l111111l1_opy_,
    bstack111lll1ll1l_opy_,
    bstack111lll11l1l_opy_,
    bstack111lll1l1l1_opy_,
    bstack111lllll1ll_opy_,
    bstack11l111ll1ll_opy_
}
bstack11l111l111l_opy_ = {bstack1ll11_opy_ (u"ࠬࡶࡹࡵࡧࡶࡸࠬᭈ")}
logger = bstack1l1l1l1111_opy_.get_logger(__name__, bstack111lll1l1l_opy_)
class bstack111llll1lll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111lllll111_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack11l11l1l_opy_:
    _1ll1ll1l1l1_opy_ = None
    def __init__(self, config):
        self.bstack111llll111l_opy_ = False
        self.bstack11l1111111l_opy_ = False
        self.bstack111lll11ll1_opy_ = False
        self.bstack11l11111ll1_opy_ = False
        self.bstack111lll11lll_opy_ = None
        self.bstack111llllll1l_opy_ = bstack111llll1lll_opy_()
        self.bstack111lll1llll_opy_ = None
        opts = config.get(bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᭉ"), {})
        self.bstack11l111111ll_opy_ = config.get(bstack1ll11_opy_ (u"ࠧࡴ࡯ࡤࡶࡹ࡙ࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࡇࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࡥࡴࡇࡑ࡚ࠬᭊ"), bstack1ll11_opy_ (u"ࠣࠤᭋ"))
        self.bstack111lllll11l_opy_ = config.get(bstack1ll11_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡇࡑࡏࠧᭌ"), bstack1ll11_opy_ (u"ࠥࠦ᭍"))
        bstack11l1111l1l1_opy_ = opts.get(bstack11l111ll1ll_opy_, {})
        bstack11l11111l11_opy_ = None
        if bstack1ll11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ᭎") in bstack11l1111l1l1_opy_:
            bstack11l11111l11_opy_ = bstack11l1111l1l1_opy_[bstack1ll11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᭏")]
            if bstack11l11111l11_opy_ is None:
                bstack11l11111l11_opy_ = []
        self.__11l111l1l11_opy_(
            bstack11l1111l1l1_opy_.get(bstack1ll11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᭐"), False),
            bstack11l1111l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧ࡮ࡱࡧࡩࠬ᭑"), bstack1ll11_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭒")),
            bstack11l11111l11_opy_
        )
        self.__111llllllll_opy_(opts.get(bstack111lll11l1l_opy_, False))
        self.__11l1111ll1l_opy_(opts.get(bstack111lll1l1l1_opy_, False))
        self.__11l1111l111_opy_(opts.get(bstack111lllll1ll_opy_, False))
    @classmethod
    def bstack1llll11l1_opy_(cls, config=None):
        if cls._1ll1ll1l1l1_opy_ is None and config is not None:
            cls._1ll1ll1l1l1_opy_ = bstack11l11l1l_opy_(config)
        return cls._1ll1ll1l1l1_opy_
    @staticmethod
    def bstack11111111_opy_(config: dict) -> bool:
        bstack11l11111111_opy_ = config.get(bstack1ll11_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭓"), {}).get(bstack11l111111l1_opy_, {})
        return bstack11l11111111_opy_.get(bstack1ll11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᭔"), False)
    @staticmethod
    def bstack111lllll_opy_(config: dict) -> int:
        bstack11l11111111_opy_ = config.get(bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭕"), {}).get(bstack11l111111l1_opy_, {})
        retries = 0
        if bstack11l11l1l_opy_.bstack11111111_opy_(config):
            retries = bstack11l11111111_opy_.get(bstack1ll11_opy_ (u"ࠬࡳࡡࡹࡔࡨࡸࡷ࡯ࡥࡴࠩ᭖"), 1)
        return retries
    @staticmethod
    def bstack1l1l11l1ll_opy_(config: dict) -> dict:
        bstack11l1111llll_opy_ = config.get(bstack1ll11_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭗"), {})
        return {
            key: value for key, value in bstack11l1111llll_opy_.items() if key in bstack111llll1l11_opy_
        }
    @staticmethod
    def bstack111lllllll1_opy_():
        bstack1ll11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭘")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠣࡣࡥࡳࡷࡺ࡟ࡣࡷ࡬ࡰࡩࡥࡻࡾࠤ᭙").format(os.getenv(bstack1ll11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ᭚")))))
    @staticmethod
    def bstack111llll1ll1_opy_(test_name: str):
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭛")
        bstack111lll11l11_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll11_opy_ (u"ࠦ࡫ࡧࡩ࡭ࡧࡧࡣࡹ࡫ࡳࡵࡵࡢࡿࢂ࠴ࡴࡹࡶࠥ᭜").format(os.getenv(bstack1ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᭝"))))
        with open(bstack111lll11l11_opy_, bstack1ll11_opy_ (u"࠭ࡡࠨ᭞")) as file:
            file.write(bstack1ll11_opy_ (u"ࠢࡼࡿ࡟ࡲࠧ᭟").format(test_name))
    @staticmethod
    def bstack11l1111l11l_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l111l111l_opy_
    @staticmethod
    def bstack11ll1111111_opy_(config: dict) -> bool:
        bstack11l111l11ll_opy_ = config.get(bstack1ll11_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭠"), {}).get(bstack111lll1ll1l_opy_, {})
        return bstack11l111l11ll_opy_.get(bstack1ll11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪ᭡"), False)
    @staticmethod
    def bstack11ll1111l11_opy_(config: dict, bstack11ll11111ll_opy_: int = 0) -> int:
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡈࡧࡷࠤࡹ࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠱ࠦࡷࡩ࡫ࡦ࡬ࠥࡩࡡ࡯ࠢࡥࡩࠥࡧ࡮ࠡࡣࡥࡷࡴࡲࡵࡵࡧࠣࡲࡺࡳࡢࡦࡴࠣࡳࡷࠦࡡࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡨࡵ࡮ࡧ࡫ࡪࠤ࠭ࡪࡩࡤࡶࠬ࠾࡚ࠥࡨࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶࡾ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡺ࡯ࡵࡣ࡯ࡣࡹ࡫ࡳࡵࡵࠣࠬ࡮ࡴࡴࠪ࠼ࠣࡘ࡭࡫ࠠࡵࡱࡷࡥࡱࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡧࠢࡷࡩࡸࡺࡳࠡࠪࡵࡩࡶࡻࡩࡳࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳࠪ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤ࡮ࡴࡴ࠻ࠢࡗ࡬ࡪࠦࡦࡢ࡫࡯ࡹࡷ࡫ࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭢")
        bstack11l111l11ll_opy_ = config.get(bstack1ll11_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭣"), {}).get(bstack1ll11_opy_ (u"ࠬࡧࡢࡰࡴࡷࡆࡺ࡯࡬ࡥࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠫ᭤"), {})
        bstack11l111l11l1_opy_ = 0
        bstack11l111ll111_opy_ = 0
        if bstack11l11l1l_opy_.bstack11ll1111111_opy_(config):
            bstack11l111ll111_opy_ = bstack11l111l11ll_opy_.get(bstack1ll11_opy_ (u"࠭࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶࠫ᭥"), 5)
            if isinstance(bstack11l111ll111_opy_, str) and bstack11l111ll111_opy_.endswith(bstack1ll11_opy_ (u"ࠧࠦࠩ᭦")):
                try:
                    percentage = int(bstack11l111ll111_opy_.strip(bstack1ll11_opy_ (u"ࠨࠧࠪ᭧")))
                    if bstack11ll11111ll_opy_ > 0:
                        bstack11l111l11l1_opy_ = math.ceil((percentage * bstack11ll11111ll_opy_) / 100)
                    else:
                        raise ValueError(bstack1ll11_opy_ (u"ࠤࡗࡳࡹࡧ࡬ࠡࡶࡨࡷࡹࡹࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡪࡴࡸࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨ࠱ࡧࡧࡳࡦࡦࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࡹ࠮ࠣ᭨"))
                except ValueError as e:
                    raise ValueError(bstack1ll11_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥࠡࡸࡤࡰࡺ࡫ࠠࡧࡱࡵࠤࡲࡧࡸࡇࡣ࡬ࡰࡺࡸࡥࡴ࠼ࠣࡿࢂࠨ᭩").format(bstack11l111ll111_opy_)) from e
            else:
                bstack11l111l11l1_opy_ = int(bstack11l111ll111_opy_)
        logger.info(bstack1ll11_opy_ (u"ࠦࡒࡧࡸࠡࡨࡤ࡭ࡱࡻࡲࡦࡵࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩࠦࡳࡦࡶࠣࡸࡴࡀࠠࡼࡿࠣࠬ࡫ࡸ࡯࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠯ࠢ᭪").format(bstack11l111l11l1_opy_, bstack11l111ll111_opy_))
        return bstack11l111l11l1_opy_
    def bstack11l111l1111_opy_(self):
        return self.bstack11l11111ll1_opy_
    def bstack11l1111ll11_opy_(self):
        return self.bstack111lll11lll_opy_
    def bstack111lll1l11l_opy_(self):
        return self.bstack111lll1llll_opy_
    def __11l111l1l11_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l11111ll1_opy_ = bool(enabled)
            if mode not in [bstack1ll11_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ᭫"), bstack1ll11_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡐࡰ࡯ࡽ᭬ࠬ")]:
                logger.warning(bstack1ll11_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠣࡱࡴࡪࡥࠡࠩࡾࢁࠬࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡴࡰࠢࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ࠲ࠧ᭭").format(mode))
                mode = bstack1ll11_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭮")
            self.bstack111lll11lll_opy_ = mode
            if source is None:
                self.bstack111lll1llll_opy_ = None
            elif isinstance(source, list):
                self.bstack111lll1llll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1ll11_opy_ (u"ࠩ࠱࡮ࡸࡵ࡮ࠨ᭯")):
                self.bstack111lll1llll_opy_ = self._111llllll11_opy_(source)
            self.__111llll1l1l_opy_()
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠥࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡳࡦࡶࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࠳ࠠࡦࡰࡤࡦࡱ࡫ࡤ࠻ࠢࡾࢁ࠱ࠦ࡭ࡰࡦࡨ࠾ࠥࢁࡽ࠭ࠢࡶࡳࡺࡸࡣࡦ࠼ࠣࡿࢂ࠴ࠠࡆࡴࡵࡳࡷࡀࠠࡼࡿࠥ᭰").format(enabled, mode, source, e))
    def bstack11l111l1lll_opy_(self):
        return self.bstack111llll111l_opy_
    def __111llllllll_opy_(self, value):
        self.bstack111llll111l_opy_ = bool(value)
        self.__111llll1l1l_opy_()
    def bstack111llll1111_opy_(self):
        return self.bstack11l1111111l_opy_
    def __11l1111ll1l_opy_(self, value):
        self.bstack11l1111111l_opy_ = bool(value)
        self.__111llll1l1l_opy_()
    def bstack11l111l1l1l_opy_(self):
        return self.bstack111lll11ll1_opy_
    def __11l1111l111_opy_(self, value):
        self.bstack111lll11ll1_opy_ = bool(value)
        self.__111llll1l1l_opy_()
    def __111llll1l1l_opy_(self):
        if self.bstack11l11111ll1_opy_:
            self.bstack111llll111l_opy_ = False
            self.bstack11l1111111l_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack111llllll1l_opy_.enable(bstack11l111ll1ll_opy_)
        elif self.bstack111llll111l_opy_:
            self.bstack11l1111111l_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111llllll1l_opy_.enable(bstack111lll11l1l_opy_)
        elif self.bstack11l1111111l_opy_:
            self.bstack111llll111l_opy_ = False
            self.bstack111lll11ll1_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111llllll1l_opy_.enable(bstack111lll1l1l1_opy_)
        elif self.bstack111lll11ll1_opy_:
            self.bstack111llll111l_opy_ = False
            self.bstack11l1111111l_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111llllll1l_opy_.enable(bstack111lllll1ll_opy_)
        else:
            self.bstack111llllll1l_opy_.disable()
    def bstack1lllll111_opy_(self):
        return self.bstack111llllll1l_opy_.bstack111lllll111_opy_()
    def bstack11lll11ll1_opy_(self):
        if self.bstack111llllll1l_opy_.bstack111lllll111_opy_():
            return self.bstack111llllll1l_opy_.get_name()
        return None
    def _111llllll11_opy_(self, bstack111llll11ll_opy_):
        bstack1ll11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡤࡶࡸ࡫ࠠࡋࡕࡒࡒࠥࡹ࡯ࡶࡴࡦࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥ࡬ࡩ࡭ࡧࠣࡥࡳࡪࠠࡧࡱࡵࡱࡦࡺࠠࡪࡶࠣࡪࡴࡸࠠࡴ࡯ࡤࡶࡹࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡵࡲࡹࡷࡩࡥࡠࡨ࡬ࡰࡪࡥࡰࡢࡶ࡫ࠤ࠭ࡹࡴࡳࠫ࠽ࠤࡕࡧࡴࡩࠢࡷࡳࠥࡺࡨࡦࠢࡍࡗࡔࡔࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦ࡬ࡪࡵࡷ࠾ࠥࡌ࡯ࡳ࡯ࡤࡸࡹ࡫ࡤࠡ࡮࡬ࡷࡹࠦ࡯ࡧࠢࡵࡩࡵࡵࡳࡪࡶࡲࡶࡾࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࡹࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭱")
        if not os.path.isfile(bstack111llll11ll_opy_):
            logger.error(bstack1ll11_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧࠡࡦࡲࡩࡸࠦ࡮ࡰࡶࠣࡩࡽ࡯ࡳࡵ࠰ࠥ᭲").format(bstack111llll11ll_opy_))
            return []
        data = None
        try:
            with open(bstack111llll11ll_opy_, bstack1ll11_opy_ (u"ࠨࡲࠣ᭳")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1ll11_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡋࡕࡒࡒࠥ࡬ࡲࡰ࡯ࠣࡷࡴࡻࡲࡤࡧࠣࡪ࡮ࡲࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥ᭴").format(bstack111llll11ll_opy_, e))
            return []
        _11l11111lll_opy_ = None
        _111lll1ll11_opy_ = None
        def _11l1111l1ll_opy_():
            bstack11l11111l1l_opy_ = {}
            bstack111lll1l111_opy_ = {}
            try:
                if self.bstack11l111111ll_opy_.startswith(bstack1ll11_opy_ (u"ࠨࡽࠪ᭵")) and self.bstack11l111111ll_opy_.endswith(bstack1ll11_opy_ (u"ࠩࢀࠫ᭶")):
                    bstack11l11111l1l_opy_ = json.loads(self.bstack11l111111ll_opy_)
                else:
                    bstack11l11111l1l_opy_ = dict(item.split(bstack1ll11_opy_ (u"ࠪ࠾ࠬ᭷")) for item in self.bstack11l111111ll_opy_.split(bstack1ll11_opy_ (u"ࠫ࠱࠭᭸")) if bstack1ll11_opy_ (u"ࠬࡀࠧ᭹") in item) if self.bstack11l111111ll_opy_ else {}
                if self.bstack111lllll11l_opy_.startswith(bstack1ll11_opy_ (u"࠭ࡻࠨ᭺")) and self.bstack111lllll11l_opy_.endswith(bstack1ll11_opy_ (u"ࠧࡾࠩ᭻")):
                    bstack111lll1l111_opy_ = json.loads(self.bstack111lllll11l_opy_)
                else:
                    bstack111lll1l111_opy_ = dict(item.split(bstack1ll11_opy_ (u"ࠨ࠼ࠪ᭼")) for item in self.bstack111lllll11l_opy_.split(bstack1ll11_opy_ (u"ࠩ࠯ࠫ᭽")) if bstack1ll11_opy_ (u"ࠪ࠾ࠬ᭾") in item) if self.bstack111lllll11l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1ll11_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡦࡸࡳࡪࡰࡪࠤ࡫࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡳࡡࡱࡲ࡬ࡲ࡬ࡹ࠺ࠡࡽࢀࠦ᭿").format(e))
            logger.debug(bstack1ll11_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳࠡࡨࡵࡳࡲࠦࡥ࡯ࡸ࠽ࠤࢀࢃࠬࠡࡅࡏࡍ࠿ࠦࡻࡾࠤᮀ").format(bstack11l11111l1l_opy_, bstack111lll1l111_opy_))
            return bstack11l11111l1l_opy_, bstack111lll1l111_opy_
        if _11l11111lll_opy_ is None or _111lll1ll11_opy_ is None:
            _11l11111lll_opy_, _111lll1ll11_opy_ = _11l1111l1ll_opy_()
        def bstack11l1111lll1_opy_(name, bstack11l111l1ll1_opy_):
            if name in _111lll1ll11_opy_:
                return _111lll1ll11_opy_[name]
            if name in _11l11111lll_opy_:
                return _11l11111lll_opy_[name]
            if bstack11l111l1ll1_opy_.get(bstack1ll11_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭ᮁ")):
                return bstack11l111l1ll1_opy_[bstack1ll11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮂ")]
            return None
        if isinstance(data, dict):
            bstack11l111ll1l1_opy_ = []
            bstack111lllll1l1_opy_ = re.compile(bstack1ll11_opy_ (u"ࡳࠩࡡ࡟ࡆ࠳࡚࠱࠯࠼ࡣࡢ࠱ࠤࠨᮃ"))
            for name, bstack11l111l1ll1_opy_ in data.items():
                if not isinstance(bstack11l111l1ll1_opy_, dict):
                    continue
                if not bstack11l111l1ll1_opy_.get(bstack1ll11_opy_ (u"ࠩࡸࡶࡱ࠭ᮄ")):
                    logger.warning(bstack1ll11_opy_ (u"ࠥࡖࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡖࡔࡏࠤ࡮ࡹࠠ࡮࡫ࡶࡷ࡮ࡴࡧࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᮅ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if not bstack111lllll1l1_opy_.match(name):
                    logger.warning(bstack1ll11_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࡩࡳࡷࡳࡡࡵࠢࡩࡳࡷࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮆ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1ll11_opy_ (u"࡙ࠧ࡯ࡶࡴࡦࡩࠥ࡯ࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠢࠪࡿࢂ࠭ࠠ࡮ࡷࡶࡸࠥ࡮ࡡࡷࡧࠣࡥࠥࡲࡥ࡯ࡩࡷ࡬ࠥࡨࡥࡵࡹࡨࡩࡳࠦ࠱ࠡࡣࡱࡨࠥ࠹࠰ࠡࡥ࡫ࡥࡷࡧࡣࡵࡧࡵࡷ࠳ࠨᮇ").format(name))
                    continue
                bstack11l111l1ll1_opy_ = bstack11l111l1ll1_opy_.copy()
                bstack11l111l1ll1_opy_[bstack1ll11_opy_ (u"࠭࡮ࡢ࡯ࡨࠫᮈ")] = name
                bstack11l111l1ll1_opy_[bstack1ll11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮉ")] = bstack11l1111lll1_opy_(name, bstack11l111l1ll1_opy_)
                if not bstack11l111l1ll1_opy_.get(bstack1ll11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮊ")):
                    logger.warning(bstack1ll11_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡲࡴࡺࠠࡴࡲࡨࡧ࡮࡬ࡩࡦࡦࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮋ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if bstack11l111l1ll1_opy_.get(bstack1ll11_opy_ (u"ࠪࡦࡦࡹࡥࡃࡴࡤࡲࡨ࡮ࠧᮌ")) and bstack11l111l1ll1_opy_[bstack1ll11_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨᮍ")] == bstack11l111l1ll1_opy_[bstack1ll11_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᮎ")]:
                    logger.warning(bstack1ll11_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠࡢࡰࡧࠤࡧࡧࡳࡦࠢࡥࡶࡦࡴࡣࡩࠢࡦࡥࡳࡴ࡯ࡵࠢࡥࡩࠥࡺࡨࡦࠢࡶࡥࡲ࡫ࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮏ").format(name, bstack11l111l1ll1_opy_))
                    continue
                bstack11l111ll1l1_opy_.append(bstack11l111l1ll1_opy_)
            return bstack11l111ll1l1_opy_
        return data
    def bstack111llll11l1_opy_(self):
        data = {
            bstack1ll11_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᮐ"): {
                bstack1ll11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮑ"): self.bstack11l111l1111_opy_(),
                bstack1ll11_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮒ"): self.bstack11l1111ll11_opy_(),
                bstack1ll11_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᮓ"): self.bstack111lll1l11l_opy_()
            }
        }
        return data
    def bstack11l111ll11l_opy_(self, config):
        bstack111lll1l1ll_opy_ = {}
        bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᮔ")] = {
            bstack1ll11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮕ"): self.bstack11l111l1111_opy_(),
            bstack1ll11_opy_ (u"࠭࡭ࡰࡦࡨࠫᮖ"): self.bstack11l1111ll11_opy_()
        }
        bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"ࠧࡳࡧࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࠪᮗ")] = {
            bstack1ll11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮘ"): self.bstack111llll1111_opy_()
        }
        bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"ࠩࡵࡹࡳࡥࡰࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡢࡪࡦ࡯࡬ࡦࡦࡢࡪ࡮ࡸࡳࡵࠩᮙ")] = {
            bstack1ll11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮚ"): self.bstack11l111l1lll_opy_()
        }
        bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"ࠫࡸࡱࡩࡱࡡࡩࡥ࡮ࡲࡩ࡯ࡩࡢࡥࡳࡪ࡟ࡧ࡮ࡤ࡯ࡾ࠭ᮛ")] = {
            bstack1ll11_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮜ"): self.bstack11l111l1l1l_opy_()
        }
        if self.bstack11111111_opy_(config):
            bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"࠭ࡲࡦࡶࡵࡽࡤࡺࡥࡴࡶࡶࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᮝ")] = {
                bstack1ll11_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮞ"): True,
                bstack1ll11_opy_ (u"ࠨ࡯ࡤࡼࡤࡸࡥࡵࡴ࡬ࡩࡸ࠭ᮟ"): self.bstack111lllll_opy_(config)
            }
        if self.bstack11ll1111111_opy_(config):
            bstack111lll1l1ll_opy_[bstack1ll11_opy_ (u"ࠩࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᮠ")] = {
                bstack1ll11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮡ"): True,
                bstack1ll11_opy_ (u"ࠫࡲࡧࡸࡠࡨࡤ࡭ࡱࡻࡲࡦࡵࠪᮢ"): self.bstack11ll1111l11_opy_(config)
            }
        return bstack111lll1l1ll_opy_
    def bstack11ll1ll11_opy_(self, config):
        bstack1ll11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆࡳࡱࡲࡥࡤࡶࡶࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡤࡼࠤࡲࡧ࡫ࡪࡰࡪࠤࡦࠦࡣࡢ࡮࡯ࠤࡹࡵࠠࡵࡪࡨࠤࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠢࡨࡲࡩࡶ࡯ࡪࡰࡷ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡺ࡯࡬ࡥࡡࡸࡹ࡮ࡪࠠࠩࡵࡷࡶ࠮ࡀࠠࡕࡪࡨࠤ࡚࡛ࡉࡅࠢࡲࡪࠥࡺࡨࡦࠢࡥࡹ࡮ࡲࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡪࡡࡵࡣࠣࡪࡴࡸ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡧ࡭ࡨࡺ࠺ࠡࡔࡨࡷࡵࡵ࡮ࡴࡧࠣࡪࡷࡵ࡭ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠱ࠦ࡯ࡳࠢࡑࡳࡳ࡫ࠠࡪࡨࠣࡪࡦ࡯࡬ࡦࡦ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮣ")
        if not (config.get(bstack1ll11_opy_ (u"࠭ࡦࡳࡣࡰࡩࡼࡵࡲ࡬ࠩᮤ"), None) in bstack11l1l11l1l1_opy_ and self.bstack11l111l1111_opy_()):
            return None
        bstack111lll1lll1_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠧࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠬᮥ"), None)
        logger.debug(bstack1ll11_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡃࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᮦ").format(bstack111lll1lll1_opy_))
        try:
            bstack11ll11lll11_opy_ = bstack1ll11_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡢࡶ࡫࡯ࡨࡸ࠵ࡻࡾ࠱ࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠢᮧ").format(bstack111lll1lll1_opy_)
            payload = {
                bstack1ll11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᮨ"): config.get(bstack1ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᮩ"), bstack1ll11_opy_ (u"᮪ࠬ࠭")),
                bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤ᮫"): config.get(bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᮬ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᮭ"): os.environ.get(bstack1ll11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᮮ"), bstack1ll11_opy_ (u"ࠥࠦᮯ")),
                bstack1ll11_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢ᮰"): int(os.environ.get(bstack1ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣ᮱")) or bstack1ll11_opy_ (u"ࠨ࠰ࠣ᮲")),
                bstack1ll11_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦ᮳"): int(os.environ.get(bstack1ll11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥ᮴")) or bstack1ll11_opy_ (u"ࠤ࠴ࠦ᮵")),
                bstack1ll11_opy_ (u"ࠥ࡬ࡴࡹࡴࡊࡰࡩࡳࠧ᮶"): get_host_info(),
            }
            logger.debug(bstack1ll11_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡱࡣࡼࡰࡴࡧࡤ࠻ࠢࡾࢁࠧ᮷").format(payload))
            response = bstack11ll1llllll_opy_.bstack11ll11ll1ll_opy_(bstack11ll11lll11_opy_, payload)
            if response:
                logger.debug(bstack1ll11_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡆࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡱࡱࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥ᮸").format(response))
                return response
            else:
                logger.error(bstack1ll11_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࡀࠠࡼࡿࠥ᮹").format(bstack111lll1lll1_opy_))
                return None
        except Exception as e:
            logger.error(bstack1ll11_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡴࡧࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡥࡹ࡮ࡲࡤࠡࡗࡘࡍࡉࠦࡻࡾ࠼ࠣࡿࢂࠨᮺ").format(bstack111lll1lll1_opy_, e))
            return None
# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import tempfile
import math
from bstack_utils import bstack111l11l1l_opy_
from bstack_utils.constants import bstack11ll111ll1_opy_, bstack11l1l111l11_opy_
from bstack_utils.helper import bstack11lll11l11l_opy_, get_host_info
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1llll1l_opy_
import json
import re
import sys
bstack11l111111l1_opy_ = bstack1l1lll1_opy_ (u"ࠤࡵࡩࡹࡸࡹࡕࡧࡶࡸࡸࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣᬾ")
bstack111llll1111_opy_ = bstack1l1lll1_opy_ (u"ࠥࡥࡧࡵࡲࡵࡄࡸ࡭ࡱࡪࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠤᬿ")
bstack111llllllll_opy_ = bstack1l1lll1_opy_ (u"ࠦࡷࡻ࡮ࡑࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡊࡦ࡯࡬ࡦࡦࡉ࡭ࡷࡹࡴࠣᭀ")
bstack11l1111111l_opy_ = bstack1l1lll1_opy_ (u"ࠧࡸࡥࡳࡷࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࡱࡿࡆࡢ࡫࡯ࡩࡩࠨᭁ")
bstack11l111l1ll1_opy_ = bstack1l1lll1_opy_ (u"ࠨࡳ࡬࡫ࡳࡊࡱࡧ࡫ࡺࡣࡱࡨࡋࡧࡩ࡭ࡧࡧࠦᭂ")
bstack111lll11l11_opy_ = bstack1l1lll1_opy_ (u"ࠢࡳࡷࡱࡗࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࠦᭃ")
bstack111lll1ll1l_opy_ = {
    bstack11l111111l1_opy_,
    bstack111llll1111_opy_,
    bstack111llllllll_opy_,
    bstack11l1111111l_opy_,
    bstack11l111l1ll1_opy_,
    bstack111lll11l11_opy_
}
bstack11l111111ll_opy_ = {bstack1l1lll1_opy_ (u"ࠨࡲࡼࡸࡪࡹࡴࠨ᭄")}
logger = bstack111l11l1l_opy_.get_logger(__name__, bstack11ll111ll1_opy_)
class bstack111lll111l1_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111llll1lll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1111llll_opy_:
    _1ll1ll1l1l1_opy_ = None
    def __init__(self, config):
        self.bstack11l111l11l1_opy_ = False
        self.bstack111lllll111_opy_ = False
        self.bstack111lll1lll1_opy_ = False
        self.bstack11l11111lll_opy_ = False
        self.bstack111lll1111l_opy_ = None
        self.bstack11l111l111l_opy_ = bstack111lll111l1_opy_()
        self.bstack11l1111l111_opy_ = None
        opts = config.get(bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᭅ"), {})
        self.bstack111llllll11_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡊࡔࡖࠨᭆ"), bstack1l1lll1_opy_ (u"ࠦࠧᭇ"))
        self.bstack11l1111ll1l_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠬࡹ࡭ࡢࡴࡷࡗࡪࡲࡥࡤࡶ࡬ࡳࡳࡌࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࡪࡹࡃࡍࡋࠪᭈ"), bstack1l1lll1_opy_ (u"ࠨࠢᭉ"))
        bstack111lll1l1l1_opy_ = opts.get(bstack111lll11l11_opy_, {})
        bstack111lll11ll1_opy_ = None
        if bstack1l1lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᭊ") in bstack111lll1l1l1_opy_:
            bstack111lll11ll1_opy_ = bstack111lll1l1l1_opy_[bstack1l1lll1_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᭋ")]
            if bstack111lll11ll1_opy_ is None:
                bstack111lll11ll1_opy_ = []
        self.__111llll1l11_opy_(
            bstack111lll1l1l1_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᭌ"), False),
            bstack111lll1l1l1_opy_.get(bstack1l1lll1_opy_ (u"ࠪࡱࡴࡪࡥࠨ᭍"), bstack1l1lll1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ᭎")),
            bstack111lll11ll1_opy_
        )
        self.__11l111l1l11_opy_(opts.get(bstack111llllllll_opy_, False))
        self.__111lllll1ll_opy_(opts.get(bstack11l1111111l_opy_, False))
        self.__11l11111ll1_opy_(opts.get(bstack11l111l1ll1_opy_, False))
    @classmethod
    def bstack11l11l1l_opy_(cls, config=None):
        if cls._1ll1ll1l1l1_opy_ is None and config is not None:
            cls._1ll1ll1l1l1_opy_ = bstack1111llll_opy_(config)
        return cls._1ll1ll1l1l1_opy_
    @staticmethod
    def bstack1lll1l1ll_opy_(config: dict) -> bool:
        bstack111lll11l1l_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭏"), {}).get(bstack11l111111l1_opy_, {})
        return bstack111lll11l1l_opy_.get(bstack1l1lll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᭐"), False)
    @staticmethod
    def bstack1lllll111_opy_(config: dict) -> int:
        bstack111lll11l1l_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭑"), {}).get(bstack11l111111l1_opy_, {})
        retries = 0
        if bstack1111llll_opy_.bstack1lll1l1ll_opy_(config):
            retries = bstack111lll11l1l_opy_.get(bstack1l1lll1_opy_ (u"ࠨ࡯ࡤࡼࡗ࡫ࡴࡳ࡫ࡨࡷࠬ᭒"), 1)
        return retries
    @staticmethod
    def bstack11l1l1l1l_opy_(config: dict) -> dict:
        bstack111lllll11l_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭓"), {})
        return {
            key: value for key, value in bstack111lllll11l_opy_.items() if key in bstack111lll1ll1l_opy_
        }
    @staticmethod
    def bstack111lll1l11l_opy_():
        bstack1l1lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭔")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧ᭕").format(os.getenv(bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᭖")))))
    @staticmethod
    def bstack111lll11lll_opy_(test_name: str):
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᭗")
        bstack11l1111l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1l1lll1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨ᭘").format(os.getenv(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᭙"))))
        with open(bstack11l1111l1ll_opy_, bstack1l1lll1_opy_ (u"ࠩࡤࠫ᭚")) as file:
            file.write(bstack1l1lll1_opy_ (u"ࠥࡿࢂࡢ࡮ࠣ᭛").format(test_name))
    @staticmethod
    def bstack11l1111l1l1_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l111111ll_opy_
    @staticmethod
    def bstack11ll1111111_opy_(config: dict) -> bool:
        bstack111lll1ll11_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭜"), {}).get(bstack111llll1111_opy_, {})
        return bstack111lll1ll11_opy_.get(bstack1l1lll1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭝"), False)
    @staticmethod
    def bstack11ll11111l1_opy_(config: dict, bstack11ll111l11l_opy_: int = 0) -> int:
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠭ࠢࡺ࡬࡮ࡩࡨࠡࡥࡤࡲࠥࡨࡥࠡࡣࡱࠤࡦࡨࡳࡰ࡮ࡸࡸࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡳࠢࡤࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡪ࡮࡭ࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡲࡸࡦࡲ࡟ࡵࡧࡶࡸࡸࠦࠨࡪࡰࡷ࠭࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤ࠭ࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭞")
        bstack111lll1ll11_opy_ = config.get(bstack1l1lll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭟"), {}).get(bstack1l1lll1_opy_ (u"ࠨࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠧ᭠"), {})
        bstack111lll1l111_opy_ = 0
        bstack111lllll1l1_opy_ = 0
        if bstack1111llll_opy_.bstack11ll1111111_opy_(config):
            bstack111lllll1l1_opy_ = bstack111lll1ll11_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹࠧ᭡"), 5)
            if isinstance(bstack111lllll1l1_opy_, str) and bstack111lllll1l1_opy_.endswith(bstack1l1lll1_opy_ (u"ࠪࠩࠬ᭢")):
                try:
                    percentage = int(bstack111lllll1l1_opy_.strip(bstack1l1lll1_opy_ (u"ࠫࠪ࠭᭣")))
                    if bstack11ll111l11l_opy_ > 0:
                        bstack111lll1l111_opy_ = math.ceil((percentage * bstack11ll111l11l_opy_) / 100)
                    else:
                        raise ValueError(bstack1l1lll1_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡱࡺࡹࡴࠡࡤࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵ࠱ࠦ᭤"))
                except ValueError as e:
                    raise ValueError(bstack1l1lll1_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨࠤࡻࡧ࡬ࡶࡧࠣࡪࡴࡸࠠ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷ࠿ࠦࡻࡾࠤ᭥").format(bstack111lllll1l1_opy_)) from e
            else:
                bstack111lll1l111_opy_ = int(bstack111lllll1l1_opy_)
        logger.info(bstack1l1lll1_opy_ (u"ࠢࡎࡣࡻࠤ࡫ࡧࡩ࡭ࡷࡵࡩࡸࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡶࡩࡹࠦࡴࡰ࠼ࠣࡿࢂࠦࠨࡧࡴࡲࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡻࡾࠫࠥ᭦").format(bstack111lll1l111_opy_, bstack111lllll1l1_opy_))
        return bstack111lll1l111_opy_
    def bstack11l11111l1l_opy_(self):
        return self.bstack11l11111lll_opy_
    def bstack11l1111llll_opy_(self):
        return self.bstack111lll1111l_opy_
    def bstack111lllllll1_opy_(self):
        return self.bstack11l1111l111_opy_
    def __111llll1l11_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l11111lll_opy_ = bool(enabled)
            if mode not in [bstack1l1lll1_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨ᭧"), bstack1l1lll1_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡓࡳࡲࡹࠨ᭨")]:
                logger.warning(bstack1l1lll1_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࡭ࡰࡦࡨࠤࠬࢁࡽࠨࠢࡳࡶࡴࡼࡩࡥࡧࡧ࠲ࠥࡊࡥࡧࡣࡸࡰࡹ࡯࡮ࡨࠢࡷࡳࠥ࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭࠮ࠣ᭩").format(mode))
                mode = bstack1l1lll1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ᭪")
            self.bstack111lll1111l_opy_ = mode
            if source is None:
                self.bstack11l1111l111_opy_ = None
            elif isinstance(source, list):
                self.bstack11l1111l111_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1l1lll1_opy_ (u"ࠬ࠴ࡪࡴࡱࡱࠫ᭫")):
                self.bstack11l1111l111_opy_ = self._11l11111111_opy_(source)
            self.__111llll11l1_opy_()
        except Exception as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡ࠯ࠣࡩࡳࡧࡢ࡭ࡧࡧ࠾ࠥࢁࡽ࠭ࠢࡰࡳࡩ࡫࠺ࠡࡽࢀ࠰ࠥࡹ࡯ࡶࡴࡦࡩ࠿ࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨ᭬").format(enabled, mode, source, e))
    def bstack111lll1llll_opy_(self):
        return self.bstack11l111l11l1_opy_
    def __11l111l1l11_opy_(self, value):
        self.bstack11l111l11l1_opy_ = bool(value)
        self.__111llll11l1_opy_()
    def bstack11l1111l11l_opy_(self):
        return self.bstack111lllll111_opy_
    def __111lllll1ll_opy_(self, value):
        self.bstack111lllll111_opy_ = bool(value)
        self.__111llll11l1_opy_()
    def bstack11l111l1lll_opy_(self):
        return self.bstack111lll1lll1_opy_
    def __11l11111ll1_opy_(self, value):
        self.bstack111lll1lll1_opy_ = bool(value)
        self.__111llll11l1_opy_()
    def __111llll11l1_opy_(self):
        if self.bstack11l11111lll_opy_:
            self.bstack11l111l11l1_opy_ = False
            self.bstack111lllll111_opy_ = False
            self.bstack111lll1lll1_opy_ = False
            self.bstack11l111l111l_opy_.enable(bstack111lll11l11_opy_)
        elif self.bstack11l111l11l1_opy_:
            self.bstack111lllll111_opy_ = False
            self.bstack111lll1lll1_opy_ = False
            self.bstack11l11111lll_opy_ = False
            self.bstack11l111l111l_opy_.enable(bstack111llllllll_opy_)
        elif self.bstack111lllll111_opy_:
            self.bstack11l111l11l1_opy_ = False
            self.bstack111lll1lll1_opy_ = False
            self.bstack11l11111lll_opy_ = False
            self.bstack11l111l111l_opy_.enable(bstack11l1111111l_opy_)
        elif self.bstack111lll1lll1_opy_:
            self.bstack11l111l11l1_opy_ = False
            self.bstack111lllll111_opy_ = False
            self.bstack11l11111lll_opy_ = False
            self.bstack11l111l111l_opy_.enable(bstack11l111l1ll1_opy_)
        else:
            self.bstack11l111l111l_opy_.disable()
    def bstack1llll11l1_opy_(self):
        return self.bstack11l111l111l_opy_.bstack111llll1lll_opy_()
    def bstack1ll1ll111l_opy_(self):
        if self.bstack11l111l111l_opy_.bstack111llll1lll_opy_():
            return self.bstack11l111l111l_opy_.get_name()
        return None
    def _11l11111111_opy_(self, bstack11l11111l11_opy_):
        bstack1l1lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡵࡲࡹࡷࡩࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠦࡡ࡯ࡦࠣࡪࡴࡸ࡭ࡢࡶࠣ࡭ࡹࠦࡦࡰࡴࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸࡵࡵࡳࡥࡨࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠠࠩࡵࡷࡶ࠮ࡀࠠࡑࡣࡷ࡬ࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡓࡐࡐࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡈࡲࡶࡲࡧࡴࡵࡧࡧࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡸࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭭")
        if not os.path.isfile(bstack11l11111l11_opy_):
            logger.error(bstack1l1lll1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠨ᭮").format(bstack11l11111l11_opy_))
            return []
        data = None
        try:
            with open(bstack11l11111l11_opy_, bstack1l1lll1_opy_ (u"ࠤࡵࠦ᭯")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡎࡘࡕࡎࠡࡨࡵࡳࡲࠦࡳࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨ᭰").format(bstack11l11111l11_opy_, e))
            return []
        _11l111l1l1l_opy_ = None
        _11l111l11ll_opy_ = None
        def _11l111ll111_opy_():
            bstack11l111l1111_opy_ = {}
            bstack111llll1ll1_opy_ = {}
            try:
                if self.bstack111llllll11_opy_.startswith(bstack1l1lll1_opy_ (u"ࠫࢀ࠭᭱")) and self.bstack111llllll11_opy_.endswith(bstack1l1lll1_opy_ (u"ࠬࢃࠧ᭲")):
                    bstack11l111l1111_opy_ = json.loads(self.bstack111llllll11_opy_)
                else:
                    bstack11l111l1111_opy_ = dict(item.split(bstack1l1lll1_opy_ (u"࠭࠺ࠨ᭳")) for item in self.bstack111llllll11_opy_.split(bstack1l1lll1_opy_ (u"ࠧ࠭ࠩ᭴")) if bstack1l1lll1_opy_ (u"ࠨ࠼ࠪ᭵") in item) if self.bstack111llllll11_opy_ else {}
                if self.bstack11l1111ll1l_opy_.startswith(bstack1l1lll1_opy_ (u"ࠩࡾࠫ᭶")) and self.bstack11l1111ll1l_opy_.endswith(bstack1l1lll1_opy_ (u"ࠪࢁࠬ᭷")):
                    bstack111llll1ll1_opy_ = json.loads(self.bstack11l1111ll1l_opy_)
                else:
                    bstack111llll1ll1_opy_ = dict(item.split(bstack1l1lll1_opy_ (u"ࠫ࠿࠭᭸")) for item in self.bstack11l1111ll1l_opy_.split(bstack1l1lll1_opy_ (u"ࠬ࠲ࠧ᭹")) if bstack1l1lll1_opy_ (u"࠭࠺ࠨ᭺") in item) if self.bstack11l1111ll1l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1l1lll1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡧࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵ࠽ࠤࢀࢃࠢ᭻").format(e))
            logger.debug(bstack1l1lll1_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡰࡥࡵࡶࡩ࡯ࡩࡶࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻࡀࠠࡼࡿ࠯ࠤࡈࡒࡉ࠻ࠢࡾࢁࠧ᭼").format(bstack11l111l1111_opy_, bstack111llll1ll1_opy_))
            return bstack11l111l1111_opy_, bstack111llll1ll1_opy_
        if _11l111l1l1l_opy_ is None or _11l111l11ll_opy_ is None:
            _11l111l1l1l_opy_, _11l111l11ll_opy_ = _11l111ll111_opy_()
        def bstack111llll1l1l_opy_(name, bstack11l1111lll1_opy_):
            if name in _11l111l11ll_opy_:
                return _11l111l11ll_opy_[name]
            if name in _11l111l1l1l_opy_:
                return _11l111l1l1l_opy_[name]
            if bstack11l1111lll1_opy_.get(bstack1l1lll1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩ᭽")):
                return bstack11l1111lll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪ᭾")]
            return None
        if isinstance(data, dict):
            bstack111llllll1l_opy_ = []
            bstack111llll11ll_opy_ = re.compile(bstack1l1lll1_opy_ (u"ࡶࠬࡤ࡛ࡂ࠯࡝࠴࠲࠿࡟࡞࠭ࠧࠫ᭿"))
            for name, bstack11l1111lll1_opy_ in data.items():
                if not isinstance(bstack11l1111lll1_opy_, dict):
                    continue
                if not bstack11l1111lll1_opy_.get(bstack1l1lll1_opy_ (u"ࠬࡻࡲ࡭ࠩᮀ")):
                    logger.warning(bstack1l1lll1_opy_ (u"ࠨࡒࡦࡲࡲࡷ࡮ࡺ࡯ࡳࡻ࡙ࠣࡗࡒࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮁ").format(name, bstack11l1111lll1_opy_))
                    continue
                if not bstack111llll11ll_opy_.match(name):
                    logger.warning(bstack1l1lll1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡬࡯ࡳࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮂ").format(name, bstack11l1111lll1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1l1lll1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࠭ࡻࡾࠩࠣࡱࡺࡹࡴࠡࡪࡤࡺࡪࠦࡡࠡ࡮ࡨࡲ࡬ࡺࡨࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢ࠴ࠤࡦࡴࡤࠡ࠵࠳ࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳ࠯ࠤᮃ").format(name))
                    continue
                bstack11l1111lll1_opy_ = bstack11l1111lll1_opy_.copy()
                bstack11l1111lll1_opy_[bstack1l1lll1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᮄ")] = name
                bstack11l1111lll1_opy_[bstack1l1lll1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮅ")] = bstack111llll1l1l_opy_(name, bstack11l1111lll1_opy_)
                if not bstack11l1111lll1_opy_.get(bstack1l1lll1_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮆ")):
                    logger.warning(bstack1l1lll1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡮ࡰࡶࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡩࡩࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮇ").format(name, bstack11l1111lll1_opy_))
                    continue
                if bstack11l1111lll1_opy_.get(bstack1l1lll1_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪᮈ")) and bstack11l1111lll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮉ")] == bstack11l1111lll1_opy_[bstack1l1lll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮊ")]:
                    logger.warning(bstack1l1lll1_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡥࡳࡪࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡶ࡫ࡩࠥࡹࡡ࡮ࡧࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮋ").format(name, bstack11l1111lll1_opy_))
                    continue
                bstack111llllll1l_opy_.append(bstack11l1111lll1_opy_)
            return bstack111llllll1l_opy_
        return data
    def bstack11l1111ll11_opy_(self):
        data = {
            bstack1l1lll1_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᮌ"): {
                bstack1l1lll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮍ"): self.bstack11l11111l1l_opy_(),
                bstack1l1lll1_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᮎ"): self.bstack11l1111llll_opy_(),
                bstack1l1lll1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᮏ"): self.bstack111lllllll1_opy_()
            }
        }
        return data
    def bstack111lll1l1ll_opy_(self, config):
        bstack111llll111l_opy_ = {}
        bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᮐ")] = {
            bstack1l1lll1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮑ"): self.bstack11l11111l1l_opy_(),
            bstack1l1lll1_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮒ"): self.bstack11l1111llll_opy_()
        }
        bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩ࠭ᮓ")] = {
            bstack1l1lll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮔ"): self.bstack11l1111l11l_opy_()
        }
        bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩࡥࡦࡪࡴࡶࡸࠬᮕ")] = {
            bstack1l1lll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮖ"): self.bstack111lll1llll_opy_()
        }
        bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠧࡴ࡭࡬ࡴࡤ࡬ࡡࡪ࡮࡬ࡲ࡬ࡥࡡ࡯ࡦࡢࡪࡱࡧ࡫ࡺࠩᮗ")] = {
            bstack1l1lll1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮘ"): self.bstack11l111l1lll_opy_()
        }
        if self.bstack1lll1l1ll_opy_(config):
            bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠩࡵࡩࡹࡸࡹࡠࡶࡨࡷࡹࡹ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᮙ")] = {
                bstack1l1lll1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮚ"): True,
                bstack1l1lll1_opy_ (u"ࠫࡲࡧࡸࡠࡴࡨࡸࡷ࡯ࡥࡴࠩᮛ"): self.bstack1lllll111_opy_(config)
            }
        if self.bstack11ll1111111_opy_(config):
            bstack111llll111l_opy_[bstack1l1lll1_opy_ (u"ࠬࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧᮜ")] = {
                bstack1l1lll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮝ"): True,
                bstack1l1lll1_opy_ (u"ࠧ࡮ࡣࡻࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡸ࠭ᮞ"): self.bstack11ll11111l1_opy_(config)
            }
        return bstack111llll111l_opy_
    def bstack111lll11l1_opy_(self, config):
        bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉ࡯࡭࡮ࡨࡧࡹࡹࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡧࡿࠠ࡮ࡣ࡮࡭ࡳ࡭ࠠࡢࠢࡦࡥࡱࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡖࡗࡌࡈࠥࡵࡦࠡࡶ࡫ࡩࠥࡨࡵࡪ࡮ࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮟ")
        if not (config.get(bstack1l1lll1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᮠ"), None) in bstack11l1l111l11_opy_ and self.bstack11l11111l1l_opy_()):
            return None
        bstack111lll111ll_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᮡ"), None)
        logger.debug(bstack1l1lll1_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡆࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᮢ").format(bstack111lll111ll_opy_))
        try:
            bstack11ll11l1l11_opy_ = bstack1l1lll1_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠥᮣ").format(bstack111lll111ll_opy_)
            payload = {
                bstack1l1lll1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦᮤ"): config.get(bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᮥ"), bstack1l1lll1_opy_ (u"ࠨࠩᮦ")),
                bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᮧ"): config.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᮨ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤᮩ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕ᮪ࠦ"), bstack1l1lll1_opy_ (u"ࠨ᮫ࠢ")),
                bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥᮬ"): int(os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᮭ")) or bstack1l1lll1_opy_ (u"ࠤ࠳ࠦᮮ")),
                bstack1l1lll1_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢᮯ"): int(os.environ.get(bstack1l1lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨ᮰")) or bstack1l1lll1_opy_ (u"ࠧ࠷ࠢ᮱")),
                bstack1l1lll1_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣ᮲"): get_host_info(),
            }
            logger.debug(bstack1l1lll1_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡴࡦࡿ࡬ࡰࡣࡧ࠾ࠥࢁࡽࠣ᮳").format(payload))
            response = bstack11ll1llll1l_opy_.bstack11ll11ll1ll_opy_(bstack11ll11l1l11_opy_, payload)
            if response:
                logger.debug(bstack1l1lll1_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡂࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨ᮴").format(response))
                return response
            else:
                logger.error(bstack1l1lll1_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨ᮵").format(bstack111lll111ll_opy_))
                return None
        except Exception as e:
            logger.error(bstack1l1lll1_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅࠢࡾࢁ࠿ࠦࡻࡾࠤ᮶").format(bstack111lll111ll_opy_, e))
            return None
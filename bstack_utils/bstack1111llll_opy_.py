# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1ll1ll111_opy_
from bstack_utils.constants import bstack1llll1ll1l_opy_, bstack11l11lll11l_opy_
from bstack_utils.helper import bstack11lll111l1l_opy_, get_host_info
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
import json
import re
import sys
bstack11l11111111_opy_ = bstack1ll1l_opy_ (u"ࠣࡴࡨࡸࡷࡿࡔࡦࡵࡷࡷࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢᬽ")
bstack111llll11ll_opy_ = bstack1ll1l_opy_ (u"ࠤࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣᬾ")
bstack11l1111l111_opy_ = bstack1ll1l_opy_ (u"ࠥࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࡈ࡬ࡶࡸࡺࠢᬿ")
bstack11l111l11l1_opy_ = bstack1ll1l_opy_ (u"ࠦࡷ࡫ࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࠧᭀ")
bstack111llll1111_opy_ = bstack1ll1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡉࡰࡦࡱࡹࡢࡰࡧࡊࡦ࡯࡬ࡦࡦࠥᭁ")
bstack111llll1l11_opy_ = bstack1ll1l_opy_ (u"ࠨࡲࡶࡰࡖࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࠥᭂ")
bstack11l1111111l_opy_ = {
    bstack11l11111111_opy_,
    bstack111llll11ll_opy_,
    bstack11l1111l111_opy_,
    bstack11l111l11l1_opy_,
    bstack111llll1111_opy_,
    bstack111llll1l11_opy_
}
bstack11l1111ll1l_opy_ = {bstack1ll1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧᭃ")}
logger = bstack1ll1ll111_opy_.get_logger(__name__, bstack1llll1ll1l_opy_)
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
    def bstack11l1111lll1_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack11111l1l_opy_:
    _1ll1ll1ll1l_opy_ = None
    def __init__(self, config):
        self.bstack111lll1lll1_opy_ = False
        self.bstack111lllll11l_opy_ = False
        self.bstack111llll1lll_opy_ = False
        self.bstack11l11111ll1_opy_ = False
        self.bstack11l111l1l1l_opy_ = None
        self.bstack111lll11lll_opy_ = bstack11l111l1l11_opy_()
        self.bstack111lll111ll_opy_ = None
        opts = config.get(bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷ᭄ࠬ"), {})
        self.bstack111lll1l111_opy_ = config.get(bstack1ll1l_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡉࡓ࡜ࠧᭅ"), bstack1ll1l_opy_ (u"ࠥࠦᭆ"))
        self.bstack111lll1ll1l_opy_ = config.get(bstack1ll1l_opy_ (u"ࠫࡸࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࡋ࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࡩࡸࡉࡌࡊࠩᭇ"), bstack1ll1l_opy_ (u"ࠧࠨᭈ"))
        bstack11l111l111l_opy_ = opts.get(bstack111llll1l11_opy_, {})
        bstack111llllllll_opy_ = None
        if bstack1ll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᭉ") in bstack11l111l111l_opy_:
            bstack111llllllll_opy_ = bstack11l111l111l_opy_[bstack1ll1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᭊ")]
            if bstack111llllllll_opy_ is None:
                bstack111llllllll_opy_ = []
        self.__111lll11ll1_opy_(
            bstack11l111l111l_opy_.get(bstack1ll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᭋ"), False),
            bstack11l111l111l_opy_.get(bstack1ll1l_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᭌ"), bstack1ll1l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭍")),
            bstack111llllllll_opy_
        )
        self.__11l111l1111_opy_(opts.get(bstack11l1111l111_opy_, False))
        self.__11l1111l11l_opy_(opts.get(bstack11l111l11l1_opy_, False))
        self.__111lll11l1l_opy_(opts.get(bstack111llll1111_opy_, False))
    @classmethod
    def bstack111l1ll1_opy_(cls, config=None):
        if cls._1ll1ll1ll1l_opy_ is None and config is not None:
            cls._1ll1ll1ll1l_opy_ = bstack11111l1l_opy_(config)
        return cls._1ll1ll1ll1l_opy_
    @staticmethod
    def bstack1111ll1l_opy_(config: dict) -> bool:
        bstack11l111111ll_opy_ = config.get(bstack1ll1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭎"), {}).get(bstack11l11111111_opy_, {})
        return bstack11l111111ll_opy_.get(bstack1ll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭏"), False)
    @staticmethod
    def bstack11l11l11_opy_(config: dict) -> int:
        bstack11l111111ll_opy_ = config.get(bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭐"), {}).get(bstack11l11111111_opy_, {})
        retries = 0
        if bstack11111l1l_opy_.bstack1111ll1l_opy_(config):
            retries = bstack11l111111ll_opy_.get(bstack1ll1l_opy_ (u"ࠧ࡮ࡣࡻࡖࡪࡺࡲࡪࡧࡶࠫ᭑"), 1)
        return retries
    @staticmethod
    def bstack11ll1ll11_opy_(config: dict) -> dict:
        bstack11l11111lll_opy_ = config.get(bstack1ll1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭒"), {})
        return {
            key: value for key, value in bstack11l11111lll_opy_.items() if key in bstack11l1111111l_opy_
        }
    @staticmethod
    def bstack111lll1llll_opy_():
        bstack1ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭓")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦ᭔").format(os.getenv(bstack1ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᭕")))))
    @staticmethod
    def bstack111lllll1l1_opy_(test_name: str):
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭖")
        bstack111lllllll1_opy_ = os.path.join(tempfile.gettempdir(), bstack1ll1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧ᭗").format(os.getenv(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ᭘"))))
        with open(bstack111lllllll1_opy_, bstack1ll1l_opy_ (u"ࠨࡣࠪ᭙")) as file:
            file.write(bstack1ll1l_opy_ (u"ࠤࡾࢁࡡࡴࠢ᭚").format(test_name))
    @staticmethod
    def bstack11l1111ll11_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l1111ll1l_opy_
    @staticmethod
    def bstack11ll111l11l_opy_(config: dict) -> bool:
        bstack11l1111llll_opy_ = config.get(bstack1ll1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᭛"), {}).get(bstack111llll11ll_opy_, {})
        return bstack11l1111llll_opy_.get(bstack1ll1l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᭜"), False)
    @staticmethod
    def bstack11ll111l111_opy_(config: dict, bstack11l1llll1ll_opy_: int = 0) -> int:
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠬࠡࡹ࡫࡭ࡨ࡮ࠠࡤࡣࡱࠤࡧ࡫ࠠࡢࡰࠣࡥࡧࡹ࡯࡭ࡷࡷࡩࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡲࠡࡣࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡩ࡭࡬ࠦࠨࡥ࡫ࡦࡸ࠮ࡀࠠࡕࡪࡨࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡱࡷࡥࡱࡥࡴࡦࡵࡷࡷࠥ࠮ࡩ࡯ࡶࠬ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࠬࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᭝")
        bstack11l1111llll_opy_ = config.get(bstack1ll1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭞"), {}).get(bstack1ll1l_opy_ (u"ࠧࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪ࠭᭟"), {})
        bstack111llllll11_opy_ = 0
        bstack11l1111l1l1_opy_ = 0
        if bstack11111l1l_opy_.bstack11ll111l11l_opy_(config):
            bstack11l1111l1l1_opy_ = bstack11l1111llll_opy_.get(bstack1ll1l_opy_ (u"ࠨ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸ࠭᭠"), 5)
            if isinstance(bstack11l1111l1l1_opy_, str) and bstack11l1111l1l1_opy_.endswith(bstack1ll1l_opy_ (u"ࠩࠨࠫ᭡")):
                try:
                    percentage = int(bstack11l1111l1l1_opy_.strip(bstack1ll1l_opy_ (u"ࠪࠩࠬ᭢")))
                    if bstack11l1llll1ll_opy_ > 0:
                        bstack111llllll11_opy_ = math.ceil((percentage * bstack11l1llll1ll_opy_) / 100)
                    else:
                        raise ValueError(bstack1ll1l_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡰࡹࡸࡺࠠࡣࡧࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴ࠰ࠥ᭣"))
                except ValueError as e:
                    raise ValueError(bstack1ll1l_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧࠣࡺࡦࡲࡵࡦࠢࡩࡳࡷࠦ࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶ࠾ࠥࢁࡽࠣ᭤").format(bstack11l1111l1l1_opy_)) from e
            else:
                bstack111llllll11_opy_ = int(bstack11l1111l1l1_opy_)
        logger.info(bstack1ll1l_opy_ (u"ࠨࡍࡢࡺࠣࡪࡦ࡯࡬ࡶࡴࡨࡷࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡵࡨࡸࠥࡺ࡯࠻ࠢࡾࢁࠥ࠮ࡦࡳࡱࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽࠪࠤ᭥").format(bstack111llllll11_opy_, bstack11l1111l1l1_opy_))
        return bstack111llllll11_opy_
    def bstack11l1111l1ll_opy_(self):
        return self.bstack11l11111ll1_opy_
    def bstack111llllll1l_opy_(self):
        return self.bstack11l111l1l1l_opy_
    def bstack111lll111l1_opy_(self):
        return self.bstack111lll111ll_opy_
    def __111lll11ll1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack11l11111ll1_opy_ = bool(enabled)
            if mode not in [bstack1ll1l_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡈ࡬ࡶࡸࡺࠧ᭦"), bstack1ll1l_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡒࡲࡱࡿࠧ᭧")]:
                logger.warning(bstack1ll1l_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡳ࡯ࡥࡧࠣࠫࢀࢃࠧࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸ࡮ࡴࡧࠡࡶࡲࠤࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ࠴ࠢ᭨").format(mode))
                mode = bstack1ll1l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭩")
            self.bstack11l111l1l1l_opy_ = mode
            if source is None:
                self.bstack111lll111ll_opy_ = None
            elif isinstance(source, list):
                self.bstack111lll111ll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1ll1l_opy_ (u"ࠫ࠳ࡰࡳࡰࡰࠪ᭪")):
                self.bstack111lll111ll_opy_ = self._111llll11l1_opy_(source)
            self.__111llll111l_opy_()
        except Exception as e:
            logger.error(bstack1ll1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠ࠮ࠢࡨࡲࡦࡨ࡬ࡦࡦ࠽ࠤࢀࢃࠬࠡ࡯ࡲࡨࡪࡀࠠࡼࡿ࠯ࠤࡸࡵࡵࡳࡥࡨ࠾ࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧ᭫").format(enabled, mode, source, e))
    def bstack11l111ll11l_opy_(self):
        return self.bstack111lll1lll1_opy_
    def __11l111l1111_opy_(self, value):
        self.bstack111lll1lll1_opy_ = bool(value)
        self.__111llll111l_opy_()
    def bstack11l111l1lll_opy_(self):
        return self.bstack111lllll11l_opy_
    def __11l1111l11l_opy_(self, value):
        self.bstack111lllll11l_opy_ = bool(value)
        self.__111llll111l_opy_()
    def bstack111lll1l1ll_opy_(self):
        return self.bstack111llll1lll_opy_
    def __111lll11l1l_opy_(self, value):
        self.bstack111llll1lll_opy_ = bool(value)
        self.__111llll111l_opy_()
    def __111llll111l_opy_(self):
        if self.bstack11l11111ll1_opy_:
            self.bstack111lll1lll1_opy_ = False
            self.bstack111lllll11l_opy_ = False
            self.bstack111llll1lll_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111llll1l11_opy_)
        elif self.bstack111lll1lll1_opy_:
            self.bstack111lllll11l_opy_ = False
            self.bstack111llll1lll_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l1111l111_opy_)
        elif self.bstack111lllll11l_opy_:
            self.bstack111lll1lll1_opy_ = False
            self.bstack111llll1lll_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l111l11l1_opy_)
        elif self.bstack111llll1lll_opy_:
            self.bstack111lll1lll1_opy_ = False
            self.bstack111lllll11l_opy_ = False
            self.bstack11l11111ll1_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack111llll1111_opy_)
        else:
            self.bstack111lll11lll_opy_.disable()
    def bstack11111ll1_opy_(self):
        return self.bstack111lll11lll_opy_.bstack11l1111lll1_opy_()
    def bstack1111lll11_opy_(self):
        if self.bstack111lll11lll_opy_.bstack11l1111lll1_opy_():
            return self.bstack111lll11lll_opy_.get_name()
        return None
    def _111llll11l1_opy_(self, bstack111lllll111_opy_):
        bstack1ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡴࡱࡸࡶࡨ࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠥࡧ࡮ࡥࠢࡩࡳࡷࡳࡡࡵࠢ࡬ࡸࠥ࡬࡯ࡳࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡴࡻࡲࡤࡧࡢࡪ࡮ࡲࡥࡠࡲࡤࡸ࡭ࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡵࡪࡨࠤࡏ࡙ࡏࡏࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡇࡱࡵࡱࡦࡺࡴࡦࡦࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡷ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭬")
        if not os.path.isfile(bstack111lllll111_opy_):
            logger.error(bstack1ll1l_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡾࠩࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠧ᭭").format(bstack111lllll111_opy_))
            return []
        data = None
        try:
            with open(bstack111lllll111_opy_, bstack1ll1l_opy_ (u"ࠣࡴࠥ᭮")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1ll1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡍࡗࡔࡔࠠࡧࡴࡲࡱࠥࡹ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧ᭯").format(bstack111lllll111_opy_, e))
            return []
        _111lll1l11l_opy_ = None
        _111llll1ll1_opy_ = None
        def _111lll11l11_opy_():
            bstack11l11111l1l_opy_ = {}
            bstack111lll1l1l1_opy_ = {}
            try:
                if self.bstack111lll1l111_opy_.startswith(bstack1ll1l_opy_ (u"ࠪࡿࠬ᭰")) and self.bstack111lll1l111_opy_.endswith(bstack1ll1l_opy_ (u"ࠫࢂ࠭᭱")):
                    bstack11l11111l1l_opy_ = json.loads(self.bstack111lll1l111_opy_)
                else:
                    bstack11l11111l1l_opy_ = dict(item.split(bstack1ll1l_opy_ (u"ࠬࡀࠧ᭲")) for item in self.bstack111lll1l111_opy_.split(bstack1ll1l_opy_ (u"࠭ࠬࠨ᭳")) if bstack1ll1l_opy_ (u"ࠧ࠻ࠩ᭴") in item) if self.bstack111lll1l111_opy_ else {}
                if self.bstack111lll1ll1l_opy_.startswith(bstack1ll1l_opy_ (u"ࠨࡽࠪ᭵")) and self.bstack111lll1ll1l_opy_.endswith(bstack1ll1l_opy_ (u"ࠩࢀࠫ᭶")):
                    bstack111lll1l1l1_opy_ = json.loads(self.bstack111lll1ll1l_opy_)
                else:
                    bstack111lll1l1l1_opy_ = dict(item.split(bstack1ll1l_opy_ (u"ࠪ࠾ࠬ᭷")) for item in self.bstack111lll1ll1l_opy_.split(bstack1ll1l_opy_ (u"ࠫ࠱࠭᭸")) if bstack1ll1l_opy_ (u"ࠬࡀࠧ᭹") in item) if self.bstack111lll1ll1l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1ll1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴ࠼ࠣࡿࢂࠨ᭺").format(e))
            logger.debug(bstack1ll1l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࠿ࠦࡻࡾ࠮ࠣࡇࡑࡏ࠺ࠡࡽࢀࠦ᭻").format(bstack11l11111l1l_opy_, bstack111lll1l1l1_opy_))
            return bstack11l11111l1l_opy_, bstack111lll1l1l1_opy_
        if _111lll1l11l_opy_ is None or _111llll1ll1_opy_ is None:
            _111lll1l11l_opy_, _111llll1ll1_opy_ = _111lll11l11_opy_()
        def bstack111lll1ll11_opy_(name, bstack11l111l1ll1_opy_):
            if name in _111llll1ll1_opy_:
                return _111llll1ll1_opy_[name]
            if name in _111lll1l11l_opy_:
                return _111lll1l11l_opy_[name]
            if bstack11l111l1ll1_opy_.get(bstack1ll1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨ᭼")):
                return bstack11l111l1ll1_opy_[bstack1ll1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩ᭽")]
            return None
        if isinstance(data, dict):
            bstack11l111111l1_opy_ = []
            bstack11l111l11ll_opy_ = re.compile(bstack1ll1l_opy_ (u"ࡵࠫࡣࡡࡁ࠮࡜࠳࠱࠾ࡥ࡝ࠬࠦࠪ᭾"))
            for name, bstack11l111l1ll1_opy_ in data.items():
                if not isinstance(bstack11l111l1ll1_opy_, dict):
                    continue
                if not bstack11l111l1ll1_opy_.get(bstack1ll1l_opy_ (u"ࠫࡺࡸ࡬ࠨ᭿")):
                    logger.warning(bstack1ll1l_opy_ (u"ࠧࡘࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡘࡖࡑࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮀ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if not bstack11l111l11ll_opy_.match(name):
                    logger.warning(bstack1ll1l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮁ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1ll1l_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤࠬࢁࡽࠨࠢࡰࡹࡸࡺࠠࡩࡣࡹࡩࠥࡧࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡣࡧࡷࡻࡪ࡫࡮ࠡ࠳ࠣࡥࡳࡪࠠ࠴࠲ࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹ࠮ࠣᮂ").format(name))
                    continue
                bstack11l111l1ll1_opy_ = bstack11l111l1ll1_opy_.copy()
                bstack11l111l1ll1_opy_[bstack1ll1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᮃ")] = name
                bstack11l111l1ll1_opy_[bstack1ll1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮄ")] = bstack111lll1ll11_opy_(name, bstack11l111l1ll1_opy_)
                if not bstack11l111l1ll1_opy_.get(bstack1ll1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮅ")):
                    logger.warning(bstack1ll1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡴ࡯ࡵࠢࡶࡴࡪࡩࡩࡧ࡫ࡨࡨࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮆ").format(name, bstack11l111l1ll1_opy_))
                    continue
                if bstack11l111l1ll1_opy_.get(bstack1ll1l_opy_ (u"ࠬࡨࡡࡴࡧࡅࡶࡦࡴࡣࡩࠩᮇ")) and bstack11l111l1ll1_opy_[bstack1ll1l_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪᮈ")] == bstack11l111l1ll1_opy_[bstack1ll1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮉ")]:
                    logger.warning(bstack1ll1l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡤࡲࡩࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮊ").format(name, bstack11l111l1ll1_opy_))
                    continue
                bstack11l111111l1_opy_.append(bstack11l111l1ll1_opy_)
            return bstack11l111111l1_opy_
        return data
    def bstack111llll1l1l_opy_(self):
        data = {
            bstack1ll1l_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᮋ"): {
                bstack1ll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮌ"): self.bstack11l1111l1ll_opy_(),
                bstack1ll1l_opy_ (u"ࠫࡲࡵࡤࡦࠩᮍ"): self.bstack111llllll1l_opy_(),
                bstack1ll1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᮎ"): self.bstack111lll111l1_opy_()
            }
        }
        return data
    def bstack111lllll1ll_opy_(self, config):
        bstack11l11111l11_opy_ = {}
        bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᮏ")] = {
            bstack1ll1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮐ"): self.bstack11l1111l1ll_opy_(),
            bstack1ll1l_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭ᮑ"): self.bstack111llllll1l_opy_()
        }
        bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࠬᮒ")] = {
            bstack1ll1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮓ"): self.bstack11l111l1lll_opy_()
        }
        bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"ࠫࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࡤ࡬ࡩࡳࡵࡷࠫᮔ")] = {
            bstack1ll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮕ"): self.bstack11l111ll11l_opy_()
        }
        bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡣ࡫ࡧࡩ࡭࡫ࡱ࡫ࡤࡧ࡮ࡥࡡࡩࡰࡦࡱࡹࠨᮖ")] = {
            bstack1ll1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮗ"): self.bstack111lll1l1ll_opy_()
        }
        if self.bstack1111ll1l_opy_(config):
            bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"ࠨࡴࡨࡸࡷࡿ࡟ࡵࡧࡶࡸࡸࡥ࡯࡯ࡡࡩࡥ࡮ࡲࡵࡳࡧࠪᮘ")] = {
                bstack1ll1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮙ"): True,
                bstack1ll1l_opy_ (u"ࠪࡱࡦࡾ࡟ࡳࡧࡷࡶ࡮࡫ࡳࠨᮚ"): self.bstack11l11l11_opy_(config)
            }
        if self.bstack11ll111l11l_opy_(config):
            bstack11l11111l11_opy_[bstack1ll1l_opy_ (u"ࠫࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᮛ")] = {
                bstack1ll1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮜ"): True,
                bstack1ll1l_opy_ (u"࠭࡭ࡢࡺࡢࡪࡦ࡯࡬ࡶࡴࡨࡷࠬᮝ"): self.bstack11ll111l111_opy_(config)
            }
        return bstack11l11111l11_opy_
    def bstack111llll11l_opy_(self, config):
        bstack1ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡵ࡬࡭ࡧࡦࡸࡸࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡦࡾࠦ࡭ࡢ࡭࡬ࡲ࡬ࠦࡡࠡࡥࡤࡰࡱࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠢࠫࡷࡹࡸࠩ࠻ࠢࡗ࡬ࡪࠦࡕࡖࡋࡇࠤࡴ࡬ࠠࡵࡪࡨࠤࡧࡻࡩ࡭ࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᮞ")
        if not (config.get(bstack1ll1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᮟ"), None) in bstack11l11lll11l_opy_ and self.bstack11l1111l1ll_opy_()):
            return None
        bstack11l111ll111_opy_ = os.environ.get(bstack1ll1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᮠ"), None)
        logger.debug(bstack1ll1l_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢᮡ").format(bstack11l111ll111_opy_))
        try:
            bstack11ll11l1lll_opy_ = bstack1ll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠤᮢ").format(bstack11l111ll111_opy_)
            payload = {
                bstack1ll1l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᮣ"): config.get(bstack1ll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᮤ"), bstack1ll1l_opy_ (u"ࠧࠨᮥ")),
                bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᮦ"): config.get(bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᮧ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᮨ"): os.environ.get(bstack1ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᮩ"), bstack1ll1l_opy_ (u"ࠧࠨ᮪")),
                bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤ᮫"): int(os.environ.get(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᮬ")) or bstack1ll1l_opy_ (u"ࠣ࠲ࠥᮭ")),
                bstack1ll1l_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨᮮ"): int(os.environ.get(bstack1ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᮯ")) or bstack1ll1l_opy_ (u"ࠦ࠶ࠨ᮰")),
                bstack1ll1l_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢ᮱"): get_host_info(),
            }
            logger.debug(bstack1ll1l_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡳࡥࡾࡲ࡯ࡢࡦ࠽ࠤࢀࢃࠢ᮲").format(payload))
            response = bstack11ll1ll1ll1_opy_.bstack11ll11l1l1l_opy_(bstack11ll11l1lll_opy_, payload)
            if response:
                logger.debug(bstack1ll1l_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡈࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧ᮳").format(response))
                return response
            else:
                logger.error(bstack1ll1l_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧ᮴").format(bstack11l111ll111_opy_))
                return None
        except Exception as e:
            logger.error(bstack1ll1l_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄࠡࡽࢀ࠾ࠥࢁࡽࠣ᮵").format(bstack11l111ll111_opy_, e))
            return None
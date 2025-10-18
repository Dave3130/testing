# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack11l1l1l1ll_opy_
from bstack_utils.constants import bstack111l1ll111_opy_, bstack11l1l11lll1_opy_
from bstack_utils.helper import bstack11ll1l1l1ll_opy_, get_host_info
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l1l111_opy_
import json
import re
import sys
bstack11l1111lll1_opy_ = bstack11ll_opy_ (u"ࠣࡴࡨࡸࡷࡿࡔࡦࡵࡷࡷࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢ᭧")
bstack111lllll111_opy_ = bstack11ll_opy_ (u"ࠤࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣ᭨")
bstack11l1111l11l_opy_ = bstack11ll_opy_ (u"ࠥࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࡈ࡬ࡶࡸࡺࠢ᭩")
bstack111lll11lll_opy_ = bstack11ll_opy_ (u"ࠦࡷ࡫ࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࠧ᭪")
bstack11l11111ll1_opy_ = bstack11ll_opy_ (u"ࠧࡹ࡫ࡪࡲࡉࡰࡦࡱࡹࡢࡰࡧࡊࡦ࡯࡬ࡦࡦࠥ᭫")
bstack111llll1ll1_opy_ = bstack11ll_opy_ (u"ࠨࡲࡶࡰࡖࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰ᭬ࠥ")
bstack11l11111lll_opy_ = {
    bstack11l1111lll1_opy_,
    bstack111lllll111_opy_,
    bstack11l1111l11l_opy_,
    bstack111lll11lll_opy_,
    bstack11l11111ll1_opy_,
    bstack111llll1ll1_opy_
}
bstack111lll1l1ll_opy_ = {bstack11ll_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ᭭")}
logger = bstack11l1l1l1ll_opy_.get_logger(__name__, bstack111l1ll111_opy_)
class bstack111lll11111_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111lllll1ll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack111ll1ll_opy_:
    _1ll1ll1111l_opy_ = None
    def __init__(self, config):
        self.bstack111llll1l1l_opy_ = False
        self.bstack111lll1111l_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack111llll11ll_opy_ = False
        self.bstack111ll1llll1_opy_ = None
        self.bstack111lll111l1_opy_ = bstack111lll11111_opy_()
        self.bstack111lll11l1l_opy_ = None
        opts = config.get(bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭮"), {})
        self.bstack11l1111l1l1_opy_ = config.get(bstack11ll_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡉࡓ࡜ࠧ᭯"), bstack11ll_opy_ (u"ࠥࠦ᭰"))
        self.bstack111llll11l1_opy_ = config.get(bstack11ll_opy_ (u"ࠫࡸࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࡋ࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࡩࡸࡉࡌࡊࠩ᭱"), bstack11ll_opy_ (u"ࠧࠨ᭲"))
        bstack111lll11ll1_opy_ = opts.get(bstack111llll1ll1_opy_, {})
        bstack111ll1lllll_opy_ = None
        if bstack11ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭᭳") in bstack111lll11ll1_opy_:
            bstack111ll1lllll_opy_ = bstack111lll11ll1_opy_[bstack11ll_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ᭴")]
            if bstack111ll1lllll_opy_ is None:
                bstack111ll1lllll_opy_ = []
        self.__11l1111llll_opy_(
            bstack111lll11ll1_opy_.get(bstack11ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩ᭵"), False),
            bstack111lll11ll1_opy_.get(bstack11ll_opy_ (u"ࠩࡰࡳࡩ࡫ࠧ᭶"), bstack11ll_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭷")),
            bstack111ll1lllll_opy_
        )
        self.__111lll1l11l_opy_(opts.get(bstack11l1111l11l_opy_, False))
        self.__111ll1ll1l1_opy_(opts.get(bstack111lll11lll_opy_, False))
        self.__111lll1l1l1_opy_(opts.get(bstack11l11111ll1_opy_, False))
    @classmethod
    def bstack11111ll1_opy_(cls, config=None):
        if cls._1ll1ll1111l_opy_ is None and config is not None:
            cls._1ll1ll1111l_opy_ = bstack111ll1ll_opy_(config)
        return cls._1ll1ll1111l_opy_
    @staticmethod
    def bstack111l1l1l_opy_(config: dict) -> bool:
        bstack11l111111ll_opy_ = config.get(bstack11ll_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭸"), {}).get(bstack11l1111lll1_opy_, {})
        return bstack11l111111ll_opy_.get(bstack11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭹"), False)
    @staticmethod
    def bstack1111l1ll_opy_(config: dict) -> int:
        bstack11l111111ll_opy_ = config.get(bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭺"), {}).get(bstack11l1111lll1_opy_, {})
        retries = 0
        if bstack111ll1ll_opy_.bstack111l1l1l_opy_(config):
            retries = bstack11l111111ll_opy_.get(bstack11ll_opy_ (u"ࠧ࡮ࡣࡻࡖࡪࡺࡲࡪࡧࡶࠫ᭻"), 1)
        return retries
    @staticmethod
    def bstack1l11ll1ll_opy_(config: dict) -> dict:
        bstack11l11111l11_opy_ = config.get(bstack11ll_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭼"), {})
        return {
            key: value for key, value in bstack11l11111l11_opy_.items() if key in bstack11l11111lll_opy_
        }
    @staticmethod
    def bstack11l11111l1l_opy_():
        bstack11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭽")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦ᭾").format(os.getenv(bstack11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᭿")))))
    @staticmethod
    def bstack11l1111ll11_opy_(test_name: str):
        bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᮀ")
        bstack11l1111ll1l_opy_ = os.path.join(tempfile.gettempdir(), bstack11ll_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧᮁ").format(os.getenv(bstack11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧᮂ"))))
        with open(bstack11l1111ll1l_opy_, bstack11ll_opy_ (u"ࠨࡣࠪᮃ")) as file:
            file.write(bstack11ll_opy_ (u"ࠤࡾࢁࡡࡴࠢᮄ").format(test_name))
    @staticmethod
    def bstack111lll1lll1_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll1l1ll_opy_
    @staticmethod
    def bstack11ll1111111_opy_(config: dict) -> bool:
        bstack111lll1l111_opy_ = config.get(bstack11ll_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᮅ"), {}).get(bstack111lllll111_opy_, {})
        return bstack111lll1l111_opy_.get(bstack11ll_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮆ"), False)
    @staticmethod
    def bstack11l1lll1lll_opy_(config: dict, bstack11l1lll1111_opy_: int = 0) -> int:
        bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠬࠡࡹ࡫࡭ࡨ࡮ࠠࡤࡣࡱࠤࡧ࡫ࠠࡢࡰࠣࡥࡧࡹ࡯࡭ࡷࡷࡩࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡲࠡࡣࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡩ࡭࡬ࠦࠨࡥ࡫ࡦࡸ࠮ࡀࠠࡕࡪࡨࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡱࡷࡥࡱࡥࡴࡦࡵࡷࡷࠥ࠮ࡩ࡯ࡶࠬ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࠬࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᮇ")
        bstack111lll1l111_opy_ = config.get(bstack11ll_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮈ"), {}).get(bstack11ll_opy_ (u"ࠧࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪ࠭ᮉ"), {})
        bstack11l111111l1_opy_ = 0
        bstack111lll111ll_opy_ = 0
        if bstack111ll1ll_opy_.bstack11ll1111111_opy_(config):
            bstack111lll111ll_opy_ = bstack111lll1l111_opy_.get(bstack11ll_opy_ (u"ࠨ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸ࠭ᮊ"), 5)
            if isinstance(bstack111lll111ll_opy_, str) and bstack111lll111ll_opy_.endswith(bstack11ll_opy_ (u"ࠩࠨࠫᮋ")):
                try:
                    percentage = int(bstack111lll111ll_opy_.strip(bstack11ll_opy_ (u"ࠪࠩࠬᮌ")))
                    if bstack11l1lll1111_opy_ > 0:
                        bstack11l111111l1_opy_ = math.ceil((percentage * bstack11l1lll1111_opy_) / 100)
                    else:
                        raise ValueError(bstack11ll_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡰࡹࡸࡺࠠࡣࡧࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴ࠰ࠥᮍ"))
                except ValueError as e:
                    raise ValueError(bstack11ll_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧࠣࡺࡦࡲࡵࡦࠢࡩࡳࡷࠦ࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶ࠾ࠥࢁࡽࠣᮎ").format(bstack111lll111ll_opy_)) from e
            else:
                bstack11l111111l1_opy_ = int(bstack111lll111ll_opy_)
        logger.info(bstack11ll_opy_ (u"ࠨࡍࡢࡺࠣࡪࡦ࡯࡬ࡶࡴࡨࡷࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡵࡨࡸࠥࡺ࡯࠻ࠢࡾࢁࠥ࠮ࡦࡳࡱࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽࠪࠤᮏ").format(bstack11l111111l1_opy_, bstack111lll111ll_opy_))
        return bstack11l111111l1_opy_
    def bstack111ll1ll111_opy_(self):
        return self.bstack111llll11ll_opy_
    def bstack111llllll11_opy_(self):
        return self.bstack111ll1llll1_opy_
    def bstack11l11111111_opy_(self):
        return self.bstack111lll11l1l_opy_
    def __11l1111llll_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll11ll_opy_ = bool(enabled)
            if mode not in [bstack11ll_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡈ࡬ࡶࡸࡺࠧᮐ"), bstack11ll_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡒࡲࡱࡿࠧᮑ")]:
                logger.warning(bstack11ll_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡳ࡯ࡥࡧࠣࠫࢀࢃࠧࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸ࡮ࡴࡧࠡࡶࡲࠤࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ࠴ࠢᮒ").format(mode))
                mode = bstack11ll_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪᮓ")
            self.bstack111ll1llll1_opy_ = mode
            if source is None:
                self.bstack111lll11l1l_opy_ = None
            elif isinstance(source, list):
                self.bstack111lll11l1l_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11ll_opy_ (u"ࠫ࠳ࡰࡳࡰࡰࠪᮔ")):
                self.bstack111lll11l1l_opy_ = self._111lll1llll_opy_(source)
            self.__11l1111111l_opy_()
        except Exception as e:
            logger.error(bstack11ll_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠ࠮ࠢࡨࡲࡦࡨ࡬ࡦࡦ࠽ࠤࢀࢃࠬࠡ࡯ࡲࡨࡪࡀࠠࡼࡿ࠯ࠤࡸࡵࡵࡳࡥࡨ࠾ࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᮕ").format(enabled, mode, source, e))
    def bstack111ll1lll1l_opy_(self):
        return self.bstack111llll1l1l_opy_
    def __111lll1l11l_opy_(self, value):
        self.bstack111llll1l1l_opy_ = bool(value)
        self.__11l1111111l_opy_()
    def bstack111lllllll1_opy_(self):
        return self.bstack111lll1111l_opy_
    def __111ll1ll1l1_opy_(self, value):
        self.bstack111lll1111l_opy_ = bool(value)
        self.__11l1111111l_opy_()
    def bstack111lll1ll1l_opy_(self):
        return self.bstack111llll1111_opy_
    def __111lll1l1l1_opy_(self, value):
        self.bstack111llll1111_opy_ = bool(value)
        self.__11l1111111l_opy_()
    def __11l1111111l_opy_(self):
        if self.bstack111llll11ll_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111lll1111l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll111l1_opy_.enable(bstack111llll1ll1_opy_)
        elif self.bstack111llll1l1l_opy_:
            self.bstack111lll1111l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll11ll_opy_ = False
            self.bstack111lll111l1_opy_.enable(bstack11l1111l11l_opy_)
        elif self.bstack111lll1111l_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111llll11ll_opy_ = False
            self.bstack111lll111l1_opy_.enable(bstack111lll11lll_opy_)
        elif self.bstack111llll1111_opy_:
            self.bstack111llll1l1l_opy_ = False
            self.bstack111lll1111l_opy_ = False
            self.bstack111llll11ll_opy_ = False
            self.bstack111lll111l1_opy_.enable(bstack11l11111ll1_opy_)
        else:
            self.bstack111lll111l1_opy_.disable()
    def bstack1111111l_opy_(self):
        return self.bstack111lll111l1_opy_.bstack111lllll1ll_opy_()
    def bstack1l111lll11_opy_(self):
        if self.bstack111lll111l1_opy_.bstack111lllll1ll_opy_():
            return self.bstack111lll111l1_opy_.get_name()
        return None
    def _111lll1llll_opy_(self, bstack111lll11l11_opy_):
        bstack11ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡴࡱࡸࡶࡨ࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠥࡧ࡮ࡥࠢࡩࡳࡷࡳࡡࡵࠢ࡬ࡸࠥ࡬࡯ࡳࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡴࡻࡲࡤࡧࡢࡪ࡮ࡲࡥࡠࡲࡤࡸ࡭ࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡵࡪࡨࠤࡏ࡙ࡏࡏࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡇࡱࡵࡱࡦࡺࡴࡦࡦࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡷ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮖ")
        if not os.path.isfile(bstack111lll11l11_opy_):
            logger.error(bstack11ll_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡾࠩࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠧᮗ").format(bstack111lll11l11_opy_))
            return []
        data = None
        try:
            with open(bstack111lll11l11_opy_, bstack11ll_opy_ (u"ࠣࡴࠥᮘ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11ll_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡍࡗࡔࡔࠠࡧࡴࡲࡱࠥࡹ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮙ").format(bstack111lll11l11_opy_, e))
            return []
        _111lllll11l_opy_ = None
        _111lllll1l1_opy_ = None
        def _111ll1ll1ll_opy_():
            bstack111llllllll_opy_ = {}
            bstack11l1111l111_opy_ = {}
            try:
                if self.bstack11l1111l1l1_opy_.startswith(bstack11ll_opy_ (u"ࠪࡿࠬᮚ")) and self.bstack11l1111l1l1_opy_.endswith(bstack11ll_opy_ (u"ࠫࢂ࠭ᮛ")):
                    bstack111llllllll_opy_ = json.loads(self.bstack11l1111l1l1_opy_)
                else:
                    bstack111llllllll_opy_ = dict(item.split(bstack11ll_opy_ (u"ࠬࡀࠧᮜ")) for item in self.bstack11l1111l1l1_opy_.split(bstack11ll_opy_ (u"࠭ࠬࠨᮝ")) if bstack11ll_opy_ (u"ࠧ࠻ࠩᮞ") in item) if self.bstack11l1111l1l1_opy_ else {}
                if self.bstack111llll11l1_opy_.startswith(bstack11ll_opy_ (u"ࠨࡽࠪᮟ")) and self.bstack111llll11l1_opy_.endswith(bstack11ll_opy_ (u"ࠩࢀࠫᮠ")):
                    bstack11l1111l111_opy_ = json.loads(self.bstack111llll11l1_opy_)
                else:
                    bstack11l1111l111_opy_ = dict(item.split(bstack11ll_opy_ (u"ࠪ࠾ࠬᮡ")) for item in self.bstack111llll11l1_opy_.split(bstack11ll_opy_ (u"ࠫ࠱࠭ᮢ")) if bstack11ll_opy_ (u"ࠬࡀࠧᮣ") in item) if self.bstack111llll11l1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11ll_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴ࠼ࠣࡿࢂࠨᮤ").format(e))
            logger.debug(bstack11ll_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࠿ࠦࡻࡾ࠮ࠣࡇࡑࡏ࠺ࠡࡽࢀࠦᮥ").format(bstack111llllllll_opy_, bstack11l1111l111_opy_))
            return bstack111llllllll_opy_, bstack11l1111l111_opy_
        if _111lllll11l_opy_ is None or _111lllll1l1_opy_ is None:
            _111lllll11l_opy_, _111lllll1l1_opy_ = _111ll1ll1ll_opy_()
        def bstack111ll1ll11l_opy_(name, bstack111ll1lll11_opy_):
            if name in _111lllll1l1_opy_:
                return _111lllll1l1_opy_[name]
            if name in _111lllll11l_opy_:
                return _111lllll11l_opy_[name]
            if bstack111ll1lll11_opy_.get(bstack11ll_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮦ")):
                return bstack111ll1lll11_opy_[bstack11ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮧ")]
            return None
        if isinstance(data, dict):
            bstack111llll111l_opy_ = []
            bstack111llllll1l_opy_ = re.compile(bstack11ll_opy_ (u"ࡵࠫࡣࡡࡁ࠮࡜࠳࠱࠾ࡥ࡝ࠬࠦࠪᮨ"))
            for name, bstack111ll1lll11_opy_ in data.items():
                if not isinstance(bstack111ll1lll11_opy_, dict):
                    continue
                if not bstack111ll1lll11_opy_.get(bstack11ll_opy_ (u"ࠫࡺࡸ࡬ࠨᮩ")):
                    logger.warning(bstack11ll_opy_ (u"ࠧࡘࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡘࡖࡑࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤ᮪").format(name, bstack111ll1lll11_opy_))
                    continue
                if not bstack111llllll1l_opy_.match(name):
                    logger.warning(bstack11ll_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡࠩࡾࢁࠬࡀࠠࡼࡿ᮫ࠥ").format(name, bstack111ll1lll11_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11ll_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤࠬࢁࡽࠨࠢࡰࡹࡸࡺࠠࡩࡣࡹࡩࠥࡧࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡣࡧࡷࡻࡪ࡫࡮ࠡ࠳ࠣࡥࡳࡪࠠ࠴࠲ࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹ࠮ࠣᮬ").format(name))
                    continue
                bstack111ll1lll11_opy_ = bstack111ll1lll11_opy_.copy()
                bstack111ll1lll11_opy_[bstack11ll_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᮭ")] = name
                bstack111ll1lll11_opy_[bstack11ll_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮮ")] = bstack111ll1ll11l_opy_(name, bstack111ll1lll11_opy_)
                if not bstack111ll1lll11_opy_.get(bstack11ll_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮯ")):
                    logger.warning(bstack11ll_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡴ࡯ࡵࠢࡶࡴࡪࡩࡩࡧ࡫ࡨࡨࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᮰").format(name, bstack111ll1lll11_opy_))
                    continue
                if bstack111ll1lll11_opy_.get(bstack11ll_opy_ (u"ࠬࡨࡡࡴࡧࡅࡶࡦࡴࡣࡩࠩ᮱")) and bstack111ll1lll11_opy_[bstack11ll_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪ᮲")] == bstack111ll1lll11_opy_[bstack11ll_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧ᮳")]:
                    logger.warning(bstack11ll_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡤࡲࡩࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣ᮴").format(name, bstack111ll1lll11_opy_))
                    continue
                bstack111llll111l_opy_.append(bstack111ll1lll11_opy_)
            return bstack111llll111l_opy_
        return data
    def bstack111llll1lll_opy_(self):
        data = {
            bstack11ll_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨ᮵"): {
                bstack11ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᮶"): self.bstack111ll1ll111_opy_(),
                bstack11ll_opy_ (u"ࠫࡲࡵࡤࡦࠩ᮷"): self.bstack111llllll11_opy_(),
                bstack11ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᮸"): self.bstack11l11111111_opy_()
            }
        }
        return data
    def bstack111llll1l11_opy_(self, config):
        bstack111lll1ll11_opy_ = {}
        bstack111lll1ll11_opy_[bstack11ll_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬ᮹")] = {
            bstack11ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮺ"): self.bstack111ll1ll111_opy_(),
            bstack11ll_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭ᮻ"): self.bstack111llllll11_opy_()
        }
        bstack111lll1ll11_opy_[bstack11ll_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࠬᮼ")] = {
            bstack11ll_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮽ"): self.bstack111lllllll1_opy_()
        }
        bstack111lll1ll11_opy_[bstack11ll_opy_ (u"ࠫࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࡤ࡬ࡩࡳࡵࡷࠫᮾ")] = {
            bstack11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮿ"): self.bstack111ll1lll1l_opy_()
        }
        bstack111lll1ll11_opy_[bstack11ll_opy_ (u"࠭ࡳ࡬࡫ࡳࡣ࡫ࡧࡩ࡭࡫ࡱ࡫ࡤࡧ࡮ࡥࡡࡩࡰࡦࡱࡹࠨᯀ")] = {
            bstack11ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯁ"): self.bstack111lll1ll1l_opy_()
        }
        if self.bstack111l1l1l_opy_(config):
            bstack111lll1ll11_opy_[bstack11ll_opy_ (u"ࠨࡴࡨࡸࡷࡿ࡟ࡵࡧࡶࡸࡸࡥ࡯࡯ࡡࡩࡥ࡮ࡲࡵࡳࡧࠪᯂ")] = {
                bstack11ll_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᯃ"): True,
                bstack11ll_opy_ (u"ࠪࡱࡦࡾ࡟ࡳࡧࡷࡶ࡮࡫ࡳࠨᯄ"): self.bstack1111l1ll_opy_(config)
            }
        if self.bstack11ll1111111_opy_(config):
            bstack111lll1ll11_opy_[bstack11ll_opy_ (u"ࠫࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᯅ")] = {
                bstack11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯆ"): True,
                bstack11ll_opy_ (u"࠭࡭ࡢࡺࡢࡪࡦ࡯࡬ࡶࡴࡨࡷࠬᯇ"): self.bstack11l1lll1lll_opy_(config)
            }
        return bstack111lll1ll11_opy_
    def bstack111lll1l11_opy_(self, config):
        bstack11ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡵ࡬࡭ࡧࡦࡸࡸࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡦࡾࠦ࡭ࡢ࡭࡬ࡲ࡬ࠦࡡࠡࡥࡤࡰࡱࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠢࠫࡷࡹࡸࠩ࠻ࠢࡗ࡬ࡪࠦࡕࡖࡋࡇࠤࡴ࡬ࠠࡵࡪࡨࠤࡧࡻࡩ࡭ࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᯈ")
        if not (config.get(bstack11ll_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᯉ"), None) in bstack11l1l11lll1_opy_ and self.bstack111ll1ll111_opy_()):
            return None
        bstack11l1111l1ll_opy_ = os.environ.get(bstack11ll_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᯊ"), None)
        logger.debug(bstack11ll_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢᯋ").format(bstack11l1111l1ll_opy_))
        try:
            bstack11ll111l11l_opy_ = bstack11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠤᯌ").format(bstack11l1111l1ll_opy_)
            payload = {
                bstack11ll_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᯍ"): config.get(bstack11ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᯎ"), bstack11ll_opy_ (u"ࠧࠨᯏ")),
                bstack11ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᯐ"): config.get(bstack11ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᯑ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᯒ"): os.environ.get(bstack11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᯓ"), bstack11ll_opy_ (u"ࠧࠨᯔ")),
                bstack11ll_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤᯕ"): int(os.environ.get(bstack11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᯖ")) or bstack11ll_opy_ (u"ࠣ࠲ࠥᯗ")),
                bstack11ll_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨᯘ"): int(os.environ.get(bstack11ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᯙ")) or bstack11ll_opy_ (u"ࠦ࠶ࠨᯚ")),
                bstack11ll_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᯛ"): get_host_info(),
            }
            logger.debug(bstack11ll_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡳࡥࡾࡲ࡯ࡢࡦ࠽ࠤࢀࢃࠢᯜ").format(payload))
            response = bstack11ll1l1l111_opy_.bstack11ll111ll11_opy_(bstack11ll111l11l_opy_, payload)
            if response:
                logger.debug(bstack11ll_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡈࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᯝ").format(response))
                return response
            else:
                logger.error(bstack11ll_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᯞ").format(bstack11l1111l1ll_opy_))
                return None
        except Exception as e:
            logger.error(bstack11ll_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄࠡࡽࢀ࠾ࠥࢁࡽࠣᯟ").format(bstack11l1111l1ll_opy_, e))
            return None
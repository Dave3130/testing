# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1l11l1lll_opy_
from bstack_utils.constants import bstack111l111ll1_opy_, bstack11l11l1l1l1_opy_
from bstack_utils.helper import bstack11ll1llllll_opy_, get_host_info
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11lll111111_opy_
import json
import re
import sys
bstack11l1111l1ll_opy_ = bstack111l1l_opy_ (u"ࠣࡴࡨࡸࡷࡿࡔࡦࡵࡷࡷࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢ᭠")
bstack11l111111l1_opy_ = bstack111l1l_opy_ (u"ࠤࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠣ᭡")
bstack11l111111ll_opy_ = bstack111l1l_opy_ (u"ࠥࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࡈ࡬ࡶࡸࡺࠢ᭢")
bstack111llll1ll1_opy_ = bstack111l1l_opy_ (u"ࠦࡷ࡫ࡲࡶࡰࡓࡶࡪࡼࡩࡰࡷࡶࡰࡾࡌࡡࡪ࡮ࡨࡨࠧ᭣")
bstack111llllll1l_opy_ = bstack111l1l_opy_ (u"ࠧࡹ࡫ࡪࡲࡉࡰࡦࡱࡹࡢࡰࡧࡊࡦ࡯࡬ࡦࡦࠥ᭤")
bstack11l11111111_opy_ = bstack111l1l_opy_ (u"ࠨࡲࡶࡰࡖࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࠥ᭥")
bstack111llll1lll_opy_ = {
    bstack11l1111l1ll_opy_,
    bstack11l111111l1_opy_,
    bstack11l111111ll_opy_,
    bstack111llll1ll1_opy_,
    bstack111llllll1l_opy_,
    bstack11l11111111_opy_
}
bstack111lll11lll_opy_ = {bstack111l1l_opy_ (u"ࠧࡱࡻࡷࡩࡸࡺࠧ᭦")}
logger = bstack1l11l1lll_opy_.get_logger(__name__, bstack111l111ll1_opy_)
class bstack11l11111ll1_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111llll1l11_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1llll1lll_opy_:
    _1ll1l1lll1l_opy_ = None
    def __init__(self, config):
        self.bstack11l1111l1l1_opy_ = False
        self.bstack111llll111l_opy_ = False
        self.bstack111lll1l1l1_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack111llll11ll_opy_ = None
        self.bstack11l1111lll1_opy_ = bstack11l11111ll1_opy_()
        self.bstack111llll11l1_opy_ = None
        opts = config.get(bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭧"), {})
        self.bstack111lllll11l_opy_ = config.get(bstack111l1l_opy_ (u"ࠩࡶࡱࡦࡸࡴࡔࡧ࡯ࡩࡨࡺࡩࡰࡰࡉࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࡧࡶࡉࡓ࡜ࠧ᭨"), bstack111l1l_opy_ (u"ࠥࠦ᭩"))
        self.bstack11l11111l11_opy_ = config.get(bstack111l1l_opy_ (u"ࠫࡸࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࡋ࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࡩࡸࡉࡌࡊࠩ᭪"), bstack111l1l_opy_ (u"ࠧࠨ᭫"))
        bstack11l11111l1l_opy_ = opts.get(bstack11l11111111_opy_, {})
        bstack111lllll1ll_opy_ = None
        if bstack111l1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ᭬࠭") in bstack11l11111l1l_opy_:
            bstack111lllll1ll_opy_ = bstack11l11111l1l_opy_[bstack111l1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧ᭭")]
            if bstack111lllll1ll_opy_ is None:
                bstack111lllll1ll_opy_ = []
        self.__111ll1llll1_opy_(
            bstack11l11111l1l_opy_.get(bstack111l1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩ᭮"), False),
            bstack11l11111l1l_opy_.get(bstack111l1l_opy_ (u"ࠩࡰࡳࡩ࡫ࠧ᭯"), bstack111l1l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪ᭰")),
            bstack111lllll1ll_opy_
        )
        self.__111ll1ll1ll_opy_(opts.get(bstack11l111111ll_opy_, False))
        self.__11l11111lll_opy_(opts.get(bstack111llll1ll1_opy_, False))
        self.__111lll1111l_opy_(opts.get(bstack111llllll1l_opy_, False))
    @classmethod
    def bstack1111ll1l_opy_(cls, config=None):
        if cls._1ll1l1lll1l_opy_ is None and config is not None:
            cls._1ll1l1lll1l_opy_ = bstack1llll1lll_opy_(config)
        return cls._1ll1l1lll1l_opy_
    @staticmethod
    def bstack1llll1l11_opy_(config: dict) -> bool:
        bstack111lll111ll_opy_ = config.get(bstack111l1l_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭱"), {}).get(bstack11l1111l1ll_opy_, {})
        return bstack111lll111ll_opy_.get(bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭲"), False)
    @staticmethod
    def bstack1111l111_opy_(config: dict) -> int:
        bstack111lll111ll_opy_ = config.get(bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪ᭳"), {}).get(bstack11l1111l1ll_opy_, {})
        retries = 0
        if bstack1llll1lll_opy_.bstack1llll1l11_opy_(config):
            retries = bstack111lll111ll_opy_.get(bstack111l1l_opy_ (u"ࠧ࡮ࡣࡻࡖࡪࡺࡲࡪࡧࡶࠫ᭴"), 1)
        return retries
    @staticmethod
    def bstack1l1l11111l_opy_(config: dict) -> dict:
        bstack111ll1ll11l_opy_ = config.get(bstack111l1l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭵"), {})
        return {
            key: value for key, value in bstack111ll1ll11l_opy_.items() if key in bstack111llll1lll_opy_
        }
    @staticmethod
    def bstack11l1111ll11_opy_():
        bstack111l1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡩࡧࡦ࡯ࠥ࡯ࡦࠡࡶ࡫ࡩࠥࡧࡢࡰࡴࡷࠤࡧࡻࡩ࡭ࡦࠣࡪ࡮ࡲࡥࠡࡧࡻ࡭ࡸࡺࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨ᭶")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠥࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡽࢀࠦ᭷").format(os.getenv(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠤ᭸")))))
    @staticmethod
    def bstack111lll11l1l_opy_(test_name: str):
        bstack111l1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡆ࡬ࡪࡩ࡫ࠡ࡫ࡩࠤࡹ࡮ࡥࠡࡣࡥࡳࡷࡺࠠࡣࡷ࡬ࡰࡩࠦࡦࡪ࡮ࡨࠤࡪࡾࡩࡴࡶࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭹")
        bstack111lll1l11l_opy_ = os.path.join(tempfile.gettempdir(), bstack111l1l_opy_ (u"ࠨࡦࡢ࡫࡯ࡩࡩࡥࡴࡦࡵࡷࡷࡤࢁࡽ࠯ࡶࡻࡸࠧ᭺").format(os.getenv(bstack111l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡆࡕࡗࡌ࡚ࡈ࡟ࡖࡗࡌࡈࠧ᭻"))))
        with open(bstack111lll1l11l_opy_, bstack111l1l_opy_ (u"ࠨࡣࠪ᭼")) as file:
            file.write(bstack111l1l_opy_ (u"ࠤࡾࢁࡡࡴࠢ᭽").format(test_name))
    @staticmethod
    def bstack111llllllll_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll11lll_opy_
    @staticmethod
    def bstack11l1llll1ll_opy_(config: dict) -> bool:
        bstack111lll1ll1l_opy_ = config.get(bstack111l1l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᭾"), {}).get(bstack11l111111l1_opy_, {})
        return bstack111lll1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᭿"), False)
    @staticmethod
    def bstack11l1llll11l_opy_(config: dict, bstack11l1lll1l11_opy_: int = 0) -> int:
        bstack111l1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡊࡩࡹࠦࡴࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠬࠡࡹ࡫࡭ࡨ࡮ࠠࡤࡣࡱࠤࡧ࡫ࠠࡢࡰࠣࡥࡧࡹ࡯࡭ࡷࡷࡩࠥࡴࡵ࡮ࡤࡨࡶࠥࡵࡲࠡࡣࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡣࡰࡰࡩ࡭࡬ࠦࠨࡥ࡫ࡦࡸ࠮ࡀࠠࡕࡪࡨࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡹ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡵࡱࡷࡥࡱࡥࡴࡦࡵࡷࡷࠥ࠮ࡩ࡯ࡶࠬ࠾࡚ࠥࡨࡦࠢࡷࡳࡹࡧ࡬ࠡࡰࡸࡱࡧ࡫ࡲࠡࡱࡩࠤࡹ࡫ࡳࡵࡵࠣࠬࡷ࡫ࡱࡶ࡫ࡵࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵࠬ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡩ࡯ࡶ࠽ࠤ࡙࡮ࡥࠡࡨࡤ࡭ࡱࡻࡲࡦࠢࡷ࡬ࡷ࡫ࡳࡩࡱ࡯ࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᮀ")
        bstack111lll1ll1l_opy_ = config.get(bstack111l1l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᮁ"), {}).get(bstack111l1l_opy_ (u"ࠧࡢࡤࡲࡶࡹࡈࡵࡪ࡮ࡧࡓࡳࡌࡡࡪ࡮ࡸࡶࡪ࠭ᮂ"), {})
        bstack111ll1lllll_opy_ = 0
        bstack111ll1ll1l1_opy_ = 0
        if bstack1llll1lll_opy_.bstack11l1llll1ll_opy_(config):
            bstack111ll1ll1l1_opy_ = bstack111lll1ll1l_opy_.get(bstack111l1l_opy_ (u"ࠨ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸ࠭ᮃ"), 5)
            if isinstance(bstack111ll1ll1l1_opy_, str) and bstack111ll1ll1l1_opy_.endswith(bstack111l1l_opy_ (u"ࠩࠨࠫᮄ")):
                try:
                    percentage = int(bstack111ll1ll1l1_opy_.strip(bstack111l1l_opy_ (u"ࠪࠩࠬᮅ")))
                    if bstack11l1lll1l11_opy_ > 0:
                        bstack111ll1lllll_opy_ = math.ceil((percentage * bstack11l1lll1l11_opy_) / 100)
                    else:
                        raise ValueError(bstack111l1l_opy_ (u"࡙ࠦࡵࡴࡢ࡮ࠣࡸࡪࡹࡴࡴࠢࡰࡹࡸࡺࠠࡣࡧࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴ࠰ࠥᮆ"))
                except ValueError as e:
                    raise ValueError(bstack111l1l_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡰࡦࡴࡦࡩࡳࡺࡡࡨࡧࠣࡺࡦࡲࡵࡦࠢࡩࡳࡷࠦ࡭ࡢࡺࡉࡥ࡮ࡲࡵࡳࡧࡶ࠾ࠥࢁࡽࠣᮇ").format(bstack111ll1ll1l1_opy_)) from e
            else:
                bstack111ll1lllll_opy_ = int(bstack111ll1ll1l1_opy_)
        logger.info(bstack111l1l_opy_ (u"ࠨࡍࡢࡺࠣࡪࡦ࡯࡬ࡶࡴࡨࡷࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࠡࡵࡨࡸࠥࡺ࡯࠻ࠢࡾࢁࠥ࠮ࡦࡳࡱࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽࠪࠤᮈ").format(bstack111ll1lllll_opy_, bstack111ll1ll1l1_opy_))
        return bstack111ll1lllll_opy_
    def bstack111lll1l111_opy_(self):
        return self.bstack111llll1111_opy_
    def bstack111ll1lll11_opy_(self):
        return self.bstack111llll11ll_opy_
    def bstack111lll11ll1_opy_(self):
        return self.bstack111llll11l1_opy_
    def __111ll1llll1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll1111_opy_ = bool(enabled)
            if mode not in [bstack111l1l_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡈ࡬ࡶࡸࡺࠧᮉ"), bstack111l1l_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡒࡲࡱࡿࠧᮊ")]:
                logger.warning(bstack111l1l_opy_ (u"ࠤࡌࡲࡻࡧ࡬ࡪࡦࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡳ࡯ࡥࡧࠣࠫࢀࢃࠧࠡࡲࡵࡳࡻ࡯ࡤࡦࡦ࠱ࠤࡉ࡫ࡦࡢࡷ࡯ࡸ࡮ࡴࡧࠡࡶࡲࠤࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ࠴ࠢᮋ").format(mode))
                mode = bstack111l1l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡋ࡯ࡲࡴࡶࠪᮌ")
            self.bstack111llll11ll_opy_ = mode
            if source is None:
                self.bstack111llll11l1_opy_ = None
            elif isinstance(source, list):
                self.bstack111llll11l1_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack111l1l_opy_ (u"ࠫ࠳ࡰࡳࡰࡰࠪᮍ")):
                self.bstack111llll11l1_opy_ = self._111llllll11_opy_(source)
            self.__111lll111l1_opy_()
        except Exception as e:
            logger.error(bstack111l1l_opy_ (u"ࠧࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡵࡨࡸࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠ࠮ࠢࡨࡲࡦࡨ࡬ࡦࡦ࠽ࠤࢀࢃࠬࠡ࡯ࡲࡨࡪࡀࠠࡼࡿ࠯ࠤࡸࡵࡵࡳࡥࡨ࠾ࠥࢁࡽ࠯ࠢࡈࡶࡷࡵࡲ࠻ࠢࡾࢁࠧᮎ").format(enabled, mode, source, e))
    def bstack111lll1l1ll_opy_(self):
        return self.bstack11l1111l1l1_opy_
    def __111ll1ll1ll_opy_(self, value):
        self.bstack11l1111l1l1_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def bstack111lllll111_opy_(self):
        return self.bstack111llll111l_opy_
    def __11l11111lll_opy_(self, value):
        self.bstack111llll111l_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def bstack111llll1l1l_opy_(self):
        return self.bstack111lll1l1l1_opy_
    def __111lll1111l_opy_(self, value):
        self.bstack111lll1l1l1_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def __111lll111l1_opy_(self):
        if self.bstack111llll1111_opy_:
            self.bstack11l1111l1l1_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack11l1111lll1_opy_.enable(bstack11l11111111_opy_)
        elif self.bstack11l1111l1l1_opy_:
            self.bstack111llll111l_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack11l1111lll1_opy_.enable(bstack11l111111ll_opy_)
        elif self.bstack111llll111l_opy_:
            self.bstack11l1111l1l1_opy_ = False
            self.bstack111lll1l1l1_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack11l1111lll1_opy_.enable(bstack111llll1ll1_opy_)
        elif self.bstack111lll1l1l1_opy_:
            self.bstack11l1111l1l1_opy_ = False
            self.bstack111llll111l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack11l1111lll1_opy_.enable(bstack111llllll1l_opy_)
        else:
            self.bstack11l1111lll1_opy_.disable()
    def bstack11111l1l_opy_(self):
        return self.bstack11l1111lll1_opy_.bstack111llll1l11_opy_()
    def bstack11ll111ll_opy_(self):
        if self.bstack11l1111lll1_opy_.bstack111llll1l11_opy_():
            return self.bstack11l1111lll1_opy_.get_name()
        return None
    def _111llllll11_opy_(self, bstack111lll1ll11_opy_):
        bstack111l1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡦࡸࡳࡦࠢࡍࡗࡔࡔࠠࡴࡱࡸࡶࡨ࡫ࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࠠࡧ࡫࡯ࡩࠥࡧ࡮ࡥࠢࡩࡳࡷࡳࡡࡵࠢ࡬ࡸࠥ࡬࡯ࡳࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡁࡳࡩࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡷࡴࡻࡲࡤࡧࡢࡪ࡮ࡲࡥࡠࡲࡤࡸ࡭ࠦࠨࡴࡶࡵ࠭࠿ࠦࡐࡢࡶ࡫ࠤࡹࡵࠠࡵࡪࡨࠤࡏ࡙ࡏࡏࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡮࡬ࡷࡹࡀࠠࡇࡱࡵࡱࡦࡺࡴࡦࡦࠣࡰ࡮ࡹࡴࠡࡱࡩࠤࡷ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࡴࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᮏ")
        if not os.path.isfile(bstack111lll1ll11_opy_):
            logger.error(bstack111l1l_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡾࠩࠣࡨࡴ࡫ࡳࠡࡰࡲࡸࠥ࡫ࡸࡪࡵࡷ࠲ࠧᮐ").format(bstack111lll1ll11_opy_))
            return []
        data = None
        try:
            with open(bstack111lll1ll11_opy_, bstack111l1l_opy_ (u"ࠣࡴࠥᮑ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack111l1l_opy_ (u"ࠤࡈࡶࡷࡵࡲࠡࡲࡤࡶࡸ࡯࡮ࡨࠢࡍࡗࡔࡔࠠࡧࡴࡲࡱࠥࡹ࡯ࡶࡴࡦࡩࠥ࡬ࡩ࡭ࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮒ").format(bstack111lll1ll11_opy_, e))
            return []
        _111lll11111_opy_ = None
        _11l1111111l_opy_ = None
        def _111lll1lll1_opy_():
            bstack11l1111ll1l_opy_ = {}
            bstack111lllllll1_opy_ = {}
            try:
                if self.bstack111lllll11l_opy_.startswith(bstack111l1l_opy_ (u"ࠪࡿࠬᮓ")) and self.bstack111lllll11l_opy_.endswith(bstack111l1l_opy_ (u"ࠫࢂ࠭ᮔ")):
                    bstack11l1111ll1l_opy_ = json.loads(self.bstack111lllll11l_opy_)
                else:
                    bstack11l1111ll1l_opy_ = dict(item.split(bstack111l1l_opy_ (u"ࠬࡀࠧᮕ")) for item in self.bstack111lllll11l_opy_.split(bstack111l1l_opy_ (u"࠭ࠬࠨᮖ")) if bstack111l1l_opy_ (u"ࠧ࠻ࠩᮗ") in item) if self.bstack111lllll11l_opy_ else {}
                if self.bstack11l11111l11_opy_.startswith(bstack111l1l_opy_ (u"ࠨࡽࠪᮘ")) and self.bstack11l11111l11_opy_.endswith(bstack111l1l_opy_ (u"ࠩࢀࠫᮙ")):
                    bstack111lllllll1_opy_ = json.loads(self.bstack11l11111l11_opy_)
                else:
                    bstack111lllllll1_opy_ = dict(item.split(bstack111l1l_opy_ (u"ࠪ࠾ࠬᮚ")) for item in self.bstack11l11111l11_opy_.split(bstack111l1l_opy_ (u"ࠫ࠱࠭ᮛ")) if bstack111l1l_opy_ (u"ࠬࡀࠧᮜ") in item) if self.bstack11l11111l11_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack111l1l_opy_ (u"ࠨࡅࡳࡴࡲࡶࠥࡶࡡࡳࡵ࡬ࡲ࡬ࠦࡦࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴ࠼ࠣࡿࢂࠨᮝ").format(e))
            logger.debug(bstack111l1l_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵࠣࡪࡷࡵ࡭ࠡࡧࡱࡺ࠿ࠦࡻࡾ࠮ࠣࡇࡑࡏ࠺ࠡࡽࢀࠦᮞ").format(bstack11l1111ll1l_opy_, bstack111lllllll1_opy_))
            return bstack11l1111ll1l_opy_, bstack111lllllll1_opy_
        if _111lll11111_opy_ is None or _11l1111111l_opy_ is None:
            _111lll11111_opy_, _11l1111111l_opy_ = _111lll1lll1_opy_()
        def bstack111ll1ll111_opy_(name, bstack111ll1l1lll_opy_):
            if name in _11l1111111l_opy_:
                return _11l1111111l_opy_[name]
            if name in _111lll11111_opy_:
                return _111lll11111_opy_[name]
            if bstack111ll1l1lll_opy_.get(bstack111l1l_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮟ")):
                return bstack111ll1l1lll_opy_[bstack111l1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮠ")]
            return None
        if isinstance(data, dict):
            bstack111lllll1l1_opy_ = []
            bstack111lll1llll_opy_ = re.compile(bstack111l1l_opy_ (u"ࡵࠫࡣࡡࡁ࠮࡜࠳࠱࠾ࡥ࡝ࠬࠦࠪᮡ"))
            for name, bstack111ll1l1lll_opy_ in data.items():
                if not isinstance(bstack111ll1l1lll_opy_, dict):
                    continue
                if not bstack111ll1l1lll_opy_.get(bstack111l1l_opy_ (u"ࠫࡺࡸ࡬ࠨᮢ")):
                    logger.warning(bstack111l1l_opy_ (u"ࠧࡘࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡘࡖࡑࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮣ").format(name, bstack111ll1l1lll_opy_))
                    continue
                if not bstack111lll1llll_opy_.match(name):
                    logger.warning(bstack111l1l_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮤ").format(name, bstack111ll1l1lll_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack111l1l_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤࠬࢁࡽࠨࠢࡰࡹࡸࡺࠠࡩࡣࡹࡩࠥࡧࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡣࡧࡷࡻࡪ࡫࡮ࠡ࠳ࠣࡥࡳࡪࠠ࠴࠲ࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹ࠮ࠣᮥ").format(name))
                    continue
                bstack111ll1l1lll_opy_ = bstack111ll1l1lll_opy_.copy()
                bstack111ll1l1lll_opy_[bstack111l1l_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᮦ")] = name
                bstack111ll1l1lll_opy_[bstack111l1l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮧ")] = bstack111ll1ll111_opy_(name, bstack111ll1l1lll_opy_)
                if not bstack111ll1l1lll_opy_.get(bstack111l1l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮨ")):
                    logger.warning(bstack111l1l_opy_ (u"ࠦࡋ࡫ࡡࡵࡷࡵࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡴ࡯ࡵࠢࡶࡴࡪࡩࡩࡧ࡫ࡨࡨࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮩ").format(name, bstack111ll1l1lll_opy_))
                    continue
                if bstack111ll1l1lll_opy_.get(bstack111l1l_opy_ (u"ࠬࡨࡡࡴࡧࡅࡶࡦࡴࡣࡩ᮪ࠩ")) and bstack111ll1l1lll_opy_[bstack111l1l_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪ᮫ࠪ")] == bstack111ll1l1lll_opy_[bstack111l1l_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮬ")]:
                    logger.warning(bstack111l1l_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡤࡲࡩࠦࡢࡢࡵࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡨࡧ࡮࡯ࡱࡷࠤࡧ࡫ࠠࡵࡪࡨࠤࡸࡧ࡭ࡦࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮭ").format(name, bstack111ll1l1lll_opy_))
                    continue
                bstack111lllll1l1_opy_.append(bstack111ll1l1lll_opy_)
            return bstack111lllll1l1_opy_
        return data
    def bstack11l1111l11l_opy_(self):
        data = {
            bstack111l1l_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᮮ"): {
                bstack111l1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮯ"): self.bstack111lll1l111_opy_(),
                bstack111l1l_opy_ (u"ࠫࡲࡵࡤࡦࠩ᮰"): self.bstack111ll1lll11_opy_(),
                bstack111l1l_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᮱"): self.bstack111lll11ll1_opy_()
            }
        }
        return data
    def bstack11l1111l111_opy_(self, config):
        bstack111lll11l11_opy_ = {}
        bstack111lll11l11_opy_[bstack111l1l_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬ᮲")] = {
            bstack111l1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᮳"): self.bstack111lll1l111_opy_(),
            bstack111l1l_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭᮴"): self.bstack111ll1lll11_opy_()
        }
        bstack111lll11l11_opy_[bstack111l1l_opy_ (u"ࠩࡵࡩࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࠬ᮵")] = {
            bstack111l1l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᮶"): self.bstack111lllll111_opy_()
        }
        bstack111lll11l11_opy_[bstack111l1l_opy_ (u"ࠫࡷࡻ࡮ࡠࡲࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡤ࡬ࡡࡪ࡮ࡨࡨࡤ࡬ࡩࡳࡵࡷࠫ᮷")] = {
            bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᮸"): self.bstack111lll1l1ll_opy_()
        }
        bstack111lll11l11_opy_[bstack111l1l_opy_ (u"࠭ࡳ࡬࡫ࡳࡣ࡫ࡧࡩ࡭࡫ࡱ࡫ࡤࡧ࡮ࡥࡡࡩࡰࡦࡱࡹࠨ᮹")] = {
            bstack111l1l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮺ"): self.bstack111llll1l1l_opy_()
        }
        if self.bstack1llll1l11_opy_(config):
            bstack111lll11l11_opy_[bstack111l1l_opy_ (u"ࠨࡴࡨࡸࡷࡿ࡟ࡵࡧࡶࡸࡸࡥ࡯࡯ࡡࡩࡥ࡮ࡲࡵࡳࡧࠪᮻ")] = {
                bstack111l1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮼ"): True,
                bstack111l1l_opy_ (u"ࠪࡱࡦࡾ࡟ࡳࡧࡷࡶ࡮࡫ࡳࠨᮽ"): self.bstack1111l111_opy_(config)
            }
        if self.bstack11l1llll1ll_opy_(config):
            bstack111lll11l11_opy_[bstack111l1l_opy_ (u"ࠫࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡲࡲࡤ࡬ࡡࡪ࡮ࡸࡶࡪ࠭ᮾ")] = {
                bstack111l1l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮿ"): True,
                bstack111l1l_opy_ (u"࠭࡭ࡢࡺࡢࡪࡦ࡯࡬ࡶࡴࡨࡷࠬᯀ"): self.bstack11l1llll11l_opy_(config)
            }
        return bstack111lll11l11_opy_
    def bstack1l1llll1l_opy_(self, config):
        bstack111l1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈࡵ࡬࡭ࡧࡦࡸࡸࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡦࡾࠦ࡭ࡢ࡭࡬ࡲ࡬ࠦࡡࠡࡥࡤࡰࡱࠦࡴࡰࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡵࡪ࡮ࡧࡣࡺࡻࡩࡥࠢࠫࡷࡹࡸࠩ࠻ࠢࡗ࡬ࡪࠦࡕࡖࡋࡇࠤࡴ࡬ࠠࡵࡪࡨࠤࡧࡻࡩ࡭ࡦࠣࡸࡴࠦࡣࡰ࡮࡯ࡩࡨࡺࠠࡥࡣࡷࡥࠥ࡬࡯ࡳ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡩ࡯ࡣࡵ࠼ࠣࡖࡪࡹࡰࡰࡰࡶࡩࠥ࡬ࡲࡰ࡯ࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺࠬࠡࡱࡵࠤࡓࡵ࡮ࡦࠢ࡬ࡪࠥ࡬ࡡࡪ࡮ࡨࡨ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᯁ")
        if not (config.get(bstack111l1l_opy_ (u"ࠨࡨࡵࡥࡲ࡫ࡷࡰࡴ࡮ࠫᯂ"), None) in bstack11l11l1l1l1_opy_ and self.bstack111lll1l111_opy_()):
            return None
        bstack111ll1lll1l_opy_ = os.environ.get(bstack111l1l_opy_ (u"ࠩࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠧᯃ"), None)
        logger.debug(bstack111l1l_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡅࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢᯄ").format(bstack111ll1lll1l_opy_))
        try:
            bstack11ll111l1ll_opy_ = bstack111l1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡤࡸ࡭ࡱࡪࡳ࠰ࡽࢀ࠳ࡨࡵ࡬࡭ࡧࡦࡸ࠲ࡨࡵࡪ࡮ࡧ࠱ࡩࡧࡴࡢࠤᯅ").format(bstack111ll1lll1l_opy_)
            payload = {
                bstack111l1l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᯆ"): config.get(bstack111l1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᯇ"), bstack111l1l_opy_ (u"ࠧࠨᯈ")),
                bstack111l1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᯉ"): config.get(bstack111l1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᯊ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack111l1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᯋ"): os.environ.get(bstack111l1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᯌ"), bstack111l1l_opy_ (u"ࠧࠨᯍ")),
                bstack111l1l_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤᯎ"): int(os.environ.get(bstack111l1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᯏ")) or bstack111l1l_opy_ (u"ࠣ࠲ࠥᯐ")),
                bstack111l1l_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨᯑ"): int(os.environ.get(bstack111l1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᯒ")) or bstack111l1l_opy_ (u"ࠦ࠶ࠨᯓ")),
                bstack111l1l_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᯔ"): get_host_info(),
            }
            logger.debug(bstack111l1l_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡳࡥࡾࡲ࡯ࡢࡦ࠽ࠤࢀࢃࠢᯕ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll111l1l1_opy_(bstack11ll111l1ll_opy_, payload)
            if response:
                logger.debug(bstack111l1l_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡈࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡦࡳࡱࡲࡥࡤࡶ࡬ࡳࡳࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᯖ").format(response))
                return response
            else:
                logger.error(bstack111l1l_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡦࡳࡱࡲࡥࡤࡶࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄ࠻ࠢࡾࢁࠧᯗ").format(bstack111ll1lll1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack111l1l_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡣࡰ࡮࡯ࡩࡨࡺࡩ࡯ࡩࠣࡦࡺ࡯࡬ࡥࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡧࡻࡩ࡭ࡦ࡙࡚ࠣࡏࡄࠡࡽࢀ࠾ࠥࢁࡽࠣᯘ").format(bstack111ll1lll1l_opy_, e))
            return None
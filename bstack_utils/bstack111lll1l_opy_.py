# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack11111l1l1_opy_
from bstack_utils.constants import bstack11l1l11ll1_opy_, bstack11l11llll11_opy_
from bstack_utils.helper import bstack11ll1l1l1ll_opy_, get_host_info
from bstack_utils.bstack11ll1llllll_opy_ import bstack11ll1llll11_opy_
import json
import re
import sys
bstack11l1111lll1_opy_ = bstack11l11l1_opy_ (u"ࠢࡳࡧࡷࡶࡾ࡚ࡥࡴࡶࡶࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨ᭘")
bstack111ll1ll1ll_opy_ = bstack11l11l1_opy_ (u"ࠣࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢ᭙")
bstack111lll1l11l_opy_ = bstack11l11l1_opy_ (u"ࠤࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࡇ࡫ࡵࡷࡹࠨ᭚")
bstack11l11111l1l_opy_ = bstack11l11l1_opy_ (u"ࠥࡶࡪࡸࡵ࡯ࡒࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡋࡧࡩ࡭ࡧࡧࠦ᭛")
bstack111lll111l1_opy_ = bstack11l11l1_opy_ (u"ࠦࡸࡱࡩࡱࡈ࡯ࡥࡰࡿࡡ࡯ࡦࡉࡥ࡮ࡲࡥࡥࠤ᭜")
bstack111llll1l11_opy_ = bstack11l11l1_opy_ (u"ࠧࡸࡵ࡯ࡕࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠤ᭝")
bstack11l1111llll_opy_ = {
    bstack11l1111lll1_opy_,
    bstack111ll1ll1ll_opy_,
    bstack111lll1l11l_opy_,
    bstack11l11111l1l_opy_,
    bstack111lll111l1_opy_,
    bstack111llll1l11_opy_
}
bstack111llll1ll1_opy_ = {bstack11l11l1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᭞")}
logger = bstack11111l1l1_opy_.get_logger(__name__, bstack11l1l11ll1_opy_)
class bstack111lll11lll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l1111l11l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1lll11ll1_opy_:
    _1ll1ll11111_opy_ = None
    def __init__(self, config):
        self.bstack111llll1111_opy_ = False
        self.bstack11l11111lll_opy_ = False
        self.bstack111lll11l1l_opy_ = False
        self.bstack111ll1ll1l1_opy_ = False
        self.bstack111llllllll_opy_ = None
        self.bstack111llllll11_opy_ = bstack111lll11lll_opy_()
        self.bstack11l111111ll_opy_ = None
        opts = config.get(bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭟"), {})
        self.bstack11l11111111_opy_ = config.get(bstack11l11l1_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡈࡒ࡛࠭᭠"), bstack11l11l1_opy_ (u"ࠤࠥ᭡"))
        self.bstack111ll1lllll_opy_ = config.get(bstack11l11l1_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡈࡒࡉࠨ᭢"), bstack11l11l1_opy_ (u"ࠦࠧ᭣"))
        bstack111lllll1ll_opy_ = opts.get(bstack111llll1l11_opy_, {})
        bstack111lllll1l1_opy_ = None
        if bstack11l11l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᭤") in bstack111lllll1ll_opy_:
            bstack111lll1lll1_opy_ = bstack111lllll1ll_opy_[bstack11l11l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭᭥")]
            if bstack111lll1lll1_opy_ is None or bstack111lll1lll1_opy_ == bstack11l11l1_opy_ (u"ࠧࠨ᭦") or (isinstance(bstack111lll1lll1_opy_, list) and len(bstack111lll1lll1_opy_) == 0):
                bstack111lllll1l1_opy_ = []
            elif isinstance(bstack111lll1lll1_opy_, list):
                bstack111lllll1l1_opy_ = bstack111lll1lll1_opy_
            elif isinstance(bstack111lll1lll1_opy_, str) and bstack111lll1lll1_opy_.strip():
                bstack111lllll1l1_opy_ = bstack111lll1lll1_opy_
            else:
                logger.warning(bstack11l11l1_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡳࡺࡸࡣࡦࠢࡹࡥࡱࡻࡥࠡ࡫ࡱࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࢁࡽ࠯ࠢࡇࡩ࡫ࡧࡵ࡭ࡶ࡬ࡲ࡬ࠦࡩࡵࠢࡤࡷࠥ࡫࡭ࡱࡶࡼࠤࡱ࡯ࡳࡵ࠰ࠥ᭧").format(bstack111lll1lll1_opy_))
                bstack111lllll1l1_opy_ = []
        self.__111lll1ll11_opy_(
            bstack111lllll1ll_opy_.get(bstack11l11l1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪ᭨"), False),
            bstack111lllll1ll_opy_.get(bstack11l11l1_opy_ (u"ࠪࡱࡴࡪࡥࠨ᭩"), bstack11l11l1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ᭪")),
            bstack111lllll1l1_opy_
        )
        self.__11l1111l1ll_opy_(opts.get(bstack111lll1l11l_opy_, False))
        self.__111lll1l1l1_opy_(opts.get(bstack11l11111l1l_opy_, False))
        self.__111lll11111_opy_(opts.get(bstack111lll111l1_opy_, False))
    @classmethod
    def bstack1llll1ll1_opy_(cls, config=None):
        if cls._1ll1ll11111_opy_ is None and config is not None:
            cls._1ll1ll11111_opy_ = bstack1lll11ll1_opy_(config)
        return cls._1ll1ll11111_opy_
    @staticmethod
    def bstack1lll1ll11_opy_(config: dict) -> bool:
        bstack111ll1lll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭫"), {}).get(bstack11l1111lll1_opy_, {})
        return bstack111ll1lll1l_opy_.get(bstack11l11l1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪ᭬ࠧ"), False)
    @staticmethod
    def bstack1111lll1_opy_(config: dict) -> int:
        bstack111ll1lll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭭"), {}).get(bstack11l1111lll1_opy_, {})
        retries = 0
        if bstack1lll11ll1_opy_.bstack1lll1ll11_opy_(config):
            retries = bstack111ll1lll1l_opy_.get(bstack11l11l1_opy_ (u"ࠨ࡯ࡤࡼࡗ࡫ࡴࡳ࡫ࡨࡷࠬ᭮"), 1)
        return retries
    @staticmethod
    def bstack1l11l111l_opy_(config: dict) -> dict:
        bstack111lll11l11_opy_ = config.get(bstack11l11l1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭯"), {})
        return {
            key: value for key, value in bstack111lll11l11_opy_.items() if key in bstack11l1111llll_opy_
        }
    @staticmethod
    def bstack11l11111ll1_opy_():
        bstack11l11l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡄࡪࡨࡧࡰࠦࡩࡧࠢࡷ࡬ࡪࠦࡡࡣࡱࡵࡸࠥࡨࡵࡪ࡮ࡧࠤ࡫࡯࡬ࡦࠢࡨࡼ࡮ࡹࡴࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢ᭰")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡢࡦࡺ࡯࡬ࡥࡡࡾࢁࠧ᭱").format(os.getenv(bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡋࡓࡕࡊࡘࡆࡤ࡛ࡕࡊࡆࠥ᭲")))))
    @staticmethod
    def bstack11l111l111l_opy_(test_name: str):
        bstack11l11l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇ࡭࡫ࡣ࡬ࠢ࡬ࡪࠥࡺࡨࡦࠢࡤࡦࡴࡸࡴࠡࡤࡸ࡭ࡱࡪࠠࡧ࡫࡯ࡩࠥ࡫ࡸࡪࡵࡷࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᭳")
        bstack111llll11l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l11l1_opy_ (u"ࠢࡧࡣ࡬ࡰࡪࡪ࡟ࡵࡧࡶࡸࡸࡥࡻࡾ࠰ࡷࡼࡹࠨ᭴").format(os.getenv(bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉࠨ᭵"))))
        with open(bstack111llll11l1_opy_, bstack11l11l1_opy_ (u"ࠩࡤࠫ᭶")) as file:
            file.write(bstack11l11l1_opy_ (u"ࠥࡿࢂࡢ࡮ࠣ᭷").format(test_name))
    @staticmethod
    def bstack11l1111ll11_opy_(framework: str) -> bool:
       return framework.lower() in bstack111llll1ll1_opy_
    @staticmethod
    def bstack11ll111111l_opy_(config: dict) -> bool:
        bstack111llllll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠫࡹ࡫ࡳࡵࡑࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡐࡲࡷ࡭ࡴࡴࡳࠨ᭸"), {}).get(bstack111ll1ll1ll_opy_, {})
        return bstack111llllll1l_opy_.get(bstack11l11l1_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭᭹"), False)
    @staticmethod
    def bstack11l1lllll1l_opy_(config: dict, bstack11l1llll11l_opy_: int = 0) -> int:
        bstack11l11l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡋࡪࡺࠠࡵࡪࡨࠤ࡫ࡧࡩ࡭ࡷࡵࡩࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤ࠭ࠢࡺ࡬࡮ࡩࡨࠡࡥࡤࡲࠥࡨࡥࠡࡣࡱࠤࡦࡨࡳࡰ࡮ࡸࡸࡪࠦ࡮ࡶ࡯ࡥࡩࡷࠦ࡯ࡳࠢࡤࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡤࡱࡱࡪ࡮࡭ࠠࠩࡦ࡬ࡧࡹ࠯࠺ࠡࡖ࡫ࡩࠥࡩ࡯࡯ࡨ࡬࡫ࡺࡸࡡࡵ࡫ࡲࡲࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡺ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡶࡲࡸࡦࡲ࡟ࡵࡧࡶࡸࡸࠦࠨࡪࡰࡷ࠭࠿ࠦࡔࡩࡧࠣࡸࡴࡺࡡ࡭ࠢࡱࡹࡲࡨࡥࡳࠢࡲࡪࠥࡺࡥࡴࡶࡶࠤ࠭ࡸࡥࡲࡷ࡬ࡶࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠭࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡪࡰࡷ࠾࡚ࠥࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭺")
        bstack111llllll1l_opy_ = config.get(bstack11l11l1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭻"), {}).get(bstack11l11l1_opy_ (u"ࠨࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠧ᭼"), {})
        bstack11l111l11l1_opy_ = 0
        bstack111lll1l1ll_opy_ = 0
        if bstack1lll11ll1_opy_.bstack11ll111111l_opy_(config):
            bstack111lll1l1ll_opy_ = bstack111llllll1l_opy_.get(bstack11l11l1_opy_ (u"ࠩࡰࡥࡽࡌࡡࡪ࡮ࡸࡶࡪࡹࠧ᭽"), 5)
            if isinstance(bstack111lll1l1ll_opy_, str) and bstack111lll1l1ll_opy_.endswith(bstack11l11l1_opy_ (u"ࠪࠩࠬ᭾")):
                try:
                    percentage = int(bstack111lll1l1ll_opy_.strip(bstack11l11l1_opy_ (u"ࠫࠪ࠭᭿")))
                    if bstack11l1llll11l_opy_ > 0:
                        bstack11l111l11l1_opy_ = math.ceil((percentage * bstack11l1llll11l_opy_) / 100)
                    else:
                        raise ValueError(bstack11l11l1_opy_ (u"࡚ࠧ࡯ࡵࡣ࡯ࠤࡹ࡫ࡳࡵࡵࠣࡱࡺࡹࡴࠡࡤࡨࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦࡦࡰࡴࠣࡴࡪࡸࡣࡦࡰࡷࡥ࡬࡫࠭ࡣࡣࡶࡩࡩࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࡵ࠱ࠦᮀ"))
                except ValueError as e:
                    raise ValueError(bstack11l11l1_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡱࡧࡵࡧࡪࡴࡴࡢࡩࡨࠤࡻࡧ࡬ࡶࡧࠣࡪࡴࡸࠠ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷ࠿ࠦࡻࡾࠤᮁ").format(bstack111lll1l1ll_opy_)) from e
            else:
                bstack11l111l11l1_opy_ = int(bstack111lll1l1ll_opy_)
        logger.info(bstack11l11l1_opy_ (u"ࠢࡎࡣࡻࠤ࡫ࡧࡩ࡭ࡷࡵࡩࡸࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥࠢࡶࡩࡹࠦࡴࡰ࠼ࠣࡿࢂࠦࠨࡧࡴࡲࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡻࡾࠫࠥᮂ").format(bstack11l111l11l1_opy_, bstack111lll1l1ll_opy_))
        return bstack11l111l11l1_opy_
    def bstack11l1111l1l1_opy_(self):
        return self.bstack111ll1ll1l1_opy_
    def bstack11l11111l11_opy_(self):
        return self.bstack111llllllll_opy_
    def bstack111lllllll1_opy_(self):
        return self.bstack11l111111ll_opy_
    def __111lll1ll11_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111ll1ll1l1_opy_ = bool(enabled)
            if mode not in [bstack11l11l1_opy_ (u"ࠨࡴࡨࡰࡪࡼࡡ࡯ࡶࡉ࡭ࡷࡹࡴࠨᮃ"), bstack11l11l1_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡓࡳࡲࡹࠨᮄ")]:
                logger.warning(bstack11l11l1_opy_ (u"ࠥࡍࡳࡼࡡ࡭࡫ࡧࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦ࡭ࡰࡦࡨࠤࠬࢁࡽࠨࠢࡳࡶࡴࡼࡩࡥࡧࡧ࠲ࠥࡊࡥࡧࡣࡸࡰࡹ࡯࡮ࡨࠢࡷࡳࠥ࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭࠮ࠣᮅ").format(mode))
                mode = bstack11l11l1_opy_ (u"ࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫᮆ")
            self.bstack111llllllll_opy_ = mode
            if source is None:
                self.bstack11l111111ll_opy_ = None
            elif isinstance(source, list):
                self.bstack11l111111ll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l11l1_opy_ (u"ࠬ࠴ࡪࡴࡱࡱࠫᮇ")):
                self.bstack11l111111ll_opy_ = self._111lll1llll_opy_(source)
            self.__111lll1ll1l_opy_()
        except Exception as e:
            logger.error(bstack11l11l1_opy_ (u"ࠨࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡶࡩࡹࠦࡳ࡮ࡣࡵࡸࠥࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡ࠯ࠣࡩࡳࡧࡢ࡭ࡧࡧ࠾ࠥࢁࡽ࠭ࠢࡰࡳࡩ࡫࠺ࠡࡽࢀ࠰ࠥࡹ࡯ࡶࡴࡦࡩ࠿ࠦࡻࡾ࠰ࠣࡉࡷࡸ࡯ࡳ࠼ࠣࡿࢂࠨᮈ").format(enabled, mode, source, e))
    def bstack11l111111l1_opy_(self):
        return self.bstack111llll1111_opy_
    def __11l1111l1ll_opy_(self, value):
        self.bstack111llll1111_opy_ = bool(value)
        self.__111lll1ll1l_opy_()
    def bstack111lllll11l_opy_(self):
        return self.bstack11l11111lll_opy_
    def __111lll1l1l1_opy_(self, value):
        self.bstack11l11111lll_opy_ = bool(value)
        self.__111lll1ll1l_opy_()
    def bstack111lllll111_opy_(self):
        return self.bstack111lll11l1l_opy_
    def __111lll11111_opy_(self, value):
        self.bstack111lll11l1l_opy_ = bool(value)
        self.__111lll1ll1l_opy_()
    def __111lll1ll1l_opy_(self):
        if self.bstack111ll1ll1l1_opy_:
            self.bstack111llll1111_opy_ = False
            self.bstack11l11111lll_opy_ = False
            self.bstack111lll11l1l_opy_ = False
            self.bstack111llllll11_opy_.enable(bstack111llll1l11_opy_)
        elif self.bstack111llll1111_opy_:
            self.bstack11l11111lll_opy_ = False
            self.bstack111lll11l1l_opy_ = False
            self.bstack111ll1ll1l1_opy_ = False
            self.bstack111llllll11_opy_.enable(bstack111lll1l11l_opy_)
        elif self.bstack11l11111lll_opy_:
            self.bstack111llll1111_opy_ = False
            self.bstack111lll11l1l_opy_ = False
            self.bstack111ll1ll1l1_opy_ = False
            self.bstack111llllll11_opy_.enable(bstack11l11111l1l_opy_)
        elif self.bstack111lll11l1l_opy_:
            self.bstack111llll1111_opy_ = False
            self.bstack11l11111lll_opy_ = False
            self.bstack111ll1ll1l1_opy_ = False
            self.bstack111llllll11_opy_.enable(bstack111lll111l1_opy_)
        else:
            self.bstack111llllll11_opy_.disable()
    def bstack111ll111_opy_(self):
        return self.bstack111llllll11_opy_.bstack11l1111l11l_opy_()
    def bstack1l1lll111l_opy_(self):
        if self.bstack111llllll11_opy_.bstack11l1111l11l_opy_():
            return self.bstack111llllll11_opy_.get_name()
        return None
    def _111lll1llll_opy_(self, bstack11l111l1111_opy_):
        bstack11l11l1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡧࡲࡴࡧࠣࡎࡘࡕࡎࠡࡵࡲࡹࡷࡩࡥࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠦࡡ࡯ࡦࠣࡪࡴࡸ࡭ࡢࡶࠣ࡭ࡹࠦࡦࡰࡴࠣࡷࡲࡧࡲࡵࠢࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡸࡵࡵࡳࡥࡨࡣ࡫࡯࡬ࡦࡡࡳࡥࡹ࡮ࠠࠩࡵࡷࡶ࠮ࡀࠠࡑࡣࡷ࡬ࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡐࡓࡐࡐࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡪ࡮ࡲࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢ࡯࡭ࡸࡺ࠺ࠡࡈࡲࡶࡲࡧࡴࡵࡧࡧࠤࡱ࡯ࡳࡵࠢࡲࡪࠥࡸࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࡵࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᮉ")
        if not os.path.isfile(bstack11l111l1111_opy_):
            logger.error(bstack11l11l1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡࡨ࡬ࡰࡪࠦࠧࡼࡿࠪࠤࡩࡵࡥࡴࠢࡱࡳࡹࠦࡥࡹ࡫ࡶࡸ࠳ࠨᮊ").format(bstack11l111l1111_opy_))
            return []
        data = None
        try:
            with open(bstack11l111l1111_opy_, bstack11l11l1_opy_ (u"ࠤࡵࠦᮋ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l11l1_opy_ (u"ࠥࡉࡷࡸ࡯ࡳࠢࡳࡥࡷࡹࡩ࡯ࡩࠣࡎࡘࡕࡎࠡࡨࡵࡳࡲࠦࡳࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮌ").format(bstack11l111l1111_opy_, e))
            return []
        _111lll111ll_opy_ = None
        _111llll11ll_opy_ = None
        def _111ll1llll1_opy_():
            bstack111llll111l_opy_ = {}
            bstack111ll1lll11_opy_ = {}
            try:
                if self.bstack11l11111111_opy_.startswith(bstack11l11l1_opy_ (u"ࠫࢀ࠭ᮍ")) and self.bstack11l11111111_opy_.endswith(bstack11l11l1_opy_ (u"ࠬࢃࠧᮎ")):
                    bstack111llll111l_opy_ = json.loads(self.bstack11l11111111_opy_)
                else:
                    bstack111llll111l_opy_ = dict(item.split(bstack11l11l1_opy_ (u"࠭࠺ࠨᮏ")) for item in self.bstack11l11111111_opy_.split(bstack11l11l1_opy_ (u"ࠧ࠭ࠩᮐ")) if bstack11l11l1_opy_ (u"ࠨ࠼ࠪᮑ") in item) if self.bstack11l11111111_opy_ else {}
                if self.bstack111ll1lllll_opy_.startswith(bstack11l11l1_opy_ (u"ࠩࡾࠫᮒ")) and self.bstack111ll1lllll_opy_.endswith(bstack11l11l1_opy_ (u"ࠪࢁࠬᮓ")):
                    bstack111ll1lll11_opy_ = json.loads(self.bstack111ll1lllll_opy_)
                else:
                    bstack111ll1lll11_opy_ = dict(item.split(bstack11l11l1_opy_ (u"ࠫ࠿࠭ᮔ")) for item in self.bstack111ll1lllll_opy_.split(bstack11l11l1_opy_ (u"ࠬ࠲ࠧᮕ")) if bstack11l11l1_opy_ (u"࠭࠺ࠨᮖ") in item) if self.bstack111ll1lllll_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l11l1_opy_ (u"ࠢࡆࡴࡵࡳࡷࠦࡰࡢࡴࡶ࡭ࡳ࡭ࠠࡧࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡ࡯ࡤࡴࡵ࡯࡮ࡨࡵ࠽ࠤࢀࢃࠢᮗ").format(e))
            logger.debug(bstack11l11l1_opy_ (u"ࠣࡈࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡰࡥࡵࡶࡩ࡯ࡩࡶࠤ࡫ࡸ࡯࡮ࠢࡨࡲࡻࡀࠠࡼࡿ࠯ࠤࡈࡒࡉ࠻ࠢࡾࢁࠧᮘ").format(bstack111llll111l_opy_, bstack111ll1lll11_opy_))
            return bstack111llll111l_opy_, bstack111ll1lll11_opy_
        if _111lll111ll_opy_ is None or _111llll11ll_opy_ is None:
            _111lll111ll_opy_, _111llll11ll_opy_ = _111ll1llll1_opy_()
        def bstack11l1111111l_opy_(name, bstack111llll1l1l_opy_):
            if name in _111llll11ll_opy_:
                return _111llll11ll_opy_[name]
            if name in _111lll111ll_opy_:
                return _111lll111ll_opy_[name]
            if bstack111llll1l1l_opy_.get(bstack11l11l1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮙ")):
                return bstack111llll1l1l_opy_[bstack11l11l1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮚ")]
            return None
        if isinstance(data, dict):
            bstack111lll1111l_opy_ = []
            bstack111llll1lll_opy_ = re.compile(bstack11l11l1_opy_ (u"ࡶࠬࡤ࡛ࡂ࠯࡝࠴࠲࠿࡟࡞࠭ࠧࠫᮛ"))
            for name, bstack111llll1l1l_opy_ in data.items():
                if not isinstance(bstack111llll1l1l_opy_, dict):
                    continue
                if not bstack111llll1l1l_opy_.get(bstack11l11l1_opy_ (u"ࠬࡻࡲ࡭ࠩᮜ")):
                    logger.warning(bstack11l11l1_opy_ (u"ࠨࡒࡦࡲࡲࡷ࡮ࡺ࡯ࡳࡻ࡙ࠣࡗࡒࠠࡪࡵࠣࡱ࡮ࡹࡳࡪࡰࡪࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮝ").format(name, bstack111llll1l1l_opy_))
                    continue
                if not bstack111llll1lll_opy_.match(name):
                    logger.warning(bstack11l11l1_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࡬࡯ࡳ࡯ࡤࡸࠥ࡬࡯ࡳࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮞ").format(name, bstack111llll1l1l_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l11l1_opy_ (u"ࠣࡕࡲࡹࡷࡩࡥࠡ࡫ࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠥ࠭ࡻࡾࠩࠣࡱࡺࡹࡴࠡࡪࡤࡺࡪࠦࡡࠡ࡮ࡨࡲ࡬ࡺࡨࠡࡤࡨࡸࡼ࡫ࡥ࡯ࠢ࠴ࠤࡦࡴࡤࠡ࠵࠳ࠤࡨ࡮ࡡࡳࡣࡦࡸࡪࡸࡳ࠯ࠤᮟ").format(name))
                    continue
                bstack111llll1l1l_opy_ = bstack111llll1l1l_opy_.copy()
                bstack111llll1l1l_opy_[bstack11l11l1_opy_ (u"ࠩࡱࡥࡲ࡫ࠧᮠ")] = name
                bstack111llll1l1l_opy_[bstack11l11l1_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᮡ")] = bstack11l1111111l_opy_(name, bstack111llll1l1l_opy_)
                if not bstack111llll1l1l_opy_.get(bstack11l11l1_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮢ")):
                    logger.warning(bstack11l11l1_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡮ࡰࡶࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡩࡩࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᮣ").format(name, bstack111llll1l1l_opy_))
                    continue
                if bstack111llll1l1l_opy_.get(bstack11l11l1_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪᮤ")) and bstack111llll1l1l_opy_[bstack11l11l1_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮥ")] == bstack111llll1l1l_opy_[bstack11l11l1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮦ")]:
                    logger.warning(bstack11l11l1_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡥࡳࡪࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡶ࡫ࡩࠥࡹࡡ࡮ࡧࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮧ").format(name, bstack111llll1l1l_opy_))
                    continue
                bstack111lll1111l_opy_.append(bstack111llll1l1l_opy_)
            return bstack111lll1111l_opy_
        return data
    def bstack11l1111l111_opy_(self):
        data = {
            bstack11l11l1_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᮨ"): {
                bstack11l11l1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮩ"): self.bstack11l1111l1l1_opy_(),
                bstack11l11l1_opy_ (u"ࠬࡳ࡯ࡥࡧ᮪ࠪ"): self.bstack11l11111l11_opy_(),
                bstack11l11l1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ᮫࠭"): self.bstack111lllllll1_opy_()
            }
        }
        return data
    def bstack111lll11ll1_opy_(self, config):
        bstack111lll1l111_opy_ = {}
        bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᮬ")] = {
            bstack11l11l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮭ"): self.bstack11l1111l1l1_opy_(),
            bstack11l11l1_opy_ (u"ࠩࡰࡳࡩ࡫ࠧᮮ"): self.bstack11l11111l11_opy_()
        }
        bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩ࠭ᮯ")] = {
            bstack11l11l1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᮰"): self.bstack111lllll11l_opy_()
        }
        bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠬࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩࡥࡦࡪࡴࡶࡸࠬ᮱")] = {
            bstack11l11l1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮲"): self.bstack11l111111l1_opy_()
        }
        bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠧࡴ࡭࡬ࡴࡤ࡬ࡡࡪ࡮࡬ࡲ࡬ࡥࡡ࡯ࡦࡢࡪࡱࡧ࡫ࡺࠩ᮳")] = {
            bstack11l11l1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩ᮴"): self.bstack111lllll111_opy_()
        }
        if self.bstack1lll1ll11_opy_(config):
            bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠩࡵࡩࡹࡸࡹࡠࡶࡨࡷࡹࡹ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫ᮵")] = {
                bstack11l11l1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᮶"): True,
                bstack11l11l1_opy_ (u"ࠫࡲࡧࡸࡠࡴࡨࡸࡷ࡯ࡥࡴࠩ᮷"): self.bstack1111lll1_opy_(config)
            }
        if self.bstack11ll111111l_opy_(config):
            bstack111lll1l111_opy_[bstack11l11l1_opy_ (u"ࠬࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧ᮸")] = {
                bstack11l11l1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮹"): True,
                bstack11l11l1_opy_ (u"ࠧ࡮ࡣࡻࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡸ࠭ᮺ"): self.bstack11l1lllll1l_opy_(config)
            }
        return bstack111lll1l111_opy_
    def bstack11l1l111l_opy_(self, config):
        bstack11l11l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉ࡯࡭࡮ࡨࡧࡹࡹࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡧࡿࠠ࡮ࡣ࡮࡭ࡳ࡭ࠠࡢࠢࡦࡥࡱࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡖࡗࡌࡈࠥࡵࡦࠡࡶ࡫ࡩࠥࡨࡵࡪ࡮ࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᮻ")
        if not (config.get(bstack11l11l1_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬᮼ"), None) in bstack11l11llll11_opy_ and self.bstack11l1111l1l1_opy_()):
            return None
        bstack11l1111ll1l_opy_ = os.environ.get(bstack11l11l1_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨᮽ"), None)
        logger.debug(bstack11l11l1_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡆࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣᮾ").format(bstack11l1111ll1l_opy_))
        try:
            bstack11ll11l1l11_opy_ = bstack11l11l1_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠥᮿ").format(bstack11l1111ll1l_opy_)
            payload = {
                bstack11l11l1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦᯀ"): config.get(bstack11l11l1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᯁ"), bstack11l11l1_opy_ (u"ࠨࠩᯂ")),
                bstack11l11l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᯃ"): config.get(bstack11l11l1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᯄ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l11l1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤᯅ"): os.environ.get(bstack11l11l1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᯆ"), bstack11l11l1_opy_ (u"ࠨࠢᯇ")),
                bstack11l11l1_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥᯈ"): int(os.environ.get(bstack11l11l1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᯉ")) or bstack11l11l1_opy_ (u"ࠤ࠳ࠦᯊ")),
                bstack11l11l1_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢᯋ"): int(os.environ.get(bstack11l11l1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨᯌ")) or bstack11l11l1_opy_ (u"ࠧ࠷ࠢᯍ")),
                bstack11l11l1_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣᯎ"): get_host_info(),
            }
            logger.debug(bstack11l11l1_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡴࡦࡿ࡬ࡰࡣࡧ࠾ࠥࢁࡽࠣᯏ").format(payload))
            response = bstack11ll1llll11_opy_.bstack11ll111llll_opy_(bstack11ll11l1l11_opy_, payload)
            if response:
                logger.debug(bstack11l11l1_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡂࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᯐ").format(response))
                return response
            else:
                logger.error(bstack11l11l1_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨᯑ").format(bstack11l1111ll1l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l11l1_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅࠢࡾࢁ࠿ࠦࡻࡾࠤᯒ").format(bstack11l1111ll1l_opy_, e))
            return None
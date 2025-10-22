# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import tempfile
import math
from bstack_utils import bstack111l11ll1l_opy_
from bstack_utils.constants import bstack11l111l11l_opy_, bstack11l11lllll1_opy_
from bstack_utils.helper import bstack11ll1l1l111_opy_, get_host_info
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
import json
import re
import sys
bstack11l11111ll1_opy_ = bstack11l1l11_opy_ (u"ࠢࡳࡧࡷࡶࡾ࡚ࡥࡴࡶࡶࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨ᭟")
bstack111lll11l11_opy_ = bstack11l1l11_opy_ (u"ࠣࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫ࠢ᭠")
bstack11l111111ll_opy_ = bstack11l1l11_opy_ (u"ࠤࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࡇ࡫ࡵࡷࡹࠨ᭡")
bstack111ll1lllll_opy_ = bstack11l1l11_opy_ (u"ࠥࡶࡪࡸࡵ࡯ࡒࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡋࡧࡩ࡭ࡧࡧࠦ᭢")
bstack11l11111111_opy_ = bstack11l1l11_opy_ (u"ࠦࡸࡱࡩࡱࡈ࡯ࡥࡰࡿࡡ࡯ࡦࡉࡥ࡮ࡲࡥࡥࠤ᭣")
bstack111lll1l1l1_opy_ = bstack11l1l11_opy_ (u"ࠧࡸࡵ࡯ࡕࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠤ᭤")
bstack111lll1l11l_opy_ = {
    bstack11l11111ll1_opy_,
    bstack111lll11l11_opy_,
    bstack11l111111ll_opy_,
    bstack111ll1lllll_opy_,
    bstack11l11111111_opy_,
    bstack111lll1l1l1_opy_
}
bstack111lll1lll1_opy_ = {bstack11l1l11_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭᭥")}
logger = bstack111l11ll1l_opy_.get_logger(__name__, bstack11l111l11l_opy_)
class bstack111lll1111l_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l1111ll11_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack111ll1l1_opy_:
    _1ll1ll11111_opy_ = None
    def __init__(self, config):
        self.bstack11l1111lll1_opy_ = False
        self.bstack11l1111l1ll_opy_ = False
        self.bstack111lll1ll11_opy_ = False
        self.bstack111lll1l111_opy_ = False
        self.bstack111lll111ll_opy_ = None
        self.bstack111ll1llll1_opy_ = bstack111lll1111l_opy_()
        self.bstack11l1111ll1l_opy_ = None
        opts = config.get(bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭦"), {})
        self.bstack111ll1ll1ll_opy_ = config.get(bstack11l1l11_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡈࡒ࡛࠭᭧"), bstack11l1l11_opy_ (u"ࠤࠥ᭨"))
        self.bstack111llll1ll1_opy_ = config.get(bstack11l1l11_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡈࡒࡉࠨ᭩"), bstack11l1l11_opy_ (u"ࠦࠧ᭪"))
        bstack111llll1l1l_opy_ = opts.get(bstack111lll1l1l1_opy_, {})
        bstack111llll11ll_opy_ = None
        if bstack11l1l11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᭫") in bstack111llll1l1l_opy_:
            bstack111llll11ll_opy_ = bstack111llll1l1l_opy_[bstack11l1l11_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ᭬࠭")]
            if bstack111llll11ll_opy_ is None:
                bstack111llll11ll_opy_ = []
        self.__11l11111l11_opy_(
            bstack111llll1l1l_opy_.get(bstack11l1l11_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᭭"), False),
            bstack111llll1l1l_opy_.get(bstack11l1l11_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭᭮"), bstack11l1l11_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩ᭯")),
            bstack111llll11ll_opy_
        )
        self.__11l1111l1l1_opy_(opts.get(bstack11l111111ll_opy_, False))
        self.__111llllll1l_opy_(opts.get(bstack111ll1lllll_opy_, False))
        self.__11l111111l1_opy_(opts.get(bstack11l11111111_opy_, False))
    @classmethod
    def bstack1llll1lll_opy_(cls, config=None):
        if cls._1ll1ll11111_opy_ is None and config is not None:
            cls._1ll1ll11111_opy_ = bstack111ll1l1_opy_(config)
        return cls._1ll1ll11111_opy_
    @staticmethod
    def bstack1llll11l1_opy_(config: dict) -> bool:
        bstack111lll11111_opy_ = config.get(bstack11l1l11_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᭰"), {}).get(bstack11l11111ll1_opy_, {})
        return bstack111lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᭱"), False)
    @staticmethod
    def bstack1lllllll1_opy_(config: dict) -> int:
        bstack111lll11111_opy_ = config.get(bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭲"), {}).get(bstack11l11111ll1_opy_, {})
        retries = 0
        if bstack111ll1l1_opy_.bstack1llll11l1_opy_(config):
            retries = bstack111lll11111_opy_.get(bstack11l1l11_opy_ (u"࠭࡭ࡢࡺࡕࡩࡹࡸࡩࡦࡵࠪ᭳"), 1)
        return retries
    @staticmethod
    def bstack11ll11l1ll_opy_(config: dict) -> dict:
        bstack111llll11l1_opy_ = config.get(bstack11l1l11_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭴"), {})
        return {
            key: value for key, value in bstack111llll11l1_opy_.items() if key in bstack111lll1l11l_opy_
        }
    @staticmethod
    def bstack111ll1lll11_opy_():
        bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᭵")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥ᭶").format(os.getenv(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᭷")))))
    @staticmethod
    def bstack111lllll111_opy_(test_name: str):
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭸")
        bstack111lll1l1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1l11_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷࠦ᭹").format(os.getenv(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᭺"))))
        with open(bstack111lll1l1ll_opy_, bstack11l1l11_opy_ (u"ࠧࡢࠩ᭻")) as file:
            file.write(bstack11l1l11_opy_ (u"ࠣࡽࢀࡠࡳࠨ᭼").format(test_name))
    @staticmethod
    def bstack111lllll1ll_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll1lll1_opy_
    @staticmethod
    def bstack11l1lll111l_opy_(config: dict) -> bool:
        bstack111ll1lll1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭽"), {}).get(bstack111lll11l11_opy_, {})
        return bstack111ll1lll1l_opy_.get(bstack11l1l11_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᭾"), False)
    @staticmethod
    def bstack11l1llll111_opy_(config: dict, bstack11l1lll1111_opy_: int = 0) -> int:
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡉࡨࡸࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠲ࠠࡸࡪ࡬ࡧ࡭ࠦࡣࡢࡰࠣࡦࡪࠦࡡ࡯ࠢࡤࡦࡸࡵ࡬ࡶࡶࡨࠤࡳࡻ࡭ࡣࡧࡵࠤࡴࡸࠠࡢࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡰࡶࡤࡰࡤࡺࡥࡴࡶࡶࠤ࠭࡯࡮ࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࠫࡶࡪࡷࡵࡪࡴࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭿")
        bstack111ll1lll1l_opy_ = config.get(bstack11l1l11_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮀ"), {}).get(bstack11l1l11_opy_ (u"࠭ࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠬᮁ"), {})
        bstack11l1111l11l_opy_ = 0
        bstack111ll1ll11l_opy_ = 0
        if bstack111ll1l1_opy_.bstack11l1lll111l_opy_(config):
            bstack111ll1ll11l_opy_ = bstack111ll1lll1l_opy_.get(bstack11l1l11_opy_ (u"ࠧ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷࠬᮂ"), 5)
            if isinstance(bstack111ll1ll11l_opy_, str) and bstack111ll1ll11l_opy_.endswith(bstack11l1l11_opy_ (u"ࠨࠧࠪᮃ")):
                try:
                    percentage = int(bstack111ll1ll11l_opy_.strip(bstack11l1l11_opy_ (u"ࠩࠨࠫᮄ")))
                    if bstack11l1lll1111_opy_ > 0:
                        bstack11l1111l11l_opy_ = math.ceil((percentage * bstack11l1lll1111_opy_) / 100)
                    else:
                        raise ValueError(bstack11l1l11_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳ࠯ࠤᮅ"))
                except ValueError as e:
                    raise ValueError(bstack11l1l11_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦࠢࡹࡥࡱࡻࡥࠡࡨࡲࡶࠥࡳࡡࡹࡈࡤ࡭ࡱࡻࡲࡦࡵ࠽ࠤࢀࢃࠢᮆ").format(bstack111ll1ll11l_opy_)) from e
            else:
                bstack11l1111l11l_opy_ = int(bstack111ll1ll11l_opy_)
        logger.info(bstack11l1l11_opy_ (u"ࠧࡓࡡࡹࠢࡩࡥ࡮ࡲࡵࡳࡧࡶࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡴࡧࡷࠤࡹࡵ࠺ࠡࡽࢀࠤ࠭࡬ࡲࡰ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࢀࢃࠩࠣᮇ").format(bstack11l1111l11l_opy_, bstack111ll1ll11l_opy_))
        return bstack11l1111l11l_opy_
    def bstack11l1111111l_opy_(self):
        return self.bstack111lll1l111_opy_
    def bstack111lllllll1_opy_(self):
        return self.bstack111lll111ll_opy_
    def bstack11l11111l1l_opy_(self):
        return self.bstack11l1111ll1l_opy_
    def __11l11111l11_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111lll1l111_opy_ = bool(enabled)
            if mode not in [bstack11l1l11_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭ᮈ"), bstack11l1l11_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡑࡱࡰࡾ࠭ᮉ")]:
                logger.warning(bstack11l1l11_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡲࡵࡤࡦࠢࠪࡿࢂ࠭ࠠࡱࡴࡲࡺ࡮ࡪࡥࡥ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ࠳ࠨᮊ").format(mode))
                mode = bstack11l1l11_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩᮋ")
            self.bstack111lll111ll_opy_ = mode
            if source is None:
                self.bstack11l1111ll1l_opy_ = None
            elif isinstance(source, list):
                self.bstack11l1111ll1l_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l1l11_opy_ (u"ࠪ࠲࡯ࡹ࡯࡯ࠩᮌ")):
                self.bstack11l1111ll1l_opy_ = self._111lll1ll1l_opy_(source)
            self.__111lllll1l1_opy_()
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦ࠭ࠡࡧࡱࡥࡧࡲࡥࡥ࠼ࠣࡿࢂ࠲ࠠ࡮ࡱࡧࡩ࠿ࠦࡻࡾ࠮ࠣࡷࡴࡻࡲࡤࡧ࠽ࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᮍ").format(enabled, mode, source, e))
    def bstack111lll11lll_opy_(self):
        return self.bstack11l1111lll1_opy_
    def __11l1111l1l1_opy_(self, value):
        self.bstack11l1111lll1_opy_ = bool(value)
        self.__111lllll1l1_opy_()
    def bstack111llll1l11_opy_(self):
        return self.bstack11l1111l1ll_opy_
    def __111llllll1l_opy_(self, value):
        self.bstack11l1111l1ll_opy_ = bool(value)
        self.__111lllll1l1_opy_()
    def bstack111lll111l1_opy_(self):
        return self.bstack111lll1ll11_opy_
    def __11l111111l1_opy_(self, value):
        self.bstack111lll1ll11_opy_ = bool(value)
        self.__111lllll1l1_opy_()
    def __111lllll1l1_opy_(self):
        if self.bstack111lll1l111_opy_:
            self.bstack11l1111lll1_opy_ = False
            self.bstack11l1111l1ll_opy_ = False
            self.bstack111lll1ll11_opy_ = False
            self.bstack111ll1llll1_opy_.enable(bstack111lll1l1l1_opy_)
        elif self.bstack11l1111lll1_opy_:
            self.bstack11l1111l1ll_opy_ = False
            self.bstack111lll1ll11_opy_ = False
            self.bstack111lll1l111_opy_ = False
            self.bstack111ll1llll1_opy_.enable(bstack11l111111ll_opy_)
        elif self.bstack11l1111l1ll_opy_:
            self.bstack11l1111lll1_opy_ = False
            self.bstack111lll1ll11_opy_ = False
            self.bstack111lll1l111_opy_ = False
            self.bstack111ll1llll1_opy_.enable(bstack111ll1lllll_opy_)
        elif self.bstack111lll1ll11_opy_:
            self.bstack11l1111lll1_opy_ = False
            self.bstack11l1111l1ll_opy_ = False
            self.bstack111lll1l111_opy_ = False
            self.bstack111ll1llll1_opy_.enable(bstack11l11111111_opy_)
        else:
            self.bstack111ll1llll1_opy_.disable()
    def bstack1111l1l1_opy_(self):
        return self.bstack111ll1llll1_opy_.bstack11l1111ll11_opy_()
    def bstack1l111l1l1l_opy_(self):
        if self.bstack111ll1llll1_opy_.bstack11l1111ll11_opy_():
            return self.bstack111ll1llll1_opy_.get_name()
        return None
    def _111lll1ll1l_opy_(self, bstack11l1111l111_opy_):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡳࡰࡷࡵࡧࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡦࡪ࡮ࡨࠤࡦࡴࡤࠡࡨࡲࡶࡲࡧࡴࠡ࡫ࡷࠤ࡫ࡵࡲࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡳࡺࡸࡣࡦࡡࡩ࡭ࡱ࡫࡟ࡱࡣࡷ࡬ࠥ࠮ࡳࡵࡴࠬ࠾ࠥࡖࡡࡵࡪࠣࡸࡴࠦࡴࡩࡧࠣࡎࡘࡕࡎࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡆࡰࡴࡰࡥࡹࡺࡥࡥࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡶࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮎ")
        if not os.path.isfile(bstack11l1111l111_opy_):
            logger.error(bstack11l1l11_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠦᮏ").format(bstack11l1111l111_opy_))
            return []
        data = None
        try:
            with open(bstack11l1111l111_opy_, bstack11l1l11_opy_ (u"ࠢࡳࠤᮐ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l1l11_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡌࡖࡓࡓࠦࡦࡳࡱࡰࠤࡸࡵࡵࡳࡥࡨࠤ࡫࡯࡬ࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᮑ").format(bstack11l1111l111_opy_, e))
            return []
        _11l11111lll_opy_ = None
        _111llllll11_opy_ = None
        def _111lll1llll_opy_():
            bstack111ll1ll1l1_opy_ = {}
            bstack111llllllll_opy_ = {}
            try:
                if self.bstack111ll1ll1ll_opy_.startswith(bstack11l1l11_opy_ (u"ࠩࡾࠫᮒ")) and self.bstack111ll1ll1ll_opy_.endswith(bstack11l1l11_opy_ (u"ࠪࢁࠬᮓ")):
                    bstack111ll1ll1l1_opy_ = json.loads(self.bstack111ll1ll1ll_opy_)
                else:
                    bstack111ll1ll1l1_opy_ = dict(item.split(bstack11l1l11_opy_ (u"ࠫ࠿࠭ᮔ")) for item in self.bstack111ll1ll1ll_opy_.split(bstack11l1l11_opy_ (u"ࠬ࠲ࠧᮕ")) if bstack11l1l11_opy_ (u"࠭࠺ࠨᮖ") in item) if self.bstack111ll1ll1ll_opy_ else {}
                if self.bstack111llll1ll1_opy_.startswith(bstack11l1l11_opy_ (u"ࠧࡼࠩᮗ")) and self.bstack111llll1ll1_opy_.endswith(bstack11l1l11_opy_ (u"ࠨࡿࠪᮘ")):
                    bstack111llllllll_opy_ = json.loads(self.bstack111llll1ll1_opy_)
                else:
                    bstack111llllllll_opy_ = dict(item.split(bstack11l1l11_opy_ (u"ࠩ࠽ࠫᮙ")) for item in self.bstack111llll1ll1_opy_.split(bstack11l1l11_opy_ (u"ࠪ࠰ࠬᮚ")) if bstack11l1l11_opy_ (u"ࠫ࠿࠭ᮛ") in item) if self.bstack111llll1ll1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l1l11_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡬ࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳ࠻ࠢࡾࢁࠧᮜ").format(e))
            logger.debug(bstack11l1l11_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴࠢࡩࡶࡴࡳࠠࡦࡰࡹ࠾ࠥࢁࡽ࠭ࠢࡆࡐࡎࡀࠠࡼࡿࠥᮝ").format(bstack111ll1ll1l1_opy_, bstack111llllllll_opy_))
            return bstack111ll1ll1l1_opy_, bstack111llllllll_opy_
        if _11l11111lll_opy_ is None or _111llllll11_opy_ is None:
            _11l11111lll_opy_, _111llllll11_opy_ = _111lll1llll_opy_()
        def bstack111llll111l_opy_(name, bstack111llll1lll_opy_):
            if name in _111llllll11_opy_:
                return _111llllll11_opy_[name]
            if name in _11l11111lll_opy_:
                return _11l11111lll_opy_[name]
            if bstack111llll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮞ")):
                return bstack111llll1lll_opy_[bstack11l1l11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮟ")]
            return None
        if isinstance(data, dict):
            bstack111ll1ll111_opy_ = []
            bstack111lll11ll1_opy_ = re.compile(bstack11l1l11_opy_ (u"ࡴࠪࡢࡠࡇ࡛࠭࠲࠰࠽ࡤࡣࠫࠥࠩᮠ"))
            for name, bstack111llll1lll_opy_ in data.items():
                if not isinstance(bstack111llll1lll_opy_, dict):
                    continue
                if not bstack111llll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠪࡹࡷࡲࠧᮡ")):
                    logger.warning(bstack11l1l11_opy_ (u"ࠦࡗ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡗࡕࡐࠥ࡯ࡳࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮢ").format(name, bstack111llll1lll_opy_))
                    continue
                if not bstack111lll11ll1_opy_.match(name):
                    logger.warning(bstack11l1l11_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳࡰࡷࡵࡧࡪࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠣࡪࡴࡸ࡭ࡢࡶࠣࡪࡴࡸࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮣ").format(name, bstack111llll1lll_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l1l11_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠣࠫࢀࢃࠧࠡ࡯ࡸࡷࡹࠦࡨࡢࡸࡨࠤࡦࠦ࡬ࡦࡰࡪࡸ࡭ࠦࡢࡦࡶࡺࡩࡪࡴࠠ࠲ࠢࡤࡲࡩࠦ࠳࠱ࠢࡦ࡬ࡦࡸࡡࡤࡶࡨࡶࡸ࠴ࠢᮤ").format(name))
                    continue
                bstack111llll1lll_opy_ = bstack111llll1lll_opy_.copy()
                bstack111llll1lll_opy_[bstack11l1l11_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᮥ")] = name
                bstack111llll1lll_opy_[bstack11l1l11_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮦ")] = bstack111llll111l_opy_(name, bstack111llll1lll_opy_)
                if not bstack111llll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮧ")):
                    logger.warning(bstack11l1l11_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡳࡵࡴࠡࡵࡳࡩࡨ࡯ࡦࡪࡧࡧࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮨ").format(name, bstack111llll1lll_opy_))
                    continue
                if bstack111llll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨᮩ")) and bstack111llll1lll_opy_[bstack11l1l11_opy_ (u"ࠬࡨࡡࡴࡧࡅࡶࡦࡴࡣࡩ᮪ࠩ")] == bstack111llll1lll_opy_[bstack11l1l11_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭᮫࠭")]:
                    logger.warning(bstack11l1l11_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡣࡱࡨࠥࡨࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡴࡩࡧࠣࡷࡦࡳࡥࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᮬ").format(name, bstack111llll1lll_opy_))
                    continue
                bstack111ll1ll111_opy_.append(bstack111llll1lll_opy_)
            return bstack111ll1ll111_opy_
        return data
    def bstack111ll1l1lll_opy_(self):
        data = {
            bstack11l1l11_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᮭ"): {
                bstack11l1l11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮮ"): self.bstack11l1111111l_opy_(),
                bstack11l1l11_opy_ (u"ࠪࡱࡴࡪࡥࠨᮯ"): self.bstack111lllllll1_opy_(),
                bstack11l1l11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫ᮰"): self.bstack11l11111l1l_opy_()
            }
        }
        return data
    def bstack111llll1111_opy_(self, config):
        bstack111lll11l1l_opy_ = {}
        bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫ᮱")] = {
            bstack11l1l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮲"): self.bstack11l1111111l_opy_(),
            bstack11l1l11_opy_ (u"ࠧ࡮ࡱࡧࡩࠬ᮳"): self.bstack111lllllll1_opy_()
        }
        bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟ࡱࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡣ࡫ࡧࡩ࡭ࡧࡧࠫ᮴")] = {
            bstack11l1l11_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪ᮵"): self.bstack111llll1l11_opy_()
        }
        bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠪࡶࡺࡴ࡟ࡱࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡣ࡫ࡧࡩ࡭ࡧࡧࡣ࡫࡯ࡲࡴࡶࠪ᮶")] = {
            bstack11l1l11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᮷"): self.bstack111lll11lll_opy_()
        }
        bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠬࡹ࡫ࡪࡲࡢࡪࡦ࡯࡬ࡪࡰࡪࡣࡦࡴࡤࡠࡨ࡯ࡥࡰࡿࠧ᮸")] = {
            bstack11l1l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᮹"): self.bstack111lll111l1_opy_()
        }
        if self.bstack1llll11l1_opy_(config):
            bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠧࡳࡧࡷࡶࡾࡥࡴࡦࡵࡷࡷࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦࠩᮺ")] = {
                bstack11l1l11_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮻ"): True,
                bstack11l1l11_opy_ (u"ࠩࡰࡥࡽࡥࡲࡦࡶࡵ࡭ࡪࡹࠧᮼ"): self.bstack1lllllll1_opy_(config)
            }
        if self.bstack11l1lll111l_opy_(config):
            bstack111lll11l1l_opy_[bstack11l1l11_opy_ (u"ࠪࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡱࡱࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠬᮽ")] = {
                bstack11l1l11_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮾ"): True,
                bstack11l1l11_opy_ (u"ࠬࡳࡡࡹࡡࡩࡥ࡮ࡲࡵࡳࡧࡶࠫᮿ"): self.bstack11l1llll111_opy_(config)
            }
        return bstack111lll11l1l_opy_
    def bstack11l1llll11_opy_(self, config):
        bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡴࡲ࡬ࡦࡥࡷࡷࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡥࡽࠥࡳࡡ࡬࡫ࡱ࡫ࠥࡧࠠࡤࡣ࡯ࡰࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠡࠪࡶࡸࡷ࠯࠺ࠡࡖ࡫ࡩ࡛ࠥࡕࡊࡆࠣࡳ࡫ࠦࡴࡩࡧࠣࡦࡺ࡯࡬ࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡤࡢࡶࡤࠤ࡫ࡵࡲ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠲ࠠࡰࡴࠣࡒࡴࡴࡥࠡ࡫ࡩࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᯀ")
        if not (config.get(bstack11l1l11_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᯁ"), None) in bstack11l11lllll1_opy_ and self.bstack11l1111111l_opy_()):
            return None
        bstack111lllll11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᯂ"), None)
        logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡄࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨᯃ").format(bstack111lllll11l_opy_))
        try:
            bstack11ll111l11l_opy_ = bstack11l1l11_opy_ (u"ࠥࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠣᯄ").format(bstack111lllll11l_opy_)
            payload = {
                bstack11l1l11_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᯅ"): config.get(bstack11l1l11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᯆ"), bstack11l1l11_opy_ (u"࠭ࠧᯇ")),
                bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᯈ"): config.get(bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᯉ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᯊ"): os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᯋ"), bstack11l1l11_opy_ (u"ࠦࠧᯌ")),
                bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣᯍ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᯎ")) or bstack11l1l11_opy_ (u"ࠢ࠱ࠤᯏ")),
                bstack11l1l11_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧᯐ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᯑ")) or bstack11l1l11_opy_ (u"ࠥ࠵ࠧᯒ")),
                bstack11l1l11_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨᯓ"): get_host_info(),
            }
            logger.debug(bstack11l1l11_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡲࡤࡽࡱࡵࡡࡥ࠼ࠣࡿࢂࠨᯔ").format(payload))
            response = bstack11ll1ll1ll1_opy_.bstack11ll11l11l1_opy_(bstack11ll111l11l_opy_, payload)
            if response:
                logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡇࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᯕ").format(response))
                return response
            else:
                logger.error(bstack11l1l11_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡘ࡙ࡎࡊ࠺ࠡࡽࢀࠦᯖ").format(bstack111lllll11l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l1l11_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡘ࡙ࡎࡊࠠࡼࡿ࠽ࠤࢀࢃࠢᯗ").format(bstack111lllll11l_opy_, e))
            return None
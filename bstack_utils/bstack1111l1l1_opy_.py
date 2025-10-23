# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import tempfile
import math
from bstack_utils import bstack11111ll111_opy_
from bstack_utils.constants import bstack11111ll1l_opy_, bstack11l11ll1l1l_opy_
from bstack_utils.helper import bstack11lll111l11_opy_, get_host_info
from bstack_utils.bstack11ll1lllll1_opy_ import bstack11lll111111_opy_
import json
import re
import sys
bstack11l111l11l1_opy_ = bstack111111l_opy_ (u"ࠥࡶࡪࡺࡲࡺࡖࡨࡷࡹࡹࡏ࡯ࡈࡤ࡭ࡱࡻࡲࡦࠤᬸ")
bstack11l1111111l_opy_ = bstack111111l_opy_ (u"ࠦࡦࡨ࡯ࡳࡶࡅࡹ࡮ࡲࡤࡐࡰࡉࡥ࡮ࡲࡵࡳࡧࠥᬹ")
bstack111lll1ll1l_opy_ = bstack111111l_opy_ (u"ࠧࡸࡵ࡯ࡒࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡋࡧࡩ࡭ࡧࡧࡊ࡮ࡸࡳࡵࠤᬺ")
bstack111lll1l1l1_opy_ = bstack111111l_opy_ (u"ࠨࡲࡦࡴࡸࡲࡕࡸࡥࡷ࡫ࡲࡹࡸࡲࡹࡇࡣ࡬ࡰࡪࡪࠢᬻ")
bstack111lll11l11_opy_ = bstack111111l_opy_ (u"ࠢࡴ࡭࡬ࡴࡋࡲࡡ࡬ࡻࡤࡲࡩࡌࡡࡪ࡮ࡨࡨࠧᬼ")
bstack11l1111lll1_opy_ = bstack111111l_opy_ (u"ࠣࡴࡸࡲࡘࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠧᬽ")
bstack111llll1lll_opy_ = {
    bstack11l111l11l1_opy_,
    bstack11l1111111l_opy_,
    bstack111lll1ll1l_opy_,
    bstack111lll1l1l1_opy_,
    bstack111lll11l11_opy_,
    bstack11l1111lll1_opy_
}
bstack11l1111l11l_opy_ = {bstack111111l_opy_ (u"ࠩࡳࡽࡹ࡫ࡳࡵࠩᬾ")}
logger = bstack11111ll111_opy_.get_logger(__name__, bstack11111ll1l_opy_)
class bstack111lll111ll_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l1111l1ll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1lll1ll11_opy_:
    _1ll1ll1l111_opy_ = None
    def __init__(self, config):
        self.bstack11l11111l11_opy_ = False
        self.bstack111lllll1ll_opy_ = False
        self.bstack11l111l111l_opy_ = False
        self.bstack111llllllll_opy_ = False
        self.bstack111lll11lll_opy_ = None
        self.bstack11l111ll11l_opy_ = bstack111lll111ll_opy_()
        self.bstack11l111ll111_opy_ = None
        opts = config.get(bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᬿ"), {})
        self.bstack111lllllll1_opy_ = config.get(bstack111111l_opy_ (u"ࠫࡸࡳࡡࡳࡶࡖࡩࡱ࡫ࡣࡵ࡫ࡲࡲࡋ࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࡩࡸࡋࡎࡗࠩᭀ"), bstack111111l_opy_ (u"ࠧࠨᭁ"))
        self.bstack11l1111l111_opy_ = config.get(bstack111111l_opy_ (u"࠭ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࡄࡎࡌࠫᭂ"), bstack111111l_opy_ (u"ࠢࠣᭃ"))
        bstack111llllll11_opy_ = opts.get(bstack11l1111lll1_opy_, {})
        bstack11l1111ll11_opy_ = None
        if bstack111111l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨ᭄") in bstack111llllll11_opy_:
            bstack11l1111ll11_opy_ = bstack111llllll11_opy_[bstack111111l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᭅ")]
            if bstack11l1111ll11_opy_ is None:
                bstack11l1111ll11_opy_ = []
        self.__11l111l1lll_opy_(
            bstack111llllll11_opy_.get(bstack111111l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᭆ"), False),
            bstack111llllll11_opy_.get(bstack111111l_opy_ (u"ࠫࡲࡵࡤࡦࠩᭇ"), bstack111111l_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬᭈ")),
            bstack11l1111ll11_opy_
        )
        self.__11l111l1l11_opy_(opts.get(bstack111lll1ll1l_opy_, False))
        self.__111lll1ll11_opy_(opts.get(bstack111lll1l1l1_opy_, False))
        self.__11l11111lll_opy_(opts.get(bstack111lll11l11_opy_, False))
    @classmethod
    def bstack111l111l_opy_(cls, config=None):
        if cls._1ll1ll1l111_opy_ is None and config is not None:
            cls._1ll1ll1l111_opy_ = bstack1lll1ll11_opy_(config)
        return cls._1ll1ll1l111_opy_
    @staticmethod
    def bstack1111lll1_opy_(config: dict) -> bool:
        bstack111llll1111_opy_ = config.get(bstack111111l_opy_ (u"࠭ࡴࡦࡵࡷࡓࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡒࡴࡹ࡯࡯࡯ࡵࠪᭉ"), {}).get(bstack11l111l11l1_opy_, {})
        return bstack111llll1111_opy_.get(bstack111111l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᭊ"), False)
    @staticmethod
    def bstack1111111l_opy_(config: dict) -> int:
        bstack111llll1111_opy_ = config.get(bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬᭋ"), {}).get(bstack11l111l11l1_opy_, {})
        retries = 0
        if bstack1lll1ll11_opy_.bstack1111lll1_opy_(config):
            retries = bstack111llll1111_opy_.get(bstack111111l_opy_ (u"ࠩࡰࡥࡽࡘࡥࡵࡴ࡬ࡩࡸ࠭ᭌ"), 1)
        return retries
    @staticmethod
    def bstack111l1l1111_opy_(config: dict) -> dict:
        bstack111llll1l1l_opy_ = config.get(bstack111111l_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᭍"), {})
        return {
            key: value for key, value in bstack111llll1l1l_opy_.items() if key in bstack111llll1lll_opy_
        }
    @staticmethod
    def bstack111lllll1l1_opy_():
        bstack111111l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭎")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠧࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡿࢂࠨ᭏").format(os.getenv(bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᭐")))))
    @staticmethod
    def bstack111lllll111_opy_(test_name: str):
        bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡈ࡮ࡥࡤ࡭ࠣ࡭࡫ࠦࡴࡩࡧࠣࡥࡧࡵࡲࡵࠢࡥࡹ࡮ࡲࡤࠡࡨ࡬ࡰࡪࠦࡥࡹ࡫ࡶࡸࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦ᭑")
        bstack111lll11l1l_opy_ = os.path.join(tempfile.gettempdir(), bstack111111l_opy_ (u"ࠣࡨࡤ࡭ࡱ࡫ࡤࡠࡶࡨࡷࡹࡹ࡟ࡼࡿ࠱ࡸࡽࡺࠢ᭒").format(os.getenv(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡈࡗ࡙ࡎࡕࡃࡡࡘ࡙ࡎࡊࠢ᭓"))))
        with open(bstack111lll11l1l_opy_, bstack111111l_opy_ (u"ࠪࡥࠬ᭔")) as file:
            file.write(bstack111111l_opy_ (u"ࠦࢀࢃ࡜࡯ࠤ᭕").format(test_name))
    @staticmethod
    def bstack111llllll1l_opy_(framework: str) -> bool:
       return framework.lower() in bstack11l1111l11l_opy_
    @staticmethod
    def bstack11l1llll11l_opy_(config: dict) -> bool:
        bstack11l11111l1l_opy_ = config.get(bstack111111l_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭖"), {}).get(bstack11l1111111l_opy_, {})
        return bstack11l11111l1l_opy_.get(bstack111111l_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ᭗"), False)
    @staticmethod
    def bstack11l1lllllll_opy_(config: dict, bstack11l1llll111_opy_: int = 0) -> int:
        bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡌ࡫ࡴࠡࡶ࡫ࡩࠥ࡬ࡡࡪ࡮ࡸࡶࡪࠦࡴࡩࡴࡨࡷ࡭ࡵ࡬ࡥ࠮ࠣࡻ࡭࡯ࡣࡩࠢࡦࡥࡳࠦࡢࡦࠢࡤࡲࠥࡧࡢࡴࡱ࡯ࡹࡹ࡫ࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡴࠣࡥࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡆࡸࡧࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡥࡲࡲ࡫࡯ࡧࠡࠪࡧ࡭ࡨࡺࠩ࠻ࠢࡗ࡬ࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳࡻ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡷࡳࡹࡧ࡬ࡠࡶࡨࡷࡹࡹࠠࠩ࡫ࡱࡸ࠮ࡀࠠࡕࡪࡨࠤࡹࡵࡴࡢ࡮ࠣࡲࡺࡳࡢࡦࡴࠣࡳ࡫ࠦࡴࡦࡵࡷࡷࠥ࠮ࡲࡦࡳࡸ࡭ࡷ࡫ࡤࠡࡨࡲࡶࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦ࠯ࡥࡥࡸ࡫ࡤࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧࡷ࠮࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴ࠼ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡ࡫ࡱࡸ࠿ࠦࡔࡩࡧࠣࡪࡦ࡯࡬ࡶࡴࡨࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᭘")
        bstack11l11111l1l_opy_ = config.get(bstack111111l_opy_ (u"ࠨࡶࡨࡷࡹࡕࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡔࡶࡴࡪࡱࡱࡷࠬ᭙"), {}).get(bstack111111l_opy_ (u"ࠩࡤࡦࡴࡸࡴࡃࡷ࡬ࡰࡩࡕ࡮ࡇࡣ࡬ࡰࡺࡸࡥࠨ᭚"), {})
        bstack11l1111llll_opy_ = 0
        bstack111llll11l1_opy_ = 0
        if bstack1lll1ll11_opy_.bstack11l1llll11l_opy_(config):
            bstack111llll11l1_opy_ = bstack11l11111l1l_opy_.get(bstack111111l_opy_ (u"ࠪࡱࡦࡾࡆࡢ࡫࡯ࡹࡷ࡫ࡳࠨ᭛"), 5)
            if isinstance(bstack111llll11l1_opy_, str) and bstack111llll11l1_opy_.endswith(bstack111111l_opy_ (u"ࠫࠪ࠭᭜")):
                try:
                    percentage = int(bstack111llll11l1_opy_.strip(bstack111111l_opy_ (u"ࠬࠫࠧ᭝")))
                    if bstack11l1llll111_opy_ > 0:
                        bstack11l1111llll_opy_ = math.ceil((percentage * bstack11l1llll111_opy_) / 100)
                    else:
                        raise ValueError(bstack111111l_opy_ (u"ࠨࡔࡰࡶࡤࡰࠥࡺࡥࡴࡶࡶࠤࡲࡻࡳࡵࠢࡥࡩࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠࡧࡱࡵࠤࡵ࡫ࡲࡤࡧࡱࡸࡦ࡭ࡥ࠮ࡤࡤࡷࡪࡪࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࡶ࠲ࠧ᭞"))
                except ValueError as e:
                    raise ValueError(bstack111111l_opy_ (u"ࠢࡊࡰࡹࡥࡱ࡯ࡤࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩࠥࡼࡡ࡭ࡷࡨࠤ࡫ࡵࡲࠡ࡯ࡤࡼࡋࡧࡩ࡭ࡷࡵࡩࡸࡀࠠࡼࡿࠥ᭟").format(bstack111llll11l1_opy_)) from e
            else:
                bstack11l1111llll_opy_ = int(bstack111llll11l1_opy_)
        logger.info(bstack111111l_opy_ (u"ࠣࡏࡤࡼࠥ࡬ࡡࡪ࡮ࡸࡶࡪࡹࠠࡵࡪࡵࡩࡸ࡮࡯࡭ࡦࠣࡷࡪࡺࠠࡵࡱ࠽ࠤࢀࢃࠠࠩࡨࡵࡳࡲࠦࡣࡰࡰࡩ࡭࡬ࡀࠠࡼࡿࠬࠦ᭠").format(bstack11l1111llll_opy_, bstack111llll11l1_opy_))
        return bstack11l1111llll_opy_
    def bstack11l111111l1_opy_(self):
        return self.bstack111llllllll_opy_
    def bstack111llll111l_opy_(self):
        return self.bstack111lll11lll_opy_
    def bstack111llll1ll1_opy_(self):
        return self.bstack11l111ll111_opy_
    def __11l111l1lll_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llllllll_opy_ = bool(enabled)
            if mode not in [bstack111111l_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩ᭡"), bstack111111l_opy_ (u"ࠪࡶࡪࡲࡥࡷࡣࡱࡸࡔࡴ࡬ࡺࠩ᭢")]:
                logger.warning(bstack111111l_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡹ࡭ࡢࡴࡷࠤࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠠ࡮ࡱࡧࡩࠥ࠭ࡻࡾࠩࠣࡴࡷࡵࡶࡪࡦࡨࡨ࠳ࠦࡄࡦࡨࡤࡹࡱࡺࡩ࡯ࡩࠣࡸࡴࠦࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡈ࡬ࡶࡸࡺࠧ࠯ࠤ᭣").format(mode))
                mode = bstack111111l_opy_ (u"ࠬࡸࡥ࡭ࡧࡹࡥࡳࡺࡆࡪࡴࡶࡸࠬ᭤")
            self.bstack111lll11lll_opy_ = mode
            if source is None:
                self.bstack11l111ll111_opy_ = None
            elif isinstance(source, list):
                self.bstack11l111ll111_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack111111l_opy_ (u"࠭࠮࡫ࡵࡲࡲࠬ᭥")):
                self.bstack11l111ll111_opy_ = self._111lll11ll1_opy_(source)
            self.__111lll111l1_opy_()
        except Exception as e:
            logger.error(bstack111111l_opy_ (u"ࠢࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡷࡪࡺࠠࡴ࡯ࡤࡶࡹࠦࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢ࠰ࠤࡪࡴࡡࡣ࡮ࡨࡨ࠿ࠦࡻࡾ࠮ࠣࡱࡴࡪࡥ࠻ࠢࡾࢁ࠱ࠦࡳࡰࡷࡵࡧࡪࡀࠠࡼࡿ࠱ࠤࡊࡸࡲࡰࡴ࠽ࠤࢀࢃࠢ᭦").format(enabled, mode, source, e))
    def bstack11l111l1ll1_opy_(self):
        return self.bstack11l11111l11_opy_
    def __11l111l1l11_opy_(self, value):
        self.bstack11l11111l11_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def bstack111lll1l1ll_opy_(self):
        return self.bstack111lllll1ll_opy_
    def __111lll1ll11_opy_(self, value):
        self.bstack111lllll1ll_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def bstack11l11111111_opy_(self):
        return self.bstack11l111l111l_opy_
    def __11l11111lll_opy_(self, value):
        self.bstack11l111l111l_opy_ = bool(value)
        self.__111lll111l1_opy_()
    def __111lll111l1_opy_(self):
        if self.bstack111llllllll_opy_:
            self.bstack11l11111l11_opy_ = False
            self.bstack111lllll1ll_opy_ = False
            self.bstack11l111l111l_opy_ = False
            self.bstack11l111ll11l_opy_.enable(bstack11l1111lll1_opy_)
        elif self.bstack11l11111l11_opy_:
            self.bstack111lllll1ll_opy_ = False
            self.bstack11l111l111l_opy_ = False
            self.bstack111llllllll_opy_ = False
            self.bstack11l111ll11l_opy_.enable(bstack111lll1ll1l_opy_)
        elif self.bstack111lllll1ll_opy_:
            self.bstack11l11111l11_opy_ = False
            self.bstack11l111l111l_opy_ = False
            self.bstack111llllllll_opy_ = False
            self.bstack11l111ll11l_opy_.enable(bstack111lll1l1l1_opy_)
        elif self.bstack11l111l111l_opy_:
            self.bstack11l11111l11_opy_ = False
            self.bstack111lllll1ll_opy_ = False
            self.bstack111llllllll_opy_ = False
            self.bstack11l111ll11l_opy_.enable(bstack111lll11l11_opy_)
        else:
            self.bstack11l111ll11l_opy_.disable()
    def bstack1111l111_opy_(self):
        return self.bstack11l111ll11l_opy_.bstack11l1111l1ll_opy_()
    def bstack111l111ll_opy_(self):
        if self.bstack11l111ll11l_opy_.bstack11l1111l1ll_opy_():
            return self.bstack11l111ll11l_opy_.get_name()
        return None
    def _111lll11ll1_opy_(self, bstack111lll1lll1_opy_):
        bstack111111l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡡࡳࡵࡨࠤࡏ࡙ࡏࡏࠢࡶࡳࡺࡸࡣࡦࠢࡦࡳࡳ࡬ࡩࡨࡷࡵࡥࡹ࡯࡯࡯ࠢࡩ࡭ࡱ࡫ࠠࡢࡰࡧࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡮ࡺࠠࡧࡱࡵࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡹ࡯ࡶࡴࡦࡩࡤ࡬ࡩ࡭ࡧࡢࡴࡦࡺࡨࠡࠪࡶࡸࡷ࠯࠺ࠡࡒࡤࡸ࡭ࠦࡴࡰࠢࡷ࡬ࡪࠦࡊࡔࡑࡑࠤࡨࡵ࡮ࡧ࡫ࡪࡹࡷࡧࡴࡪࡱࡱࠤ࡫࡯࡬ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡰ࡮ࡹࡴ࠻ࠢࡉࡳࡷࡳࡡࡵࡶࡨࡨࠥࡲࡩࡴࡶࠣࡳ࡫ࠦࡲࡦࡲࡲࡷ࡮ࡺ࡯ࡳࡻࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࡶࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭧")
        if not os.path.isfile(bstack111lll1lll1_opy_):
            logger.error(bstack111111l_opy_ (u"ࠤࡖࡳࡺࡸࡣࡦࠢࡩ࡭ࡱ࡫ࠠࠨࡽࢀࠫࠥࡪ࡯ࡦࡵࠣࡲࡴࡺࠠࡦࡺ࡬ࡷࡹ࠴ࠢ᭨").format(bstack111lll1lll1_opy_))
            return []
        data = None
        try:
            with open(bstack111lll1lll1_opy_, bstack111111l_opy_ (u"ࠥࡶࠧ᭩")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack111111l_opy_ (u"ࠦࡊࡸࡲࡰࡴࠣࡴࡦࡸࡳࡪࡰࡪࠤࡏ࡙ࡏࡏࠢࡩࡶࡴࡳࠠࡴࡱࡸࡶࡨ࡫ࠠࡧ࡫࡯ࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢ᭪").format(bstack111lll1lll1_opy_, e))
            return []
        _111llll1l11_opy_ = None
        _111lllll11l_opy_ = None
        def _111lll1l11l_opy_():
            bstack111lll1l111_opy_ = {}
            bstack11l11111ll1_opy_ = {}
            try:
                if self.bstack111lllllll1_opy_.startswith(bstack111111l_opy_ (u"ࠬࢁࠧ᭫")) and self.bstack111lllllll1_opy_.endswith(bstack111111l_opy_ (u"࠭ࡽࠨ᭬")):
                    bstack111lll1l111_opy_ = json.loads(self.bstack111lllllll1_opy_)
                else:
                    bstack111lll1l111_opy_ = dict(item.split(bstack111111l_opy_ (u"ࠧ࠻ࠩ᭭")) for item in self.bstack111lllllll1_opy_.split(bstack111111l_opy_ (u"ࠨ࠮ࠪ᭮")) if bstack111111l_opy_ (u"ࠩ࠽ࠫ᭯") in item) if self.bstack111lllllll1_opy_ else {}
                if self.bstack11l1111l111_opy_.startswith(bstack111111l_opy_ (u"ࠪࡿࠬ᭰")) and self.bstack11l1111l111_opy_.endswith(bstack111111l_opy_ (u"ࠫࢂ࠭᭱")):
                    bstack11l11111ll1_opy_ = json.loads(self.bstack11l1111l111_opy_)
                else:
                    bstack11l11111ll1_opy_ = dict(item.split(bstack111111l_opy_ (u"ࠬࡀࠧ᭲")) for item in self.bstack11l1111l111_opy_.split(bstack111111l_opy_ (u"࠭ࠬࠨ᭳")) if bstack111111l_opy_ (u"ࠧ࠻ࠩ᭴") in item) if self.bstack11l1111l111_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack111111l_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡨࡨࡥࡹࡻࡲࡦࠢࡥࡶࡦࡴࡣࡩࠢࡰࡥࡵࡶࡩ࡯ࡩࡶ࠾ࠥࢁࡽࠣ᭵").format(e))
            logger.debug(bstack111111l_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡱࡦࡶࡰࡪࡰࡪࡷࠥ࡬ࡲࡰ࡯ࠣࡩࡳࡼ࠺ࠡࡽࢀ࠰ࠥࡉࡌࡊ࠼ࠣࡿࢂࠨ᭶").format(bstack111lll1l111_opy_, bstack11l11111ll1_opy_))
            return bstack111lll1l111_opy_, bstack11l11111ll1_opy_
        if _111llll1l11_opy_ is None or _111lllll11l_opy_ is None:
            _111llll1l11_opy_, _111lllll11l_opy_ = _111lll1l11l_opy_()
        def bstack111llll11ll_opy_(name, bstack11l111111ll_opy_):
            if name in _111lllll11l_opy_:
                return _111lllll11l_opy_[name]
            if name in _111llll1l11_opy_:
                return _111llll1l11_opy_[name]
            if bstack11l111111ll_opy_.get(bstack111111l_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪ᭷")):
                return bstack11l111111ll_opy_[bstack111111l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫ᭸")]
            return None
        if isinstance(data, dict):
            bstack11l1111l1l1_opy_ = []
            bstack11l1111ll1l_opy_ = re.compile(bstack111111l_opy_ (u"ࡷ࠭࡞࡜ࡃ࠰࡞࠵࠳࠹ࡠ࡟࠮ࠨࠬ᭹"))
            for name, bstack11l111111ll_opy_ in data.items():
                if not isinstance(bstack11l111111ll_opy_, dict):
                    continue
                if not bstack11l111111ll_opy_.get(bstack111111l_opy_ (u"࠭ࡵࡳ࡮ࠪ᭺")):
                    logger.warning(bstack111111l_opy_ (u"ࠢࡓࡧࡳࡳࡸ࡯ࡴࡰࡴࡼࠤ࡚ࡘࡌࠡ࡫ࡶࠤࡲ࡯ࡳࡴ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡶࡳࡺࡸࡣࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᭻").format(name, bstack11l111111ll_opy_))
                    continue
                if not bstack11l1111ll1l_opy_.match(name):
                    logger.warning(bstack111111l_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡳࡺࡸࡣࡦࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠦࡦࡰࡴࡰࡥࡹࠦࡦࡰࡴࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧ᭼").format(name, bstack11l111111ll_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack111111l_opy_ (u"ࠤࡖࡳࡺࡸࡣࡦࠢ࡬ࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠦࠧࡼࡿࠪࠤࡲࡻࡳࡵࠢ࡫ࡥࡻ࡫ࠠࡢࠢ࡯ࡩࡳ࡭ࡴࡩࠢࡥࡩࡹࡽࡥࡦࡰࠣ࠵ࠥࡧ࡮ࡥࠢ࠶࠴ࠥࡩࡨࡢࡴࡤࡧࡹ࡫ࡲࡴ࠰ࠥ᭽").format(name))
                    continue
                bstack11l111111ll_opy_ = bstack11l111111ll_opy_.copy()
                bstack11l111111ll_opy_[bstack111111l_opy_ (u"ࠪࡲࡦࡳࡥࠨ᭾")] = name
                bstack11l111111ll_opy_[bstack111111l_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫ᭿")] = bstack111llll11ll_opy_(name, bstack11l111111ll_opy_)
                if not bstack11l111111ll_opy_.get(bstack111111l_opy_ (u"ࠬ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠬᮀ")):
                    logger.warning(bstack111111l_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡯ࡱࡷࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡪࡪࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᮁ").format(name, bstack11l111111ll_opy_))
                    continue
                if bstack11l111111ll_opy_.get(bstack111111l_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᮂ")) and bstack11l111111ll_opy_[bstack111111l_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬᮃ")] == bstack11l111111ll_opy_[bstack111111l_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮄ")]:
                    logger.warning(bstack111111l_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡦࡴࡤࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡢࡰࡱࡳࡹࠦࡢࡦࠢࡷ࡬ࡪࠦࡳࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮅ").format(name, bstack11l111111ll_opy_))
                    continue
                bstack11l1111l1l1_opy_.append(bstack11l111111ll_opy_)
            return bstack11l1111l1l1_opy_
        return data
    def bstack11l111l1111_opy_(self):
        data = {
            bstack111111l_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᮆ"): {
                bstack111111l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮇ"): self.bstack11l111111l1_opy_(),
                bstack111111l_opy_ (u"࠭࡭ࡰࡦࡨࠫᮈ"): self.bstack111llll111l_opy_(),
                bstack111111l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᮉ"): self.bstack111llll1ll1_opy_()
            }
        }
        return data
    def bstack11l111l1l1l_opy_(self, config):
        bstack111lll1llll_opy_ = {}
        bstack111lll1llll_opy_[bstack111111l_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᮊ")] = {
            bstack111111l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮋ"): self.bstack11l111111l1_opy_(),
            bstack111111l_opy_ (u"ࠪࡱࡴࡪࡥࠨᮌ"): self.bstack111llll111l_opy_()
        }
        bstack111lll1llll_opy_[bstack111111l_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡴࡷ࡫ࡶࡪࡱࡸࡷࡱࡿ࡟ࡧࡣ࡬ࡰࡪࡪࠧᮍ")] = {
            bstack111111l_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᮎ"): self.bstack111lll1l1ll_opy_()
        }
        bstack111lll1llll_opy_[bstack111111l_opy_ (u"࠭ࡲࡶࡰࡢࡴࡷ࡫ࡶࡪࡱࡸࡷࡱࡿ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡧ࡫ࡵࡷࡹ࠭ᮏ")] = {
            bstack111111l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮐ"): self.bstack11l111l1ll1_opy_()
        }
        bstack111lll1llll_opy_[bstack111111l_opy_ (u"ࠨࡵ࡮࡭ࡵࡥࡦࡢ࡫࡯࡭ࡳ࡭࡟ࡢࡰࡧࡣ࡫ࡲࡡ࡬ࡻࠪᮑ")] = {
            bstack111111l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮒ"): self.bstack11l11111111_opy_()
        }
        if self.bstack1111lll1_opy_(config):
            bstack111lll1llll_opy_[bstack111111l_opy_ (u"ࠪࡶࡪࡺࡲࡺࡡࡷࡩࡸࡺࡳࡠࡱࡱࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠬᮓ")] = {
                bstack111111l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮔ"): True,
                bstack111111l_opy_ (u"ࠬࡳࡡࡹࡡࡵࡩࡹࡸࡩࡦࡵࠪᮕ"): self.bstack1111111l_opy_(config)
            }
        if self.bstack11l1llll11l_opy_(config):
            bstack111lll1llll_opy_[bstack111111l_opy_ (u"࠭ࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᮖ")] = {
                bstack111111l_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮗ"): True,
                bstack111111l_opy_ (u"ࠨ࡯ࡤࡼࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡹࠧᮘ"): self.bstack11l1lllllll_opy_(config)
            }
        return bstack111lll1llll_opy_
    def bstack1111lll11l_opy_(self, config):
        bstack111111l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡰ࡮࡯ࡩࡨࡺࡳࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡨࡹࠡ࡯ࡤ࡯࡮ࡴࡧࠡࡣࠣࡧࡦࡲ࡬ࠡࡶࡲࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠤ࠭ࡹࡴࡳࠫ࠽ࠤ࡙࡮ࡥࠡࡗࡘࡍࡉࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡢࡶ࡫࡯ࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡧࡥࡹࡧࠠࡧࡱࡵ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡪࡥࡷ࠾ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮙ")
        if not (config.get(bstack111111l_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭ᮚ"), None) in bstack11l11ll1l1l_opy_ and self.bstack11l111111l1_opy_()):
            return None
        bstack11l111l11ll_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩᮛ"), None)
        logger.debug(bstack111111l_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡤࡸ࡭ࡱࡪࠠࡖࡗࡌࡈ࠿ࠦࡻࡾࠤᮜ").format(bstack11l111l11ll_opy_))
        try:
            bstack11ll11ll111_opy_ = bstack111111l_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠦᮝ").format(bstack11l111l11ll_opy_)
            payload = {
                bstack111111l_opy_ (u"ࠢࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠧᮞ"): config.get(bstack111111l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᮟ"), bstack111111l_opy_ (u"ࠩࠪᮠ")),
                bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠨᮡ"): config.get(bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᮢ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥᮣ"): os.environ.get(bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧᮤ"), bstack111111l_opy_ (u"ࠢࠣᮥ")),
                bstack111111l_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦᮦ"): int(os.environ.get(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᮧ")) or bstack111111l_opy_ (u"ࠥ࠴ࠧᮨ")),
                bstack111111l_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣᮩ"): int(os.environ.get(bstack111111l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ᮪࡚ࠢ")) or bstack111111l_opy_ (u"ࠨ࠱᮫ࠣ")),
                bstack111111l_opy_ (u"ࠢࡩࡱࡶࡸࡎࡴࡦࡰࠤᮬ"): get_host_info(),
            }
            logger.debug(bstack111111l_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡵࡧࡹ࡭ࡱࡤࡨ࠿ࠦࡻࡾࠤᮭ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll11ll11l_opy_(bstack11ll11ll111_opy_, payload)
            if response:
                logger.debug(bstack111111l_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡃࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᮮ").format(response))
                return response
            else:
                logger.error(bstack111111l_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢᮯ").format(bstack11l111l11ll_opy_))
                return None
        except Exception as e:
            logger.error(bstack111111l_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆࠣࡿࢂࡀࠠࡼࡿࠥ᮰").format(bstack11l111l11ll_opy_, e))
            return None
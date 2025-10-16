# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import tempfile
import math
from bstack_utils import bstack1ll11111l1_opy_
from bstack_utils.constants import bstack11l11ll111_opy_, bstack11l1l1ll1ll_opy_
from bstack_utils.helper import bstack11lll11l1ll_opy_, get_host_info
from bstack_utils.bstack11lll11l111_opy_ import bstack11lll111111_opy_
import json
import re
import sys
bstack111lll1ll1l_opy_ = bstack1lllll1_opy_ (u"ࠢࡳࡧࡷࡶࡾ࡚ࡥࡴࡶࡶࡓࡳࡌࡡࡪ࡮ࡸࡶࡪࠨᭃ")
bstack111lll11ll1_opy_ = bstack1lllll1_opy_ (u"ࠣࡣࡥࡳࡷࡺࡂࡶ࡫࡯ࡨࡔࡴࡆࡢ࡫࡯ࡹࡷ࡫᭄ࠢ")
bstack11l11111ll1_opy_ = bstack1lllll1_opy_ (u"ࠤࡵࡹࡳࡖࡲࡦࡸ࡬ࡳࡺࡹ࡬ࡺࡈࡤ࡭ࡱ࡫ࡤࡇ࡫ࡵࡷࡹࠨᭅ")
bstack11l1111l1ll_opy_ = bstack1lllll1_opy_ (u"ࠥࡶࡪࡸࡵ࡯ࡒࡵࡩࡻ࡯࡯ࡶࡵ࡯ࡽࡋࡧࡩ࡭ࡧࡧࠦᭆ")
bstack11l111ll111_opy_ = bstack1lllll1_opy_ (u"ࠦࡸࡱࡩࡱࡈ࡯ࡥࡰࡿࡡ࡯ࡦࡉࡥ࡮ࡲࡥࡥࠤᭇ")
bstack11l11111l1l_opy_ = bstack1lllll1_opy_ (u"ࠧࡸࡵ࡯ࡕࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠤᭈ")
bstack111lll1l11l_opy_ = {
    bstack111lll1ll1l_opy_,
    bstack111lll11ll1_opy_,
    bstack11l11111ll1_opy_,
    bstack11l1111l1ll_opy_,
    bstack11l111ll111_opy_,
    bstack11l11111l1l_opy_
}
bstack111lll11l11_opy_ = {bstack1lllll1_opy_ (u"࠭ࡰࡺࡶࡨࡷࡹ࠭ᭉ")}
logger = bstack1ll11111l1_opy_.get_logger(__name__, bstack11l11ll111_opy_)
class bstack11l1111l111_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l111ll11l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack11l111ll_opy_:
    _1ll1ll11lll_opy_ = None
    def __init__(self, config):
        self.bstack111llll1lll_opy_ = False
        self.bstack11l1111ll1l_opy_ = False
        self.bstack111llll1l11_opy_ = False
        self.bstack111llll1111_opy_ = False
        self.bstack11l111l11l1_opy_ = None
        self.bstack111lll11lll_opy_ = bstack11l1111l111_opy_()
        self.bstack11l11111lll_opy_ = None
        opts = config.get(bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᭊ"), {})
        self.bstack11l111l1111_opy_ = config.get(bstack1lllll1_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡈࡒ࡛࠭ᭋ"), bstack1lllll1_opy_ (u"ࠤࠥᭌ"))
        self.bstack11l111111l1_opy_ = config.get(bstack1lllll1_opy_ (u"ࠪࡷࡲࡧࡲࡵࡕࡨࡰࡪࡩࡴࡪࡱࡱࡊࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࡨࡷࡈࡒࡉࠨ᭍"), bstack1lllll1_opy_ (u"ࠦࠧ᭎"))
        bstack111lllllll1_opy_ = opts.get(bstack11l11111l1l_opy_, {})
        bstack111llll1l1l_opy_ = None
        if bstack1lllll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬ᭏") in bstack111lllllll1_opy_:
            bstack111llll1l1l_opy_ = bstack111lllllll1_opy_[bstack1lllll1_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭᭐")]
            if bstack111llll1l1l_opy_ is None:
                bstack111llll1l1l_opy_ = []
        self.__11l1111l11l_opy_(
            bstack111lllllll1_opy_.get(bstack1lllll1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᭑"), False),
            bstack111lllllll1_opy_.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭᭒"), bstack1lllll1_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩ᭓")),
            bstack111llll1l1l_opy_
        )
        self.__111llll1ll1_opy_(opts.get(bstack11l11111ll1_opy_, False))
        self.__11l111l1l1l_opy_(opts.get(bstack11l1111l1ll_opy_, False))
        self.__111llll11ll_opy_(opts.get(bstack11l111ll111_opy_, False))
    @classmethod
    def bstack11111l1l_opy_(cls, config=None):
        if cls._1ll1ll11lll_opy_ is None and config is not None:
            cls._1ll1ll11lll_opy_ = bstack11l111ll_opy_(config)
        return cls._1ll1ll11lll_opy_
    @staticmethod
    def bstack1111111l_opy_(config: dict) -> bool:
        bstack11l111l1lll_opy_ = config.get(bstack1lllll1_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧ᭔"), {}).get(bstack111lll1ll1l_opy_, {})
        return bstack11l111l1lll_opy_.get(bstack1lllll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬ᭕"), False)
    @staticmethod
    def bstack111ll1ll_opy_(config: dict) -> int:
        bstack11l111l1lll_opy_ = config.get(bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭖"), {}).get(bstack111lll1ll1l_opy_, {})
        retries = 0
        if bstack11l111ll_opy_.bstack1111111l_opy_(config):
            retries = bstack11l111l1lll_opy_.get(bstack1lllll1_opy_ (u"࠭࡭ࡢࡺࡕࡩࡹࡸࡩࡦࡵࠪ᭗"), 1)
        return retries
    @staticmethod
    def bstack11l1ll1ll1_opy_(config: dict) -> dict:
        bstack11l111ll1l1_opy_ = config.get(bstack1lllll1_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫ᭘"), {})
        return {
            key: value for key, value in bstack11l111ll1l1_opy_.items() if key in bstack111lll1l11l_opy_
        }
    @staticmethod
    def bstack11l1111ll11_opy_():
        bstack1lllll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᭙")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥ᭚").format(os.getenv(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣ᭛")))))
    @staticmethod
    def bstack11l11111l11_opy_(test_name: str):
        bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᭜")
        bstack11l111ll1ll_opy_ = os.path.join(tempfile.gettempdir(), bstack1lllll1_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷࠦ᭝").format(os.getenv(bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇࠦ᭞"))))
        with open(bstack11l111ll1ll_opy_, bstack1lllll1_opy_ (u"ࠧࡢࠩ᭟")) as file:
            file.write(bstack1lllll1_opy_ (u"ࠣࡽࢀࡠࡳࠨ᭠").format(test_name))
    @staticmethod
    def bstack111llllllll_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll11l11_opy_
    @staticmethod
    def bstack11ll1111ll1_opy_(config: dict) -> bool:
        bstack111llll111l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭᭡"), {}).get(bstack111lll11ll1_opy_, {})
        return bstack111llll111l_opy_.get(bstack1lllll1_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫ᭢"), False)
    @staticmethod
    def bstack11ll111l111_opy_(config: dict, bstack11ll111111l_opy_: int = 0) -> int:
        bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡉࡨࡸࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠲ࠠࡸࡪ࡬ࡧ࡭ࠦࡣࡢࡰࠣࡦࡪࠦࡡ࡯ࠢࡤࡦࡸࡵ࡬ࡶࡶࡨࠤࡳࡻ࡭ࡣࡧࡵࠤࡴࡸࠠࡢࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡰࡶࡤࡰࡤࡺࡥࡴࡶࡶࠤ࠭࡯࡮ࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࠫࡶࡪࡷࡵࡪࡴࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᭣")
        bstack111llll111l_opy_ = config.get(bstack1lllll1_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᭤"), {}).get(bstack1lllll1_opy_ (u"࠭ࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠬ᭥"), {})
        bstack111llllll1l_opy_ = 0
        bstack111lll1l1l1_opy_ = 0
        if bstack11l111ll_opy_.bstack11ll1111ll1_opy_(config):
            bstack111lll1l1l1_opy_ = bstack111llll111l_opy_.get(bstack1lllll1_opy_ (u"ࠧ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷࠬ᭦"), 5)
            if isinstance(bstack111lll1l1l1_opy_, str) and bstack111lll1l1l1_opy_.endswith(bstack1lllll1_opy_ (u"ࠨࠧࠪ᭧")):
                try:
                    percentage = int(bstack111lll1l1l1_opy_.strip(bstack1lllll1_opy_ (u"ࠩࠨࠫ᭨")))
                    if bstack11ll111111l_opy_ > 0:
                        bstack111llllll1l_opy_ = math.ceil((percentage * bstack11ll111111l_opy_) / 100)
                    else:
                        raise ValueError(bstack1lllll1_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳ࠯ࠤ᭩"))
                except ValueError as e:
                    raise ValueError(bstack1lllll1_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦࠢࡹࡥࡱࡻࡥࠡࡨࡲࡶࠥࡳࡡࡹࡈࡤ࡭ࡱࡻࡲࡦࡵ࠽ࠤࢀࢃࠢ᭪").format(bstack111lll1l1l1_opy_)) from e
            else:
                bstack111llllll1l_opy_ = int(bstack111lll1l1l1_opy_)
        logger.info(bstack1lllll1_opy_ (u"ࠧࡓࡡࡹࠢࡩࡥ࡮ࡲࡵࡳࡧࡶࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡴࡧࡷࠤࡹࡵ࠺ࠡࡽࢀࠤ࠭࡬ࡲࡰ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࢀࢃࠩࠣ᭫").format(bstack111llllll1l_opy_, bstack111lll1l1l1_opy_))
        return bstack111llllll1l_opy_
    def bstack11l111l1ll1_opy_(self):
        return self.bstack111llll1111_opy_
    def bstack11l111111ll_opy_(self):
        return self.bstack11l111l11l1_opy_
    def bstack11l1111llll_opy_(self):
        return self.bstack11l11111lll_opy_
    def __11l1111l11l_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll1111_opy_ = bool(enabled)
            if mode not in [bstack1lllll1_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ᭬࠭"), bstack1lllll1_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡑࡱࡰࡾ࠭᭭")]:
                logger.warning(bstack1lllll1_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡲࡵࡤࡦࠢࠪࡿࢂ࠭ࠠࡱࡴࡲࡺ࡮ࡪࡥࡥ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ࠳ࠨ᭮").format(mode))
                mode = bstack1lllll1_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩ᭯")
            self.bstack11l111l11l1_opy_ = mode
            if source is None:
                self.bstack11l11111lll_opy_ = None
            elif isinstance(source, list):
                self.bstack11l11111lll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack1lllll1_opy_ (u"ࠪ࠲࡯ࡹ࡯࡯ࠩ᭰")):
                self.bstack11l11111lll_opy_ = self._111llll11l1_opy_(source)
            self.__111lllll1ll_opy_()
        except Exception as e:
            logger.error(bstack1lllll1_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦ࠭ࠡࡧࡱࡥࡧࡲࡥࡥ࠼ࠣࡿࢂ࠲ࠠ࡮ࡱࡧࡩ࠿ࠦࡻࡾ࠮ࠣࡷࡴࡻࡲࡤࡧ࠽ࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦ᭱").format(enabled, mode, source, e))
    def bstack111lll1lll1_opy_(self):
        return self.bstack111llll1lll_opy_
    def __111llll1ll1_opy_(self, value):
        self.bstack111llll1lll_opy_ = bool(value)
        self.__111lllll1ll_opy_()
    def bstack11l1111111l_opy_(self):
        return self.bstack11l1111ll1l_opy_
    def __11l111l1l1l_opy_(self, value):
        self.bstack11l1111ll1l_opy_ = bool(value)
        self.__111lllll1ll_opy_()
    def bstack11l1111lll1_opy_(self):
        return self.bstack111llll1l11_opy_
    def __111llll11ll_opy_(self, value):
        self.bstack111llll1l11_opy_ = bool(value)
        self.__111lllll1ll_opy_()
    def __111lllll1ll_opy_(self):
        if self.bstack111llll1111_opy_:
            self.bstack111llll1lll_opy_ = False
            self.bstack11l1111ll1l_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l11111l1l_opy_)
        elif self.bstack111llll1lll_opy_:
            self.bstack11l1111ll1l_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l11111ll1_opy_)
        elif self.bstack11l1111ll1l_opy_:
            self.bstack111llll1lll_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l1111l1ll_opy_)
        elif self.bstack111llll1l11_opy_:
            self.bstack111llll1lll_opy_ = False
            self.bstack11l1111ll1l_opy_ = False
            self.bstack111llll1111_opy_ = False
            self.bstack111lll11lll_opy_.enable(bstack11l111ll111_opy_)
        else:
            self.bstack111lll11lll_opy_.disable()
    def bstack111ll111_opy_(self):
        return self.bstack111lll11lll_opy_.bstack11l111ll11l_opy_()
    def bstack1ll1l1llll_opy_(self):
        if self.bstack111lll11lll_opy_.bstack11l111ll11l_opy_():
            return self.bstack111lll11lll_opy_.get_name()
        return None
    def _111llll11l1_opy_(self, bstack11l111l1l11_opy_):
        bstack1lllll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡳࡰࡷࡵࡧࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡦࡪ࡮ࡨࠤࡦࡴࡤࠡࡨࡲࡶࡲࡧࡴࠡ࡫ࡷࠤ࡫ࡵࡲࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡳࡺࡸࡣࡦࡡࡩ࡭ࡱ࡫࡟ࡱࡣࡷ࡬ࠥ࠮ࡳࡵࡴࠬ࠾ࠥࡖࡡࡵࡪࠣࡸࡴࠦࡴࡩࡧࠣࡎࡘࡕࡎࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡆࡰࡴࡰࡥࡹࡺࡥࡥࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡶࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᭲")
        if not os.path.isfile(bstack11l111l1l11_opy_):
            logger.error(bstack1lllll1_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠦ᭳").format(bstack11l111l1l11_opy_))
            return []
        data = None
        try:
            with open(bstack11l111l1l11_opy_, bstack1lllll1_opy_ (u"ࠢࡳࠤ᭴")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡌࡖࡓࡓࠦࡦࡳࡱࡰࠤࡸࡵࡵࡳࡥࡨࠤ࡫࡯࡬ࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦ᭵").format(bstack11l111l1l11_opy_, e))
            return []
        _111lllll11l_opy_ = None
        _111lll1llll_opy_ = None
        def _111lllll111_opy_():
            bstack111lll11l1l_opy_ = {}
            bstack111lll1l1ll_opy_ = {}
            try:
                if self.bstack11l111l1111_opy_.startswith(bstack1lllll1_opy_ (u"ࠩࡾࠫ᭶")) and self.bstack11l111l1111_opy_.endswith(bstack1lllll1_opy_ (u"ࠪࢁࠬ᭷")):
                    bstack111lll11l1l_opy_ = json.loads(self.bstack11l111l1111_opy_)
                else:
                    bstack111lll11l1l_opy_ = dict(item.split(bstack1lllll1_opy_ (u"ࠫ࠿࠭᭸")) for item in self.bstack11l111l1111_opy_.split(bstack1lllll1_opy_ (u"ࠬ࠲ࠧ᭹")) if bstack1lllll1_opy_ (u"࠭࠺ࠨ᭺") in item) if self.bstack11l111l1111_opy_ else {}
                if self.bstack11l111111l1_opy_.startswith(bstack1lllll1_opy_ (u"ࠧࡼࠩ᭻")) and self.bstack11l111111l1_opy_.endswith(bstack1lllll1_opy_ (u"ࠨࡿࠪ᭼")):
                    bstack111lll1l1ll_opy_ = json.loads(self.bstack11l111111l1_opy_)
                else:
                    bstack111lll1l1ll_opy_ = dict(item.split(bstack1lllll1_opy_ (u"ࠩ࠽ࠫ᭽")) for item in self.bstack11l111111l1_opy_.split(bstack1lllll1_opy_ (u"ࠪ࠰ࠬ᭾")) if bstack1lllll1_opy_ (u"ࠫ࠿࠭᭿") in item) if self.bstack11l111111l1_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack1lllll1_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡬ࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳ࠻ࠢࡾࢁࠧᮀ").format(e))
            logger.debug(bstack1lllll1_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴࠢࡩࡶࡴࡳࠠࡦࡰࡹ࠾ࠥࢁࡽ࠭ࠢࡆࡐࡎࡀࠠࡼࡿࠥᮁ").format(bstack111lll11l1l_opy_, bstack111lll1l1ll_opy_))
            return bstack111lll11l1l_opy_, bstack111lll1l1ll_opy_
        if _111lllll11l_opy_ is None or _111lll1llll_opy_ is None:
            _111lllll11l_opy_, _111lll1llll_opy_ = _111lllll111_opy_()
        def bstack111lll1l111_opy_(name, bstack11l11111111_opy_):
            if name in _111lll1llll_opy_:
                return _111lll1llll_opy_[name]
            if name in _111lllll11l_opy_:
                return _111lllll11l_opy_[name]
            if bstack11l11111111_opy_.get(bstack1lllll1_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᮂ")):
                return bstack11l11111111_opy_[bstack1lllll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮃ")]
            return None
        if isinstance(data, dict):
            bstack111lll1ll11_opy_ = []
            bstack11l1111l1l1_opy_ = re.compile(bstack1lllll1_opy_ (u"ࡴࠪࡢࡠࡇ࡛࠭࠲࠰࠽ࡤࡣࠫࠥࠩᮄ"))
            for name, bstack11l11111111_opy_ in data.items():
                if not isinstance(bstack11l11111111_opy_, dict):
                    continue
                if not bstack11l11111111_opy_.get(bstack1lllll1_opy_ (u"ࠪࡹࡷࡲࠧᮅ")):
                    logger.warning(bstack1lllll1_opy_ (u"ࠦࡗ࡫ࡰࡰࡵ࡬ࡸࡴࡸࡹࠡࡗࡕࡐࠥ࡯ࡳࠡ࡯࡬ࡷࡸ࡯࡮ࡨࠢࡩࡳࡷࠦࡳࡰࡷࡵࡧࡪࠦࠧࡼࡿࠪ࠾ࠥࢁࡽࠣᮆ").format(name, bstack11l11111111_opy_))
                    continue
                if not bstack11l1111l1l1_opy_.match(name):
                    logger.warning(bstack1lllll1_opy_ (u"ࠧࡏ࡮ࡷࡣ࡯࡭ࡩࠦࡳࡰࡷࡵࡧࡪࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠣࡪࡴࡸ࡭ࡢࡶࠣࡪࡴࡸࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᮇ").format(name, bstack11l11111111_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack1lllll1_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡩࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠣࠫࢀࢃࠧࠡ࡯ࡸࡷࡹࠦࡨࡢࡸࡨࠤࡦࠦ࡬ࡦࡰࡪࡸ࡭ࠦࡢࡦࡶࡺࡩࡪࡴࠠ࠲ࠢࡤࡲࡩࠦ࠳࠱ࠢࡦ࡬ࡦࡸࡡࡤࡶࡨࡶࡸ࠴ࠢᮈ").format(name))
                    continue
                bstack11l11111111_opy_ = bstack11l11111111_opy_.copy()
                bstack11l11111111_opy_[bstack1lllll1_opy_ (u"ࠧ࡯ࡣࡰࡩࠬᮉ")] = name
                bstack11l11111111_opy_[bstack1lllll1_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᮊ")] = bstack111lll1l111_opy_(name, bstack11l11111111_opy_)
                if not bstack11l11111111_opy_.get(bstack1lllll1_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᮋ")):
                    logger.warning(bstack1lllll1_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡳࡵࡴࠡࡵࡳࡩࡨ࡯ࡦࡪࡧࡧࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᮌ").format(name, bstack11l11111111_opy_))
                    continue
                if bstack11l11111111_opy_.get(bstack1lllll1_opy_ (u"ࠫࡧࡧࡳࡦࡄࡵࡥࡳࡩࡨࠨᮍ")) and bstack11l11111111_opy_[bstack1lllll1_opy_ (u"ࠬࡨࡡࡴࡧࡅࡶࡦࡴࡣࡩࠩᮎ")] == bstack11l11111111_opy_[bstack1lllll1_opy_ (u"࠭ࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࠭ᮏ")]:
                    logger.warning(bstack1lllll1_opy_ (u"ࠢࡇࡧࡤࡸࡺࡸࡥࠡࡤࡵࡥࡳࡩࡨࠡࡣࡱࡨࠥࡨࡡࡴࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡧࡦࡴ࡮ࡰࡶࠣࡦࡪࠦࡴࡩࡧࠣࡷࡦࡳࡥࠡࡨࡲࡶࠥࡹ࡯ࡶࡴࡦࡩࠥ࠭ࡻࡾࠩ࠽ࠤࢀࢃࠢᮐ").format(name, bstack11l11111111_opy_))
                    continue
                bstack111lll1ll11_opy_.append(bstack11l11111111_opy_)
            return bstack111lll1ll11_opy_
        return data
    def bstack11l111l111l_opy_(self):
        data = {
            bstack1lllll1_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᮑ"): {
                bstack1lllll1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮒ"): self.bstack11l111l1ll1_opy_(),
                bstack1lllll1_opy_ (u"ࠪࡱࡴࡪࡥࠨᮓ"): self.bstack11l111111ll_opy_(),
                bstack1lllll1_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᮔ"): self.bstack11l1111llll_opy_()
            }
        }
        return data
    def bstack11l111l11ll_opy_(self, config):
        bstack111lllll1l1_opy_ = {}
        bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᮕ")] = {
            bstack1lllll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮖ"): self.bstack11l111l1ll1_opy_(),
            bstack1lllll1_opy_ (u"ࠧ࡮ࡱࡧࡩࠬᮗ"): self.bstack11l111111ll_opy_()
        }
        bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠨࡴࡨࡶࡺࡴ࡟ࡱࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡣ࡫ࡧࡩ࡭ࡧࡧࠫᮘ")] = {
            bstack1lllll1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᮙ"): self.bstack11l1111111l_opy_()
        }
        bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡶࡺࡴ࡟ࡱࡴࡨࡺ࡮ࡵࡵࡴ࡮ࡼࡣ࡫ࡧࡩ࡭ࡧࡧࡣ࡫࡯ࡲࡴࡶࠪᮚ")] = {
            bstack1lllll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮛ"): self.bstack111lll1lll1_opy_()
        }
        bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠬࡹ࡫ࡪࡲࡢࡪࡦ࡯࡬ࡪࡰࡪࡣࡦࡴࡤࡠࡨ࡯ࡥࡰࡿࠧᮜ")] = {
            bstack1lllll1_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᮝ"): self.bstack11l1111lll1_opy_()
        }
        if self.bstack1111111l_opy_(config):
            bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠧࡳࡧࡷࡶࡾࡥࡴࡦࡵࡷࡷࡤࡵ࡮ࡠࡨࡤ࡭ࡱࡻࡲࡦࠩᮞ")] = {
                bstack1lllll1_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᮟ"): True,
                bstack1lllll1_opy_ (u"ࠩࡰࡥࡽࡥࡲࡦࡶࡵ࡭ࡪࡹࠧᮠ"): self.bstack111ll1ll_opy_(config)
            }
        if self.bstack11ll1111ll1_opy_(config):
            bstack111lllll1l1_opy_[bstack1lllll1_opy_ (u"ࠪࡥࡧࡵࡲࡵࡡࡥࡹ࡮ࡲࡤࡠࡱࡱࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠬᮡ")] = {
                bstack1lllll1_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮢ"): True,
                bstack1lllll1_opy_ (u"ࠬࡳࡡࡹࡡࡩࡥ࡮ࡲࡵࡳࡧࡶࠫᮣ"): self.bstack11ll111l111_opy_(config)
            }
        return bstack111lllll1l1_opy_
    def bstack1111lll11_opy_(self, config):
        bstack1lllll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡇࡴࡲ࡬ࡦࡥࡷࡷࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡥࡽࠥࡳࡡ࡬࡫ࡱ࡫ࠥࡧࠠࡤࡣ࡯ࡰࠥࡺ࡯ࠡࡶ࡫ࡩࠥࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠣࡩࡳࡪࡰࡰ࡫ࡱࡸ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡂࡴࡪࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧࡻࡩ࡭ࡦࡢࡹࡺ࡯ࡤࠡࠪࡶࡸࡷ࠯࠺ࠡࡖ࡫ࡩ࡛ࠥࡕࡊࡆࠣࡳ࡫ࠦࡴࡩࡧࠣࡦࡺ࡯࡬ࡥࠢࡷࡳࠥࡩ࡯࡭࡮ࡨࡧࡹࠦࡤࡢࡶࡤࠤ࡫ࡵࡲ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡨ࡮ࡩࡴ࠻ࠢࡕࡩࡸࡶ࡯࡯ࡵࡨࠤ࡫ࡸ࡯࡮ࠢࡷ࡬ࡪࠦࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠤࡪࡴࡤࡱࡱ࡬ࡲࡹ࠲ࠠࡰࡴࠣࡒࡴࡴࡥࠡ࡫ࡩࠤ࡫ࡧࡩ࡭ࡧࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᮤ")
        if not (config.get(bstack1lllll1_opy_ (u"ࠧࡧࡴࡤࡱࡪࡽ࡯ࡳ࡭ࠪᮥ"), None) in bstack11l1l1ll1ll_opy_ and self.bstack11l111l1ll1_opy_()):
            return None
        bstack111llllll11_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠨࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡇࡖࡘࡍ࡛ࡂࡠࡗࡘࡍࡉ࠭ᮦ"), None)
        logger.debug(bstack1lllll1_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡄࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨᮧ").format(bstack111llllll11_opy_))
        try:
            bstack11ll11l1ll1_opy_ = bstack1lllll1_opy_ (u"ࠥࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡣࡷ࡬ࡰࡩࡹ࠯ࡼࡿ࠲ࡧࡴࡲ࡬ࡦࡥࡷ࠱ࡧࡻࡩ࡭ࡦ࠰ࡨࡦࡺࡡࠣᮨ").format(bstack111llllll11_opy_)
            payload = {
                bstack1lllll1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᮩ"): config.get(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧ᮪ࠪ"), bstack1lllll1_opy_ (u"᮫࠭ࠧ")),
                bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᮬ"): config.get(bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᮭ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᮮ"): os.environ.get(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᮯ"), bstack1lllll1_opy_ (u"ࠦࠧ᮰")),
                bstack1lllll1_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣ᮱"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤ᮲")) or bstack1lllll1_opy_ (u"ࠢ࠱ࠤ᮳")),
                bstack1lllll1_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧ᮴"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦ᮵")) or bstack1lllll1_opy_ (u"ࠥ࠵ࠧ᮶")),
                bstack1lllll1_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨ᮷"): get_host_info(),
            }
            logger.debug(bstack1lllll1_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡲࡤࡽࡱࡵࡡࡥ࠼ࠣࡿࢂࠨ᮸").format(payload))
            response = bstack11lll111111_opy_.bstack11ll11lll11_opy_(bstack11ll11l1ll1_opy_, payload)
            if response:
                logger.debug(bstack1lllll1_opy_ (u"ࠨ࡛ࡤࡱ࡯ࡰࡪࡩࡴࡃࡷ࡬ࡰࡩࡊࡡࡵࡣࡠࠤࡇࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡲࡲࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦ᮹").format(response))
                return response
            else:
                logger.error(bstack1lllll1_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡘ࡙ࡎࡊ࠺ࠡࡽࢀࠦᮺ").format(bstack111llllll11_opy_))
                return None
        except Exception as e:
            logger.error(bstack1lllll1_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡩ࡯࡭࡮ࡨࡧࡹ࡯࡮ࡨࠢࡥࡹ࡮ࡲࡤࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡦࡺ࡯࡬ࡥࠢࡘ࡙ࡎࡊࠠࡼࡿ࠽ࠤࢀࢃࠢᮻ").format(bstack111llllll11_opy_, e))
            return None
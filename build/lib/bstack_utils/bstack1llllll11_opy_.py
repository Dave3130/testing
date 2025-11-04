# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import os
import tempfile
import math
from bstack_utils import bstack11ll1l11l1_opy_
from bstack_utils.constants import bstack1l11l11l1l_opy_, bstack11l11l1l1ll_opy_
from bstack_utils.helper import bstack11ll1ll1111_opy_, get_host_info
from bstack_utils.bstack11ll1l11l1l_opy_ import bstack11ll1l1l1l1_opy_
import json
import re
import sys
bstack111llllll11_opy_ = bstack11l1111_opy_ (u"ࠧࡸࡥࡵࡴࡼࡘࡪࡹࡴࡴࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦᮎ")
bstack11l111111ll_opy_ = bstack11l1111_opy_ (u"ࠨࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧᮏ")
bstack111lll1ll1l_opy_ = bstack11l1111_opy_ (u"ࠢࡳࡷࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࡱࡿࡆࡢ࡫࡯ࡩࡩࡌࡩࡳࡵࡷࠦᮐ")
bstack111lll11ll1_opy_ = bstack11l1111_opy_ (u"ࠣࡴࡨࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࠤᮑ")
bstack111ll1ll1l1_opy_ = bstack11l1111_opy_ (u"ࠤࡶ࡯࡮ࡶࡆ࡭ࡣ࡮ࡽࡦࡴࡤࡇࡣ࡬ࡰࡪࡪࠢᮒ")
bstack111llll111l_opy_ = bstack11l1111_opy_ (u"ࠥࡶࡺࡴࡓ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠢᮓ")
bstack11l111111l1_opy_ = {
    bstack111llllll11_opy_,
    bstack11l111111ll_opy_,
    bstack111lll1ll1l_opy_,
    bstack111lll11ll1_opy_,
    bstack111ll1ll1l1_opy_,
    bstack111llll111l_opy_
}
bstack111lll11l11_opy_ = {bstack11l1111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᮔ")}
logger = bstack11ll1l11l1_opy_.get_logger(__name__, bstack1l11l11l1l_opy_)
class bstack111llllll1l_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack111ll1ll1ll_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack1lllllll1_opy_:
    _1ll1l1l1ll1_opy_ = None
    def __init__(self, config):
        self.bstack111ll1l1l11_opy_ = False
        self.bstack111lll1l111_opy_ = False
        self.bstack111ll1l1111_opy_ = False
        self.bstack111llll1l11_opy_ = False
        self.bstack111lll1l1ll_opy_ = None
        self.bstack111ll1lllll_opy_ = bstack111llllll1l_opy_()
        self.bstack111ll1l1lll_opy_ = None
        opts = config.get(bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮕ"), {})
        self.bstack111ll1l11l1_opy_ = config.get(bstack11l1111_opy_ (u"࠭ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࡆࡐ࡙ࠫᮖ"), bstack11l1111_opy_ (u"ࠢࠣᮗ"))
        self.bstack111lll1111l_opy_ = config.get(bstack11l1111_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡆࡐࡎ࠭ᮘ"), bstack11l1111_opy_ (u"ࠤࠥᮙ"))
        bstack111ll1lll1l_opy_ = opts.get(bstack111llll111l_opy_, {})
        bstack11l11111lll_opy_ = None
        if bstack11l1111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᮚ") in bstack111ll1lll1l_opy_:
            bstack111lll11lll_opy_ = bstack111ll1lll1l_opy_[bstack11l1111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᮛ")]
            if bstack111lll11lll_opy_ is None or (isinstance(bstack111lll11lll_opy_, str) and bstack111lll11lll_opy_.strip() == bstack11l1111_opy_ (u"ࠬ࠭ᮜ")) or (isinstance(bstack111lll11lll_opy_, list) and len(bstack111lll11lll_opy_) == 0):
                bstack11l11111lll_opy_ = []
            elif isinstance(bstack111lll11lll_opy_, list):
                bstack11l11111lll_opy_ = bstack111lll11lll_opy_
            elif isinstance(bstack111lll11lll_opy_, str) and bstack111lll11lll_opy_.strip():
                bstack11l11111lll_opy_ = bstack111lll11lll_opy_
            else:
                logger.warning(bstack11l1111_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡷࡣ࡯ࡹࡪࠦࡩ࡯ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡪࡰࡪࠤࡹࡵࠠࡦ࡯ࡳࡸࡾࠦ࡬ࡪࡵࡷ࠲ࠧᮝ").format(bstack111lll11lll_opy_))
                bstack11l11111lll_opy_ = []
        self.__111llll1l1l_opy_(
            bstack111ll1lll1l_opy_.get(bstack11l1111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮞ"), False),
            bstack111ll1lll1l_opy_.get(bstack11l1111_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭ᮟ"), bstack11l1111_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩᮠ")),
            bstack11l11111lll_opy_
        )
        self.__111lll111ll_opy_(opts.get(bstack111lll1ll1l_opy_, False))
        self.__111lllll111_opy_(opts.get(bstack111lll11ll1_opy_, False))
        self.__111lllllll1_opy_(opts.get(bstack111ll1ll1l1_opy_, False))
    @classmethod
    def bstack1llllllll_opy_(cls, config=None):
        if cls._1ll1l1l1ll1_opy_ is None and config is not None:
            cls._1ll1l1l1ll1_opy_ = bstack1lllllll1_opy_(config)
        return cls._1ll1l1l1ll1_opy_
    @staticmethod
    def bstack1lll1llll_opy_(config: dict) -> bool:
        bstack111lll11l1l_opy_ = config.get(bstack11l1111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᮡ"), {}).get(bstack111llllll11_opy_, {})
        return bstack111lll11l1l_opy_.get(bstack11l1111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮢ"), False)
    @staticmethod
    def bstack1lll111ll_opy_(config: dict) -> int:
        bstack111lll11l1l_opy_ = config.get(bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮣ"), {}).get(bstack111llllll11_opy_, {})
        retries = 0
        if bstack1lllllll1_opy_.bstack1lll1llll_opy_(config):
            retries = bstack111lll11l1l_opy_.get(bstack11l1111_opy_ (u"࠭࡭ࡢࡺࡕࡩࡹࡸࡩࡦࡵࠪᮤ"), 1)
        return retries
    @staticmethod
    def bstack1111l1ll11_opy_(config: dict) -> dict:
        bstack11l11111ll1_opy_ = config.get(bstack11l1111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᮥ"), {})
        return {
            key: value for key, value in bstack11l11111ll1_opy_.items() if key in bstack11l111111l1_opy_
        }
    @staticmethod
    def bstack111llll1lll_opy_():
        bstack11l1111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮦ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥᮧ").format(os.getenv(bstack11l1111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᮨ")))))
    @staticmethod
    def bstack111ll1ll111_opy_(test_name: str):
        bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮩ")
        bstack111lll1l1l1_opy_ = os.path.join(tempfile.gettempdir(), bstack11l1111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷ᮪ࠦ").format(os.getenv(bstack11l1111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇ᮫ࠦ"))))
        with open(bstack111lll1l1l1_opy_, bstack11l1111_opy_ (u"ࠧࡢࠩᮬ")) as file:
            file.write(bstack11l1111_opy_ (u"ࠣࡽࢀࡠࡳࠨᮭ").format(test_name))
    @staticmethod
    def bstack111lll1ll11_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll11l11_opy_
    @staticmethod
    def bstack11l1ll1llll_opy_(config: dict) -> bool:
        bstack111lllll11l_opy_ = config.get(bstack11l1111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᮮ"), {}).get(bstack11l111111ll_opy_, {})
        return bstack111lllll11l_opy_.get(bstack11l1111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮯ"), False)
    @staticmethod
    def bstack11l1ll1l111_opy_(config: dict, bstack11l1lll1ll1_opy_: int = 0) -> int:
        bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡉࡨࡸࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠲ࠠࡸࡪ࡬ࡧ࡭ࠦࡣࡢࡰࠣࡦࡪࠦࡡ࡯ࠢࡤࡦࡸࡵ࡬ࡶࡶࡨࠤࡳࡻ࡭ࡣࡧࡵࠤࡴࡸࠠࡢࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡰࡶࡤࡰࡤࡺࡥࡴࡶࡶࠤ࠭࡯࡮ࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࠫࡶࡪࡷࡵࡪࡴࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᮰")
        bstack111lllll11l_opy_ = config.get(bstack11l1111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᮱"), {}).get(bstack11l1111_opy_ (u"࠭ࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠬ᮲"), {})
        bstack11l11111l11_opy_ = 0
        bstack111ll1l11ll_opy_ = 0
        if bstack1lllllll1_opy_.bstack11l1ll1llll_opy_(config):
            bstack111ll1l11ll_opy_ = bstack111lllll11l_opy_.get(bstack11l1111_opy_ (u"ࠧ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷࠬ᮳"), 5)
            if isinstance(bstack111ll1l11ll_opy_, str) and bstack111ll1l11ll_opy_.endswith(bstack11l1111_opy_ (u"ࠨࠧࠪ᮴")):
                try:
                    percentage = int(bstack111ll1l11ll_opy_.strip(bstack11l1111_opy_ (u"ࠩࠨࠫ᮵")))
                    if bstack11l1lll1ll1_opy_ > 0:
                        bstack11l11111l11_opy_ = math.ceil((percentage * bstack11l1lll1ll1_opy_) / 100)
                    else:
                        raise ValueError(bstack11l1111_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳ࠯ࠤ᮶"))
                except ValueError as e:
                    raise ValueError(bstack11l1111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦࠢࡹࡥࡱࡻࡥࠡࡨࡲࡶࠥࡳࡡࡹࡈࡤ࡭ࡱࡻࡲࡦࡵ࠽ࠤࢀࢃࠢ᮷").format(bstack111ll1l11ll_opy_)) from e
            else:
                bstack11l11111l11_opy_ = int(bstack111ll1l11ll_opy_)
        logger.info(bstack11l1111_opy_ (u"ࠧࡓࡡࡹࠢࡩࡥ࡮ࡲࡵࡳࡧࡶࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡴࡧࡷࠤࡹࡵ࠺ࠡࡽࢀࠤ࠭࡬ࡲࡰ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࢀࢃࠩࠣ᮸").format(bstack11l11111l11_opy_, bstack111ll1l11ll_opy_))
        return bstack11l11111l11_opy_
    def bstack111ll1ll11l_opy_(self):
        return self.bstack111llll1l11_opy_
    def bstack111lll1l11l_opy_(self):
        return self.bstack111lll1l1ll_opy_
    def bstack111lllll1l1_opy_(self):
        return self.bstack111ll1l1lll_opy_
    def __111llll1l1l_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111llll1l11_opy_ = bool(enabled)
            if mode not in [bstack11l1111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭᮹"), bstack11l1111_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡑࡱࡰࡾ࠭ᮺ")]:
                logger.warning(bstack11l1111_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡲࡵࡤࡦࠢࠪࡿࢂ࠭ࠠࡱࡴࡲࡺ࡮ࡪࡥࡥ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ࠳ࠨᮻ").format(mode))
                mode = bstack11l1111_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩᮼ")
            self.bstack111lll1l1ll_opy_ = mode
            if source is None:
                self.bstack111ll1l1lll_opy_ = None
            elif isinstance(source, list):
                self.bstack111ll1l1lll_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11l1111_opy_ (u"ࠪ࠲࡯ࡹ࡯࡯ࠩᮽ")):
                self.bstack111ll1l1lll_opy_ = self._111llll1ll1_opy_(source)
            self.__111llll11ll_opy_()
        except Exception as e:
            logger.error(bstack11l1111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦ࠭ࠡࡧࡱࡥࡧࡲࡥࡥ࠼ࠣࡿࢂ࠲ࠠ࡮ࡱࡧࡩ࠿ࠦࡻࡾ࠮ࠣࡷࡴࡻࡲࡤࡧ࠽ࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᮾ").format(enabled, mode, source, e))
    def bstack111lll11111_opy_(self):
        return self.bstack111ll1l1l11_opy_
    def __111lll111ll_opy_(self, value):
        self.bstack111ll1l1l11_opy_ = bool(value)
        self.__111llll11ll_opy_()
    def bstack11l11111111_opy_(self):
        return self.bstack111lll1l111_opy_
    def __111lllll111_opy_(self, value):
        self.bstack111lll1l111_opy_ = bool(value)
        self.__111llll11ll_opy_()
    def bstack111ll1l1ll1_opy_(self):
        return self.bstack111ll1l1111_opy_
    def __111lllllll1_opy_(self, value):
        self.bstack111ll1l1111_opy_ = bool(value)
        self.__111llll11ll_opy_()
    def __111llll11ll_opy_(self):
        if self.bstack111llll1l11_opy_:
            self.bstack111ll1l1l11_opy_ = False
            self.bstack111lll1l111_opy_ = False
            self.bstack111ll1l1111_opy_ = False
            self.bstack111ll1lllll_opy_.enable(bstack111llll111l_opy_)
        elif self.bstack111ll1l1l11_opy_:
            self.bstack111lll1l111_opy_ = False
            self.bstack111ll1l1111_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111ll1lllll_opy_.enable(bstack111lll1ll1l_opy_)
        elif self.bstack111lll1l111_opy_:
            self.bstack111ll1l1l11_opy_ = False
            self.bstack111ll1l1111_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111ll1lllll_opy_.enable(bstack111lll11ll1_opy_)
        elif self.bstack111ll1l1111_opy_:
            self.bstack111ll1l1l11_opy_ = False
            self.bstack111lll1l111_opy_ = False
            self.bstack111llll1l11_opy_ = False
            self.bstack111ll1lllll_opy_.enable(bstack111ll1ll1l1_opy_)
        else:
            self.bstack111ll1lllll_opy_.disable()
    def bstack1111lll1_opy_(self):
        return self.bstack111ll1lllll_opy_.bstack111ll1ll1ll_opy_()
    def bstack1ll11ll1ll_opy_(self):
        if self.bstack111ll1lllll_opy_.bstack111ll1ll1ll_opy_():
            return self.bstack111ll1lllll_opy_.get_name()
        return None
    def _111llll1ll1_opy_(self, bstack111lll111l1_opy_):
        bstack11l1111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡳࡰࡷࡵࡧࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡦࡪ࡮ࡨࠤࡦࡴࡤࠡࡨࡲࡶࡲࡧࡴࠡ࡫ࡷࠤ࡫ࡵࡲࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡳࡺࡸࡣࡦࡡࡩ࡭ࡱ࡫࡟ࡱࡣࡷ࡬ࠥ࠮ࡳࡵࡴࠬ࠾ࠥࡖࡡࡵࡪࠣࡸࡴࠦࡴࡩࡧࠣࡎࡘࡕࡎࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡆࡰࡴࡰࡥࡹࡺࡥࡥࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡶࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮿ")
        if not os.path.isfile(bstack111lll111l1_opy_):
            logger.error(bstack11l1111_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠦᯀ").format(bstack111lll111l1_opy_))
            return []
        data = None
        try:
            with open(bstack111lll111l1_opy_, bstack11l1111_opy_ (u"ࠢࡳࠤᯁ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11l1111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡌࡖࡓࡓࠦࡦࡳࡱࡰࠤࡸࡵࡵࡳࡥࡨࠤ࡫࡯࡬ࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᯂ").format(bstack111lll111l1_opy_, e))
            return []
        _111lllll1ll_opy_ = None
        _111ll11llll_opy_ = None
        def _111ll1llll1_opy_():
            bstack111ll1l111l_opy_ = {}
            bstack111ll11lll1_opy_ = {}
            try:
                if self.bstack111ll1l11l1_opy_.startswith(bstack11l1111_opy_ (u"ࠩࡾࠫᯃ")) and self.bstack111ll1l11l1_opy_.endswith(bstack11l1111_opy_ (u"ࠪࢁࠬᯄ")):
                    bstack111ll1l111l_opy_ = json.loads(self.bstack111ll1l11l1_opy_)
                else:
                    bstack111ll1l111l_opy_ = dict(item.split(bstack11l1111_opy_ (u"ࠫ࠿࠭ᯅ")) for item in self.bstack111ll1l11l1_opy_.split(bstack11l1111_opy_ (u"ࠬ࠲ࠧᯆ")) if bstack11l1111_opy_ (u"࠭࠺ࠨᯇ") in item) if self.bstack111ll1l11l1_opy_ else {}
                if self.bstack111lll1111l_opy_.startswith(bstack11l1111_opy_ (u"ࠧࡼࠩᯈ")) and self.bstack111lll1111l_opy_.endswith(bstack11l1111_opy_ (u"ࠨࡿࠪᯉ")):
                    bstack111ll11lll1_opy_ = json.loads(self.bstack111lll1111l_opy_)
                else:
                    bstack111ll11lll1_opy_ = dict(item.split(bstack11l1111_opy_ (u"ࠩ࠽ࠫᯊ")) for item in self.bstack111lll1111l_opy_.split(bstack11l1111_opy_ (u"ࠪ࠰ࠬᯋ")) if bstack11l1111_opy_ (u"ࠫ࠿࠭ᯌ") in item) if self.bstack111lll1111l_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11l1111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡬ࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳ࠻ࠢࡾࢁࠧᯍ").format(e))
            logger.debug(bstack11l1111_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴࠢࡩࡶࡴࡳࠠࡦࡰࡹ࠾ࠥࢁࡽ࠭ࠢࡆࡐࡎࡀࠠࡼࡿࠥᯎ").format(bstack111ll1l111l_opy_, bstack111ll11lll1_opy_))
            return bstack111ll1l111l_opy_, bstack111ll11lll1_opy_
        if _111lllll1ll_opy_ is None or _111ll11llll_opy_ is None:
            _111lllll1ll_opy_, _111ll11llll_opy_ = _111ll1llll1_opy_()
        def bstack111llll11l1_opy_(name, bstack111llll1111_opy_):
            if name in _111ll11llll_opy_:
                return _111ll11llll_opy_[name]
            if name in _111lllll1ll_opy_:
                return _111lllll1ll_opy_[name]
            if bstack111llll1111_opy_.get(bstack11l1111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᯏ")):
                return bstack111llll1111_opy_[bstack11l1111_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᯐ")]
            return None
        if isinstance(data, dict):
            bstack111llllllll_opy_ = []
            bstack111ll1l1l1l_opy_ = re.compile(bstack11l1111_opy_ (u"ࡴࠪࡢࡠࡇ࡛࠭࠲࠰࠽ࡤࡣࠫࠥࠩᯑ"))
            for name, bstack111llll1111_opy_ in data.items():
                if not isinstance(bstack111llll1111_opy_, dict):
                    continue
                url = bstack111llll1111_opy_.get(bstack11l1111_opy_ (u"ࠪࡹࡷࡲࠧᯒ"))
                if url is None or (isinstance(url, str) and url.strip() == bstack11l1111_opy_ (u"ࠫࠬᯓ")):
                    logger.warning(bstack11l1111_opy_ (u"ࠧࡘࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡘࡖࡑࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᯔ").format(name, bstack111llll1111_opy_))
                    continue
                if not bstack111ll1l1l1l_opy_.match(name):
                    logger.warning(bstack11l1111_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᯕ").format(name, bstack111llll1111_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11l1111_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤࠬࢁࡽࠨࠢࡰࡹࡸࡺࠠࡩࡣࡹࡩࠥࡧࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡣࡧࡷࡻࡪ࡫࡮ࠡ࠳ࠣࡥࡳࡪࠠ࠴࠲ࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹ࠮ࠣᯖ").format(name))
                    continue
                bstack111llll1111_opy_ = bstack111llll1111_opy_.copy()
                bstack111llll1111_opy_[bstack11l1111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᯗ")] = name
                bstack111llll1111_opy_[bstack11l1111_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᯘ")] = bstack111llll11l1_opy_(name, bstack111llll1111_opy_)
                bstack111lll1lll1_opy_ = bstack111llll1111_opy_.get(bstack11l1111_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᯙ"))
                if not bstack111lll1lll1_opy_ or (isinstance(bstack111lll1lll1_opy_, str) and bstack111lll1lll1_opy_.strip() == bstack11l1111_opy_ (u"ࠫࠬᯚ")):
                    logger.warning(bstack11l1111_opy_ (u"ࠧࡌࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡮ࡰࡶࠣࡷࡵ࡫ࡣࡪࡨ࡬ࡩࡩࠦࡦࡰࡴࠣࡷࡴࡻࡲࡤࡧࠣࠫࢀࢃࠧ࠻ࠢࡾࢁࠧᯛ").format(name, bstack111llll1111_opy_))
                    continue
                if bstack111llll1111_opy_.get(bstack11l1111_opy_ (u"࠭ࡢࡢࡵࡨࡆࡷࡧ࡮ࡤࡪࠪᯜ")) and bstack111llll1111_opy_[bstack11l1111_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᯝ")] == bstack111llll1111_opy_[bstack11l1111_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᯞ")]:
                    logger.warning(bstack11l1111_opy_ (u"ࠤࡉࡩࡦࡺࡵࡳࡧࠣࡦࡷࡧ࡮ࡤࡪࠣࡥࡳࡪࠠࡣࡣࡶࡩࠥࡨࡲࡢࡰࡦ࡬ࠥࡩࡡ࡯ࡰࡲࡸࠥࡨࡥࠡࡶ࡫ࡩࠥࡹࡡ࡮ࡧࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᯟ").format(name, bstack111llll1111_opy_))
                    continue
                bstack111llllllll_opy_.append(bstack111llll1111_opy_)
            return bstack111llllllll_opy_
        return data
    def bstack11l11111l1l_opy_(self):
        data = {
            bstack11l1111_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᯠ"): {
                bstack11l1111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᯡ"): self.bstack111ll1ll11l_opy_(),
                bstack11l1111_opy_ (u"ࠬࡳ࡯ࡥࡧࠪᯢ"): self.bstack111lll1l11l_opy_(),
                bstack11l1111_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᯣ"): self.bstack111lllll1l1_opy_()
            }
        }
        return data
    def bstack111ll1lll11_opy_(self, config):
        bstack111lll1llll_opy_ = {}
        bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᯤ")] = {
            bstack11l1111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯥ"): self.bstack111ll1ll11l_opy_(),
            bstack11l1111_opy_ (u"ࠩࡰࡳࡩ࡫᯦ࠧ"): self.bstack111lll1l11l_opy_()
        }
        bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠪࡶࡪࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩ࠭ᯧ")] = {
            bstack11l1111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᯨ"): self.bstack11l11111111_opy_()
        }
        bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠬࡸࡵ࡯ࡡࡳࡶࡪࡼࡩࡰࡷࡶࡰࡾࡥࡦࡢ࡫࡯ࡩࡩࡥࡦࡪࡴࡶࡸࠬᯩ")] = {
            bstack11l1111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᯪ"): self.bstack111lll11111_opy_()
        }
        bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠧࡴ࡭࡬ࡴࡤ࡬ࡡࡪ࡮࡬ࡲ࡬ࡥࡡ࡯ࡦࡢࡪࡱࡧ࡫ࡺࠩᯫ")] = {
            bstack11l1111_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᯬ"): self.bstack111ll1l1ll1_opy_()
        }
        if self.bstack1lll1llll_opy_(config):
            bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠩࡵࡩࡹࡸࡹࡠࡶࡨࡷࡹࡹ࡟ࡰࡰࡢࡪࡦ࡯࡬ࡶࡴࡨࠫᯭ")] = {
                bstack11l1111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᯮ"): True,
                bstack11l1111_opy_ (u"ࠫࡲࡧࡸࡠࡴࡨࡸࡷ࡯ࡥࡴࠩᯯ"): self.bstack1lll111ll_opy_(config)
            }
        if self.bstack11l1ll1llll_opy_(config):
            bstack111lll1llll_opy_[bstack11l1111_opy_ (u"ࠬࡧࡢࡰࡴࡷࡣࡧࡻࡩ࡭ࡦࡢࡳࡳࡥࡦࡢ࡫࡯ࡹࡷ࡫ࠧᯰ")] = {
                bstack11l1111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᯱ"): True,
                bstack11l1111_opy_ (u"ࠧ࡮ࡣࡻࡣ࡫ࡧࡩ࡭ࡷࡵࡩࡸ᯲࠭"): self.bstack11l1ll1l111_opy_(config)
            }
        return bstack111lll1llll_opy_
    def bstack1llllllll1_opy_(self, config):
        bstack11l1111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉ࡯࡭࡮ࡨࡧࡹࡹࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡧࡿࠠ࡮ࡣ࡮࡭ࡳ࡭ࠠࡢࠢࡦࡥࡱࡲࠠࡵࡱࠣࡸ࡭࡫ࠠࡤࡱ࡯ࡰࡪࡩࡴ࠮ࡤࡸ࡭ࡱࡪ࠭ࡥࡣࡷࡥࠥ࡫࡮ࡥࡲࡲ࡭ࡳࡺ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡄࡶ࡬ࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡶ࡫࡯ࡨࡤࡻࡵࡪࡦࠣࠬࡸࡺࡲࠪ࠼ࠣࡘ࡭࡫ࠠࡖࡗࡌࡈࠥࡵࡦࠡࡶ࡫ࡩࠥࡨࡵࡪ࡮ࡧࠤࡹࡵࠠࡤࡱ࡯ࡰࡪࡩࡴࠡࡦࡤࡸࡦࠦࡦࡰࡴ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡪࡩࡤࡶ࠽ࠤࡗ࡫ࡳࡱࡱࡱࡷࡪࠦࡦࡳࡱࡰࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠭ࠢࡲࡶࠥࡔ࡯࡯ࡧࠣ࡭࡫ࠦࡦࡢ࡫࡯ࡩࡩ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤ᯳ࠥࠦ")
        if not (config.get(bstack11l1111_opy_ (u"ࠩࡩࡶࡦࡳࡥࡸࡱࡵ࡯ࠬ᯴"), None) in bstack11l11l1l1ll_opy_ and self.bstack111ll1ll11l_opy_()):
            return None
        bstack11l1111111l_opy_ = os.environ.get(bstack11l1111_opy_ (u"ࠪࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠨ᯵"), None)
        logger.debug(bstack11l1111_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡆࡳࡱࡲࡥࡤࡶ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡣࡷ࡬ࡰࡩࠦࡕࡖࡋࡇ࠾ࠥࢁࡽࠣ᯶").format(bstack11l1111111l_opy_))
        try:
            bstack11ll111l111_opy_ = bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡥࡹ࡮ࡲࡤࡴ࠱ࡾࢁ࠴ࡩ࡯࡭࡮ࡨࡧࡹ࠳ࡢࡶ࡫࡯ࡨ࠲ࡪࡡࡵࡣࠥ᯷").format(bstack11l1111111l_opy_)
            payload = {
                bstack11l1111_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦ᯸"): config.get(bstack11l1111_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬ᯹"), bstack11l1111_opy_ (u"ࠨࠩ᯺")),
                bstack11l1111_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧ᯻"): config.get(bstack11l1111_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭᯼"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤ᯽"): os.environ.get(bstack11l1111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦ᯾"), bstack11l1111_opy_ (u"ࠨࠢ᯿")),
                bstack11l1111_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥᰀ"): int(os.environ.get(bstack11l1111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᰁ")) or bstack11l1111_opy_ (u"ࠤ࠳ࠦᰂ")),
                bstack11l1111_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢᰃ"): int(os.environ.get(bstack11l1111_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨᰄ")) or bstack11l1111_opy_ (u"ࠧ࠷ࠢᰅ")),
                bstack11l1111_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣᰆ"): get_host_info(),
            }
            logger.debug(bstack11l1111_opy_ (u"ࠢ࡜ࡥࡲࡰࡱ࡫ࡣࡵࡄࡸ࡭ࡱࡪࡄࡢࡶࡤࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡢࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡴࡦࡿ࡬ࡰࡣࡧ࠾ࠥࢁࡽࠣᰇ").format(payload))
            response = bstack11ll1l1l1l1_opy_.bstack11ll1111ll1_opy_(bstack11ll111l111_opy_, payload)
            if response:
                logger.debug(bstack11l1111_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡂࡶ࡫࡯ࡨࠥࡪࡡࡵࡣࠣࡧࡴࡲ࡬ࡦࡥࡷ࡭ࡴࡴࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᰈ").format(response))
                return response
            else:
                logger.error(bstack11l1111_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣࡧࡴࡲ࡬ࡦࡥࡷࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅ࠼ࠣࡿࢂࠨᰉ").format(bstack11l1111111l_opy_))
                return None
        except Exception as e:
            logger.error(bstack11l1111_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡤࡱ࡯ࡰࡪࡩࡴࡪࡰࡪࠤࡧࡻࡩ࡭ࡦࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡨࡵࡪ࡮ࡧࠤ࡚࡛ࡉࡅࠢࡾࢁ࠿ࠦࡻࡾࠤᰊ").format(bstack11l1111111l_opy_, e))
            return None
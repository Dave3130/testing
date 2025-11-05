# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import os
import tempfile
import math
from bstack_utils import bstack111111l11l_opy_
from bstack_utils.constants import bstack1lllll1l11_opy_, bstack11l11llllll_opy_
from bstack_utils.helper import bstack11ll1l1l11l_opy_, get_host_info
from bstack_utils.bstack11ll1ll111l_opy_ import bstack11ll1l1l111_opy_
import json
import re
import sys
bstack111lllll11l_opy_ = bstack11111_opy_ (u"ࠧࡸࡥࡵࡴࡼࡘࡪࡹࡴࡴࡑࡱࡊࡦ࡯࡬ࡶࡴࡨࠦᮎ")
bstack111lllllll1_opy_ = bstack11111_opy_ (u"ࠨࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠧᮏ")
bstack111ll1ll1l1_opy_ = bstack11111_opy_ (u"ࠢࡳࡷࡱࡔࡷ࡫ࡶࡪࡱࡸࡷࡱࡿࡆࡢ࡫࡯ࡩࡩࡌࡩࡳࡵࡷࠦᮐ")
bstack111lll11l1l_opy_ = bstack11111_opy_ (u"ࠣࡴࡨࡶࡺࡴࡐࡳࡧࡹ࡭ࡴࡻࡳ࡭ࡻࡉࡥ࡮ࡲࡥࡥࠤᮑ")
bstack111lll11ll1_opy_ = bstack11111_opy_ (u"ࠤࡶ࡯࡮ࡶࡆ࡭ࡣ࡮ࡽࡦࡴࡤࡇࡣ࡬ࡰࡪࡪࠢᮒ")
bstack11l1111111l_opy_ = bstack11111_opy_ (u"ࠥࡶࡺࡴࡓ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠢᮓ")
bstack111lll1lll1_opy_ = {
    bstack111lllll11l_opy_,
    bstack111lllllll1_opy_,
    bstack111ll1ll1l1_opy_,
    bstack111lll11l1l_opy_,
    bstack111lll11ll1_opy_,
    bstack11l1111111l_opy_
}
bstack111lll1l11l_opy_ = {bstack11111_opy_ (u"ࠫࡵࡿࡴࡦࡵࡷࠫᮔ")}
logger = bstack111111l11l_opy_.get_logger(__name__, bstack1lllll1l11_opy_)
class bstack111lllll1l1_opy_:
    def __init__(self):
        self.enabled = False
        self.name = None
    def enable(self, name):
        self.enabled = True
        self.name = name
    def disable(self):
        self.enabled = False
        self.name = None
    def bstack11l11111l1l_opy_(self):
        return self.enabled
    def get_name(self):
        return self.name
class bstack111l11ll_opy_:
    _1ll1l1lll11_opy_ = None
    def __init__(self, config):
        self.bstack111llll1l11_opy_ = False
        self.bstack111ll1lllll_opy_ = False
        self.bstack11l111111l1_opy_ = False
        self.bstack111ll1l11l1_opy_ = False
        self.bstack111lll1ll11_opy_ = None
        self.bstack111ll1l1ll1_opy_ = bstack111lllll1l1_opy_()
        self.bstack111ll1ll11l_opy_ = None
        opts = config.get(bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮕ"), {})
        self.bstack111llll11l1_opy_ = config.get(bstack11111_opy_ (u"࠭ࡳ࡮ࡣࡵࡸࡘ࡫࡬ࡦࡥࡷ࡭ࡴࡴࡆࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭࡫ࡳࡆࡐ࡙ࠫᮖ"), bstack11111_opy_ (u"ࠢࠣᮗ"))
        self.bstack11l11111111_opy_ = config.get(bstack11111_opy_ (u"ࠨࡵࡰࡥࡷࡺࡓࡦ࡮ࡨࡧࡹ࡯࡯࡯ࡈࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࡦࡵࡆࡐࡎ࠭ᮘ"), bstack11111_opy_ (u"ࠤࠥᮙ"))
        bstack111lll11l11_opy_ = opts.get(bstack11l1111111l_opy_, {})
        bstack111llllll1l_opy_ = None
        if bstack11111_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᮚ") in bstack111lll11l11_opy_:
            bstack111ll1l1111_opy_ = bstack111lll11l11_opy_[bstack11111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᮛ")]
            if bstack111ll1l1111_opy_ is None or (isinstance(bstack111ll1l1111_opy_, str) and bstack111ll1l1111_opy_.strip() == bstack11111_opy_ (u"ࠬ࠭ᮜ")) or (isinstance(bstack111ll1l1111_opy_, list) and len(bstack111ll1l1111_opy_) == 0):
                bstack111llllll1l_opy_ = []
            elif isinstance(bstack111ll1l1111_opy_, list):
                bstack111llllll1l_opy_ = bstack111ll1l1111_opy_
            elif isinstance(bstack111ll1l1111_opy_, str) and bstack111ll1l1111_opy_.strip():
                bstack111llllll1l_opy_ = bstack111ll1l1111_opy_
            else:
                logger.warning(bstack11111_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡷࡣ࡯ࡹࡪࠦࡩ࡯ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡿࢂ࠴ࠠࡅࡧࡩࡥࡺࡲࡴࡪࡰࡪࠤࡹࡵࠠࡦ࡯ࡳࡸࡾࠦ࡬ࡪࡵࡷ࠲ࠧᮝ").format(bstack111ll1l1111_opy_))
                bstack111llllll1l_opy_ = []
        self.__111lll111l1_opy_(
            bstack111lll11l11_opy_.get(bstack11111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᮞ"), False),
            bstack111lll11l11_opy_.get(bstack11111_opy_ (u"ࠨ࡯ࡲࡨࡪ࠭ᮟ"), bstack11111_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩᮠ")),
            bstack111llllll1l_opy_
        )
        self.__111ll1l111l_opy_(opts.get(bstack111ll1ll1l1_opy_, False))
        self.__111lll1111l_opy_(opts.get(bstack111lll11l1l_opy_, False))
        self.__111lll1l111_opy_(opts.get(bstack111lll11ll1_opy_, False))
    @classmethod
    def bstack1111llll_opy_(cls, config=None):
        if cls._1ll1l1lll11_opy_ is None and config is not None:
            cls._1ll1l1lll11_opy_ = bstack111l11ll_opy_(config)
        return cls._1ll1l1lll11_opy_
    @staticmethod
    def bstack111l1111_opy_(config: dict) -> bool:
        bstack111llll111l_opy_ = config.get(bstack11111_opy_ (u"ࠪࡸࡪࡹࡴࡐࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡏࡱࡶ࡬ࡳࡳࡹࠧᮡ"), {}).get(bstack111lllll11l_opy_, {})
        return bstack111llll111l_opy_.get(bstack11111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᮢ"), False)
    @staticmethod
    def bstack1lllll1l1_opy_(config: dict) -> int:
        bstack111llll111l_opy_ = config.get(bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩᮣ"), {}).get(bstack111lllll11l_opy_, {})
        retries = 0
        if bstack111l11ll_opy_.bstack111l1111_opy_(config):
            retries = bstack111llll111l_opy_.get(bstack11111_opy_ (u"࠭࡭ࡢࡺࡕࡩࡹࡸࡩࡦࡵࠪᮤ"), 1)
        return retries
    @staticmethod
    def bstack1llllll1l1_opy_(config: dict) -> dict:
        bstack111lll11lll_opy_ = config.get(bstack11111_opy_ (u"ࠧࡵࡧࡶࡸࡔࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡓࡵࡺࡩࡰࡰࡶࠫᮥ"), {})
        return {
            key: value for key, value in bstack111lll11lll_opy_.items() if key in bstack111lll1lll1_opy_
        }
    @staticmethod
    def bstack11l11111ll1_opy_():
        bstack11111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡉࡨࡦࡥ࡮ࠤ࡮࡬ࠠࡵࡪࡨࠤࡦࡨ࡯ࡳࡶࠣࡦࡺ࡯࡬ࡥࠢࡩ࡭ࡱ࡫ࠠࡦࡺ࡬ࡷࡹࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮦ")
        return os.path.exists(os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠤࡤࡦࡴࡸࡴࡠࡤࡸ࡭ࡱࡪ࡟ࡼࡿࠥᮧ").format(os.getenv(bstack11111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡉࡘ࡚ࡈࡖࡄࡢ࡙࡚ࡏࡄࠣᮨ")))))
    @staticmethod
    def bstack111llll1l1l_opy_(test_name: str):
        bstack11111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡅ࡫ࡩࡨࡱࠠࡪࡨࠣࡸ࡭࡫ࠠࡢࡤࡲࡶࡹࠦࡢࡶ࡫࡯ࡨࠥ࡬ࡩ࡭ࡧࠣࡩࡽ࡯ࡳࡵࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᮩ")
        bstack111ll1llll1_opy_ = os.path.join(tempfile.gettempdir(), bstack11111_opy_ (u"ࠧ࡬ࡡࡪ࡮ࡨࡨࡤࡺࡥࡴࡶࡶࡣࢀࢃ࠮ࡵࡺࡷ᮪ࠦ").format(os.getenv(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡅࡔࡖࡋ࡙ࡇࡥࡕࡖࡋࡇ᮫ࠦ"))))
        with open(bstack111ll1llll1_opy_, bstack11111_opy_ (u"ࠧࡢࠩᮬ")) as file:
            file.write(bstack11111_opy_ (u"ࠣࡽࢀࡠࡳࠨᮭ").format(test_name))
    @staticmethod
    def bstack111ll1l1lll_opy_(framework: str) -> bool:
       return framework.lower() in bstack111lll1l11l_opy_
    @staticmethod
    def bstack11l1ll1ll11_opy_(config: dict) -> bool:
        bstack111lll1l1ll_opy_ = config.get(bstack11111_opy_ (u"ࠩࡷࡩࡸࡺࡏࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡕࡰࡵ࡫ࡲࡲࡸ࠭ᮮ"), {}).get(bstack111lllllll1_opy_, {})
        return bstack111lll1l1ll_opy_.get(bstack11111_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᮯ"), False)
    @staticmethod
    def bstack11l1ll1lll1_opy_(config: dict, bstack11l1lll1lll_opy_: int = 0) -> int:
        bstack11111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡉࡨࡸࠥࡺࡨࡦࠢࡩࡥ࡮ࡲࡵࡳࡧࠣࡸ࡭ࡸࡥࡴࡪࡲࡰࡩ࠲ࠠࡸࡪ࡬ࡧ࡭ࠦࡣࡢࡰࠣࡦࡪࠦࡡ࡯ࠢࡤࡦࡸࡵ࡬ࡶࡶࡨࠤࡳࡻ࡭ࡣࡧࡵࠤࡴࡸࠠࡢࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡃࡵ࡫ࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡩ࡯࡯ࡨ࡬࡫ࠥ࠮ࡤࡪࡥࡷ࠭࠿ࠦࡔࡩࡧࠣࡧࡴࡴࡦࡪࡩࡸࡶࡦࡺࡩࡰࡰࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷࡿ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡴࡰࡶࡤࡰࡤࡺࡥࡴࡶࡶࠤ࠭࡯࡮ࡵࠫ࠽ࠤ࡙࡮ࡥࠡࡶࡲࡸࡦࡲࠠ࡯ࡷࡰࡦࡪࡸࠠࡰࡨࠣࡸࡪࡹࡴࡴࠢࠫࡶࡪࡷࡵࡪࡴࡨࡨࠥ࡬࡯ࡳࠢࡳࡩࡷࡩࡥ࡯ࡶࡤ࡫ࡪ࠳ࡢࡢࡵࡨࡨࠥࡺࡨࡳࡧࡶ࡬ࡴࡲࡤࡴࠫ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥ࡯࡮ࡵ࠼ࠣࡘ࡭࡫ࠠࡧࡣ࡬ࡰࡺࡸࡥࠡࡶ࡫ࡶࡪࡹࡨࡰ࡮ࡧ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤ᮰")
        bstack111lll1l1ll_opy_ = config.get(bstack11111_opy_ (u"ࠬࡺࡥࡴࡶࡒࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡑࡳࡸ࡮ࡵ࡮ࡴࠩ᮱"), {}).get(bstack11111_opy_ (u"࠭ࡡࡣࡱࡵࡸࡇࡻࡩ࡭ࡦࡒࡲࡋࡧࡩ࡭ࡷࡵࡩࠬ᮲"), {})
        bstack111lllll1ll_opy_ = 0
        bstack111lll111ll_opy_ = 0
        if bstack111l11ll_opy_.bstack11l1ll1ll11_opy_(config):
            bstack111lll111ll_opy_ = bstack111lll1l1ll_opy_.get(bstack11111_opy_ (u"ࠧ࡮ࡣࡻࡊࡦ࡯࡬ࡶࡴࡨࡷࠬ᮳"), 5)
            if isinstance(bstack111lll111ll_opy_, str) and bstack111lll111ll_opy_.endswith(bstack11111_opy_ (u"ࠨࠧࠪ᮴")):
                try:
                    percentage = int(bstack111lll111ll_opy_.strip(bstack11111_opy_ (u"ࠩࠨࠫ᮵")))
                    if bstack11l1lll1lll_opy_ > 0:
                        bstack111lllll1ll_opy_ = math.ceil((percentage * bstack11l1lll1lll_opy_) / 100)
                    else:
                        raise ValueError(bstack11111_opy_ (u"ࠥࡘࡴࡺࡡ࡭ࠢࡷࡩࡸࡺࡳࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤ࡫ࡵࡲࠡࡲࡨࡶࡨ࡫࡮ࡵࡣࡪࡩ࠲ࡨࡡࡴࡧࡧࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࡳ࠯ࠤ᮶"))
                except ValueError as e:
                    raise ValueError(bstack11111_opy_ (u"ࠦࡎࡴࡶࡢ࡮࡬ࡨࠥࡶࡥࡳࡥࡨࡲࡹࡧࡧࡦࠢࡹࡥࡱࡻࡥࠡࡨࡲࡶࠥࡳࡡࡹࡈࡤ࡭ࡱࡻࡲࡦࡵ࠽ࠤࢀࢃࠢ᮷").format(bstack111lll111ll_opy_)) from e
            else:
                bstack111lllll1ll_opy_ = int(bstack111lll111ll_opy_)
        logger.info(bstack11111_opy_ (u"ࠧࡓࡡࡹࠢࡩࡥ࡮ࡲࡵࡳࡧࡶࠤࡹ࡮ࡲࡦࡵ࡫ࡳࡱࡪࠠࡴࡧࡷࠤࡹࡵ࠺ࠡࡽࢀࠤ࠭࡬ࡲࡰ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࢀࢃࠩࠣ᮸").format(bstack111lllll1ll_opy_, bstack111lll111ll_opy_))
        return bstack111lllll1ll_opy_
    def bstack11l11111l11_opy_(self):
        return self.bstack111ll1l11l1_opy_
    def bstack111llllll11_opy_(self):
        return self.bstack111lll1ll11_opy_
    def bstack111ll11llll_opy_(self):
        return self.bstack111ll1ll11l_opy_
    def __111lll111l1_opy_(self, enabled, mode, source=None):
        try:
            self.bstack111ll1l11l1_opy_ = bool(enabled)
            if mode not in [bstack11111_opy_ (u"࠭ࡲࡦ࡮ࡨࡺࡦࡴࡴࡇ࡫ࡵࡷࡹ࠭᮹"), bstack11111_opy_ (u"ࠧࡳࡧ࡯ࡩࡻࡧ࡮ࡵࡑࡱࡰࡾ࠭ᮺ")]:
                logger.warning(bstack11111_opy_ (u"ࠣࡋࡱࡺࡦࡲࡩࡥࠢࡶࡱࡦࡸࡴࠡࡵࡨࡰࡪࡩࡴࡪࡱࡱࠤࡲࡵࡤࡦࠢࠪࡿࢂ࠭ࠠࡱࡴࡲࡺ࡮ࡪࡥࡥ࠰ࠣࡈࡪ࡬ࡡࡶ࡮ࡷ࡭ࡳ࡭ࠠࡵࡱࠣࠫࡷ࡫࡬ࡦࡸࡤࡲࡹࡌࡩࡳࡵࡷࠫ࠳ࠨᮻ").format(mode))
                mode = bstack11111_opy_ (u"ࠩࡵࡩࡱ࡫ࡶࡢࡰࡷࡊ࡮ࡸࡳࡵࠩᮼ")
            self.bstack111lll1ll11_opy_ = mode
            if source is None:
                self.bstack111ll1ll11l_opy_ = None
            elif isinstance(source, list):
                self.bstack111ll1ll11l_opy_ = source
            elif isinstance(source, str) and source.endswith(bstack11111_opy_ (u"ࠪ࠲࡯ࡹ࡯࡯ࠩᮽ")):
                self.bstack111ll1ll11l_opy_ = self._111ll1lll1l_opy_(source)
            self.__111ll1ll1ll_opy_()
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠦࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡴࡧࡷࠤࡸࡳࡡࡳࡶࠣࡷࡪࡲࡥࡤࡶ࡬ࡳࡳࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦ࠭ࠡࡧࡱࡥࡧࡲࡥࡥ࠼ࠣࡿࢂ࠲ࠠ࡮ࡱࡧࡩ࠿ࠦࡻࡾ࠮ࠣࡷࡴࡻࡲࡤࡧ࠽ࠤࢀࢃ࠮ࠡࡇࡵࡶࡴࡸ࠺ࠡࡽࢀࠦᮾ").format(enabled, mode, source, e))
    def bstack111llll11ll_opy_(self):
        return self.bstack111llll1l11_opy_
    def __111ll1l111l_opy_(self, value):
        self.bstack111llll1l11_opy_ = bool(value)
        self.__111ll1ll1ll_opy_()
    def bstack11l11111lll_opy_(self):
        return self.bstack111ll1lllll_opy_
    def __111lll1111l_opy_(self, value):
        self.bstack111ll1lllll_opy_ = bool(value)
        self.__111ll1ll1ll_opy_()
    def bstack111ll1lll11_opy_(self):
        return self.bstack11l111111l1_opy_
    def __111lll1l111_opy_(self, value):
        self.bstack11l111111l1_opy_ = bool(value)
        self.__111ll1ll1ll_opy_()
    def __111ll1ll1ll_opy_(self):
        if self.bstack111ll1l11l1_opy_:
            self.bstack111llll1l11_opy_ = False
            self.bstack111ll1lllll_opy_ = False
            self.bstack11l111111l1_opy_ = False
            self.bstack111ll1l1ll1_opy_.enable(bstack11l1111111l_opy_)
        elif self.bstack111llll1l11_opy_:
            self.bstack111ll1lllll_opy_ = False
            self.bstack11l111111l1_opy_ = False
            self.bstack111ll1l11l1_opy_ = False
            self.bstack111ll1l1ll1_opy_.enable(bstack111ll1ll1l1_opy_)
        elif self.bstack111ll1lllll_opy_:
            self.bstack111llll1l11_opy_ = False
            self.bstack11l111111l1_opy_ = False
            self.bstack111ll1l11l1_opy_ = False
            self.bstack111ll1l1ll1_opy_.enable(bstack111lll11l1l_opy_)
        elif self.bstack11l111111l1_opy_:
            self.bstack111llll1l11_opy_ = False
            self.bstack111ll1lllll_opy_ = False
            self.bstack111ll1l11l1_opy_ = False
            self.bstack111ll1l1ll1_opy_.enable(bstack111lll11ll1_opy_)
        else:
            self.bstack111ll1l1ll1_opy_.disable()
    def bstack1lll1ll1l_opy_(self):
        return self.bstack111ll1l1ll1_opy_.bstack11l11111l1l_opy_()
    def bstack11llll1lll_opy_(self):
        if self.bstack111ll1l1ll1_opy_.bstack11l11111l1l_opy_():
            return self.bstack111ll1l1ll1_opy_.get_name()
        return None
    def _111ll1lll1l_opy_(self, bstack111lll1l1l1_opy_):
        bstack11111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡥࡷࡹࡥࠡࡌࡖࡓࡓࠦࡳࡰࡷࡵࡧࡪࠦࡣࡰࡰࡩ࡭࡬ࡻࡲࡢࡶ࡬ࡳࡳࠦࡦࡪ࡮ࡨࠤࡦࡴࡤࠡࡨࡲࡶࡲࡧࡴࠡ࡫ࡷࠤ࡫ࡵࡲࠡࡵࡰࡥࡷࡺࠠࡴࡧ࡯ࡩࡨࡺࡩࡰࡰ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࡇࡲࡨࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡶࡳࡺࡸࡣࡦࡡࡩ࡭ࡱ࡫࡟ࡱࡣࡷ࡬ࠥ࠮ࡳࡵࡴࠬ࠾ࠥࡖࡡࡵࡪࠣࡸࡴࠦࡴࡩࡧࠣࡎࡘࡕࡎࠡࡥࡲࡲ࡫࡯ࡧࡶࡴࡤࡸ࡮ࡵ࡮ࠡࡨ࡬ࡰࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠ࡭࡫ࡶࡸ࠿ࠦࡆࡰࡴࡰࡥࡹࡺࡥࡥࠢ࡯࡭ࡸࡺࠠࡰࡨࠣࡶࡪࡶ࡯ࡴ࡫ࡷࡳࡷࡿࠠࡤࡱࡱࡪ࡮࡭ࡵࡳࡣࡷ࡭ࡴࡴࡳࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᮿ")
        if not os.path.isfile(bstack111lll1l1l1_opy_):
            logger.error(bstack11111_opy_ (u"ࠨࡓࡰࡷࡵࡧࡪࠦࡦࡪ࡮ࡨࠤࠬࢁࡽࠨࠢࡧࡳࡪࡹࠠ࡯ࡱࡷࠤࡪࡾࡩࡴࡶ࠱ࠦᯀ").format(bstack111lll1l1l1_opy_))
            return []
        data = None
        try:
            with open(bstack111lll1l1l1_opy_, bstack11111_opy_ (u"ࠢࡳࠤᯁ")) as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            logger.error(bstack11111_opy_ (u"ࠣࡇࡵࡶࡴࡸࠠࡱࡣࡵࡷ࡮ࡴࡧࠡࡌࡖࡓࡓࠦࡦࡳࡱࡰࠤࡸࡵࡵࡳࡥࡨࠤ࡫࡯࡬ࡦࠢࠪࡿࢂ࠭࠺ࠡࡽࢀࠦᯂ").format(bstack111lll1l1l1_opy_, e))
            return []
        _111lll1llll_opy_ = None
        _111lll1ll1l_opy_ = None
        def _111lllll111_opy_():
            bstack111ll1l1l11_opy_ = {}
            bstack111llll1111_opy_ = {}
            try:
                if self.bstack111llll11l1_opy_.startswith(bstack11111_opy_ (u"ࠩࡾࠫᯃ")) and self.bstack111llll11l1_opy_.endswith(bstack11111_opy_ (u"ࠪࢁࠬᯄ")):
                    bstack111ll1l1l11_opy_ = json.loads(self.bstack111llll11l1_opy_)
                else:
                    bstack111ll1l1l11_opy_ = dict(item.split(bstack11111_opy_ (u"ࠫ࠿࠭ᯅ")) for item in self.bstack111llll11l1_opy_.split(bstack11111_opy_ (u"ࠬ࠲ࠧᯆ")) if bstack11111_opy_ (u"࠭࠺ࠨᯇ") in item) if self.bstack111llll11l1_opy_ else {}
                if self.bstack11l11111111_opy_.startswith(bstack11111_opy_ (u"ࠧࡼࠩᯈ")) and self.bstack11l11111111_opy_.endswith(bstack11111_opy_ (u"ࠨࡿࠪᯉ")):
                    bstack111llll1111_opy_ = json.loads(self.bstack11l11111111_opy_)
                else:
                    bstack111llll1111_opy_ = dict(item.split(bstack11111_opy_ (u"ࠩ࠽ࠫᯊ")) for item in self.bstack11l11111111_opy_.split(bstack11111_opy_ (u"ࠪ࠰ࠬᯋ")) if bstack11111_opy_ (u"ࠫ࠿࠭ᯌ") in item) if self.bstack11l11111111_opy_ else {}
            except json.JSONDecodeError as e:
                logger.error(bstack11111_opy_ (u"ࠧࡋࡲࡳࡱࡵࠤࡵࡧࡲࡴ࡫ࡱ࡫ࠥ࡬ࡥࡢࡶࡸࡶࡪࠦࡢࡳࡣࡱࡧ࡭ࠦ࡭ࡢࡲࡳ࡭ࡳ࡭ࡳ࠻ࠢࡾࢁࠧᯍ").format(e))
            logger.debug(bstack11111_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡮ࡣࡳࡴ࡮ࡴࡧࡴࠢࡩࡶࡴࡳࠠࡦࡰࡹ࠾ࠥࢁࡽ࠭ࠢࡆࡐࡎࡀࠠࡼࡿࠥᯎ").format(bstack111ll1l1l11_opy_, bstack111llll1111_opy_))
            return bstack111ll1l1l11_opy_, bstack111llll1111_opy_
        if _111lll1llll_opy_ is None or _111lll1ll1l_opy_ is None:
            _111lll1llll_opy_, _111lll1ll1l_opy_ = _111lllll111_opy_()
        def bstack111ll1l11ll_opy_(name, bstack111ll1ll111_opy_):
            if name in _111lll1ll1l_opy_:
                return _111lll1ll1l_opy_[name]
            if name in _111lll1llll_opy_:
                return _111lll1llll_opy_[name]
            if bstack111ll1ll111_opy_.get(bstack11111_opy_ (u"ࠧࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠧᯏ")):
                return bstack111ll1ll111_opy_[bstack11111_opy_ (u"ࠨࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠨᯐ")]
            return None
        if isinstance(data, dict):
            bstack11l111111ll_opy_ = []
            bstack111llllllll_opy_ = re.compile(bstack11111_opy_ (u"ࡴࠪࡢࡠࡇ࡛࠭࠲࠰࠽ࡤࡣࠫࠥࠩᯑ"))
            for name, bstack111ll1ll111_opy_ in data.items():
                if not isinstance(bstack111ll1ll111_opy_, dict):
                    continue
                url = bstack111ll1ll111_opy_.get(bstack11111_opy_ (u"ࠪࡹࡷࡲࠧᯒ"))
                if url is None or (isinstance(url, str) and url.strip() == bstack11111_opy_ (u"ࠫࠬᯓ")):
                    logger.warning(bstack11111_opy_ (u"ࠧࡘࡥࡱࡱࡶ࡭ࡹࡵࡲࡺࠢࡘࡖࡑࠦࡩࡴࠢࡰ࡭ࡸࡹࡩ࡯ࡩࠣࡪࡴࡸࠠࡴࡱࡸࡶࡨ࡫ࠠࠨࡽࢀࠫ࠿ࠦࡻࡾࠤᯔ").format(name, bstack111ll1ll111_opy_))
                    continue
                if not bstack111llllllll_opy_.match(name):
                    logger.warning(bstack11111_opy_ (u"ࠨࡉ࡯ࡸࡤࡰ࡮ࡪࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤ࡫ࡵࡲ࡮ࡣࡷࠤ࡫ࡵࡲࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᯕ").format(name, bstack111ll1ll111_opy_))
                    continue
                if len(name) > 30 or len(name) < 1:
                    logger.warning(bstack11111_opy_ (u"ࠢࡔࡱࡸࡶࡨ࡫ࠠࡪࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠤࠬࢁࡽࠨࠢࡰࡹࡸࡺࠠࡩࡣࡹࡩࠥࡧࠠ࡭ࡧࡱ࡫ࡹ࡮ࠠࡣࡧࡷࡻࡪ࡫࡮ࠡ࠳ࠣࡥࡳࡪࠠ࠴࠲ࠣࡧ࡭ࡧࡲࡢࡥࡷࡩࡷࡹ࠮ࠣᯖ").format(name))
                    continue
                bstack111ll1ll111_opy_ = bstack111ll1ll111_opy_.copy()
                bstack111ll1ll111_opy_[bstack11111_opy_ (u"ࠨࡰࡤࡱࡪ࠭ᯗ")] = name
                bstack111ll1ll111_opy_[bstack11111_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᯘ")] = bstack111ll1l11ll_opy_(name, bstack111ll1ll111_opy_)
                if not bstack111ll1ll111_opy_.get(bstack11111_opy_ (u"ࠪࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠪᯙ")) or bstack111ll1ll111_opy_.get(bstack11111_opy_ (u"ࠫ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠫᯚ")) == bstack11111_opy_ (u"ࠬ࠭ᯛ"):
                    logger.warning(bstack11111_opy_ (u"ࠨࡆࡦࡣࡷࡹࡷ࡫ࠠࡣࡴࡤࡲࡨ࡮ࠠ࡯ࡱࡷࠤࡸࡶࡥࡤ࡫ࡩ࡭ࡪࡪࠠࡧࡱࡵࠤࡸࡵࡵࡳࡥࡨࠤࠬࢁࡽࠨ࠼ࠣࡿࢂࠨᯜ").format(name, bstack111ll1ll111_opy_))
                    continue
                if bstack111ll1ll111_opy_.get(bstack11111_opy_ (u"ࠧࡣࡣࡶࡩࡇࡸࡡ࡯ࡥ࡫ࠫᯝ")) and bstack111ll1ll111_opy_[bstack11111_opy_ (u"ࠨࡤࡤࡷࡪࡈࡲࡢࡰࡦ࡬ࠬᯞ")] == bstack111ll1ll111_opy_[bstack11111_opy_ (u"ࠩࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠩᯟ")]:
                    logger.warning(bstack11111_opy_ (u"ࠥࡊࡪࡧࡴࡶࡴࡨࠤࡧࡸࡡ࡯ࡥ࡫ࠤࡦࡴࡤࠡࡤࡤࡷࡪࠦࡢࡳࡣࡱࡧ࡭ࠦࡣࡢࡰࡱࡳࡹࠦࡢࡦࠢࡷ࡬ࡪࠦࡳࡢ࡯ࡨࠤ࡫ࡵࡲࠡࡵࡲࡹࡷࡩࡥࠡࠩࡾࢁࠬࡀࠠࡼࡿࠥᯠ").format(name, bstack111ll1ll111_opy_))
                    continue
                bstack11l111111ll_opy_.append(bstack111ll1ll111_opy_)
            return bstack11l111111ll_opy_
        return data
    def bstack111lll11111_opy_(self):
        data = {
            bstack11111_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᯡ"): {
                bstack11111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯢ"): self.bstack11l11111l11_opy_(),
                bstack11111_opy_ (u"࠭࡭ࡰࡦࡨࠫᯣ"): self.bstack111llllll11_opy_(),
                bstack11111_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᯤ"): self.bstack111ll11llll_opy_()
            }
        }
        return data
    def bstack111llll1ll1_opy_(self, config):
        bstack111ll1l1l1l_opy_ = {}
        bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᯥ")] = {
            bstack11111_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦ᯦ࠪ"): self.bstack11l11111l11_opy_(),
            bstack11111_opy_ (u"ࠪࡱࡴࡪࡥࠨᯧ"): self.bstack111llllll11_opy_()
        }
        bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"ࠫࡷ࡫ࡲࡶࡰࡢࡴࡷ࡫ࡶࡪࡱࡸࡷࡱࡿ࡟ࡧࡣ࡬ࡰࡪࡪࠧᯨ")] = {
            bstack11111_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᯩ"): self.bstack11l11111lll_opy_()
        }
        bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"࠭ࡲࡶࡰࡢࡴࡷ࡫ࡶࡪࡱࡸࡷࡱࡿ࡟ࡧࡣ࡬ࡰࡪࡪ࡟ࡧ࡫ࡵࡷࡹ࠭ᯪ")] = {
            bstack11111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᯫ"): self.bstack111llll11ll_opy_()
        }
        bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"ࠨࡵ࡮࡭ࡵࡥࡦࡢ࡫࡯࡭ࡳ࡭࡟ࡢࡰࡧࡣ࡫ࡲࡡ࡬ࡻࠪᯬ")] = {
            bstack11111_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᯭ"): self.bstack111ll1lll11_opy_()
        }
        if self.bstack111l1111_opy_(config):
            bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"ࠪࡶࡪࡺࡲࡺࡡࡷࡩࡸࡺࡳࡠࡱࡱࡣ࡫ࡧࡩ࡭ࡷࡵࡩࠬᯮ")] = {
                bstack11111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᯯ"): True,
                bstack11111_opy_ (u"ࠬࡳࡡࡹࡡࡵࡩࡹࡸࡩࡦࡵࠪᯰ"): self.bstack1lllll1l1_opy_(config)
            }
        if self.bstack11l1ll1ll11_opy_(config):
            bstack111ll1l1l1l_opy_[bstack11111_opy_ (u"࠭ࡡࡣࡱࡵࡸࡤࡨࡵࡪ࡮ࡧࡣࡴࡴ࡟ࡧࡣ࡬ࡰࡺࡸࡥࠨᯱ")] = {
                bstack11111_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨ᯲"): True,
                bstack11111_opy_ (u"ࠨ࡯ࡤࡼࡤ࡬ࡡࡪ࡮ࡸࡶࡪࡹ᯳ࠧ"): self.bstack11l1ll1lll1_opy_(config)
            }
        return bstack111ll1l1l1l_opy_
    def bstack1l111l1l11_opy_(self, config):
        bstack11111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡃࡰ࡮࡯ࡩࡨࡺࡳࠡࡤࡸ࡭ࡱࡪࠠࡥࡣࡷࡥࠥࡨࡹࠡ࡯ࡤ࡯࡮ࡴࡧࠡࡣࠣࡧࡦࡲ࡬ࠡࡶࡲࠤࡹ࡮ࡥࠡࡥࡲࡰࡱ࡫ࡣࡵ࠯ࡥࡹ࡮ࡲࡤ࠮ࡦࡤࡸࡦࠦࡥ࡯ࡦࡳࡳ࡮ࡴࡴ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡅࡷ࡭ࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡷ࡬ࡰࡩࡥࡵࡶ࡫ࡧࠤ࠭ࡹࡴࡳࠫ࠽ࠤ࡙࡮ࡥࠡࡗࡘࡍࡉࠦ࡯ࡧࠢࡷ࡬ࡪࠦࡢࡶ࡫࡯ࡨࠥࡺ࡯ࠡࡥࡲࡰࡱ࡫ࡣࡵࠢࡧࡥࡹࡧࠠࡧࡱࡵ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡤࡪࡥࡷ࠾ࠥࡘࡥࡴࡲࡲࡲࡸ࡫ࠠࡧࡴࡲࡱࠥࡺࡨࡦࠢࡦࡳࡱࡲࡥࡤࡶ࠰ࡦࡺ࡯࡬ࡥ࠯ࡧࡥࡹࡧࠠࡦࡰࡧࡴࡴ࡯࡮ࡵ࠮ࠣࡳࡷࠦࡎࡰࡰࡨࠤ࡮࡬ࠠࡧࡣ࡬ࡰࡪࡪ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧ᯴")
        if not (config.get(bstack11111_opy_ (u"ࠪࡪࡷࡧ࡭ࡦࡹࡲࡶࡰ࠭᯵"), None) in bstack11l11llllll_opy_ and self.bstack11l11111l11_opy_()):
            return None
        bstack111llll1lll_opy_ = os.environ.get(bstack11111_opy_ (u"ࠫࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡊ࡙ࡔࡉࡗࡅࡣ࡚࡛ࡉࡅࠩ᯶"), None)
        logger.debug(bstack11111_opy_ (u"ࠧࡡࡣࡰ࡮࡯ࡩࡨࡺࡂࡶ࡫࡯ࡨࡉࡧࡴࡢ࡟ࠣࡇࡴࡲ࡬ࡦࡥࡷ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡤࡸ࡭ࡱࡪࠠࡖࡗࡌࡈ࠿ࠦࡻࡾࠤ᯷").format(bstack111llll1lll_opy_))
        try:
            bstack11ll111l11l_opy_ = bstack11111_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡦࡺ࡯࡬ࡥࡵ࠲ࡿࢂ࠵ࡣࡰ࡮࡯ࡩࡨࡺ࠭ࡣࡷ࡬ࡰࡩ࠳ࡤࡢࡶࡤࠦ᯸").format(bstack111llll1lll_opy_)
            payload = {
                bstack11111_opy_ (u"ࠢࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠧ᯹"): config.get(bstack11111_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭᯺"), bstack11111_opy_ (u"ࠩࠪ᯻")),
                bstack11111_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠨ᯼"): config.get(bstack11111_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧ᯽"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11111_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥ᯾"): os.environ.get(bstack11111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧ᯿"), bstack11111_opy_ (u"ࠢࠣᰀ")),
                bstack11111_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦᰁ"): int(os.environ.get(bstack11111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᰂ")) or bstack11111_opy_ (u"ࠥ࠴ࠧᰃ")),
                bstack11111_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣᰄ"): int(os.environ.get(bstack11111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢᰅ")) or bstack11111_opy_ (u"ࠨ࠱ࠣᰆ")),
                bstack11111_opy_ (u"ࠢࡩࡱࡶࡸࡎࡴࡦࡰࠤᰇ"): get_host_info(),
            }
            logger.debug(bstack11111_opy_ (u"ࠣ࡝ࡦࡳࡱࡲࡥࡤࡶࡅࡹ࡮ࡲࡤࡅࡣࡷࡥࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡣࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡵࡧࡹ࡭ࡱࡤࡨ࠿ࠦࡻࡾࠤᰈ").format(payload))
            response = bstack11ll1l1l111_opy_.bstack11ll1111l1l_opy_(bstack11ll111l11l_opy_, payload)
            if response:
                logger.debug(bstack11111_opy_ (u"ࠤ࡞ࡧࡴࡲ࡬ࡦࡥࡷࡆࡺ࡯࡬ࡥࡆࡤࡸࡦࡣࠠࡃࡷ࡬ࡰࡩࠦࡤࡢࡶࡤࠤࡨࡵ࡬࡭ࡧࡦࡸ࡮ࡵ࡮ࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᰉ").format(response))
                return response
            else:
                logger.error(bstack11111_opy_ (u"ࠥ࡟ࡨࡵ࡬࡭ࡧࡦࡸࡇࡻࡩ࡭ࡦࡇࡥࡹࡧ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤࡨࡵ࡬࡭ࡧࡦࡸࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆ࠽ࠤࢀࢃࠢᰊ").format(bstack111llll1lll_opy_))
                return None
        except Exception as e:
            logger.error(bstack11111_opy_ (u"ࠦࡠࡩ࡯࡭࡮ࡨࡧࡹࡈࡵࡪ࡮ࡧࡈࡦࡺࡡ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡥࡲࡰࡱ࡫ࡣࡵ࡫ࡱ࡫ࠥࡨࡵࡪ࡮ࡧࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡢࡶ࡫࡯ࡨ࡛ࠥࡕࡊࡆࠣࡿࢂࡀࠠࡼࡿࠥᰋ").format(bstack111llll1lll_opy_, e))
            return None
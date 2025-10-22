# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import time
from bstack_utils.bstack11ll1ll1lll_opy_ import bstack11ll1l1llll_opy_
from bstack_utils.constants import bstack11ll1lll11l_opy_
from bstack_utils.helper import get_host_info, bstack11ll1l1l1ll_opy_
class bstack11ll1ll11ll_opy_:
    bstack1lllll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡋࡥࡳࡪ࡬ࡦࡵࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡶ࡫ࡩࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡸ࡫ࡲࡷࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᙙ")
    def __init__(self, config, logger):
        bstack1lllll1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡤࡱࡱࡪ࡮࡭࠺ࠡࡦ࡬ࡧࡹ࠲ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡥࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡶࡸࡷ࠲ࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺࠢࡱࡥࡲ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙚ")
        self.config = config
        self.logger = logger
        self.bstack11ll1lllll1_opy_ = bstack1lllll1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡳࡰ࡮ࡺ࠭ࡵࡧࡶࡸࡸࠨᙛ")
        self.bstack11ll1lll111_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1l1ll1l_opy_ = 5
        self.bstack11ll1l1ll11_opy_ = 0
    def bstack11ll1ll1ll1_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1lllll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡌࡲ࡮ࡺࡩࡢࡶࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡴࡹࡪࡹࡴࠡࡣࡱࡨࠥࡹࡴࡰࡴࡨࡷࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡰࡰ࡮࡯࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙜ")
        self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡯࡮ࡨࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦᙝ").format(orchestration_strategy))
        try:
            bstack11lll1111ll_opy_ = []
            bstack1lllll1l_opy_ (u"ࠢࠣࠤ࡚ࡩࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡧࡧࡷࡧ࡭ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡯ࡳࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡶࠤࡹࡿࡰࡦࠢࡲࡪࠥࡧࡲࡳࡣࡼࠤࡦࡴࡤࠡ࡫ࡷࠫࡸࠦࡥ࡭ࡧࡰࡩࡳࡺࡳࠡࡣࡵࡩࠥࡵࡦࠡࡶࡼࡴࡪࠦࡤࡪࡥࡷࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡩࡨࡧࡵࡴࡧࠣ࡭ࡳࠦࡴࡩࡣࡷࠤࡨࡧࡳࡦ࠮ࠣࡹࡸ࡫ࡲࠡࡪࡤࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠ࡮ࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡸࡵࡵࡳࡥࡨࠤࡼ࡯ࡴࡩࠢࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦࠧࠨᙞ")
            source = orchestration_metadata[bstack1lllll1l_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᙟ")].get(bstack1lllll1l_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᙠ"), [])
            bstack11ll1l1l11l_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1lllll1l_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᙡ")].get(bstack1lllll1l_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᙢ"), False) and not bstack11ll1l1l11l_opy_:
                bstack11lll1111ll_opy_ = bstack11ll1l1l1ll_opy_(source) # bstack11ll1ll11l1_opy_-repo is handled bstack11ll1lll1l1_opy_
            payload = {
                bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙣ"): [{bstack1lllll1l_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣᙤ"): f} for f in test_files],
                bstack1lllll1l_opy_ (u"ࠢࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡓࡵࡴࡤࡸࡪ࡭ࡹࠣᙥ"): orchestration_strategy,
                bstack1lllll1l_opy_ (u"ࠣࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡎࡧࡷࡥࡩࡧࡴࡢࠤᙦ"): orchestration_metadata,
                bstack1lllll1l_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᙧ"): int(os.environ.get(bstack1lllll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᙨ")) or bstack1lllll1l_opy_ (u"ࠦ࠵ࠨᙩ")),
                bstack1lllll1l_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᙪ"): int(os.environ.get(bstack1lllll1l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᙫ")) or bstack1lllll1l_opy_ (u"ࠢ࠲ࠤᙬ")),
                bstack1lllll1l_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨ᙭"): self.config.get(bstack1lllll1l_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧ᙮"), bstack1lllll1l_opy_ (u"ࠪࠫᙯ")),
                bstack1lllll1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᙰ"): self.config.get(bstack1lllll1l_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᙱ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lllll1l_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᙲ"): os.environ.get(bstack1lllll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᙳ"), bstack1lllll1l_opy_ (u"ࠣࠤᙴ")),
                bstack1lllll1l_opy_ (u"ࠤ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠦᙵ"): get_host_info(),
                bstack1lllll1l_opy_ (u"ࠥࡴࡷࡊࡥࡵࡣ࡬ࡰࡸࠨᙶ"): bstack11lll1111ll_opy_
            }
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧᙷ").format(payload))
            response = bstack11ll1l1llll_opy_.bstack11ll1ll1l1l_opy_(self.bstack11ll1lllll1_opy_, payload)
            if response:
                self.bstack11ll1lll111_opy_ = self._11ll1l1l1l1_opy_(response)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡘࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᙸ").format(self.bstack11ll1lll111_opy_))
            else:
                self.logger.error(bstack1lllll1l_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨᙹ"))
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽࠾ࠥࢁࡽࠣᙺ").format(e))
    def _11ll1l1l1l1_opy_(self, response):
        bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡅࡕࡏࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡤࡲࡩࠦࡥࡹࡶࡵࡥࡨࡺࡳࠡࡴࡨࡰࡪࡼࡡ࡯ࡶࠣࡪ࡮࡫࡬ࡥࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙻ")
        bstack1lll11l111_opy_ = {}
        bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᙼ")] = response.get(bstack1lllll1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦᙽ"), self.default_timeout)
        bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᙾ")] = response.get(bstack1lllll1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᙿ"), self.bstack11ll1l1ll1l_opy_)
        bstack11lll111111_opy_ = response.get(bstack1lllll1l_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤ "))
        bstack11ll1ll1l11_opy_ = response.get(bstack1lllll1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚁ"))
        if bstack11lll111111_opy_:
            bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚂ")] = bstack11lll111111_opy_.split(bstack11ll1lll11l_opy_ + bstack1lllll1l_opy_ (u"ࠤ࠲ࠦᚃ"))[1] if bstack11ll1lll11l_opy_ + bstack1lllll1l_opy_ (u"ࠥ࠳ࠧᚄ") in bstack11lll111111_opy_ else bstack11lll111111_opy_
        else:
            bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᚅ")] = None
        if bstack11ll1ll1l11_opy_:
            bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᚆ")] = bstack11ll1ll1l11_opy_.split(bstack11ll1lll11l_opy_ + bstack1lllll1l_opy_ (u"ࠨ࠯ࠣᚇ"))[1] if bstack11ll1lll11l_opy_ + bstack1lllll1l_opy_ (u"ࠢ࠰ࠤᚈ") in bstack11ll1ll1l11_opy_ else bstack11ll1ll1l11_opy_
        else:
            bstack1lll11l111_opy_[bstack1lllll1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚉ")] = None
        if (
            response.get(bstack1lllll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᚊ")) is None or
            response.get(bstack1lllll1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᚋ")) is None or
            response.get(bstack1lllll1l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᚌ")) is None or
            response.get(bstack1lllll1l_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᚍ")) is None
        ):
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠨ࡛ࡱࡴࡲࡧࡪࡹࡳࡠࡵࡳࡰ࡮ࡺ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡵࡳࡳࡳࡹࡥ࡞ࠢࡕࡩࡨ࡫ࡩࡷࡧࡧࠤࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥࠩࡵࠬࠤ࡫ࡵࡲࠡࡵࡲࡱࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࡵࠣ࡭ࡳࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥᚎ"))
        return bstack1lll11l111_opy_
    def bstack11ll1ll111l_opy_(self):
        if not self.bstack11ll1lll111_opy_:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡐࡲࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸ࠴ࠢᚏ"))
            return None
        bstack11ll1lll1ll_opy_ = None
        test_files = []
        bstack11ll1llll11_opy_ = int(time.time() * 1000) # bstack11ll1ll1111_opy_ sec
        bstack11lll1111l1_opy_ = int(self.bstack11ll1lll111_opy_.get(bstack1lllll1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᚐ"), self.bstack11ll1l1ll1l_opy_))
        bstack11lll11111l_opy_ = int(self.bstack11ll1lll111_opy_.get(bstack1lllll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᚑ"), self.default_timeout)) * 1000
        bstack11ll1ll1l11_opy_ = self.bstack11ll1lll111_opy_.get(bstack1lllll1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᚒ"), None)
        bstack11lll111111_opy_ = self.bstack11ll1lll111_opy_.get(bstack1lllll1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᚓ"), None)
        if bstack11lll111111_opy_ is None and bstack11ll1ll1l11_opy_ is None:
            return None
        try:
            while bstack11lll111111_opy_ and (time.time() * 1000 - bstack11ll1llll11_opy_) < bstack11lll11111l_opy_:
                response = bstack11ll1l1llll_opy_.bstack11ll1llllll_opy_(bstack11lll111111_opy_, {})
                if response and response.get(bstack1lllll1l_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᚔ")):
                    bstack11ll1lll1ll_opy_ = response.get(bstack1lllll1l_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚕ"))
                self.bstack11ll1l1ll11_opy_ += 1
                if bstack11ll1lll1ll_opy_:
                    break
                time.sleep(bstack11lll1111l1_opy_)
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡈࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡪࡷࡵ࡭ࠡࡴࡨࡷࡺࡲࡴࠡࡗࡕࡐࠥࡧࡦࡵࡧࡵࠤࡼࡧࡩࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡾࢁࠥࡹࡥࡤࡱࡱࡨࡸ࠴ࠢᚖ").format(bstack11lll1111l1_opy_))
            if bstack11ll1ll1l11_opy_ and not bstack11ll1lll1ll_opy_:
                self.logger.debug(bstack1lllll1l_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡉࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡭ࡲ࡫࡯ࡶࡶ࡙ࠣࡗࡒࠢᚗ"))
                response = bstack11ll1l1llll_opy_.bstack11ll1llllll_opy_(bstack11ll1ll1l11_opy_, {})
                if response and response.get(bstack1lllll1l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚘ")):
                    bstack11ll1lll1ll_opy_ = response.get(bstack1lllll1l_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᚙ"))
            if bstack11ll1lll1ll_opy_ and len(bstack11ll1lll1ll_opy_) > 0:
                for bstack11lll1ll_opy_ in bstack11ll1lll1ll_opy_:
                    file_path = bstack11lll1ll_opy_.get(bstack1lllll1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡒࡤࡸ࡭ࠨᚚ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1lll1ll_opy_:
                return None
            self.logger.debug(bstack1lllll1l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡏࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡷ࡫ࡣࡦ࡫ࡹࡩࡩࡀࠠࡼࡿࠥ᚛").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1lllll1l_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀࠠࡼࡿࠥ᚜").format(e))
            return None
    def bstack11ll1llll1l_opy_(self):
        bstack1lllll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢࡦࡳࡺࡴࡴࠡࡱࡩࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡄࡔࡎࠦࡣࡢ࡮࡯ࡷࠥࡳࡡࡥࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣ᚝")
        return self.bstack11ll1l1ll11_opy_
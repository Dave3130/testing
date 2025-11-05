# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import time
from bstack_utils.bstack11ll1ll1l1l_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.constants import bstack11ll1l1lll1_opy_
from bstack_utils.helper import get_host_info, bstack11ll1l1ll11_opy_
class bstack11ll1lll1ll_opy_:
    bstack1lll11l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡢࡰࡧࡰࡪࡹࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᙝ")
    def __init__(self, config, logger):
        bstack1lll11l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࡪࡩࡤࡶ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡦࡳࡳ࡬ࡩࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡢࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡳࡵࡴ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦ࡮ࡢ࡯ࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙞ")
        self.config = config
        self.logger = logger
        self.bstack11ll1llll11_opy_ = bstack1lll11l_opy_ (u"ࠣࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡰ࡭࡫ࡷ࠱ࡹ࡫ࡳࡵࡵࠥᙟ")
        self.bstack11ll1l1llll_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1l1l111_opy_ = 5
        self.bstack11ll1lll1l1_opy_ = 0
    def bstack11ll1l11ll1_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1lll11l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡉ࡯࡫ࡷ࡭ࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡧ࡮ࡥࠢࡶࡸࡴࡸࡥࡴࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡴࡴࡲ࡬ࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᙠ")
        self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡌࡲ࡮ࡺࡩࡢࡶ࡬ࡲ࡬ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡼ࡯ࡴࡩࠢࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࢁࡽࠣᙡ").format(orchestration_strategy))
        try:
            bstack11ll1lll111_opy_ = []
            bstack1lll11l_opy_ (u"ࠦࠧࠨࡗࡦࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤ࡫࡫ࡴࡤࡪࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢ࡬ࡷࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡳࠡࡶࡼࡴࡪࠦ࡯ࡧࠢࡤࡶࡷࡧࡹࠡࡣࡱࡨࠥ࡯ࡴࠨࡵࠣࡩࡱ࡫࡭ࡦࡰࡷࡷࠥࡧࡲࡦࠢࡲࡪࠥࡺࡹࡱࡧࠣࡨ࡮ࡩࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡦࡥࡤࡹࡸ࡫ࠠࡪࡰࠣࡸ࡭ࡧࡴࠡࡥࡤࡷࡪ࠲ࠠࡶࡵࡨࡶࠥ࡮ࡡࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤࡲࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡵࡲࡹࡷࡩࡥࠡࡹ࡬ࡸ࡭ࠦࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭ࠦࡩ࡯ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣࠤࠥᙢ")
            source = orchestration_metadata[bstack1lll11l_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᙣ")].get(bstack1lll11l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᙤ"), [])
            bstack11ll1lllll1_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1lll11l_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᙥ")].get(bstack1lll11l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᙦ"), False) and not bstack11ll1lllll1_opy_:
                bstack11ll1lll111_opy_ = bstack11ll1l1ll11_opy_(source) # bstack11ll1lll11l_opy_-repo is handled bstack11ll1l1l1ll_opy_
            payload = {
                bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᙧ"): [{bstack1lll11l_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧᙨ"): f} for f in test_files],
                bstack1lll11l_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡹࡸࡡࡵࡧࡪࡽࠧᙩ"): orchestration_strategy,
                bstack1lll11l_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡒ࡫ࡴࡢࡦࡤࡸࡦࠨᙪ"): orchestration_metadata,
                bstack1lll11l_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤᙫ"): int(os.environ.get(bstack1lll11l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᙬ")) or bstack1lll11l_opy_ (u"ࠣ࠲ࠥ᙭")),
                bstack1lll11l_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨ᙮"): int(os.environ.get(bstack1lll11l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᙯ")) or bstack1lll11l_opy_ (u"ࠦ࠶ࠨᙰ")),
                bstack1lll11l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᙱ"): self.config.get(bstack1lll11l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᙲ"), bstack1lll11l_opy_ (u"ࠧࠨᙳ")),
                bstack1lll11l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᙴ"): self.config.get(bstack1lll11l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᙵ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lll11l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᙶ"): os.environ.get(bstack1lll11l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᙷ"), bstack1lll11l_opy_ (u"ࠧࠨᙸ")),
                bstack1lll11l_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣᙹ"): get_host_info(),
                bstack1lll11l_opy_ (u"ࠢࡱࡴࡇࡩࡹࡧࡩ࡭ࡵࠥᙺ"): bstack11ll1lll111_opy_
            }
            self.logger.debug(bstack1lll11l_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤᙻ").format(payload))
            response = bstack11ll1ll11ll_opy_.bstack11ll1ll1lll_opy_(self.bstack11ll1llll11_opy_, payload)
            if response:
                self.bstack11ll1l1llll_opy_ = self._11ll1llll1l_opy_(response)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᙼ").format(self.bstack11ll1l1llll_opy_))
            else:
                self.logger.error(bstack1lll11l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥᙽ"))
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺࠻ࠢࡾࢁࠧᙾ").format(e))
    def _11ll1llll1l_opy_(self, response):
        bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡲࡢࡥࡷࡷࠥࡸࡥ࡭ࡧࡹࡥࡳࡺࠠࡧ࡫ࡨࡰࡩࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙿ")
        bstack11llll1lll_opy_ = {}
        bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ ")] = response.get(bstack1lll11l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᚁ"), self.default_timeout)
        bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᚂ")] = response.get(bstack1lll11l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᚃ"), self.bstack11ll1l1l111_opy_)
        bstack11ll1l11l11_opy_ = response.get(bstack1lll11l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᚄ"))
        bstack11ll1ll11l1_opy_ = response.get(bstack1lll11l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᚅ"))
        if bstack11ll1l11l11_opy_:
            bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᚆ")] = bstack11ll1l11l11_opy_.split(bstack11ll1l1lll1_opy_ + bstack1lll11l_opy_ (u"ࠨ࠯ࠣᚇ"))[1] if bstack11ll1l1lll1_opy_ + bstack1lll11l_opy_ (u"ࠢ࠰ࠤᚈ") in bstack11ll1l11l11_opy_ else bstack11ll1l11l11_opy_
        else:
            bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚉ")] = None
        if bstack11ll1ll11l1_opy_:
            bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᚊ")] = bstack11ll1ll11l1_opy_.split(bstack11ll1l1lll1_opy_ + bstack1lll11l_opy_ (u"ࠥ࠳ࠧᚋ"))[1] if bstack11ll1l1lll1_opy_ + bstack1lll11l_opy_ (u"ࠦ࠴ࠨᚌ") in bstack11ll1ll11l1_opy_ else bstack11ll1ll11l1_opy_
        else:
            bstack11llll1lll_opy_[bstack1lll11l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᚍ")] = None
        if (
            response.get(bstack1lll11l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᚎ")) is None or
            response.get(bstack1lll11l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᚏ")) is None or
            response.get(bstack1lll11l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚐ")) is None or
            response.get(bstack1lll11l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᚑ")) is None
        ):
            self.logger.debug(bstack1lll11l_opy_ (u"ࠥ࡟ࡵࡸ࡯ࡤࡧࡶࡷࡤࡹࡰ࡭࡫ࡷࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡹࡰࡰࡰࡶࡩࡢࠦࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠭ࡹࠩࠡࡨࡲࡶࠥࡹ࡯࡮ࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡹࠠࡪࡰࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢᚒ"))
        return bstack11llll1lll_opy_
    def bstack11ll1l1l1l1_opy_(self):
        if not self.bstack11ll1l1llll_opy_:
            self.logger.error(bstack1lll11l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠱ࠦᚓ"))
            return None
        bstack11ll1ll1ll1_opy_ = None
        test_files = []
        bstack11ll1ll111l_opy_ = int(time.time() * 1000) # bstack11ll1l11l1l_opy_ sec
        bstack11ll1ll1111_opy_ = int(self.bstack11ll1l1llll_opy_.get(bstack1lll11l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᚔ"), self.bstack11ll1l1l111_opy_))
        bstack11ll1ll1l11_opy_ = int(self.bstack11ll1l1llll_opy_.get(bstack1lll11l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᚕ"), self.default_timeout)) * 1000
        bstack11ll1ll11l1_opy_ = self.bstack11ll1l1llll_opy_.get(bstack1lll11l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚖ"), None)
        bstack11ll1l11l11_opy_ = self.bstack11ll1l1llll_opy_.get(bstack1lll11l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚗ"), None)
        if bstack11ll1l11l11_opy_ is None and bstack11ll1ll11l1_opy_ is None:
            return None
        try:
            while bstack11ll1l11l11_opy_ and (time.time() * 1000 - bstack11ll1ll111l_opy_) < bstack11ll1ll1l11_opy_:
                response = bstack11ll1ll11ll_opy_.bstack11ll1l1l11l_opy_(bstack11ll1l11l11_opy_, {})
                if response and response.get(bstack1lll11l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚘ")):
                    bstack11ll1ll1ll1_opy_ = response.get(bstack1lll11l_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᚙ"))
                self.bstack11ll1lll1l1_opy_ += 1
                if bstack11ll1ll1ll1_opy_:
                    break
                time.sleep(bstack11ll1ll1111_opy_)
                self.logger.debug(bstack1lll11l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡸࡥࡴࡷ࡯ࡸ࡛ࠥࡒࡍࠢࡤࡪࡹ࡫ࡲࠡࡹࡤ࡭ࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡻࡾࠢࡶࡩࡨࡵ࡮ࡥࡵ࠱ࠦᚚ").format(bstack11ll1ll1111_opy_))
            if bstack11ll1ll11l1_opy_ and not bstack11ll1ll1ll1_opy_:
                self.logger.debug(bstack1lll11l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡴࡪ࡯ࡨࡳࡺࡺࠠࡖࡔࡏࠦ᚛"))
                response = bstack11ll1ll11ll_opy_.bstack11ll1l1l11l_opy_(bstack11ll1ll11l1_opy_, {})
                if response and response.get(bstack1lll11l_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧ᚜")):
                    bstack11ll1ll1ll1_opy_ = response.get(bstack1lll11l_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨ᚝"))
            if bstack11ll1ll1ll1_opy_ and len(bstack11ll1ll1ll1_opy_) > 0:
                for bstack1l1ll111_opy_ in bstack11ll1ll1ll1_opy_:
                    file_path = bstack1l1ll111_opy_.get(bstack1lll11l_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥ᚞"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1ll1ll1_opy_:
                return None
            self.logger.debug(bstack1lll11l_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡓࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡴࡨࡧࡪ࡯ࡶࡦࡦ࠽ࠤࢀࢃࠢ᚟").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1lll11l_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᚠ").format(e))
            return None
    def bstack11ll1l1ll1l_opy_(self):
        bstack1lll11l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡧࡦࡲ࡬ࡴࠢࡰࡥࡩ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᚡ")
        return self.bstack11ll1lll1l1_opy_
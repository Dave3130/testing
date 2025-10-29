# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import time
from bstack_utils.bstack11ll1lll1l1_opy_ import bstack11ll1ll1l11_opy_
from bstack_utils.constants import bstack11ll1ll1ll1_opy_
from bstack_utils.helper import get_host_info, bstack11ll1ll111l_opy_
class bstack11ll1l11ll1_opy_:
    bstack11l11ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡌࡦࡴࡤ࡭ࡧࡶࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡼ࡯ࡴࡩࠢࡷ࡬ࡪࠦࡂࡳࡱࡺࡷࡪࡸࡓࡵࡣࡦ࡯ࠥࡹࡥࡳࡸࡨࡶ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᙨ")
    def __init__(self, config, logger):
        bstack11l11ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡥࡲࡲ࡫࡯ࡧ࠻ࠢࡧ࡭ࡨࡺࠬࠡࡶࡨࡷࡹࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡣࡰࡰࡩ࡭࡬ࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࡟ࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡷࡹࡸࠬࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡵࡷࡶࡦࡺࡥࡨࡻࠣࡲࡦࡳࡥࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙩ")
        self.config = config
        self.logger = logger
        self.bstack11ll1lll111_opy_ = bstack11l11ll_opy_ (u"ࠧࡺࡥࡴࡶࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯࠱ࡤࡴ࡮࠵ࡶ࠲࠱ࡶࡴࡱ࡯ࡴ࠮ࡶࡨࡷࡹࡹࠢᙪ")
        self.bstack11ll1ll1111_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1lllll1_opy_ = 5
        self.bstack11ll1llll11_opy_ = 0
    def bstack11ll1lll11l_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11l11ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡍࡳ࡯ࡴࡪࡣࡷࡩࡸࠦࡴࡩࡧࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡤࡲࡩࠦࡳࡵࡱࡵࡩࡸࠦࡴࡩࡧࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡪࡡࡵࡣࠣࡪࡴࡸࠠࡱࡱ࡯ࡰ࡮ࡴࡧ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙫ")
        self.logger.debug(bstack11l11ll_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡉ࡯࡫ࡷ࡭ࡦࡺࡩ࡯ࡩࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡹ࡬ࡸ࡭ࠦࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡾࢁࠧᙬ").format(orchestration_strategy))
        try:
            bstack11ll1ll11l1_opy_ = []
            bstack11l11ll_opy_ (u"ࠣࠤ࡛ࠥࡪࠦࡷࡪ࡮࡯ࠤࡳࡵࡴࠡࡨࡨࡸࡨ࡮ࠠࡨ࡫ࡷࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡩࡴࠢࡶࡳࡺࡸࡣࡦࠢ࡬ࡷࠥࡺࡹࡱࡧࠣࡳ࡫ࠦࡡࡳࡴࡤࡽࠥࡧ࡮ࡥࠢ࡬ࡸࠬࡹࠠࡦ࡮ࡨࡱࡪࡴࡴࡴࠢࡤࡶࡪࠦ࡯ࡧࠢࡷࡽࡵ࡫ࠠࡥ࡫ࡦࡸࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࡦࡪࡩࡡࡶࡵࡨࠤ࡮ࡴࠠࡵࡪࡤࡸࠥࡩࡡࡴࡧ࠯ࠤࡺࡹࡥࡳࠢ࡫ࡥࡸࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡤࠡ࡯ࡸࡰࡹ࡯࠭ࡳࡧࡳࡳࠥࡹ࡯ࡶࡴࡦࡩࠥࡽࡩࡵࡪࠣࡪࡪࡧࡴࡶࡴࡨࡆࡷࡧ࡮ࡤࡪࠣ࡭ࡳࠦࡢࡳࡱࡺࡷࡪࡸࡳࡵࡣࡦ࡯ࠧࠨࠢ᙭")
            source = orchestration_metadata[bstack11l11ll_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨ᙮")].get(bstack11l11ll_opy_ (u"ࠪࡷࡴࡻࡲࡤࡧࠪᙯ"), [])
            bstack11ll1l1l11l_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11l11ll_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᙰ")].get(bstack11l11ll_opy_ (u"ࠬ࡫࡮ࡢࡤ࡯ࡩࡩ࠭ᙱ"), False) and not bstack11ll1l1l11l_opy_:
                bstack11ll1ll11l1_opy_ = bstack11ll1ll111l_opy_(source) # bstack11ll1l1l1l1_opy_-repo is handled bstack11ll1l1ll11_opy_
            payload = {
                bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᙲ"): [{bstack11l11ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡕࡧࡴࡩࠤᙳ"): f} for f in test_files],
                bstack11l11ll_opy_ (u"ࠣࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡔࡶࡵࡥࡹ࡫ࡧࡺࠤᙴ"): orchestration_strategy,
                bstack11l11ll_opy_ (u"ࠤࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡏࡨࡸࡦࡪࡡࡵࡣࠥᙵ"): orchestration_metadata,
                bstack11l11ll_opy_ (u"ࠥࡲࡴࡪࡥࡊࡰࡧࡩࡽࠨᙶ"): int(os.environ.get(bstack11l11ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡒࡔࡊࡅࡠࡋࡑࡈࡊ࡞ࠢᙷ")) or bstack11l11ll_opy_ (u"ࠧ࠶ࠢᙸ")),
                bstack11l11ll_opy_ (u"ࠨࡴࡰࡶࡤࡰࡓࡵࡤࡦࡵࠥᙹ"): int(os.environ.get(bstack11l11ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡔࡐࡖࡄࡐࡤࡔࡏࡅࡇࡢࡇࡔ࡛ࡎࡕࠤᙺ")) or bstack11l11ll_opy_ (u"ࠣ࠳ࠥᙻ")),
                bstack11l11ll_opy_ (u"ࠤࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠢᙼ"): self.config.get(bstack11l11ll_opy_ (u"ࠪࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠨᙽ"), bstack11l11ll_opy_ (u"ࠫࠬᙾ")),
                bstack11l11ll_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠣᙿ"): self.config.get(bstack11l11ll_opy_ (u"࠭ࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠩ "), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l11ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡘࡵ࡯ࡋࡧࡩࡳࡺࡩࡧ࡫ࡨࡶࠧᚁ"): os.environ.get(bstack11l11ll_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡃࡗࡌࡐࡉࡥࡒࡖࡐࡢࡍࡉࡋࡎࡕࡋࡉࡍࡊࡘࠢᚂ"), bstack11l11ll_opy_ (u"ࠤࠥᚃ")),
                bstack11l11ll_opy_ (u"ࠥ࡬ࡴࡹࡴࡊࡰࡩࡳࠧᚄ"): get_host_info(),
                bstack11l11ll_opy_ (u"ࠦࡵࡸࡄࡦࡶࡤ࡭ࡱࡹࠢᚅ"): bstack11ll1ll11l1_opy_
            }
            self.logger.debug(bstack11l11ll_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡘ࡫࡮ࡥ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨᚆ").format(payload))
            response = bstack11ll1ll1l11_opy_.bstack11ll1ll1lll_opy_(self.bstack11ll1lll111_opy_, payload)
            if response:
                self.bstack11ll1ll1111_opy_ = self._11ll1l1llll_opy_(response)
                self.logger.debug(bstack11l11ll_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡ࡙ࠥࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠿ࠦࡻࡾࠤᚇ").format(self.bstack11ll1ll1111_opy_))
            else:
                self.logger.error(bstack11l11ll_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡆࡢ࡫࡯ࡩࡩࠦࡴࡰࠢࡪࡩࡹࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪ࠴ࠢᚈ"))
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡳࡦࡰࡧ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾࠿ࠦࡻࡾࠤᚉ").format(e))
    def _11ll1l1llll_opy_(self, response):
        bstack11l11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡐࡳࡱࡦࡩࡸࡹࡥࡴࠢࡷ࡬ࡪࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠣࡥࡳࡪࠠࡦࡺࡷࡶࡦࡩࡴࡴࠢࡵࡩࡱ࡫ࡶࡢࡰࡷࠤ࡫࡯ࡥ࡭ࡦࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᚊ")
        bstack111l1lll11_opy_ = {}
        bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦᚋ")] = response.get(bstack11l11ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚌ"), self.default_timeout)
        bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᚍ")] = response.get(bstack11l11ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᚎ"), self.bstack11ll1lllll1_opy_)
        bstack11ll1l11lll_opy_ = response.get(bstack11l11ll_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚏ"))
        bstack11ll1l1ll1l_opy_ = response.get(bstack11l11ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚐ"))
        if bstack11ll1l11lll_opy_:
            bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᚑ")] = bstack11ll1l11lll_opy_.split(bstack11ll1ll1ll1_opy_ + bstack11l11ll_opy_ (u"ࠥ࠳ࠧᚒ"))[1] if bstack11ll1ll1ll1_opy_ + bstack11l11ll_opy_ (u"ࠦ࠴ࠨᚓ") in bstack11ll1l11lll_opy_ else bstack11ll1l11lll_opy_
        else:
            bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᚔ")] = None
        if bstack11ll1l1ll1l_opy_:
            bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚕ")] = bstack11ll1l1ll1l_opy_.split(bstack11ll1ll1ll1_opy_ + bstack11l11ll_opy_ (u"ࠢ࠰ࠤᚖ"))[1] if bstack11ll1ll1ll1_opy_ + bstack11l11ll_opy_ (u"ࠣ࠱ࠥᚗ") in bstack11ll1l1ll1l_opy_ else bstack11ll1l1ll1l_opy_
        else:
            bstack111l1lll11_opy_[bstack11l11ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᚘ")] = None
        if (
            response.get(bstack11l11ll_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦᚙ")) is None or
            response.get(bstack11l11ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᚚ")) is None or
            response.get(bstack11l11ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤ᚛")) is None or
            response.get(bstack11l11ll_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤ᚜")) is None
        ):
            self.logger.debug(bstack11l11ll_opy_ (u"ࠢ࡜ࡲࡵࡳࡨ࡫ࡳࡴࡡࡶࡴࡱ࡯ࡴࡠࡶࡨࡷࡹࡹ࡟ࡳࡧࡶࡴࡴࡴࡳࡦ࡟ࠣࡖࡪࡩࡥࡪࡸࡨࡨࠥࡴࡵ࡭࡮ࠣࡺࡦࡲࡵࡦࠪࡶ࠭ࠥ࡬࡯ࡳࠢࡶࡳࡲ࡫ࠠࡢࡶࡷࡶ࡮ࡨࡵࡵࡧࡶࠤ࡮ࡴࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠦ᚝"))
        return bstack111l1lll11_opy_
    def bstack11ll1lll1ll_opy_(self):
        if not self.bstack11ll1ll1111_opy_:
            self.logger.error(bstack11l11ll_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡑࡳࠥࡸࡥࡲࡷࡨࡷࡹࠦࡤࡢࡶࡤࠤࡦࡼࡡࡪ࡮ࡤࡦࡱ࡫ࠠࡵࡱࠣࡪࡪࡺࡣࡩࠢࡲࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠮ࠣ᚞"))
            return None
        bstack11ll1l11l1l_opy_ = None
        test_files = []
        bstack11ll1ll11ll_opy_ = int(time.time() * 1000) # bstack11ll1l1lll1_opy_ sec
        bstack11ll1l1l1ll_opy_ = int(self.bstack11ll1ll1111_opy_.get(bstack11l11ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦ᚟"), self.bstack11ll1lllll1_opy_))
        bstack11ll1ll1l1l_opy_ = int(self.bstack11ll1ll1111_opy_.get(bstack11l11ll_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦᚠ"), self.default_timeout)) * 1000
        bstack11ll1l1ll1l_opy_ = self.bstack11ll1ll1111_opy_.get(bstack11l11ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᚡ"), None)
        bstack11ll1l11lll_opy_ = self.bstack11ll1ll1111_opy_.get(bstack11l11ll_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᚢ"), None)
        if bstack11ll1l11lll_opy_ is None and bstack11ll1l1ll1l_opy_ is None:
            return None
        try:
            while bstack11ll1l11lll_opy_ and (time.time() * 1000 - bstack11ll1ll11ll_opy_) < bstack11ll1ll1l1l_opy_:
                response = bstack11ll1ll1l11_opy_.bstack11ll1llll1l_opy_(bstack11ll1l11lll_opy_, {})
                if response and response.get(bstack11l11ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚣ")):
                    bstack11ll1l11l1l_opy_ = response.get(bstack11l11ll_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᚤ"))
                self.bstack11ll1llll11_opy_ += 1
                if bstack11ll1l11l1l_opy_:
                    break
                time.sleep(bstack11ll1l1l1ll_opy_)
                self.logger.debug(bstack11l11ll_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡉࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡵࡩࡸࡻ࡬ࡵࠢࡘࡖࡑࠦࡡࡧࡶࡨࡶࠥࡽࡡࡪࡶ࡬ࡲ࡬ࠦࡦࡰࡴࠣࡿࢂࠦࡳࡦࡥࡲࡲࡩࡹ࠮ࠣᚥ").format(bstack11ll1l1l1ll_opy_))
            if bstack11ll1l1ll1l_opy_ and not bstack11ll1l11l1l_opy_:
                self.logger.debug(bstack11l11ll_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡊࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡸ࡮ࡳࡥࡰࡷࡷࠤ࡚ࡘࡌࠣᚦ"))
                response = bstack11ll1ll1l11_opy_.bstack11ll1llll1l_opy_(bstack11ll1l1ll1l_opy_, {})
                if response and response.get(bstack11l11ll_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᚧ")):
                    bstack11ll1l11l1l_opy_ = response.get(bstack11l11ll_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᚨ"))
            if bstack11ll1l11l1l_opy_ and len(bstack11ll1l11l1l_opy_) > 0:
                for bstack1ll1llll_opy_ in bstack11ll1l11l1l_opy_:
                    file_path = bstack1ll1llll_opy_.get(bstack11l11ll_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡓࡥࡹ࡮ࠢᚩ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1l11l1l_opy_:
                return None
            self.logger.debug(bstack11l11ll_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡐࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷࠥࡸࡥࡤࡧ࡬ࡺࡪࡪ࠺ࠡࡽࢀࠦᚪ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l11ll_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡧࡧࡷࡧ࡭࡯࡮ࡨࠢࡲࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺ࠡࡽࢀࠦᚫ").format(e))
            return None
    def bstack11ll1llllll_opy_(self):
        bstack11l11ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡘࡥࡵࡷࡵࡲࡸࠦࡴࡩࡧࠣࡧࡴࡻ࡮ࡵࠢࡲࡪࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡅࡕࡏࠠࡤࡣ࡯ࡰࡸࠦ࡭ࡢࡦࡨ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᚬ")
        return self.bstack11ll1llll11_opy_
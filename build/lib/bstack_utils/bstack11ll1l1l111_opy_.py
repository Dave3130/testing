# coding: UTF-8
import sys
bstack1l111_opy_ = sys.version_info [0] == 2
bstack11l111_opy_ = 2048
bstack1l1l_opy_ = 7
def bstack1l111ll_opy_ (bstack1llllll1_opy_):
    global bstack111l1l1_opy_
    bstack1lll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1ll11l1_opy_ = bstack1llllll1_opy_ [:-1]
    bstack1l11lll_opy_ = bstack1lll111_opy_ % len (bstack1ll11l1_opy_)
    bstack11l1l1_opy_ = bstack1ll11l1_opy_ [:bstack1l11lll_opy_] + bstack1ll11l1_opy_ [bstack1l11lll_opy_:]
    if bstack1l111_opy_:
        bstack11l11l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    else:
        bstack11l11l_opy_ = str () .join ([chr (ord (char) - bstack11l111_opy_ - (bstack11l1l1l_opy_ + bstack1lll111_opy_) % bstack1l1l_opy_) for bstack11l1l1l_opy_, char in enumerate (bstack11l1l1_opy_)])
    return eval (bstack11l11l_opy_)
import os
import time
from bstack_utils.bstack11ll1l1l1l1_opy_ import bstack11ll1ll11ll_opy_
from bstack_utils.constants import bstack11lll111111_opy_
from bstack_utils.helper import get_host_info, bstack11ll1lll11l_opy_
class bstack11ll1llll1l_opy_:
    bstack1l111ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡢࡰࡧࡰࡪࡹࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᙖ")
    def __init__(self, config, logger):
        bstack1l111ll_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࡪࡩࡤࡶ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡦࡳࡳ࡬ࡩࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡢࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡳࡵࡴ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦ࡮ࡢ࡯ࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙗ")
        self.config = config
        self.logger = logger
        self.bstack11ll1llll11_opy_ = bstack1l111ll_opy_ (u"ࠣࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡰ࡭࡫ࡷ࠱ࡹ࡫ࡳࡵࡵࠥᙘ")
        self.bstack11ll1lll111_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1ll1l1l_opy_ = 5
        self.bstack11ll1ll11l1_opy_ = 0
    def bstack11ll1ll1lll_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1l111ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡉ࡯࡫ࡷ࡭ࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡧ࡮ࡥࠢࡶࡸࡴࡸࡥࡴࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡴࡴࡲ࡬ࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᙙ")
        self.logger.debug(bstack1l111ll_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡌࡲ࡮ࡺࡩࡢࡶ࡬ࡲ࡬ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡼ࡯ࡴࡩࠢࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࢁࡽࠣᙚ").format(orchestration_strategy))
        try:
            bstack11ll1ll1ll1_opy_ = []
            bstack1l111ll_opy_ (u"ࠦࠧࠨࡗࡦࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤ࡫࡫ࡴࡤࡪࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢ࡬ࡷࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡳࠡࡶࡼࡴࡪࠦ࡯ࡧࠢࡤࡶࡷࡧࡹࠡࡣࡱࡨࠥ࡯ࡴࠨࡵࠣࡩࡱ࡫࡭ࡦࡰࡷࡷࠥࡧࡲࡦࠢࡲࡪࠥࡺࡹࡱࡧࠣࡨ࡮ࡩࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡦࡥࡤࡹࡸ࡫ࠠࡪࡰࠣࡸ࡭ࡧࡴࠡࡥࡤࡷࡪ࠲ࠠࡶࡵࡨࡶࠥ࡮ࡡࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤࡲࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡵࡲࡹࡷࡩࡥࠡࡹ࡬ࡸ࡭ࠦࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭ࠦࡩ࡯ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣࠤࠥᙛ")
            source = orchestration_metadata[bstack1l111ll_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᙜ")].get(bstack1l111ll_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᙝ"), [])
            bstack11ll1lllll1_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1l111ll_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᙞ")].get(bstack1l111ll_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᙟ"), False) and not bstack11ll1lllll1_opy_:
                bstack11ll1ll1ll1_opy_ = bstack11ll1lll11l_opy_(source) # bstack11ll1l1ll11_opy_-repo is handled bstack11ll1lll1l1_opy_
            payload = {
                bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᙠ"): [{bstack1l111ll_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧᙡ"): f} for f in test_files],
                bstack1l111ll_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡹࡸࡡࡵࡧࡪࡽࠧᙢ"): orchestration_strategy,
                bstack1l111ll_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡒ࡫ࡴࡢࡦࡤࡸࡦࠨᙣ"): orchestration_metadata,
                bstack1l111ll_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤᙤ"): int(os.environ.get(bstack1l111ll_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᙥ")) or bstack1l111ll_opy_ (u"ࠣ࠲ࠥᙦ")),
                bstack1l111ll_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨᙧ"): int(os.environ.get(bstack1l111ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᙨ")) or bstack1l111ll_opy_ (u"ࠦ࠶ࠨᙩ")),
                bstack1l111ll_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᙪ"): self.config.get(bstack1l111ll_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᙫ"), bstack1l111ll_opy_ (u"ࠧࠨᙬ")),
                bstack1l111ll_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦ᙭"): self.config.get(bstack1l111ll_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬ᙮"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l111ll_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᙯ"): os.environ.get(bstack1l111ll_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᙰ"), bstack1l111ll_opy_ (u"ࠧࠨᙱ")),
                bstack1l111ll_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣᙲ"): get_host_info(),
                bstack1l111ll_opy_ (u"ࠢࡱࡴࡇࡩࡹࡧࡩ࡭ࡵࠥᙳ"): bstack11ll1ll1ll1_opy_
            }
            self.logger.debug(bstack1l111ll_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤᙴ").format(payload))
            response = bstack11ll1ll11ll_opy_.bstack11ll1l1lll1_opy_(self.bstack11ll1llll11_opy_, payload)
            if response:
                self.bstack11ll1lll111_opy_ = self._11ll1lll1ll_opy_(response)
                self.logger.debug(bstack1l111ll_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᙵ").format(self.bstack11ll1lll111_opy_))
            else:
                self.logger.error(bstack1l111ll_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥᙶ"))
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺࠻ࠢࡾࢁࠧᙷ").format(e))
    def _11ll1lll1ll_opy_(self, response):
        bstack1l111ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡲࡢࡥࡷࡷࠥࡸࡥ࡭ࡧࡹࡥࡳࡺࠠࡧ࡫ࡨࡰࡩࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙸ")
        bstack111l1ll11l_opy_ = {}
        bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙹ")] = response.get(bstack1l111ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙺ"), self.default_timeout)
        bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙻ")] = response.get(bstack1l111ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᙼ"), self.bstack11ll1ll1l1l_opy_)
        bstack11ll1l1ll1l_opy_ = response.get(bstack1l111ll_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙽ"))
        bstack11lll11111l_opy_ = response.get(bstack1l111ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙾ"))
        if bstack11ll1l1ll1l_opy_:
            bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᙿ")] = bstack11ll1l1ll1l_opy_.split(bstack11lll111111_opy_ + bstack1l111ll_opy_ (u"ࠨ࠯ࠣ "))[1] if bstack11lll111111_opy_ + bstack1l111ll_opy_ (u"ࠢ࠰ࠤᚁ") in bstack11ll1l1ll1l_opy_ else bstack11ll1l1ll1l_opy_
        else:
            bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚂ")] = None
        if bstack11lll11111l_opy_:
            bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᚃ")] = bstack11lll11111l_opy_.split(bstack11lll111111_opy_ + bstack1l111ll_opy_ (u"ࠥ࠳ࠧᚄ"))[1] if bstack11lll111111_opy_ + bstack1l111ll_opy_ (u"ࠦ࠴ࠨᚅ") in bstack11lll11111l_opy_ else bstack11lll11111l_opy_
        else:
            bstack111l1ll11l_opy_[bstack1l111ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᚆ")] = None
        if (
            response.get(bstack1l111ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᚇ")) is None or
            response.get(bstack1l111ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᚈ")) is None or
            response.get(bstack1l111ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚉ")) is None or
            response.get(bstack1l111ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᚊ")) is None
        ):
            self.logger.debug(bstack1l111ll_opy_ (u"ࠥ࡟ࡵࡸ࡯ࡤࡧࡶࡷࡤࡹࡰ࡭࡫ࡷࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡹࡰࡰࡰࡶࡩࡢࠦࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠭ࡹࠩࠡࡨࡲࡶࠥࡹ࡯࡮ࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡹࠠࡪࡰࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢᚋ"))
        return bstack111l1ll11l_opy_
    def bstack11ll1l1l1ll_opy_(self):
        if not self.bstack11ll1lll111_opy_:
            self.logger.error(bstack1l111ll_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠱ࠦᚌ"))
            return None
        bstack11ll1l1llll_opy_ = None
        test_files = []
        bstack11ll1l1l11l_opy_ = int(time.time() * 1000) # bstack11ll1ll1111_opy_ sec
        bstack11ll1ll1l11_opy_ = int(self.bstack11ll1lll111_opy_.get(bstack1l111ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᚍ"), self.bstack11ll1ll1l1l_opy_))
        bstack11ll1llllll_opy_ = int(self.bstack11ll1lll111_opy_.get(bstack1l111ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᚎ"), self.default_timeout)) * 1000
        bstack11lll11111l_opy_ = self.bstack11ll1lll111_opy_.get(bstack1l111ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚏ"), None)
        bstack11ll1l1ll1l_opy_ = self.bstack11ll1lll111_opy_.get(bstack1l111ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚐ"), None)
        if bstack11ll1l1ll1l_opy_ is None and bstack11lll11111l_opy_ is None:
            return None
        try:
            while bstack11ll1l1ll1l_opy_ and (time.time() * 1000 - bstack11ll1l1l11l_opy_) < bstack11ll1llllll_opy_:
                response = bstack11ll1ll11ll_opy_.bstack11ll1ll111l_opy_(bstack11ll1l1ll1l_opy_, {})
                if response and response.get(bstack1l111ll_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚑ")):
                    bstack11ll1l1llll_opy_ = response.get(bstack1l111ll_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᚒ"))
                self.bstack11ll1ll11l1_opy_ += 1
                if bstack11ll1l1llll_opy_:
                    break
                time.sleep(bstack11ll1ll1l11_opy_)
                self.logger.debug(bstack1l111ll_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡸࡥࡴࡷ࡯ࡸ࡛ࠥࡒࡍࠢࡤࡪࡹ࡫ࡲࠡࡹࡤ࡭ࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡻࡾࠢࡶࡩࡨࡵ࡮ࡥࡵ࠱ࠦᚓ").format(bstack11ll1ll1l11_opy_))
            if bstack11lll11111l_opy_ and not bstack11ll1l1llll_opy_:
                self.logger.debug(bstack1l111ll_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡴࡪ࡯ࡨࡳࡺࡺࠠࡖࡔࡏࠦᚔ"))
                response = bstack11ll1ll11ll_opy_.bstack11ll1ll111l_opy_(bstack11lll11111l_opy_, {})
                if response and response.get(bstack1l111ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚕ")):
                    bstack11ll1l1llll_opy_ = response.get(bstack1l111ll_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᚖ"))
            if bstack11ll1l1llll_opy_ and len(bstack11ll1l1llll_opy_) > 0:
                for bstack1lll1111_opy_ in bstack11ll1l1llll_opy_:
                    file_path = bstack1lll1111_opy_.get(bstack1l111ll_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᚗ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1l1llll_opy_:
                return None
            self.logger.debug(bstack1l111ll_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡓࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡴࡨࡧࡪ࡯ࡶࡦࡦ࠽ࠤࢀࢃࠢᚘ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l111ll_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᚙ").format(e))
            return None
    def bstack11ll1l11lll_opy_(self):
        bstack1l111ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡧࡦࡲ࡬ࡴࠢࡰࡥࡩ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᚚ")
        return self.bstack11ll1ll11l1_opy_
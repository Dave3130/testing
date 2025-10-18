# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import time
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11ll1l1l11l_opy_
from bstack_utils.constants import bstack11ll1ll1l1l_opy_
from bstack_utils.helper import get_host_info, bstack11ll1ll11l1_opy_
class bstack11lll1111ll_opy_:
    bstack11l111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍࡧ࡮ࡥ࡮ࡨࡷࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡳࡦࡴࡹࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᙛ")
    def __init__(self, config, logger):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡨ࡮ࡩࡴ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡠࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࡸࡺࡲ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤࡳࡧ࡭ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙜ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1l11_opy_ = bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡵࡲࡩࡵ࠯ࡷࡩࡸࡺࡳࠣᙝ")
        self.bstack11ll1l1llll_opy_ = None
        self.default_timeout = 60
        self.bstack11lll1111l1_opy_ = 5
        self.bstack11ll1l1l1l1_opy_ = 0
    def bstack11ll1lll1ll_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࡩࡵ࡫ࡤࡸࡪࡹࠠࡵࡪࡨࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡶࡻࡥࡴࡶࠣࡥࡳࡪࠠࡴࡶࡲࡶࡪࡹࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡲࡲࡰࡱ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙞ")
        self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨᙟ").format(orchestration_strategy))
        try:
            bstack11ll1l1lll1_opy_ = []
            bstack11l111_opy_ (u"ࠤࠥࠦ࡜࡫ࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡩࡩࡹࡩࡨࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡪࡵࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡸࠦࡴࡺࡲࡨࠤࡴ࡬ࠠࡢࡴࡵࡥࡾࠦࡡ࡯ࡦࠣ࡭ࡹ࠭ࡳࠡࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡥࡷ࡫ࠠࡰࡨࠣࡸࡾࡶࡥࠡࡦ࡬ࡧࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧ࡫ࡣࡢࡷࡶࡩࠥ࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡵࡨ࠰ࠥࡻࡳࡦࡴࠣ࡬ࡦࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡰࡹࡱࡺࡩ࠮ࡴࡨࡴࡴࠦࡳࡰࡷࡵࡧࡪࠦࡷࡪࡶ࡫ࠤ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠤ࡮ࡴࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨࠢࠣᙠ")
            source = orchestration_metadata[bstack11l111_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᙡ")].get(bstack11l111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᙢ"), [])
            bstack11ll1l1ll11_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11l111_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᙣ")].get(bstack11l111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᙤ"), False) and not bstack11ll1l1ll11_opy_:
                bstack11ll1l1lll1_opy_ = bstack11ll1ll11l1_opy_(source) # bstack11lll111111_opy_-repo is handled bstack11ll1ll1lll_opy_
            payload = {
                bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙥ"): [{bstack11l111_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᙦ"): f} for f in test_files],
                bstack11l111_opy_ (u"ࠤࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡷࡶࡦࡺࡥࡨࡻࠥᙧ"): orchestration_strategy,
                bstack11l111_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡐࡩࡹࡧࡤࡢࡶࡤࠦᙨ"): orchestration_metadata,
                bstack11l111_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᙩ"): int(os.environ.get(bstack11l111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᙪ")) or bstack11l111_opy_ (u"ࠨ࠰ࠣᙫ")),
                bstack11l111_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᙬ"): int(os.environ.get(bstack11l111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥ᙭")) or bstack11l111_opy_ (u"ࠤ࠴ࠦ᙮")),
                bstack11l111_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᙯ"): self.config.get(bstack11l111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᙰ"), bstack11l111_opy_ (u"ࠬ࠭ᙱ")),
                bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᙲ"): self.config.get(bstack11l111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᙳ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᙴ"): os.environ.get(bstack11l111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᙵ"), bstack11l111_opy_ (u"ࠥࠦᙶ")),
                bstack11l111_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨᙷ"): get_host_info(),
                bstack11l111_opy_ (u"ࠧࡶࡲࡅࡧࡷࡥ࡮ࡲࡳࠣᙸ"): bstack11ll1l1lll1_opy_
            }
            self.logger.debug(bstack11l111_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᙹ").format(payload))
            response = bstack11ll1l1l11l_opy_.bstack11ll1l1l1ll_opy_(self.bstack11ll1ll1l11_opy_, payload)
            if response:
                self.bstack11ll1l1llll_opy_ = self._11ll1ll1111_opy_(response)
                self.logger.debug(bstack11l111_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᙺ").format(self.bstack11ll1l1llll_opy_))
            else:
                self.logger.error(bstack11l111_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣᙻ"))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࡀࠠࡼࡿࠥᙼ").format(e))
    def _11ll1ll1111_opy_(self, response):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡦࡴࡤࠡࡧࡻࡸࡷࡧࡣࡵࡵࠣࡶࡪࡲࡥࡷࡣࡱࡸࠥ࡬ࡩࡦ࡮ࡧࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᙽ")
        bstack1l11lll1l1_opy_ = {}
        bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙾ")] = response.get(bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙿ"), self.default_timeout)
        bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣ ")] = response.get(bstack11l111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᚁ"), self.bstack11lll1111l1_opy_)
        bstack11ll1lllll1_opy_ = response.get(bstack11l111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚂ"))
        bstack11ll1lll11l_opy_ = response.get(bstack11l111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᚃ"))
        if bstack11ll1lllll1_opy_:
            bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᚄ")] = bstack11ll1lllll1_opy_.split(bstack11ll1ll1l1l_opy_ + bstack11l111_opy_ (u"ࠦ࠴ࠨᚅ"))[1] if bstack11ll1ll1l1l_opy_ + bstack11l111_opy_ (u"ࠧ࠵ࠢᚆ") in bstack11ll1lllll1_opy_ else bstack11ll1lllll1_opy_
        else:
            bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᚇ")] = None
        if bstack11ll1lll11l_opy_:
            bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚈ")] = bstack11ll1lll11l_opy_.split(bstack11ll1ll1l1l_opy_ + bstack11l111_opy_ (u"ࠣ࠱ࠥᚉ"))[1] if bstack11ll1ll1l1l_opy_ + bstack11l111_opy_ (u"ࠤ࠲ࠦᚊ") in bstack11ll1lll11l_opy_ else bstack11ll1lll11l_opy_
        else:
            bstack1l11lll1l1_opy_[bstack11l111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᚋ")] = None
        if (
            response.get(bstack11l111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚌ")) is None or
            response.get(bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᚍ")) is None or
            response.get(bstack11l111_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚎ")) is None or
            response.get(bstack11l111_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚏ")) is None
        ):
            self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡳࡶࡴࡩࡥࡴࡵࡢࡷࡵࡲࡩࡵࡡࡷࡩࡸࡺࡳࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࡠࠤࡗ࡫ࡣࡦ࡫ࡹࡩࡩࠦ࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧࠫࡷ࠮ࠦࡦࡰࡴࠣࡷࡴࡳࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࡷࠥ࡯࡮ࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᚐ"))
        return bstack1l11lll1l1_opy_
    def bstack11lll11111l_opy_(self):
        if not self.bstack11ll1l1llll_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠯ࠤᚑ"))
            return None
        bstack11ll1llllll_opy_ = None
        test_files = []
        bstack11ll1ll111l_opy_ = int(time.time() * 1000) # bstack11ll1llll11_opy_ sec
        bstack11ll1lll1l1_opy_ = int(self.bstack11ll1l1llll_opy_.get(bstack11l111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᚒ"), self.bstack11lll1111l1_opy_))
        bstack11ll1ll11ll_opy_ = int(self.bstack11ll1l1llll_opy_.get(bstack11l111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚓ"), self.default_timeout)) * 1000
        bstack11ll1lll11l_opy_ = self.bstack11ll1l1llll_opy_.get(bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᚔ"), None)
        bstack11ll1lllll1_opy_ = self.bstack11ll1l1llll_opy_.get(bstack11l111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᚕ"), None)
        if bstack11ll1lllll1_opy_ is None and bstack11ll1lll11l_opy_ is None:
            return None
        try:
            while bstack11ll1lllll1_opy_ and (time.time() * 1000 - bstack11ll1ll111l_opy_) < bstack11ll1ll11ll_opy_:
                response = bstack11ll1l1l11l_opy_.bstack11ll1llll1l_opy_(bstack11ll1lllll1_opy_, {})
                if response and response.get(bstack11l111_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᚖ")):
                    bstack11ll1llllll_opy_ = response.get(bstack11l111_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚗ"))
                self.bstack11ll1l1l1l1_opy_ += 1
                if bstack11ll1llllll_opy_:
                    break
                time.sleep(bstack11ll1lll1l1_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡊࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡶࡪࡹࡵ࡭ࡶ࡙ࠣࡗࡒࠠࡢࡨࡷࡩࡷࠦࡷࡢ࡫ࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࢀࢃࠠࡴࡧࡦࡳࡳࡪࡳ࠯ࠤᚘ").format(bstack11ll1lll1l1_opy_))
            if bstack11ll1lll11l_opy_ and not bstack11ll1llllll_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡯࡭ࡦࡱࡸࡸ࡛ࠥࡒࡍࠤᚙ"))
                response = bstack11ll1l1l11l_opy_.bstack11ll1llll1l_opy_(bstack11ll1lll11l_opy_, {})
                if response and response.get(bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᚚ")):
                    bstack11ll1llllll_opy_ = response.get(bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦ᚛"))
            if bstack11ll1llllll_opy_ and len(bstack11ll1llllll_opy_) > 0:
                for bstack1ll1l1l1_opy_ in bstack11ll1llllll_opy_:
                    file_path = bstack1ll1l1l1_opy_.get(bstack11l111_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣ᚜"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1llllll_opy_:
                return None
            self.logger.debug(bstack11l111_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡑࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡲࡦࡥࡨ࡭ࡻ࡫ࡤ࠻ࠢࡾࢁࠧ᚝").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧ᚞").format(e))
            return None
    def bstack11ll1lll111_opy_(self):
        bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡥࡤࡰࡱࡹࠠ࡮ࡣࡧࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥ᚟")
        return self.bstack11ll1l1l1l1_opy_
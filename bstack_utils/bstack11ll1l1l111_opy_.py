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
import time
from bstack_utils.bstack11ll1l11l1l_opy_ import bstack11ll1l1l1l1_opy_
from bstack_utils.constants import bstack11ll1l1lll1_opy_
from bstack_utils.helper import get_host_info, bstack11ll1ll1111_opy_
class bstack11ll1l1111l_opy_:
    bstack11l1111_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍࡧ࡮ࡥ࡮ࡨࡷࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡳࡦࡴࡹࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᙷ")
    def __init__(self, config, logger):
        bstack11l1111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡨ࡮ࡩࡴ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡠࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࡸࡺࡲ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤࡳࡧ࡭ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙸ")
        self.config = config
        self.logger = logger
        self.bstack11ll1lll1l1_opy_ = bstack11l1111_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡵࡲࡩࡵ࠯ࡷࡩࡸࡺࡳࠣᙹ")
        self.bstack11ll1l1l11l_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1ll1ll1_opy_ = 5
        self.bstack11ll1l11l11_opy_ = 0
    def bstack11ll1ll11l1_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11l1111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࡩࡵ࡫ࡤࡸࡪࡹࠠࡵࡪࡨࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡶࡻࡥࡴࡶࠣࡥࡳࡪࠠࡴࡶࡲࡶࡪࡹࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡲࡲࡰࡱ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙺ")
        self.logger.debug(bstack11l1111_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨᙻ").format(orchestration_strategy))
        try:
            bstack11ll1lll111_opy_ = []
            bstack11l1111_opy_ (u"ࠤࠥࠦ࡜࡫ࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡩࡩࡹࡩࡨࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡪࡵࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡸࠦࡴࡺࡲࡨࠤࡴ࡬ࠠࡢࡴࡵࡥࡾࠦࡡ࡯ࡦࠣ࡭ࡹ࠭ࡳࠡࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡥࡷ࡫ࠠࡰࡨࠣࡸࡾࡶࡥࠡࡦ࡬ࡧࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧ࡫ࡣࡢࡷࡶࡩࠥ࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡵࡨ࠰ࠥࡻࡳࡦࡴࠣ࡬ࡦࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡰࡹࡱࡺࡩ࠮ࡴࡨࡴࡴࠦࡳࡰࡷࡵࡧࡪࠦࡷࡪࡶ࡫ࠤ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠤ࡮ࡴࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨࠢࠣᙼ")
            source = orchestration_metadata[bstack11l1111_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᙽ")].get(bstack11l1111_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᙾ"), [])
            bstack11ll1l1llll_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11l1111_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᙿ")].get(bstack11l1111_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧ "), False) and not bstack11ll1l1llll_opy_:
                bstack11ll1lll111_opy_ = bstack11ll1ll1111_opy_(source) # bstack11ll1ll1lll_opy_-repo is handled bstack11ll1l1l1ll_opy_
            payload = {
                bstack11l1111_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᚁ"): [{bstack11l1111_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᚂ"): f} for f in test_files],
                bstack11l1111_opy_ (u"ࠤࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡷࡶࡦࡺࡥࡨࡻࠥᚃ"): orchestration_strategy,
                bstack11l1111_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡐࡩࡹࡧࡤࡢࡶࡤࠦᚄ"): orchestration_metadata,
                bstack11l1111_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᚅ"): int(os.environ.get(bstack11l1111_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᚆ")) or bstack11l1111_opy_ (u"ࠨ࠰ࠣᚇ")),
                bstack11l1111_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᚈ"): int(os.environ.get(bstack11l1111_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᚉ")) or bstack11l1111_opy_ (u"ࠤ࠴ࠦᚊ")),
                bstack11l1111_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᚋ"): self.config.get(bstack11l1111_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᚌ"), bstack11l1111_opy_ (u"ࠬ࠭ᚍ")),
                bstack11l1111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᚎ"): self.config.get(bstack11l1111_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᚏ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1111_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᚐ"): os.environ.get(bstack11l1111_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᚑ"), bstack11l1111_opy_ (u"ࠥࠦᚒ")),
                bstack11l1111_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨᚓ"): get_host_info(),
                bstack11l1111_opy_ (u"ࠧࡶࡲࡅࡧࡷࡥ࡮ࡲࡳࠣᚔ"): bstack11ll1lll111_opy_
            }
            self.logger.debug(bstack11l1111_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᚕ").format(payload))
            response = bstack11ll1l1l1l1_opy_.bstack11ll1ll1l11_opy_(self.bstack11ll1lll1l1_opy_, payload)
            if response:
                self.bstack11ll1l1l11l_opy_ = self._11ll1lll11l_opy_(response)
                self.logger.debug(bstack11l1111_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᚖ").format(self.bstack11ll1l1l11l_opy_))
            else:
                self.logger.error(bstack11l1111_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣᚗ"))
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࡀࠠࡼࡿࠥᚘ").format(e))
    def _11ll1lll11l_opy_(self, response):
        bstack11l1111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡦࡴࡤࠡࡧࡻࡸࡷࡧࡣࡵࡵࠣࡶࡪࡲࡥࡷࡣࡱࡸࠥ࡬ࡩࡦ࡮ࡧࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᚙ")
        bstack1111llll1_opy_ = {}
        bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚚ")] = response.get(bstack11l1111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨ᚛"), self.default_timeout)
        bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣ᚜")] = response.get(bstack11l1111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤ᚝"), self.bstack11ll1ll1ll1_opy_)
        bstack11ll1ll111l_opy_ = response.get(bstack11l1111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ᚞"))
        bstack11ll1l1ll11_opy_ = response.get(bstack11l1111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨ᚟"))
        if bstack11ll1ll111l_opy_:
            bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᚠ")] = bstack11ll1ll111l_opy_.split(bstack11ll1l1lll1_opy_ + bstack11l1111_opy_ (u"ࠦ࠴ࠨᚡ"))[1] if bstack11ll1l1lll1_opy_ + bstack11l1111_opy_ (u"ࠧ࠵ࠢᚢ") in bstack11ll1ll111l_opy_ else bstack11ll1ll111l_opy_
        else:
            bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᚣ")] = None
        if bstack11ll1l1ll11_opy_:
            bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚤ")] = bstack11ll1l1ll11_opy_.split(bstack11ll1l1lll1_opy_ + bstack11l1111_opy_ (u"ࠣ࠱ࠥᚥ"))[1] if bstack11ll1l1lll1_opy_ + bstack11l1111_opy_ (u"ࠤ࠲ࠦᚦ") in bstack11ll1l1ll11_opy_ else bstack11ll1l1ll11_opy_
        else:
            bstack1111llll1_opy_[bstack11l1111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᚧ")] = None
        if (
            response.get(bstack11l1111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚨ")) is None or
            response.get(bstack11l1111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᚩ")) is None or
            response.get(bstack11l1111_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚪ")) is None or
            response.get(bstack11l1111_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚫ")) is None
        ):
            self.logger.debug(bstack11l1111_opy_ (u"ࠣ࡝ࡳࡶࡴࡩࡥࡴࡵࡢࡷࡵࡲࡩࡵࡡࡷࡩࡸࡺࡳࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࡠࠤࡗ࡫ࡣࡦ࡫ࡹࡩࡩࠦ࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧࠫࡷ࠮ࠦࡦࡰࡴࠣࡷࡴࡳࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࡷࠥ࡯࡮ࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᚬ"))
        return bstack1111llll1_opy_
    def bstack11ll1ll11ll_opy_(self):
        if not self.bstack11ll1l1l11l_opy_:
            self.logger.error(bstack11l1111_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠯ࠤᚭ"))
            return None
        bstack11ll1l111ll_opy_ = None
        test_files = []
        bstack11ll1l11ll1_opy_ = int(time.time() * 1000) # bstack11ll1l11111_opy_ sec
        bstack11ll1ll1l1l_opy_ = int(self.bstack11ll1l1l11l_opy_.get(bstack11l1111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᚮ"), self.bstack11ll1ll1ll1_opy_))
        bstack11ll1l1ll1l_opy_ = int(self.bstack11ll1l1l11l_opy_.get(bstack11l1111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᚯ"), self.default_timeout)) * 1000
        bstack11ll1l1ll11_opy_ = self.bstack11ll1l1l11l_opy_.get(bstack11l1111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᚰ"), None)
        bstack11ll1ll111l_opy_ = self.bstack11ll1l1l11l_opy_.get(bstack11l1111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᚱ"), None)
        if bstack11ll1ll111l_opy_ is None and bstack11ll1l1ll11_opy_ is None:
            return None
        try:
            while bstack11ll1ll111l_opy_ and (time.time() * 1000 - bstack11ll1l11ll1_opy_) < bstack11ll1l1ll1l_opy_:
                response = bstack11ll1l1l1l1_opy_.bstack11ll1l111l1_opy_(bstack11ll1ll111l_opy_, {})
                if response and response.get(bstack11l1111_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᚲ")):
                    bstack11ll1l111ll_opy_ = response.get(bstack11l1111_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚳ"))
                self.bstack11ll1l11l11_opy_ += 1
                if bstack11ll1l111ll_opy_:
                    break
                time.sleep(bstack11ll1ll1l1l_opy_)
                self.logger.debug(bstack11l1111_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡊࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡶࡪࡹࡵ࡭ࡶ࡙ࠣࡗࡒࠠࡢࡨࡷࡩࡷࠦࡷࡢ࡫ࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࢀࢃࠠࡴࡧࡦࡳࡳࡪࡳ࠯ࠤᚴ").format(bstack11ll1ll1l1l_opy_))
            if bstack11ll1l1ll11_opy_ and not bstack11ll1l111ll_opy_:
                self.logger.debug(bstack11l1111_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡯࡭ࡦࡱࡸࡸ࡛ࠥࡒࡍࠤᚵ"))
                response = bstack11ll1l1l1l1_opy_.bstack11ll1l111l1_opy_(bstack11ll1l1ll11_opy_, {})
                if response and response.get(bstack11l1111_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᚶ")):
                    bstack11ll1l111ll_opy_ = response.get(bstack11l1111_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᚷ"))
            if bstack11ll1l111ll_opy_ and len(bstack11ll1l111ll_opy_) > 0:
                for bstack1llll1ll_opy_ in bstack11ll1l111ll_opy_:
                    file_path = bstack1llll1ll_opy_.get(bstack11l1111_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣᚸ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1l111ll_opy_:
                return None
            self.logger.debug(bstack11l1111_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡑࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡲࡦࡥࡨ࡭ࡻ࡫ࡤ࠻ࠢࡾࢁࠧᚹ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l1111_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧᚺ").format(e))
            return None
    def bstack11ll1l11lll_opy_(self):
        bstack11l1111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡥࡤࡰࡱࡹࠠ࡮ࡣࡧࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᚻ")
        return self.bstack11ll1l11l11_opy_
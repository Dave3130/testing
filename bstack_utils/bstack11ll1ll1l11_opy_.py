# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import time
from bstack_utils.bstack11ll1ll11ll_opy_ import bstack11ll1l111l1_opy_
from bstack_utils.constants import bstack11ll1l1llll_opy_
from bstack_utils.helper import get_host_info, bstack11ll1l1ll11_opy_
class bstack11ll1l11l11_opy_:
    bstack11ll1ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡡ࡯ࡦ࡯ࡩࡸࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡴࡧࡵࡺࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᙸ")
    def __init__(self, config, logger):
        bstack11ll1ll_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࡩ࡯ࡣࡵ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡡࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࡹࡴࡳ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥࡴࡡ࡮ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙹ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1lll_opy_ = bstack11ll1ll_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡶ࡬ࡪࡶ࠰ࡸࡪࡹࡴࡴࠤᙺ")
        self.bstack11ll1l1l1l1_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1lll1l1_opy_ = 5
        self.bstack11ll1l11lll_opy_ = 0
    def bstack11ll1lll111_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11ll1ll_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡷࡵࡦࡵࡷࠤࡦࡴࡤࠡࡵࡷࡳࡷ࡫ࡳࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡳࡳࡱࡲࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙻ")
        self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫ࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢᙼ").format(orchestration_strategy))
        try:
            bstack11ll1l1l1ll_opy_ = []
            bstack11ll1ll_opy_ (u"ࠥࠦࠧ࡝ࡥࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡪࡪࡺࡣࡩࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡ࡫ࡶࠤࡸࡵࡵࡳࡥࡨࠤ࡮ࡹࠠࡵࡻࡳࡩࠥࡵࡦࠡࡣࡵࡶࡦࡿࠠࡢࡰࡧࠤ࡮ࡺࠧࡴࠢࡨࡰࡪࡳࡥ࡯ࡶࡶࠤࡦࡸࡥࠡࡱࡩࠤࡹࡿࡰࡦࠢࡧ࡭ࡨࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡥࡤࡣࡸࡷࡪࠦࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡶࡩ࠱ࠦࡵࡴࡧࡵࠤ࡭ࡧࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡱࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡴࡱࡸࡶࡨ࡫ࠠࡸ࡫ࡷ࡬ࠥ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠥ࡯࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢࠣࠤᙽ")
            source = orchestration_metadata[bstack11ll1ll_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᙾ")].get(bstack11ll1ll_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᙿ"), [])
            bstack11ll1l111ll_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11ll1ll_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬ ")].get(bstack11ll1ll_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᚁ"), False) and not bstack11ll1l111ll_opy_:
                bstack11ll1l1l1ll_opy_ = bstack11ll1l1ll11_opy_(source) # bstack11ll1l1111l_opy_-repo is handled bstack11ll1lll11l_opy_
            payload = {
                bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚂ"): [{bstack11ll1ll_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᚃ"): f} for f in test_files],
                bstack11ll1ll_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡸࡷࡧࡴࡦࡩࡼࠦᚄ"): orchestration_strategy,
                bstack11ll1ll_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡑࡪࡺࡡࡥࡣࡷࡥࠧᚅ"): orchestration_metadata,
                bstack11ll1ll_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣᚆ"): int(os.environ.get(bstack11ll1ll_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᚇ")) or bstack11ll1ll_opy_ (u"ࠢ࠱ࠤᚈ")),
                bstack11ll1ll_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧᚉ"): int(os.environ.get(bstack11ll1ll_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᚊ")) or bstack11ll1ll_opy_ (u"ࠥ࠵ࠧᚋ")),
                bstack11ll1ll_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᚌ"): self.config.get(bstack11ll1ll_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᚍ"), bstack11ll1ll_opy_ (u"࠭ࠧᚎ")),
                bstack11ll1ll_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᚏ"): self.config.get(bstack11ll1ll_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᚐ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11ll1ll_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᚑ"): os.environ.get(bstack11ll1ll_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᚒ"), bstack11ll1ll_opy_ (u"ࠦࠧᚓ")),
                bstack11ll1ll_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᚔ"): get_host_info(),
                bstack11ll1ll_opy_ (u"ࠨࡰࡳࡆࡨࡸࡦ࡯࡬ࡴࠤᚕ"): bstack11ll1l1l1ll_opy_
            }
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᚖ").format(payload))
            response = bstack11ll1l111l1_opy_.bstack11ll1ll1ll1_opy_(self.bstack11ll1ll1lll_opy_, payload)
            if response:
                self.bstack11ll1l1l1l1_opy_ = self._11ll1l11ll1_opy_(response)
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᚗ").format(self.bstack11ll1l1l1l1_opy_))
            else:
                self.logger.error(bstack11ll1ll_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤᚘ"))
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀ࠺ࠡࡽࢀࠦᚙ").format(e))
    def _11ll1l11ll1_opy_(self, response):
        bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡧ࡮ࡥࠢࡨࡼࡹࡸࡡࡤࡶࡶࠤࡷ࡫࡬ࡦࡸࡤࡲࡹࠦࡦࡪࡧ࡯ࡨࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᚚ")
        bstack1111l11111_opy_ = {}
        bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨ᚛")] = response.get(bstack11ll1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢ᚜"), self.default_timeout)
        bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤ᚝")] = response.get(bstack11ll1ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥ᚞"), self.bstack11ll1lll1l1_opy_)
        bstack11ll1ll11l1_opy_ = response.get(bstack11ll1ll_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧ᚟"))
        bstack11ll1l11l1l_opy_ = response.get(bstack11ll1ll_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᚠ"))
        if bstack11ll1ll11l1_opy_:
            bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᚡ")] = bstack11ll1ll11l1_opy_.split(bstack11ll1l1llll_opy_ + bstack11ll1ll_opy_ (u"ࠧ࠵ࠢᚢ"))[1] if bstack11ll1l1llll_opy_ + bstack11ll1ll_opy_ (u"ࠨ࠯ࠣᚣ") in bstack11ll1ll11l1_opy_ else bstack11ll1ll11l1_opy_
        else:
            bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚤ")] = None
        if bstack11ll1l11l1l_opy_:
            bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚥ")] = bstack11ll1l11l1l_opy_.split(bstack11ll1l1llll_opy_ + bstack11ll1ll_opy_ (u"ࠤ࠲ࠦᚦ"))[1] if bstack11ll1l1llll_opy_ + bstack11ll1ll_opy_ (u"ࠥ࠳ࠧᚧ") in bstack11ll1l11l1l_opy_ else bstack11ll1l11l1l_opy_
        else:
            bstack1111l11111_opy_[bstack11ll1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᚨ")] = None
        if (
            response.get(bstack11ll1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᚩ")) is None or
            response.get(bstack11ll1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᚪ")) is None or
            response.get(bstack11ll1ll_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚫ")) is None or
            response.get(bstack11ll1ll_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚬ")) is None
        ):
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠤ࡞ࡴࡷࡵࡣࡦࡵࡶࡣࡸࡶ࡬ࡪࡶࡢࡸࡪࡹࡴࡴࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࡡࠥࡘࡥࡤࡧ࡬ࡺࡪࡪࠠ࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨࠬࡸ࠯ࠠࡧࡱࡵࠤࡸࡵ࡭ࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࡸࠦࡩ࡯ࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨᚭ"))
        return bstack1111l11111_opy_
    def bstack11ll1l1l11l_opy_(self):
        if not self.bstack11ll1l1l1l1_opy_:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠰ࠥᚮ"))
            return None
        bstack11ll1l1ll1l_opy_ = None
        test_files = []
        bstack11ll1l1l111_opy_ = int(time.time() * 1000) # bstack11ll1l11111_opy_ sec
        bstack11ll1ll1111_opy_ = int(self.bstack11ll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᚯ"), self.bstack11ll1lll1l1_opy_))
        bstack11ll1l1lll1_opy_ = int(self.bstack11ll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᚰ"), self.default_timeout)) * 1000
        bstack11ll1l11l1l_opy_ = self.bstack11ll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚱ"), None)
        bstack11ll1ll11l1_opy_ = self.bstack11ll1l1l1l1_opy_.get(bstack11ll1ll_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚲ"), None)
        if bstack11ll1ll11l1_opy_ is None and bstack11ll1l11l1l_opy_ is None:
            return None
        try:
            while bstack11ll1ll11l1_opy_ and (time.time() * 1000 - bstack11ll1l1l111_opy_) < bstack11ll1l1lll1_opy_:
                response = bstack11ll1l111l1_opy_.bstack11ll1ll111l_opy_(bstack11ll1ll11l1_opy_, {})
                if response and response.get(bstack11ll1ll_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚳ")):
                    bstack11ll1l1ll1l_opy_ = response.get(bstack11ll1ll_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚴ"))
                self.bstack11ll1l11lll_opy_ += 1
                if bstack11ll1l1ll1l_opy_:
                    break
                time.sleep(bstack11ll1ll1111_opy_)
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡚ࡘࡌࠡࡣࡩࡸࡪࡸࠠࡸࡣ࡬ࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࢁࡽࠡࡵࡨࡧࡴࡴࡤࡴ࠰ࠥᚵ").format(bstack11ll1ll1111_opy_))
            if bstack11ll1l11l1l_opy_ and not bstack11ll1l1ll1l_opy_:
                self.logger.debug(bstack11ll1ll_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡺࡩ࡮ࡧࡲࡹࡹࠦࡕࡓࡎࠥᚶ"))
                response = bstack11ll1l111l1_opy_.bstack11ll1ll111l_opy_(bstack11ll1l11l1l_opy_, {})
                if response and response.get(bstack11ll1ll_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᚷ")):
                    bstack11ll1l1ll1l_opy_ = response.get(bstack11ll1ll_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚸ"))
            if bstack11ll1l1ll1l_opy_ and len(bstack11ll1l1ll1l_opy_) > 0:
                for bstack1lll1l11_opy_ in bstack11ll1l1ll1l_opy_:
                    file_path = bstack1lll1l11_opy_.get(bstack11ll1ll_opy_ (u"ࠢࡧ࡫࡯ࡩࡕࡧࡴࡩࠤᚹ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1l1ll1l_opy_:
                return None
            self.logger.debug(bstack11ll1ll_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡒࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡳࡧࡦࡩ࡮ࡼࡥࡥ࠼ࠣࡿࢂࠨᚺ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11ll1ll_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨᚻ").format(e))
            return None
    def bstack11ll1ll1l1l_opy_(self):
        bstack11ll1ll_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡦࡥࡱࡲࡳࠡ࡯ࡤࡨࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᚼ")
        return self.bstack11ll1l11lll_opy_
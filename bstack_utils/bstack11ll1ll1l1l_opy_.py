# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import os
import time
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
from bstack_utils.constants import bstack11ll1llll1l_opy_
from bstack_utils.helper import get_host_info, bstack11ll1l1l111_opy_
class bstack11ll1l1l11l_opy_:
    bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡡ࡯ࡦ࡯ࡩࡸࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡴࡧࡵࡺࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᙕ")
    def __init__(self, config, logger):
        bstack11l1l11_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࡩ࡯ࡣࡵ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡡࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࡹࡴࡳ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥࡴࡡ࡮ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙖ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1111_opy_ = bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡶ࡬ࡪࡶ࠰ࡸࡪࡹࡴࡴࠤᙗ")
        self.bstack11ll1lll1l1_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1lll111_opy_ = 5
        self.bstack11ll1ll1lll_opy_ = 0
    def bstack11ll1ll1l11_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11l1l11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡷࡵࡦࡵࡷࠤࡦࡴࡤࠡࡵࡷࡳࡷ࡫ࡳࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡳࡳࡱࡲࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙘ")
        self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫ࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢᙙ").format(orchestration_strategy))
        try:
            bstack11ll1l1lll1_opy_ = []
            bstack11l1l11_opy_ (u"ࠥࠦࠧ࡝ࡥࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡪࡪࡺࡣࡩࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡ࡫ࡶࠤࡸࡵࡵࡳࡥࡨࠤ࡮ࡹࠠࡵࡻࡳࡩࠥࡵࡦࠡࡣࡵࡶࡦࡿࠠࡢࡰࡧࠤ࡮ࡺࠧࡴࠢࡨࡰࡪࡳࡥ࡯ࡶࡶࠤࡦࡸࡥࠡࡱࡩࠤࡹࡿࡰࡦࠢࡧ࡭ࡨࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡥࡤࡣࡸࡷࡪࠦࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡶࡩ࠱ࠦࡵࡴࡧࡵࠤ࡭ࡧࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡱࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡴࡱࡸࡶࡨ࡫ࠠࡸ࡫ࡷ࡬ࠥ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠥ࡯࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢࠣࠤᙚ")
            source = orchestration_metadata[bstack11l1l11_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᙛ")].get(bstack11l1l11_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᙜ"), [])
            bstack11ll1lll1ll_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11l1l11_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᙝ")].get(bstack11l1l11_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᙞ"), False) and not bstack11ll1lll1ll_opy_:
                bstack11ll1l1lll1_opy_ = bstack11ll1l1l111_opy_(source) # bstack11ll1l11lll_opy_-repo is handled bstack11lll11111l_opy_
            payload = {
                bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙟ"): [{bstack11l1l11_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᙠ"): f} for f in test_files],
                bstack11l1l11_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡸࡷࡧࡴࡦࡩࡼࠦᙡ"): orchestration_strategy,
                bstack11l1l11_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡑࡪࡺࡡࡥࡣࡷࡥࠧᙢ"): orchestration_metadata,
                bstack11l1l11_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣᙣ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᙤ")) or bstack11l1l11_opy_ (u"ࠢ࠱ࠤᙥ")),
                bstack11l1l11_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧᙦ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᙧ")) or bstack11l1l11_opy_ (u"ࠥ࠵ࠧᙨ")),
                bstack11l1l11_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᙩ"): self.config.get(bstack11l1l11_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᙪ"), bstack11l1l11_opy_ (u"࠭ࠧᙫ")),
                bstack11l1l11_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᙬ"): self.config.get(bstack11l1l11_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫ᙭"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1l11_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢ᙮"): os.environ.get(bstack11l1l11_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᙯ"), bstack11l1l11_opy_ (u"ࠦࠧᙰ")),
                bstack11l1l11_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᙱ"): get_host_info(),
                bstack11l1l11_opy_ (u"ࠨࡰࡳࡆࡨࡸࡦ࡯࡬ࡴࠤᙲ"): bstack11ll1l1lll1_opy_
            }
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᙳ").format(payload))
            response = bstack11ll1ll1ll1_opy_.bstack11ll1l1ll1l_opy_(self.bstack11ll1ll1111_opy_, payload)
            if response:
                self.bstack11ll1lll1l1_opy_ = self._11ll1lllll1_opy_(response)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᙴ").format(self.bstack11ll1lll1l1_opy_))
            else:
                self.logger.error(bstack11l1l11_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤᙵ"))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀ࠺ࠡࡽࢀࠦᙶ").format(e))
    def _11ll1lllll1_opy_(self, response):
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡧ࡮ࡥࠢࡨࡼࡹࡸࡡࡤࡶࡶࠤࡷ࡫࡬ࡦࡸࡤࡲࡹࠦࡦࡪࡧ࡯ࡨࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙷ")
        bstack111lll1l11_opy_ = {}
        bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙸ")] = response.get(bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙹ"), self.default_timeout)
        bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙺ")] = response.get(bstack11l1l11_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙻ"), self.bstack11ll1lll111_opy_)
        bstack11ll1l1l1ll_opy_ = response.get(bstack11l1l11_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙼ"))
        bstack11ll1llllll_opy_ = response.get(bstack11l1l11_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙽ"))
        if bstack11ll1l1l1ll_opy_:
            bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙾ")] = bstack11ll1l1l1ll_opy_.split(bstack11ll1llll1l_opy_ + bstack11l1l11_opy_ (u"ࠧ࠵ࠢᙿ"))[1] if bstack11ll1llll1l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠯ࠣ ") in bstack11ll1l1l1ll_opy_ else bstack11ll1l1l1ll_opy_
        else:
            bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚁ")] = None
        if bstack11ll1llllll_opy_:
            bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᚂ")] = bstack11ll1llllll_opy_.split(bstack11ll1llll1l_opy_ + bstack11l1l11_opy_ (u"ࠤ࠲ࠦᚃ"))[1] if bstack11ll1llll1l_opy_ + bstack11l1l11_opy_ (u"ࠥ࠳ࠧᚄ") in bstack11ll1llllll_opy_ else bstack11ll1llllll_opy_
        else:
            bstack111lll1l11_opy_[bstack11l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᚅ")] = None
        if (
            response.get(bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᚆ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᚇ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚈ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚉ")) is None
        ):
            self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞ࡴࡷࡵࡣࡦࡵࡶࡣࡸࡶ࡬ࡪࡶࡢࡸࡪࡹࡴࡴࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࡡࠥࡘࡥࡤࡧ࡬ࡺࡪࡪࠠ࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨࠬࡸ࠯ࠠࡧࡱࡵࠤࡸࡵ࡭ࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࡸࠦࡩ࡯ࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨᚊ"))
        return bstack111lll1l11_opy_
    def bstack11ll1llll11_opy_(self):
        if not self.bstack11ll1lll1l1_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠰ࠥᚋ"))
            return None
        bstack11ll1lll11l_opy_ = None
        test_files = []
        bstack11lll111111_opy_ = int(time.time() * 1000) # bstack11ll1ll11ll_opy_ sec
        bstack11ll1l1l1l1_opy_ = int(self.bstack11ll1lll1l1_opy_.get(bstack11l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᚌ"), self.bstack11ll1lll111_opy_))
        bstack11ll1l1llll_opy_ = int(self.bstack11ll1lll1l1_opy_.get(bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᚍ"), self.default_timeout)) * 1000
        bstack11ll1llllll_opy_ = self.bstack11ll1lll1l1_opy_.get(bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚎ"), None)
        bstack11ll1l1l1ll_opy_ = self.bstack11ll1lll1l1_opy_.get(bstack11l1l11_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚏ"), None)
        if bstack11ll1l1l1ll_opy_ is None and bstack11ll1llllll_opy_ is None:
            return None
        try:
            while bstack11ll1l1l1ll_opy_ and (time.time() * 1000 - bstack11lll111111_opy_) < bstack11ll1l1llll_opy_:
                response = bstack11ll1ll1ll1_opy_.bstack11ll1l1ll11_opy_(bstack11ll1l1l1ll_opy_, {})
                if response and response.get(bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚐ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack11l1l11_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚑ"))
                self.bstack11ll1ll1lll_opy_ += 1
                if bstack11ll1lll11l_opy_:
                    break
                time.sleep(bstack11ll1l1l1l1_opy_)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡚ࡘࡌࠡࡣࡩࡸࡪࡸࠠࡸࡣ࡬ࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࢁࡽࠡࡵࡨࡧࡴࡴࡤࡴ࠰ࠥᚒ").format(bstack11ll1l1l1l1_opy_))
            if bstack11ll1llllll_opy_ and not bstack11ll1lll11l_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡺࡩ࡮ࡧࡲࡹࡹࠦࡕࡓࡎࠥᚓ"))
                response = bstack11ll1ll1ll1_opy_.bstack11ll1l1ll11_opy_(bstack11ll1llllll_opy_, {})
                if response and response.get(bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᚔ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚕ"))
            if bstack11ll1lll11l_opy_ and len(bstack11ll1lll11l_opy_) > 0:
                for bstack1ll1l1l1_opy_ in bstack11ll1lll11l_opy_:
                    file_path = bstack1ll1l1l1_opy_.get(bstack11l1l11_opy_ (u"ࠢࡧ࡫࡯ࡩࡕࡧࡴࡩࠤᚖ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1lll11l_opy_:
                return None
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡒࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡳࡧࡦࡩ࡮ࡼࡥࡥ࠼ࠣࡿࢂࠨᚗ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨᚘ").format(e))
            return None
    def bstack11ll1ll111l_opy_(self):
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡦࡥࡱࡲࡳࠡ࡯ࡤࡨࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᚙ")
        return self.bstack11ll1ll1lll_opy_
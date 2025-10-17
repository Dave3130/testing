# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import time
from bstack_utils.bstack11lll111lll_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll111l11_opy_
from bstack_utils.helper import get_host_info, bstack11ll1ll11ll_opy_
class bstack11ll1lll11l_opy_:
    bstack11l111_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡋࡥࡳࡪ࡬ࡦࡵࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡻ࡮ࡺࡨࠡࡶ࡫ࡩࠥࡈࡲࡰࡹࡶࡩࡷ࡙ࡴࡢࡥ࡮ࠤࡸ࡫ࡲࡷࡧࡵ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᘨ")
    def __init__(self, config, logger):
        bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠ࠻ࡲࡤࡶࡦࡳࠠࡤࡱࡱࡪ࡮࡭࠺ࠡࡦ࡬ࡧࡹ࠲ࠠࡵࡧࡶࡸࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡩ࡯࡯ࡨ࡬࡫ࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡥࡳࡵࡴࡤࡸࡪ࡭ࡹ࠻ࠢࡶࡸࡷ࠲ࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺࠢࡱࡥࡲ࡫ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘩ")
        self.config = config
        self.logger = logger
        self.bstack11ll1lll1l1_opy_ = bstack11l111_opy_ (u"ࠦࡹ࡫ࡳࡵࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮࠰ࡣࡳ࡭࠴ࡼ࠱࠰ࡵࡳࡰ࡮ࡺ࠭ࡵࡧࡶࡸࡸࠨᘪ")
        self.bstack11ll1lllll1_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1llll1l_opy_ = 5
        self.bstack11ll1ll11l1_opy_ = 0
    def bstack11lll111l1l_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack11l111_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡌࡲ࡮ࡺࡩࡢࡶࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡴࡹࡪࡹࡴࠡࡣࡱࡨࠥࡹࡴࡰࡴࡨࡷࠥࡺࡨࡦࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡩࡧࡴࡢࠢࡩࡳࡷࠦࡰࡰ࡮࡯࡭ࡳ࡭࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᘫ")
        self.logger.debug(bstack11l111_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡯࡮ࡨࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡸ࡫ࡷ࡬ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡽࢀࠦᘬ").format(orchestration_strategy))
        try:
            bstack11lll11l1l1_opy_ = []
            bstack11l111_opy_ (u"ࠢࠣࠤ࡚ࡩࠥࡽࡩ࡭࡮ࠣࡲࡴࡺࠠࡧࡧࡷࡧ࡭ࠦࡧࡪࡶࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡯ࡳࠡࡵࡲࡹࡷࡩࡥࠡ࡫ࡶࠤࡹࡿࡰࡦࠢࡲࡪࠥࡧࡲࡳࡣࡼࠤࡦࡴࡤࠡ࡫ࡷࠫࡸࠦࡥ࡭ࡧࡰࡩࡳࡺࡳࠡࡣࡵࡩࠥࡵࡦࠡࡶࡼࡴࡪࠦࡤࡪࡥࡷࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࡥࡩࡨࡧࡵࡴࡧࠣ࡭ࡳࠦࡴࡩࡣࡷࠤࡨࡧࡳࡦ࠮ࠣࡹࡸ࡫ࡲࠡࡪࡤࡷࠥࡶࡲࡰࡸ࡬ࡨࡪࡪࠠ࡮ࡷ࡯ࡸ࡮࠳ࡲࡦࡲࡲࠤࡸࡵࡵࡳࡥࡨࠤࡼ࡯ࡴࡩࠢࡩࡩࡦࡺࡵࡳࡧࡅࡶࡦࡴࡣࡩࠢ࡬ࡲࠥࡨࡲࡰࡹࡶࡩࡷࡹࡴࡢࡥ࡮ࠦࠧࠨᘭ")
            source = orchestration_metadata[bstack11l111_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᘮ")].get(bstack11l111_opy_ (u"ࠩࡶࡳࡺࡸࡣࡦࠩᘯ"), [])
            bstack11ll1lll111_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack11l111_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᘰ")].get(bstack11l111_opy_ (u"ࠫࡪࡴࡡࡣ࡮ࡨࡨࠬᘱ"), False) and not bstack11ll1lll111_opy_:
                bstack11lll11l1l1_opy_ = bstack11ll1ll11ll_opy_(source) # bstack11ll1ll111l_opy_-repo is handled bstack11ll1ll1111_opy_
            payload = {
                bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᘲ"): [{bstack11l111_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣᘳ"): f} for f in test_files],
                bstack11l111_opy_ (u"ࠢࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡓࡵࡴࡤࡸࡪ࡭ࡹࠣᘴ"): orchestration_strategy,
                bstack11l111_opy_ (u"ࠣࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡎࡧࡷࡥࡩࡧࡴࡢࠤᘵ"): orchestration_metadata,
                bstack11l111_opy_ (u"ࠤࡱࡳࡩ࡫ࡉ࡯ࡦࡨࡼࠧᘶ"): int(os.environ.get(bstack11l111_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡑࡓࡉࡋ࡟ࡊࡐࡇࡉ࡝ࠨᘷ")) or bstack11l111_opy_ (u"ࠦ࠵ࠨᘸ")),
                bstack11l111_opy_ (u"ࠧࡺ࡯ࡵࡣ࡯ࡒࡴࡪࡥࡴࠤᘹ"): int(os.environ.get(bstack11l111_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤ࡚ࡏࡕࡃࡏࡣࡓࡕࡄࡆࡡࡆࡓ࡚ࡔࡔࠣᘺ")) or bstack11l111_opy_ (u"ࠢ࠲ࠤᘻ")),
                bstack11l111_opy_ (u"ࠣࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪࠨᘼ"): self.config.get(bstack11l111_opy_ (u"ࠩࡳࡶࡴࡰࡥࡤࡶࡑࡥࡲ࡫ࠧᘽ"), bstack11l111_opy_ (u"ࠪࠫᘾ")),
                bstack11l111_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠢᘿ"): self.config.get(bstack11l111_opy_ (u"ࠬࡨࡵࡪ࡮ࡧࡒࡦࡳࡥࠨᙀ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l111_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡗࡻ࡮ࡊࡦࡨࡲࡹ࡯ࡦࡪࡧࡵࠦᙁ"): os.environ.get(bstack11l111_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡂࡖࡋࡏࡈࡤࡘࡕࡏࡡࡌࡈࡊࡔࡔࡊࡈࡌࡉࡗࠨᙂ"), bstack11l111_opy_ (u"ࠣࠤᙃ")),
                bstack11l111_opy_ (u"ࠤ࡫ࡳࡸࡺࡉ࡯ࡨࡲࠦᙄ"): get_host_info(),
                bstack11l111_opy_ (u"ࠥࡴࡷࡊࡥࡵࡣ࡬ࡰࡸࠨᙅ"): bstack11lll11l1l1_opy_
            }
            self.logger.debug(bstack11l111_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡗࡪࡴࡤࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧᙆ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll1ll1l11_opy_(self.bstack11ll1lll1l1_opy_, payload)
            if response:
                self.bstack11ll1lllll1_opy_ = self._11lll1111l1_opy_(response)
                self.logger.debug(bstack11l111_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡘࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠾ࠥࢁࡽࠣᙇ").format(self.bstack11ll1lllll1_opy_))
            else:
                self.logger.error(bstack11l111_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡࠥࡌࡡࡪ࡮ࡨࡨࠥࡺ࡯ࠡࡩࡨࡸࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡹࡰࡰࡰࡶࡩ࠳ࠨᙈ"))
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥࡹࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽࠾ࠥࢁࡽࠣᙉ").format(e))
    def _11lll1111l1_opy_(self, response):
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡖࡲࡰࡥࡨࡷࡸ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡅࡕࡏࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡤࡲࡩࠦࡥࡹࡶࡵࡥࡨࡺࡳࠡࡴࡨࡰࡪࡼࡡ࡯ࡶࠣࡪ࡮࡫࡬ࡥࡵ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙊ")
        bstack1ll1ll11ll_opy_ = {}
        bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᙋ")] = response.get(bstack11l111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࠦᙌ"), self.default_timeout)
        bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᙍ")] = response.get(bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᙎ"), self.bstack11ll1llll1l_opy_)
        bstack11lll11l111_opy_ = response.get(bstack11l111_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙏ"))
        bstack11ll1llllll_opy_ = response.get(bstack11l111_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙐ"))
        if bstack11lll11l111_opy_:
            bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᙑ")] = bstack11lll11l111_opy_.split(bstack11lll111l11_opy_ + bstack11l111_opy_ (u"ࠤ࠲ࠦᙒ"))[1] if bstack11lll111l11_opy_ + bstack11l111_opy_ (u"ࠥ࠳ࠧᙓ") in bstack11lll11l111_opy_ else bstack11lll11l111_opy_
        else:
            bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙔ")] = None
        if bstack11ll1llllll_opy_:
            bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙕ")] = bstack11ll1llllll_opy_.split(bstack11lll111l11_opy_ + bstack11l111_opy_ (u"ࠨ࠯ࠣᙖ"))[1] if bstack11lll111l11_opy_ + bstack11l111_opy_ (u"ࠢ࠰ࠤᙗ") in bstack11ll1llllll_opy_ else bstack11ll1llllll_opy_
        else:
            bstack1ll1ll11ll_opy_[bstack11l111_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᙘ")] = None
        if (
            response.get(bstack11l111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᙙ")) is None or
            response.get(bstack11l111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙚ")) is None or
            response.get(bstack11l111_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙛ")) is None or
            response.get(bstack11l111_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᙜ")) is None
        ):
            self.logger.debug(bstack11l111_opy_ (u"ࠨ࡛ࡱࡴࡲࡧࡪࡹࡳࡠࡵࡳࡰ࡮ࡺ࡟ࡵࡧࡶࡸࡸࡥࡲࡦࡵࡳࡳࡳࡹࡥ࡞ࠢࡕࡩࡨ࡫ࡩࡷࡧࡧࠤࡳࡻ࡬࡭ࠢࡹࡥࡱࡻࡥࠩࡵࠬࠤ࡫ࡵࡲࠡࡵࡲࡱࡪࠦࡡࡵࡶࡵ࡭ࡧࡻࡴࡦࡵࠣ࡭ࡳࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠥᙝ"))
        return bstack1ll1ll11ll_opy_
    def bstack11ll1ll1lll_opy_(self):
        if not self.bstack11ll1lllll1_opy_:
            self.logger.error(bstack11l111_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡐࡲࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡪࡡࡵࡣࠣࡥࡻࡧࡩ࡭ࡣࡥࡰࡪࠦࡴࡰࠢࡩࡩࡹࡩࡨࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸ࠴ࠢᙞ"))
            return None
        bstack11lll11l11l_opy_ = None
        test_files = []
        bstack11ll1lll1ll_opy_ = int(time.time() * 1000) # bstack11lll1111ll_opy_ sec
        bstack11lll111ll1_opy_ = int(self.bstack11ll1lllll1_opy_.get(bstack11l111_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙟ"), self.bstack11ll1llll1l_opy_))
        bstack11ll1ll1ll1_opy_ = int(self.bstack11ll1lllll1_opy_.get(bstack11l111_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᙠ"), self.default_timeout)) * 1000
        bstack11ll1llllll_opy_ = self.bstack11ll1lllll1_opy_.get(bstack11l111_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙡ"), None)
        bstack11lll11l111_opy_ = self.bstack11ll1lllll1_opy_.get(bstack11l111_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙢ"), None)
        if bstack11lll11l111_opy_ is None and bstack11ll1llllll_opy_ is None:
            return None
        try:
            while bstack11lll11l111_opy_ and (time.time() * 1000 - bstack11ll1lll1ll_opy_) < bstack11ll1ll1ll1_opy_:
                response = bstack11lll111111_opy_.bstack11lll11111l_opy_(bstack11lll11l111_opy_, {})
                if response and response.get(bstack11l111_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙣ")):
                    bstack11lll11l11l_opy_ = response.get(bstack11l111_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᙤ"))
                self.bstack11ll1ll11l1_opy_ += 1
                if bstack11lll11l11l_opy_:
                    break
                time.sleep(bstack11lll111ll1_opy_)
                self.logger.debug(bstack11l111_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡈࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡪࡷࡵ࡭ࠡࡴࡨࡷࡺࡲࡴࠡࡗࡕࡐࠥࡧࡦࡵࡧࡵࠤࡼࡧࡩࡵ࡫ࡱ࡫ࠥ࡬࡯ࡳࠢࡾࢁࠥࡹࡥࡤࡱࡱࡨࡸ࠴ࠢᙥ").format(bstack11lll111ll1_opy_))
            if bstack11ll1llllll_opy_ and not bstack11lll11l11l_opy_:
                self.logger.debug(bstack11l111_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡉࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࡶࠤ࡫ࡸ࡯࡮ࠢࡷ࡭ࡲ࡫࡯ࡶࡶ࡙ࠣࡗࡒࠢᙦ"))
                response = bstack11lll111111_opy_.bstack11lll11111l_opy_(bstack11ll1llllll_opy_, {})
                if response and response.get(bstack11l111_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᙧ")):
                    bstack11lll11l11l_opy_ = response.get(bstack11l111_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᙨ"))
            if bstack11lll11l11l_opy_ and len(bstack11lll11l11l_opy_) > 0:
                for bstack1l111lll_opy_ in bstack11lll11l11l_opy_:
                    file_path = bstack1l111lll_opy_.get(bstack11l111_opy_ (u"ࠦ࡫࡯࡬ࡦࡒࡤࡸ࡭ࠨᙩ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11lll11l11l_opy_:
                return None
            self.logger.debug(bstack11l111_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡏࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶࠤࡷ࡫ࡣࡦ࡫ࡹࡩࡩࡀࠠࡼࡿࠥᙪ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l111_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣ࡭ࡳࠦࡦࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀࠠࡼࡿࠥᙫ").format(e))
            return None
    def bstack11ll1ll1l1l_opy_(self):
        bstack11l111_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡗ࡫ࡴࡶࡴࡱࡷࠥࡺࡨࡦࠢࡦࡳࡺࡴࡴࠡࡱࡩࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡄࡔࡎࠦࡣࡢ࡮࡯ࡷࠥࡳࡡࡥࡧ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙬ")
        return self.bstack11ll1ll11l1_opy_
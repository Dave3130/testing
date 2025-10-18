# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import time
from bstack_utils.bstack11ll1ll1l11_opy_ import bstack11ll1llll1l_opy_
from bstack_utils.constants import bstack11ll1llllll_opy_
from bstack_utils.helper import get_host_info, bstack11lll11l11l_opy_
class bstack11ll1ll111l_opy_:
    bstack1l1lll1_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡣࡱࡨࡱ࡫ࡳࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡶࡩࡷࡼࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᘴ")
    def __init__(self, config, logger):
        bstack1l1lll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡤࡪࡥࡷ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡣࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡴࡶࡵ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠ࡯ࡣࡰࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᘵ")
        self.config = config
        self.logger = logger
        self.bstack11lll111111_opy_ = bstack1l1lll1_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡱ࡮࡬ࡸ࠲ࡺࡥࡴࡶࡶࠦᘶ")
        self.bstack11ll1ll11l1_opy_ = None
        self.default_timeout = 60
        self.bstack11lll111ll1_opy_ = 5
        self.bstack11lll11111l_opy_ = 0
    def bstack11lll111l11_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1l1lll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡲࡷࡨࡷࡹࠦࡡ࡯ࡦࠣࡷࡹࡵࡲࡦࡵࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡵࡵ࡬࡭࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᘷ")
        self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤᘸ").format(orchestration_strategy))
        try:
            bstack11ll1llll11_opy_ = []
            bstack1l1lll1_opy_ (u"ࠧࠨࠢࡘࡧࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥ࡬ࡥࡵࡥ࡫ࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣ࡭ࡸࠦࡳࡰࡷࡵࡧࡪࠦࡩࡴࠢࡷࡽࡵ࡫ࠠࡰࡨࠣࡥࡷࡸࡡࡺࠢࡤࡲࡩࠦࡩࡵࠩࡶࠤࡪࡲࡥ࡮ࡧࡱࡸࡸࠦࡡࡳࡧࠣࡳ࡫ࠦࡴࡺࡲࡨࠤࡩ࡯ࡣࡵࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡧࡦࡥࡺࡹࡥࠡ࡫ࡱࠤࡹ࡮ࡡࡵࠢࡦࡥࡸ࡫ࠬࠡࡷࡶࡩࡷࠦࡨࡢࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥࡳࡵ࡭ࡶ࡬࠱ࡷ࡫ࡰࡰࠢࡶࡳࡺࡸࡣࡦࠢࡺ࡭ࡹ࡮ࠠࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠠࡪࡰࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤࠥࠦᘹ")
            source = orchestration_metadata[bstack1l1lll1_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᘺ")].get(bstack1l1lll1_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᘻ"), [])
            bstack11lll11l111_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1l1lll1_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᘼ")].get(bstack1l1lll1_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᘽ"), False) and not bstack11lll11l111_opy_:
                bstack11ll1llll11_opy_ = bstack11lll11l11l_opy_(source) # bstack11lll1111ll_opy_-repo is handled bstack11ll1ll1lll_opy_
            payload = {
                bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᘾ"): [{bstack1l1lll1_opy_ (u"ࠦ࡫࡯࡬ࡦࡒࡤࡸ࡭ࠨᘿ"): f} for f in test_files],
                bstack1l1lll1_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡘࡺࡲࡢࡶࡨ࡫ࡾࠨᙀ"): orchestration_strategy,
                bstack1l1lll1_opy_ (u"ࠨ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡓࡥࡵࡣࡧࡥࡹࡧࠢᙁ"): orchestration_metadata,
                bstack1l1lll1_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥᙂ"): int(os.environ.get(bstack1l1lll1_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᙃ")) or bstack1l1lll1_opy_ (u"ࠤ࠳ࠦᙄ")),
                bstack1l1lll1_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢᙅ"): int(os.environ.get(bstack1l1lll1_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨᙆ")) or bstack1l1lll1_opy_ (u"ࠧ࠷ࠢᙇ")),
                bstack1l1lll1_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦᙈ"): self.config.get(bstack1l1lll1_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᙉ"), bstack1l1lll1_opy_ (u"ࠨࠩᙊ")),
                bstack1l1lll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᙋ"): self.config.get(bstack1l1lll1_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᙌ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l1lll1_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤᙍ"): os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᙎ"), bstack1l1lll1_opy_ (u"ࠨࠢᙏ")),
                bstack1l1lll1_opy_ (u"ࠢࡩࡱࡶࡸࡎࡴࡦࡰࠤᙐ"): get_host_info(),
                bstack1l1lll1_opy_ (u"ࠣࡲࡵࡈࡪࡺࡡࡪ࡮ࡶࠦᙑ"): bstack11ll1llll11_opy_
            }
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀࠠࡼࡿࠥᙒ").format(payload))
            response = bstack11ll1llll1l_opy_.bstack11ll1lll11l_opy_(self.bstack11lll111111_opy_, payload)
            if response:
                self.bstack11ll1ll11l1_opy_ = self._11ll1ll1l1l_opy_(response)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡖࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᙓ").format(self.bstack11ll1ll11l1_opy_))
            else:
                self.logger.error(bstack1l1lll1_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠱ࠦᙔ"))
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡴࡤࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻࠼ࠣࡿࢂࠨᙕ").format(e))
    def _11ll1ll1l1l_opy_(self, response):
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡷࡵࡣࡦࡵࡶࡩࡸࠦࡴࡩࡧࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡢࡰࡧࠤࡪࡾࡴࡳࡣࡦࡸࡸࠦࡲࡦ࡮ࡨࡺࡦࡴࡴࠡࡨ࡬ࡩࡱࡪࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙖ")
        bstack11ll11111l_opy_ = {}
        bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙗ")] = response.get(bstack1l1lll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤᙘ"), self.default_timeout)
        bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᙙ")] = response.get(bstack1l1lll1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙚ"), self.bstack11lll111ll1_opy_)
        bstack11ll1ll11ll_opy_ = response.get(bstack1l1lll1_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙛ"))
        bstack11ll1lll111_opy_ = response.get(bstack1l1lll1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙜ"))
        if bstack11ll1ll11ll_opy_:
            bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙝ")] = bstack11ll1ll11ll_opy_.split(bstack11ll1llllll_opy_ + bstack1l1lll1_opy_ (u"ࠢ࠰ࠤᙞ"))[1] if bstack11ll1llllll_opy_ + bstack1l1lll1_opy_ (u"ࠣ࠱ࠥᙟ") in bstack11ll1ll11ll_opy_ else bstack11ll1ll11ll_opy_
        else:
            bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙠ")] = None
        if bstack11ll1lll111_opy_:
            bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙡ")] = bstack11ll1lll111_opy_.split(bstack11ll1llllll_opy_ + bstack1l1lll1_opy_ (u"ࠦ࠴ࠨᙢ"))[1] if bstack11ll1llllll_opy_ + bstack1l1lll1_opy_ (u"ࠧ࠵ࠢᙣ") in bstack11ll1lll111_opy_ else bstack11ll1lll111_opy_
        else:
            bstack11ll11111l_opy_[bstack1l1lll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙤ")] = None
        if (
            response.get(bstack1l1lll1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙥ")) is None or
            response.get(bstack1l1lll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙦ")) is None or
            response.get(bstack1l1lll1_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᙧ")) is None or
            response.get(bstack1l1lll1_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙨ")) is None
        ):
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠦࡠࡶࡲࡰࡥࡨࡷࡸࡥࡳࡱ࡮࡬ࡸࡤࡺࡥࡴࡶࡶࡣࡷ࡫ࡳࡱࡱࡱࡷࡪࡣࠠࡓࡧࡦࡩ࡮ࡼࡥࡥࠢࡱࡹࡱࡲࠠࡷࡣ࡯ࡹࡪ࠮ࡳࠪࠢࡩࡳࡷࠦࡳࡰ࡯ࡨࠤࡦࡺࡴࡳ࡫ࡥࡹࡹ࡫ࡳࠡ࡫ࡱࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡄࡔࡎࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣᙩ"))
        return bstack11ll11111l_opy_
    def bstack11ll1lllll1_opy_(self):
        if not self.bstack11ll1ll11l1_opy_:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡎࡰࠢࡵࡩࡶࡻࡥࡴࡶࠣࡨࡦࡺࡡࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠲ࠧᙪ"))
            return None
        bstack11lll1111l1_opy_ = None
        test_files = []
        bstack11lll111l1l_opy_ = int(time.time() * 1000) # bstack11lll11l1l1_opy_ sec
        bstack11lll111lll_opy_ = int(self.bstack11ll1ll11l1_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᙫ"), self.bstack11lll111ll1_opy_))
        bstack11ll1ll1ll1_opy_ = int(self.bstack11ll1ll11l1_opy_.get(bstack1l1lll1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙬ"), self.default_timeout)) * 1000
        bstack11ll1lll111_opy_ = self.bstack11ll1ll11l1_opy_.get(bstack1l1lll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧ᙭"), None)
        bstack11ll1ll11ll_opy_ = self.bstack11ll1ll11l1_opy_.get(bstack1l1lll1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧ᙮"), None)
        if bstack11ll1ll11ll_opy_ is None and bstack11ll1lll111_opy_ is None:
            return None
        try:
            while bstack11ll1ll11ll_opy_ and (time.time() * 1000 - bstack11lll111l1l_opy_) < bstack11ll1ll1ll1_opy_:
                response = bstack11ll1llll1l_opy_.bstack11ll1lll1ll_opy_(bstack11ll1ll11ll_opy_, {})
                if response and response.get(bstack1l1lll1_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᙯ")):
                    bstack11lll1111l1_opy_ = response.get(bstack1l1lll1_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᙰ"))
                self.bstack11lll11111l_opy_ += 1
                if bstack11lll1111l1_opy_:
                    break
                time.sleep(bstack11lll111lll_opy_)
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡲࡦࡵࡸࡰࡹࠦࡕࡓࡎࠣࡥ࡫ࡺࡥࡳࠢࡺࡥ࡮ࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡼࡿࠣࡷࡪࡩ࡯࡯ࡦࡶ࠲ࠧᙱ").format(bstack11lll111lll_opy_))
            if bstack11ll1lll111_opy_ and not bstack11lll1111l1_opy_:
                self.logger.debug(bstack1l1lll1_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡇࡧࡷࡧ࡭࡯࡮ࡨࠢࡲࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࡴࠢࡩࡶࡴࡳࠠࡵ࡫ࡰࡩࡴࡻࡴࠡࡗࡕࡐࠧᙲ"))
                response = bstack11ll1llll1l_opy_.bstack11ll1lll1ll_opy_(bstack11ll1lll111_opy_, {})
                if response and response.get(bstack1l1lll1_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙳ")):
                    bstack11lll1111l1_opy_ = response.get(bstack1l1lll1_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙴ"))
            if bstack11lll1111l1_opy_ and len(bstack11lll1111l1_opy_) > 0:
                for bstack1l1l111l_opy_ in bstack11lll1111l1_opy_:
                    file_path = bstack1l1l111l_opy_.get(bstack1l1lll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᙵ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11lll1111l1_opy_:
                return None
            self.logger.debug(bstack1l1lll1_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡔࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡵࡩࡨ࡫ࡩࡷࡧࡧ࠾ࠥࢁࡽࠣᙶ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l1lll1_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᙷ").format(e))
            return None
    def bstack11lll11l1ll_opy_(self):
        bstack1l1lll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡨࡧ࡬࡭ࡵࠣࡱࡦࡪࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙸ")
        return self.bstack11lll11111l_opy_
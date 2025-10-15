# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import time
from bstack_utils.bstack11ll1ll11l1_opy_ import bstack11ll1ll1ll1_opy_
from bstack_utils.constants import bstack11ll1ll1lll_opy_
from bstack_utils.helper import get_host_info, bstack11lll111l1l_opy_
class bstack11lll111lll_opy_:
    bstack1ll1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡈࡢࡰࡧࡰࡪࡹࠠࡵࡧࡶࡸࠥࡵࡲࡥࡧࡵ࡭ࡳ࡭ࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡸ࡫ࡷ࡬ࠥࡺࡨࡦࠢࡅࡶࡴࡽࡳࡦࡴࡖࡸࡦࡩ࡫ࠡࡵࡨࡶࡻ࡫ࡲ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᘳ")
    def __init__(self, config, logger):
        bstack1ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡨࡵ࡮ࡧ࡫ࡪ࠾ࠥࡪࡩࡤࡶ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡦࡳࡳ࡬ࡩࡨࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡢࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡳࡵࡴ࠯ࠤࡹ࡫ࡳࡵࠢࡲࡶࡩ࡫ࡲࡪࡰࡪࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࠦ࡮ࡢ࡯ࡨࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᘴ")
        self.config = config
        self.logger = logger
        self.bstack11ll1lll1l1_opy_ = bstack1ll1l_opy_ (u"ࠣࡶࡨࡷࡹࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲ࠴ࡧࡰࡪ࠱ࡹ࠵࠴ࡹࡰ࡭࡫ࡷ࠱ࡹ࡫ࡳࡵࡵࠥᘵ")
        self.bstack11ll1ll1l1l_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1lllll1_opy_ = 5
        self.bstack11ll1llll11_opy_ = 0
    def bstack11lll1111ll_opy_(self, test_files, orchestration_strategy, bstack1l1l1111lll_opy_={}):
        bstack1ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡉ࡯࡫ࡷ࡭ࡦࡺࡥࡴࠢࡷ࡬ࡪࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡱࡶࡧࡶࡸࠥࡧ࡮ࡥࠢࡶࡸࡴࡸࡥࡴࠢࡷ࡬ࡪࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡࡦࡤࡸࡦࠦࡦࡰࡴࠣࡴࡴࡲ࡬ࡪࡰࡪ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᘶ")
        self.logger.debug(bstack1ll1l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡌࡲ࡮ࡺࡩࡢࡶ࡬ࡲ࡬ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡼ࡯ࡴࡩࠢࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࢁࡽࠣᘷ").format(orchestration_strategy))
        try:
            bstack11ll1ll1l11_opy_ = []
            bstack1ll1l_opy_ (u"ࠦࠧࠨࡗࡦࠢࡺ࡭ࡱࡲࠠ࡯ࡱࡷࠤ࡫࡫ࡴࡤࡪࠣ࡫࡮ࡺࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢ࡬ࡷࠥࡹ࡯ࡶࡴࡦࡩࠥ࡯ࡳࠡࡶࡼࡴࡪࠦ࡯ࡧࠢࡤࡶࡷࡧࡹࠡࡣࡱࡨࠥ࡯ࡴࠨࡵࠣࡩࡱ࡫࡭ࡦࡰࡷࡷࠥࡧࡲࡦࠢࡲࡪࠥࡺࡹࡱࡧࠣࡨ࡮ࡩࡴࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࡢࡦࡥࡤࡹࡸ࡫ࠠࡪࡰࠣࡸ࡭ࡧࡴࠡࡥࡤࡷࡪ࠲ࠠࡶࡵࡨࡶࠥ࡮ࡡࡴࠢࡳࡶࡴࡼࡩࡥࡧࡧࠤࡲࡻ࡬ࡵ࡫࠰ࡶࡪࡶ࡯ࠡࡵࡲࡹࡷࡩࡥࠡࡹ࡬ࡸ࡭ࠦࡦࡦࡣࡷࡹࡷ࡫ࡂࡳࡣࡱࡧ࡭ࠦࡩ࡯ࠢࡥࡶࡴࡽࡳࡦࡴࡶࡸࡦࡩ࡫ࠣࠤࠥᘸ")
            source = bstack1l1l1111lll_opy_[bstack1ll1l_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᘹ")].get(bstack1ll1l_opy_ (u"࠭ࡳࡰࡷࡵࡧࡪ࠭ᘺ"), [])
            bstack11ll1llll1l_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if bstack1l1l1111lll_opy_[bstack1ll1l_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᘻ")].get(bstack1ll1l_opy_ (u"ࠨࡧࡱࡥࡧࡲࡥࡥࠩᘼ"), False) and not bstack11ll1llll1l_opy_:
                bstack11ll1ll1l11_opy_ = bstack11lll111l1l_opy_(source) # bstack11lll11ll11_opy_-repo is handled bstack11lll11111l_opy_
            payload = {
                bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᘽ"): [{bstack1ll1l_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧᘾ"): f} for f in test_files],
                bstack1ll1l_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡗࡹࡸࡡࡵࡧࡪࡽࠧᘿ"): orchestration_strategy,
                bstack1ll1l_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡒ࡫ࡴࡢࡦࡤࡸࡦࠨᙀ"): bstack1l1l1111lll_opy_,
                bstack1ll1l_opy_ (u"ࠨ࡮ࡰࡦࡨࡍࡳࡪࡥࡹࠤᙁ"): int(os.environ.get(bstack1ll1l_opy_ (u"ࠢࡃࡔࡒ࡛ࡘࡋࡒࡔࡖࡄࡇࡐࡥࡎࡐࡆࡈࡣࡎࡔࡄࡆ࡚ࠥᙂ")) or bstack1ll1l_opy_ (u"ࠣ࠲ࠥᙃ")),
                bstack1ll1l_opy_ (u"ࠤࡷࡳࡹࡧ࡬ࡏࡱࡧࡩࡸࠨᙄ"): int(os.environ.get(bstack1ll1l_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡗࡓ࡙ࡇࡌࡠࡐࡒࡈࡊࡥࡃࡐࡗࡑࡘࠧᙅ")) or bstack1ll1l_opy_ (u"ࠦ࠶ࠨᙆ")),
                bstack1ll1l_opy_ (u"ࠧࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠥᙇ"): self.config.get(bstack1ll1l_opy_ (u"࠭ࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠫᙈ"), bstack1ll1l_opy_ (u"ࠧࠨᙉ")),
                bstack1ll1l_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠦᙊ"): self.config.get(bstack1ll1l_opy_ (u"ࠩࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠬᙋ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1ll1l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡔࡸࡲࡎࡪࡥ࡯ࡶ࡬ࡪ࡮࡫ࡲࠣᙌ"): os.environ.get(bstack1ll1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡆ࡚ࡏࡌࡅࡡࡕ࡙ࡓࡥࡉࡅࡇࡑࡘࡎࡌࡉࡆࡔࠥᙍ"), bstack1ll1l_opy_ (u"ࠧࠨᙎ")),
                bstack1ll1l_opy_ (u"ࠨࡨࡰࡵࡷࡍࡳ࡬࡯ࠣᙏ"): get_host_info(),
                bstack1ll1l_opy_ (u"ࠢࡱࡴࡇࡩࡹࡧࡩ࡭ࡵࠥᙐ"): bstack11ll1ll1l11_opy_
            }
            self.logger.debug(bstack1ll1l_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤᙑ").format(payload))
            response = bstack11ll1ll1ll1_opy_.bstack11lll11l1ll_opy_(self.bstack11ll1lll1l1_opy_, payload)
            if response:
                self.bstack11ll1ll1l1l_opy_ = self._11ll1llllll_opy_(response)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠻ࠢࡾࢁࠧᙒ").format(self.bstack11ll1ll1l1l_opy_))
            else:
                self.logger.error(bstack1ll1l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡉࡥ࡮ࡲࡥࡥࠢࡷࡳࠥ࡭ࡥࡵࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠰ࠥᙓ"))
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡶࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺࠻ࠢࡾࢁࠧᙔ").format(e))
    def _11ll1llllll_opy_(self, response):
        bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡓࡶࡴࡩࡥࡴࡵࡨࡷࠥࡺࡨࡦࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡡ࡯ࡦࠣࡩࡽࡺࡲࡢࡥࡷࡷࠥࡸࡥ࡭ࡧࡹࡥࡳࡺࠠࡧ࡫ࡨࡰࡩࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙕ")
        bstack1ll1l1lll_opy_ = {}
        bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙖ")] = response.get(bstack1ll1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙗ"), self.default_timeout)
        bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙘ")] = response.get(bstack1ll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᙙ"), self.bstack11ll1lllll1_opy_)
        bstack11ll1lll11l_opy_ = response.get(bstack1ll1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙚ"))
        bstack11ll1ll11ll_opy_ = response.get(bstack1ll1l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙛ"))
        if bstack11ll1lll11l_opy_:
            bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᙜ")] = bstack11ll1lll11l_opy_.split(bstack11ll1ll1lll_opy_ + bstack1ll1l_opy_ (u"ࠨ࠯ࠣᙝ"))[1] if bstack11ll1ll1lll_opy_ + bstack1ll1l_opy_ (u"ࠢ࠰ࠤᙞ") in bstack11ll1lll11l_opy_ else bstack11ll1lll11l_opy_
        else:
            bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᙟ")] = None
        if bstack11ll1ll11ll_opy_:
            bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᙠ")] = bstack11ll1ll11ll_opy_.split(bstack11ll1ll1lll_opy_ + bstack1ll1l_opy_ (u"ࠥ࠳ࠧᙡ"))[1] if bstack11ll1ll1lll_opy_ + bstack1ll1l_opy_ (u"ࠦ࠴ࠨᙢ") in bstack11ll1ll11ll_opy_ else bstack11ll1ll11ll_opy_
        else:
            bstack1ll1l1lll_opy_[bstack1ll1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙣ")] = None
        if (
            response.get(bstack1ll1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙤ")) is None or
            response.get(bstack1ll1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙥ")) is None or
            response.get(bstack1ll1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᙦ")) is None or
            response.get(bstack1ll1l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙧ")) is None
        ):
            self.logger.debug(bstack1ll1l_opy_ (u"ࠥ࡟ࡵࡸ࡯ࡤࡧࡶࡷࡤࡹࡰ࡭࡫ࡷࡣࡹ࡫ࡳࡵࡵࡢࡶࡪࡹࡰࡰࡰࡶࡩࡢࠦࡒࡦࡥࡨ࡭ࡻ࡫ࡤࠡࡰࡸࡰࡱࠦࡶࡢ࡮ࡸࡩ࠭ࡹࠩࠡࡨࡲࡶࠥࡹ࡯࡮ࡧࠣࡥࡹࡺࡲࡪࡤࡸࡸࡪࡹࠠࡪࡰࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠢᙨ"))
        return bstack1ll1l1lll_opy_
    def bstack11lll111l11_opy_(self):
        if not self.bstack11ll1ll1l1l_opy_:
            self.logger.error(bstack1ll1l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡔ࡯ࠡࡴࡨࡵࡺ࡫ࡳࡵࠢࡧࡥࡹࡧࠠࡢࡸࡤ࡭ࡱࡧࡢ࡭ࡧࠣࡸࡴࠦࡦࡦࡶࡦ࡬ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠱ࠦᙩ"))
            return None
        bstack11lll11l11l_opy_ = None
        test_files = []
        bstack11ll1lll1ll_opy_ = int(time.time() * 1000) # bstack11lll1111l1_opy_ sec
        bstack11lll11l111_opy_ = int(self.bstack11ll1ll1l1l_opy_.get(bstack1ll1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᙪ"), self.bstack11ll1lllll1_opy_))
        bstack11lll111ll1_opy_ = int(self.bstack11ll1ll1l1l_opy_.get(bstack1ll1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙫ"), self.default_timeout)) * 1000
        bstack11ll1ll11ll_opy_ = self.bstack11ll1ll1l1l_opy_.get(bstack1ll1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙬ"), None)
        bstack11ll1lll11l_opy_ = self.bstack11ll1ll1l1l_opy_.get(bstack1ll1l_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ᙭"), None)
        if bstack11ll1lll11l_opy_ is None and bstack11ll1ll11ll_opy_ is None:
            return None
        try:
            while bstack11ll1lll11l_opy_ and (time.time() * 1000 - bstack11ll1lll1ll_opy_) < bstack11lll111ll1_opy_:
                response = bstack11ll1ll1ll1_opy_.bstack11lll111111_opy_(bstack11ll1lll11l_opy_, {})
                if response and response.get(bstack1ll1l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣ᙮")):
                    bstack11lll11l11l_opy_ = response.get(bstack1ll1l_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᙯ"))
                self.bstack11ll1llll11_opy_ += 1
                if bstack11lll11l11l_opy_:
                    break
                time.sleep(bstack11lll11l111_opy_)
                self.logger.debug(bstack1ll1l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡸࡥࡴࡷ࡯ࡸ࡛ࠥࡒࡍࠢࡤࡪࡹ࡫ࡲࠡࡹࡤ࡭ࡹ࡯࡮ࡨࠢࡩࡳࡷࠦࡻࡾࠢࡶࡩࡨࡵ࡮ࡥࡵ࠱ࠦᙰ").format(bstack11lll11l111_opy_))
            if bstack11ll1ll11ll_opy_ and not bstack11lll11l11l_opy_:
                self.logger.debug(bstack1ll1l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡴࡪ࡯ࡨࡳࡺࡺࠠࡖࡔࡏࠦᙱ"))
                response = bstack11ll1ll1ll1_opy_.bstack11lll111111_opy_(bstack11ll1ll11ll_opy_, {})
                if response and response.get(bstack1ll1l_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᙲ")):
                    bstack11lll11l11l_opy_ = response.get(bstack1ll1l_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙳ"))
            if bstack11lll11l11l_opy_ and len(bstack11lll11l11l_opy_) > 0:
                for bstack1l1l1ll1_opy_ in bstack11lll11l11l_opy_:
                    file_path = bstack1l1l1ll1_opy_.get(bstack1ll1l_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᙴ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11lll11l11l_opy_:
                return None
            self.logger.debug(bstack1ll1l_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡓࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳࠡࡴࡨࡧࡪ࡯ࡶࡦࡦ࠽ࠤࢀࢃࠢᙵ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1ll1l_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡪࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᙶ").format(e))
            return None
    def bstack11lll11l1l1_opy_(self):
        bstack1ll1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡔࡨࡸࡺࡸ࡮ࡴࠢࡷ࡬ࡪࠦࡣࡰࡷࡱࡸࠥࡵࡦࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡧࡦࡲ࡬ࡴࠢࡰࡥࡩ࡫࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᙷ")
        return self.bstack11ll1llll11_opy_
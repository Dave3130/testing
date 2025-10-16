# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import time
from bstack_utils.bstack11lll11l111_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll11lll1_opy_
from bstack_utils.helper import get_host_info, bstack11lll11l1ll_opy_
class bstack11lll111l11_opy_:
    bstack1lllll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡡ࡯ࡦ࡯ࡩࡸࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡴࡧࡵࡺࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᘹ")
    def __init__(self, config, logger):
        bstack1lllll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࡩ࡯ࡣࡵ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡡࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࡹࡴࡳ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥࡴࡡ࡮ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘺ")
        self.config = config
        self.logger = logger
        self.bstack11lll111ll1_opy_ = bstack1lllll1_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡶ࡬ࡪࡶ࠰ࡸࡪࡹࡴࡴࠤᘻ")
        self.bstack11ll1ll1lll_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1lllll1_opy_ = 5
        self.bstack11lll1111ll_opy_ = 0
    def bstack11lll111lll_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1lllll1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡷࡵࡦࡵࡷࠤࡦࡴࡤࠡࡵࡷࡳࡷ࡫ࡳࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡳࡳࡱࡲࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᘼ")
        self.logger.debug(bstack1lllll1_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫ࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢᘽ").format(orchestration_strategy))
        try:
            bstack11ll1lll1ll_opy_ = []
            bstack1lllll1_opy_ (u"ࠥࠦࠧ࡝ࡥࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡪࡪࡺࡣࡩࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡ࡫ࡶࠤࡸࡵࡵࡳࡥࡨࠤ࡮ࡹࠠࡵࡻࡳࡩࠥࡵࡦࠡࡣࡵࡶࡦࡿࠠࡢࡰࡧࠤ࡮ࡺࠧࡴࠢࡨࡰࡪࡳࡥ࡯ࡶࡶࠤࡦࡸࡥࠡࡱࡩࠤࡹࡿࡰࡦࠢࡧ࡭ࡨࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡥࡤࡣࡸࡷࡪࠦࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡶࡩ࠱ࠦࡵࡴࡧࡵࠤ࡭ࡧࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡱࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡴࡱࡸࡶࡨ࡫ࠠࡸ࡫ࡷ࡬ࠥ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠥ࡯࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢࠣࠤᘾ")
            source = orchestration_metadata[bstack1lllll1_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᘿ")].get(bstack1lllll1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᙀ"), [])
            bstack11ll1llll1l_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1lllll1_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᙁ")].get(bstack1lllll1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᙂ"), False) and not bstack11ll1llll1l_opy_:
                bstack11ll1lll1ll_opy_ = bstack11lll11l1ll_opy_(source) # bstack11lll1111l1_opy_-repo is handled bstack11lll11l1l1_opy_
            payload = {
                bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙃ"): [{bstack1lllll1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᙄ"): f} for f in test_files],
                bstack1lllll1_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡸࡷࡧࡴࡦࡩࡼࠦᙅ"): orchestration_strategy,
                bstack1lllll1_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡑࡪࡺࡡࡥࡣࡷࡥࠧᙆ"): orchestration_metadata,
                bstack1lllll1_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣᙇ"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᙈ")) or bstack1lllll1_opy_ (u"ࠢ࠱ࠤᙉ")),
                bstack1lllll1_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧᙊ"): int(os.environ.get(bstack1lllll1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᙋ")) or bstack1lllll1_opy_ (u"ࠥ࠵ࠧᙌ")),
                bstack1lllll1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᙍ"): self.config.get(bstack1lllll1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᙎ"), bstack1lllll1_opy_ (u"࠭ࠧᙏ")),
                bstack1lllll1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᙐ"): self.config.get(bstack1lllll1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᙑ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1lllll1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᙒ"): os.environ.get(bstack1lllll1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᙓ"), bstack1lllll1_opy_ (u"ࠦࠧᙔ")),
                bstack1lllll1_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᙕ"): get_host_info(),
                bstack1lllll1_opy_ (u"ࠨࡰࡳࡆࡨࡸࡦ࡯࡬ࡴࠤᙖ"): bstack11ll1lll1ll_opy_
            }
            self.logger.debug(bstack1lllll1_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᙗ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll1ll1l11_opy_(self.bstack11lll111ll1_opy_, payload)
            if response:
                self.bstack11ll1ll1lll_opy_ = self._11ll1llll11_opy_(response)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦᙘ").format(self.bstack11ll1ll1lll_opy_))
            else:
                self.logger.error(bstack1lllll1_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤᙙ"))
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀ࠺ࠡࡽࢀࠦᙚ").format(e))
    def _11ll1llll11_opy_(self, response):
        bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡧ࡮ࡥࠢࡨࡼࡹࡸࡡࡤࡶࡶࠤࡷ࡫࡬ࡦࡸࡤࡲࡹࠦࡦࡪࡧ࡯ࡨࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙛ")
        bstack1l11ll1l1l_opy_ = {}
        bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙜ")] = response.get(bstack1lllll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙝ"), self.default_timeout)
        bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙞ")] = response.get(bstack1lllll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙟ"), self.bstack11ll1lllll1_opy_)
        bstack11ll1lll1l1_opy_ = response.get(bstack1lllll1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙠ"))
        bstack11ll1lll111_opy_ = response.get(bstack1lllll1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙡ"))
        if bstack11ll1lll1l1_opy_:
            bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙢ")] = bstack11ll1lll1l1_opy_.split(bstack11lll11lll1_opy_ + bstack1lllll1_opy_ (u"ࠧ࠵ࠢᙣ"))[1] if bstack11lll11lll1_opy_ + bstack1lllll1_opy_ (u"ࠨ࠯ࠣᙤ") in bstack11ll1lll1l1_opy_ else bstack11ll1lll1l1_opy_
        else:
            bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙥ")] = None
        if bstack11ll1lll111_opy_:
            bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᙦ")] = bstack11ll1lll111_opy_.split(bstack11lll11lll1_opy_ + bstack1lllll1_opy_ (u"ࠤ࠲ࠦᙧ"))[1] if bstack11lll11lll1_opy_ + bstack1lllll1_opy_ (u"ࠥ࠳ࠧᙨ") in bstack11ll1lll111_opy_ else bstack11ll1lll111_opy_
        else:
            bstack1l11ll1l1l_opy_[bstack1lllll1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙩ")] = None
        if (
            response.get(bstack1lllll1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙪ")) is None or
            response.get(bstack1lllll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᙫ")) is None or
            response.get(bstack1lllll1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙬ")) is None or
            response.get(bstack1lllll1_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦ᙭")) is None
        ):
            self.logger.debug(bstack1lllll1_opy_ (u"ࠤ࡞ࡴࡷࡵࡣࡦࡵࡶࡣࡸࡶ࡬ࡪࡶࡢࡸࡪࡹࡴࡴࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࡡࠥࡘࡥࡤࡧ࡬ࡺࡪࡪࠠ࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨࠬࡸ࠯ࠠࡧࡱࡵࠤࡸࡵ࡭ࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࡸࠦࡩ࡯ࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨ᙮"))
        return bstack1l11ll1l1l_opy_
    def bstack11ll1llllll_opy_(self):
        if not self.bstack11ll1ll1lll_opy_:
            self.logger.error(bstack1lllll1_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠰ࠥᙯ"))
            return None
        bstack11ll1lll11l_opy_ = None
        test_files = []
        bstack11lll11ll1l_opy_ = int(time.time() * 1000) # bstack11lll11l11l_opy_ sec
        bstack11lll11ll11_opy_ = int(self.bstack11ll1ll1lll_opy_.get(bstack1lllll1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᙰ"), self.bstack11ll1lllll1_opy_))
        bstack11lll11111l_opy_ = int(self.bstack11ll1ll1lll_opy_.get(bstack1lllll1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙱ"), self.default_timeout)) * 1000
        bstack11ll1lll111_opy_ = self.bstack11ll1ll1lll_opy_.get(bstack1lllll1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙲ"), None)
        bstack11ll1lll1l1_opy_ = self.bstack11ll1ll1lll_opy_.get(bstack1lllll1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙳ"), None)
        if bstack11ll1lll1l1_opy_ is None and bstack11ll1lll111_opy_ is None:
            return None
        try:
            while bstack11ll1lll1l1_opy_ and (time.time() * 1000 - bstack11lll11ll1l_opy_) < bstack11lll11111l_opy_:
                response = bstack11lll111111_opy_.bstack11lll111l1l_opy_(bstack11ll1lll1l1_opy_, {})
                if response and response.get(bstack1lllll1_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙴ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack1lllll1_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᙵ"))
                self.bstack11lll1111ll_opy_ += 1
                if bstack11ll1lll11l_opy_:
                    break
                time.sleep(bstack11lll11ll11_opy_)
                self.logger.debug(bstack1lllll1_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡚ࡘࡌࠡࡣࡩࡸࡪࡸࠠࡸࡣ࡬ࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࢁࡽࠡࡵࡨࡧࡴࡴࡤࡴ࠰ࠥᙶ").format(bstack11lll11ll11_opy_))
            if bstack11ll1lll111_opy_ and not bstack11ll1lll11l_opy_:
                self.logger.debug(bstack1lllll1_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡺࡩ࡮ࡧࡲࡹࡹࠦࡕࡓࡎࠥᙷ"))
                response = bstack11lll111111_opy_.bstack11lll111l1l_opy_(bstack11ll1lll111_opy_, {})
                if response and response.get(bstack1lllll1_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙸ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack1lllll1_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᙹ"))
            if bstack11ll1lll11l_opy_ and len(bstack11ll1lll11l_opy_) > 0:
                for bstack1ll11lll_opy_ in bstack11ll1lll11l_opy_:
                    file_path = bstack1ll11lll_opy_.get(bstack1lllll1_opy_ (u"ࠢࡧ࡫࡯ࡩࡕࡧࡴࡩࠤᙺ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1lll11l_opy_:
                return None
            self.logger.debug(bstack1lllll1_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡒࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡳࡧࡦࡩ࡮ࡼࡥࡥ࠼ࠣࡿࢂࠨᙻ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1lllll1_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨᙼ").format(e))
            return None
    def bstack11ll1ll1l1l_opy_(self):
        bstack1lllll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡦࡥࡱࡲࡳࠡ࡯ࡤࡨࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙽ")
        return self.bstack11lll1111ll_opy_
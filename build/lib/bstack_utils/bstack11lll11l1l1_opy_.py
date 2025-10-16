# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import time
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lll111_opy_
from bstack_utils.constants import bstack11lll1111ll_opy_
from bstack_utils.helper import get_host_info, bstack11lll11111l_opy_
class bstack11ll1lll1ll_opy_:
    bstack1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡉࡣࡱࡨࡱ࡫ࡳࠡࡶࡨࡷࡹࠦ࡯ࡳࡦࡨࡶ࡮ࡴࡧࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡹ࡬ࡸ࡭ࠦࡴࡩࡧࠣࡆࡷࡵࡷࡴࡧࡵࡗࡹࡧࡣ࡬ࠢࡶࡩࡷࡼࡥࡳ࠰ࠍࠤࠥࠦࠠࠣࠤࠥᘻ")
    def __init__(self, config, logger):
        bstack1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡩ࡯࡯ࡨ࡬࡫࠿ࠦࡤࡪࡥࡷ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࠣࡧࡴࡴࡦࡪࡩࠍࠤࠥࠦࠠࠡࠢࠣࠤ࠿ࡶࡡࡳࡣࡰࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡣࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡴࡶࡵ࠰ࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡹࡴࡳࡣࡷࡩ࡬ࡿࠠ࡯ࡣࡰࡩࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᘼ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1lll_opy_ = bstack1l_opy_ (u"ࠤࡷࡩࡸࡺ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࠵ࡡࡱ࡫࠲ࡺ࠶࠵ࡳࡱ࡮࡬ࡸ࠲ࡺࡥࡴࡶࡶࠦᘽ")
        self.bstack11ll1llllll_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1llll1l_opy_ = 5
        self.bstack11lll11l11l_opy_ = 0
    def bstack11lll11ll1l_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡲࡷࡨࡷࡹࠦࡡ࡯ࡦࠣࡷࡹࡵࡲࡦࡵࠣࡸ࡭࡫ࠠࡳࡧࡶࡴࡴࡴࡳࡦࠢࡧࡥࡹࡧࠠࡧࡱࡵࠤࡵࡵ࡬࡭࡫ࡱ࡫࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᘾ")
        self.logger.debug(bstack1l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡍࡳ࡯ࡴࡪࡣࡷ࡭ࡳ࡭ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡽࡩࡵࡪࠣࡷࡹࡸࡡࡵࡧࡪࡽ࠿ࠦࡻࡾࠤᘿ").format(orchestration_strategy))
        try:
            bstack11lll111111_opy_ = []
            bstack1l_opy_ (u"ࠧࠨࠢࡘࡧࠣࡻ࡮ࡲ࡬ࠡࡰࡲࡸࠥ࡬ࡥࡵࡥ࡫ࠤ࡬࡯ࡴࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣ࡭ࡸࠦࡳࡰࡷࡵࡧࡪࠦࡩࡴࠢࡷࡽࡵ࡫ࠠࡰࡨࠣࡥࡷࡸࡡࡺࠢࡤࡲࡩࠦࡩࡵࠩࡶࠤࡪࡲࡥ࡮ࡧࡱࡸࡸࠦࡡࡳࡧࠣࡳ࡫ࠦࡴࡺࡲࡨࠤࡩ࡯ࡣࡵࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࡣࡧࡦࡥࡺࡹࡥࠡ࡫ࡱࠤࡹ࡮ࡡࡵࠢࡦࡥࡸ࡫ࠬࠡࡷࡶࡩࡷࠦࡨࡢࡵࠣࡴࡷࡵࡶࡪࡦࡨࡨࠥࡳࡵ࡭ࡶ࡬࠱ࡷ࡫ࡰࡰࠢࡶࡳࡺࡸࡣࡦࠢࡺ࡭ࡹ࡮ࠠࡧࡧࡤࡸࡺࡸࡥࡃࡴࡤࡲࡨ࡮ࠠࡪࡰࠣࡦࡷࡵࡷࡴࡧࡵࡷࡹࡧࡣ࡬ࠤࠥࠦᙀ")
            source = orchestration_metadata[bstack1l_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᙁ")].get(bstack1l_opy_ (u"ࠧࡴࡱࡸࡶࡨ࡫ࠧᙂ"), [])
            bstack11lll1111l1_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1l_opy_ (u"ࠨࡴࡸࡲࡤࡹ࡭ࡢࡴࡷࡣࡸ࡫࡬ࡦࡥࡷ࡭ࡴࡴࠧᙃ")].get(bstack1l_opy_ (u"ࠩࡨࡲࡦࡨ࡬ࡦࡦࠪᙄ"), False) and not bstack11lll1111l1_opy_:
                bstack11lll111111_opy_ = bstack11lll11111l_opy_(source) # bstack11lll11ll11_opy_-repo is handled bstack11ll1lllll1_opy_
            payload = {
                bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᙅ"): [{bstack1l_opy_ (u"ࠦ࡫࡯࡬ࡦࡒࡤࡸ࡭ࠨᙆ"): f} for f in test_files],
                bstack1l_opy_ (u"ࠧࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡘࡺࡲࡢࡶࡨ࡫ࡾࠨᙇ"): orchestration_strategy,
                bstack1l_opy_ (u"ࠨ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࡓࡥࡵࡣࡧࡥࡹࡧࠢᙈ"): orchestration_metadata,
                bstack1l_opy_ (u"ࠢ࡯ࡱࡧࡩࡎࡴࡤࡦࡺࠥᙉ"): int(os.environ.get(bstack1l_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡏࡑࡇࡉࡤࡏࡎࡅࡇ࡛ࠦᙊ")) or bstack1l_opy_ (u"ࠤ࠳ࠦᙋ")),
                bstack1l_opy_ (u"ࠥࡸࡴࡺࡡ࡭ࡐࡲࡨࡪࡹࠢᙌ"): int(os.environ.get(bstack1l_opy_ (u"ࠦࡇࡘࡏࡘࡕࡈࡖࡘ࡚ࡁࡄࡍࡢࡘࡔ࡚ࡁࡍࡡࡑࡓࡉࡋ࡟ࡄࡑࡘࡒ࡙ࠨᙍ")) or bstack1l_opy_ (u"ࠧ࠷ࠢᙎ")),
                bstack1l_opy_ (u"ࠨࡰࡳࡱ࡭ࡩࡨࡺࡎࡢ࡯ࡨࠦᙏ"): self.config.get(bstack1l_opy_ (u"ࠧࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠬᙐ"), bstack1l_opy_ (u"ࠨࠩᙑ")),
                bstack1l_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡏࡣࡰࡩࠧᙒ"): self.config.get(bstack1l_opy_ (u"ࠪࡦࡺ࡯࡬ࡥࡐࡤࡱࡪ࠭ᙓ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l_opy_ (u"ࠦࡧࡻࡩ࡭ࡦࡕࡹࡳࡏࡤࡦࡰࡷ࡭࡫࡯ࡥࡳࠤᙔ"): os.environ.get(bstack1l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡇ࡛ࡉࡍࡆࡢࡖ࡚ࡔ࡟ࡊࡆࡈࡒ࡙ࡏࡆࡊࡇࡕࠦᙕ"), bstack1l_opy_ (u"ࠨࠢᙖ")),
                bstack1l_opy_ (u"ࠢࡩࡱࡶࡸࡎࡴࡦࡰࠤᙗ"): get_host_info(),
                bstack1l_opy_ (u"ࠣࡲࡵࡈࡪࡺࡡࡪ࡮ࡶࠦᙘ"): bstack11lll111111_opy_
            }
            self.logger.debug(bstack1l_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡕࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀࠠࡼࡿࠥᙙ").format(payload))
            response = bstack11ll1lll111_opy_.bstack11lll111l11_opy_(self.bstack11ll1ll1lll_opy_, payload)
            if response:
                self.bstack11ll1llllll_opy_ = self._11ll1ll1l11_opy_(response)
                self.logger.debug(bstack1l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡖࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡳࡧࡶࡴࡴࡴࡳࡦ࠼ࠣࡿࢂࠨᙚ").format(self.bstack11ll1llllll_opy_))
            else:
                self.logger.error(bstack1l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡊࡦ࡯࡬ࡦࡦࠣࡸࡴࠦࡧࡦࡶࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠱ࠦᙛ"))
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡪࡰࠣࡷࡪࡴࡤࡪࡰࡪࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻࠼ࠣࡿࢂࠨᙜ").format(e))
    def _11ll1ll1l11_opy_(self, response):
        bstack1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡔࡷࡵࡣࡦࡵࡶࡩࡸࠦࡴࡩࡧࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡢࡰࡧࠤࡪࡾࡴࡳࡣࡦࡸࡸࠦࡲࡦ࡮ࡨࡺࡦࡴࡴࠡࡨ࡬ࡩࡱࡪࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙝ")
        bstack111llllll_opy_ = {}
        bstack111llllll_opy_[bstack1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙞ")] = response.get(bstack1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤᙟ"), self.default_timeout)
        bstack111llllll_opy_[bstack1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᙠ")] = response.get(bstack1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙡ"), self.bstack11ll1llll1l_opy_)
        bstack11lll11l1ll_opy_ = response.get(bstack1l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙢ"))
        bstack11ll1ll1l1l_opy_ = response.get(bstack1l_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙣ"))
        if bstack11lll11l1ll_opy_:
            bstack111llllll_opy_[bstack1l_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙤ")] = bstack11lll11l1ll_opy_.split(bstack11lll1111ll_opy_ + bstack1l_opy_ (u"ࠢ࠰ࠤᙥ"))[1] if bstack11lll1111ll_opy_ + bstack1l_opy_ (u"ࠣ࠱ࠥᙦ") in bstack11lll11l1ll_opy_ else bstack11lll11l1ll_opy_
        else:
            bstack111llllll_opy_[bstack1l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙧ")] = None
        if bstack11ll1ll1l1l_opy_:
            bstack111llllll_opy_[bstack1l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙨ")] = bstack11ll1ll1l1l_opy_.split(bstack11lll1111ll_opy_ + bstack1l_opy_ (u"ࠦ࠴ࠨᙩ"))[1] if bstack11lll1111ll_opy_ + bstack1l_opy_ (u"ࠧ࠵ࠢᙪ") in bstack11ll1ll1l1l_opy_ else bstack11ll1ll1l1l_opy_
        else:
            bstack111llllll_opy_[bstack1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙫ")] = None
        if (
            response.get(bstack1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙬ")) is None or
            response.get(bstack1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥ᙭")) is None or
            response.get(bstack1l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨ᙮")) is None or
            response.get(bstack1l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙯ")) is None
        ):
            self.logger.debug(bstack1l_opy_ (u"ࠦࡠࡶࡲࡰࡥࡨࡷࡸࡥࡳࡱ࡮࡬ࡸࡤࡺࡥࡴࡶࡶࡣࡷ࡫ࡳࡱࡱࡱࡷࡪࡣࠠࡓࡧࡦࡩ࡮ࡼࡥࡥࠢࡱࡹࡱࡲࠠࡷࡣ࡯ࡹࡪ࠮ࡳࠪࠢࡩࡳࡷࠦࡳࡰ࡯ࡨࠤࡦࡺࡴࡳ࡫ࡥࡹࡹ࡫ࡳࠡ࡫ࡱࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡄࡔࡎࠦࡲࡦࡵࡳࡳࡳࡹࡥࠣᙰ"))
        return bstack111llllll_opy_
    def bstack11lll11lll1_opy_(self):
        if not self.bstack11ll1llllll_opy_:
            self.logger.error(bstack1l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡎࡰࠢࡵࡩࡶࡻࡥࡴࡶࠣࡨࡦࡺࡡࠡࡣࡹࡥ࡮ࡲࡡࡣ࡮ࡨࠤࡹࡵࠠࡧࡧࡷࡧ࡭ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠲ࠧᙱ"))
            return None
        bstack11ll1lll11l_opy_ = None
        test_files = []
        bstack11lll111lll_opy_ = int(time.time() * 1000) # bstack11ll1lll1l1_opy_ sec
        bstack11ll1ll1ll1_opy_ = int(self.bstack11ll1llllll_opy_.get(bstack1l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᙲ"), self.bstack11ll1llll1l_opy_))
        bstack11lll11l111_opy_ = int(self.bstack11ll1llllll_opy_.get(bstack1l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࠣᙳ"), self.default_timeout)) * 1000
        bstack11ll1ll1l1l_opy_ = self.bstack11ll1llllll_opy_.get(bstack1l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᙴ"), None)
        bstack11lll11l1ll_opy_ = self.bstack11ll1llllll_opy_.get(bstack1l_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙵ"), None)
        if bstack11lll11l1ll_opy_ is None and bstack11ll1ll1l1l_opy_ is None:
            return None
        try:
            while bstack11lll11l1ll_opy_ and (time.time() * 1000 - bstack11lll111lll_opy_) < bstack11lll11l111_opy_:
                response = bstack11ll1lll111_opy_.bstack11lll111ll1_opy_(bstack11lll11l1ll_opy_, {})
                if response and response.get(bstack1l_opy_ (u"ࠥࡸࡪࡹࡴࡴࠤᙶ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack1l_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᙷ"))
                self.bstack11lll11l11l_opy_ += 1
                if bstack11ll1lll11l_opy_:
                    break
                time.sleep(bstack11ll1ll1ll1_opy_)
                self.logger.debug(bstack1l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡆࡦࡶࡦ࡬࡮ࡴࡧࠡࡱࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࡳࠡࡨࡵࡳࡲࠦࡲࡦࡵࡸࡰࡹࠦࡕࡓࡎࠣࡥ࡫ࡺࡥࡳࠢࡺࡥ࡮ࡺࡩ࡯ࡩࠣࡪࡴࡸࠠࡼࡿࠣࡷࡪࡩ࡯࡯ࡦࡶ࠲ࠧᙸ").format(bstack11ll1ll1ll1_opy_))
            if bstack11ll1ll1l1l_opy_ and not bstack11ll1lll11l_opy_:
                self.logger.debug(bstack1l_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡇࡧࡷࡧ࡭࡯࡮ࡨࠢࡲࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࡴࠢࡩࡶࡴࡳࠠࡵ࡫ࡰࡩࡴࡻࡴࠡࡗࡕࡐࠧᙹ"))
                response = bstack11ll1lll111_opy_.bstack11lll111ll1_opy_(bstack11ll1ll1l1l_opy_, {})
                if response and response.get(bstack1l_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙺ")):
                    bstack11ll1lll11l_opy_ = response.get(bstack1l_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙻ"))
            if bstack11ll1lll11l_opy_ and len(bstack11ll1lll11l_opy_) > 0:
                for bstack1lll1111_opy_ in bstack11ll1lll11l_opy_:
                    file_path = bstack1lll1111_opy_.get(bstack1l_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᙼ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1lll11l_opy_:
                return None
            self.logger.debug(bstack1l_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡔࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴࠢࡵࡩࡨ࡫ࡩࡷࡧࡧ࠾ࠥࢁࡽࠣᙽ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤ࡫࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᙾ").format(e))
            return None
    def bstack11ll1llll11_opy_(self):
        bstack1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡕࡩࡹࡻࡲ࡯ࡵࠣࡸ࡭࡫ࠠࡤࡱࡸࡲࡹࠦ࡯ࡧࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡨࡧ࡬࡭ࡵࠣࡱࡦࡪࡥ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᙿ")
        return self.bstack11lll11l11l_opy_
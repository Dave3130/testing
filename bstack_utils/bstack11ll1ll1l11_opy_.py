# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import time
from bstack_utils.bstack11lll1111ll_opy_ import bstack11ll1llllll_opy_
from bstack_utils.constants import bstack11lll11l1ll_opy_
from bstack_utils.helper import get_host_info, bstack11lll11l1l1_opy_
class bstack11ll1ll1lll_opy_:
    bstack1ll11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍࡧ࡮ࡥ࡮ࡨࡷࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡳࡦࡴࡹࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘸ")
    def __init__(self, config, logger):
        bstack1ll11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡨ࡮ࡩࡴ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡠࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࡸࡺࡲ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤࡳࡧ࡭ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᘹ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1l1l_opy_ = bstack1ll11_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡵࡲࡩࡵ࠯ࡷࡩࡸࡺࡳࠣᘺ")
        self.bstack11ll1lllll1_opy_ = None
        self.default_timeout = 60
        self.bstack11lll11lll1_opy_ = 5
        self.bstack11ll1lll1ll_opy_ = 0
    def bstack11lll111111_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1ll11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࡩࡵ࡫ࡤࡸࡪࡹࠠࡵࡪࡨࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡶࡻࡥࡴࡶࠣࡥࡳࡪࠠࡴࡶࡲࡶࡪࡹࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡲࡲࡰࡱ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘻ")
        self.logger.debug(bstack1ll11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨᘼ").format(orchestration_strategy))
        try:
            bstack11ll1lll11l_opy_ = []
            bstack1ll11_opy_ (u"ࠤࠥࠦ࡜࡫ࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡩࡩࡹࡩࡨࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡪࡵࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡸࠦࡴࡺࡲࡨࠤࡴ࡬ࠠࡢࡴࡵࡥࡾࠦࡡ࡯ࡦࠣ࡭ࡹ࠭ࡳࠡࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡥࡷ࡫ࠠࡰࡨࠣࡸࡾࡶࡥࠡࡦ࡬ࡧࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧ࡫ࡣࡢࡷࡶࡩࠥ࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡵࡨ࠰ࠥࡻࡳࡦࡴࠣ࡬ࡦࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡰࡹࡱࡺࡩ࠮ࡴࡨࡴࡴࠦࡳࡰࡷࡵࡧࡪࠦࡷࡪࡶ࡫ࠤ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠤ࡮ࡴࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨࠢࠣᘽ")
            source = orchestration_metadata[bstack1ll11_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᘾ")].get(bstack1ll11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᘿ"), [])
            bstack11ll1llll11_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1ll11_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᙀ")].get(bstack1ll11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᙁ"), False) and not bstack11ll1llll11_opy_:
                bstack11ll1lll11l_opy_ = bstack11lll11l1l1_opy_(source) # bstack11lll111ll1_opy_-repo is handled bstack11lll11ll11_opy_
            payload = {
                bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙂ"): [{bstack1ll11_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᙃ"): f} for f in test_files],
                bstack1ll11_opy_ (u"ࠤࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡷࡶࡦࡺࡥࡨࡻࠥᙄ"): orchestration_strategy,
                bstack1ll11_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡐࡩࡹࡧࡤࡢࡶࡤࠦᙅ"): orchestration_metadata,
                bstack1ll11_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᙆ"): int(os.environ.get(bstack1ll11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᙇ")) or bstack1ll11_opy_ (u"ࠨ࠰ࠣᙈ")),
                bstack1ll11_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᙉ"): int(os.environ.get(bstack1ll11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᙊ")) or bstack1ll11_opy_ (u"ࠤ࠴ࠦᙋ")),
                bstack1ll11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᙌ"): self.config.get(bstack1ll11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᙍ"), bstack1ll11_opy_ (u"ࠬ࠭ᙎ")),
                bstack1ll11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᙏ"): self.config.get(bstack1ll11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᙐ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1ll11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᙑ"): os.environ.get(bstack1ll11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᙒ"), bstack1ll11_opy_ (u"ࠥࠦᙓ")),
                bstack1ll11_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨᙔ"): get_host_info(),
                bstack1ll11_opy_ (u"ࠧࡶࡲࡅࡧࡷࡥ࡮ࡲࡳࠣᙕ"): bstack11ll1lll11l_opy_
            }
            self.logger.debug(bstack1ll11_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᙖ").format(payload))
            response = bstack11ll1llllll_opy_.bstack11lll111l11_opy_(self.bstack11ll1ll1l1l_opy_, payload)
            if response:
                self.bstack11ll1lllll1_opy_ = self._11lll11l11l_opy_(response)
                self.logger.debug(bstack1ll11_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᙗ").format(self.bstack11ll1lllll1_opy_))
            else:
                self.logger.error(bstack1ll11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣᙘ"))
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࡀࠠࡼࡿࠥᙙ").format(e))
    def _11lll11l11l_opy_(self, response):
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡦࡴࡤࠡࡧࡻࡸࡷࡧࡣࡵࡵࠣࡶࡪࡲࡥࡷࡣࡱࡸࠥ࡬ࡩࡦ࡮ࡧࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᙚ")
        bstack111l1ll1l1_opy_ = {}
        bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙛ")] = response.get(bstack1ll11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙜ"), self.default_timeout)
        bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᙝ")] = response.get(bstack1ll11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙞ"), self.bstack11lll11lll1_opy_)
        bstack11lll111lll_opy_ = response.get(bstack1ll11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᙟ"))
        bstack11ll1ll1ll1_opy_ = response.get(bstack1ll11_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᙠ"))
        if bstack11lll111lll_opy_:
            bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙡ")] = bstack11lll111lll_opy_.split(bstack11lll11l1ll_opy_ + bstack1ll11_opy_ (u"ࠦ࠴ࠨᙢ"))[1] if bstack11lll11l1ll_opy_ + bstack1ll11_opy_ (u"ࠧ࠵ࠢᙣ") in bstack11lll111lll_opy_ else bstack11lll111lll_opy_
        else:
            bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙤ")] = None
        if bstack11ll1ll1ll1_opy_:
            bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙥ")] = bstack11ll1ll1ll1_opy_.split(bstack11lll11l1ll_opy_ + bstack1ll11_opy_ (u"ࠣ࠱ࠥᙦ"))[1] if bstack11lll11l1ll_opy_ + bstack1ll11_opy_ (u"ࠤ࠲ࠦᙧ") in bstack11ll1ll1ll1_opy_ else bstack11ll1ll1ll1_opy_
        else:
            bstack111l1ll1l1_opy_[bstack1ll11_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙨ")] = None
        if (
            response.get(bstack1ll11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙩ")) is None or
            response.get(bstack1ll11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᙪ")) is None or
            response.get(bstack1ll11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙫ")) is None or
            response.get(bstack1ll11_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙬ")) is None
        ):
            self.logger.debug(bstack1ll11_opy_ (u"ࠣ࡝ࡳࡶࡴࡩࡥࡴࡵࡢࡷࡵࡲࡩࡵࡡࡷࡩࡸࡺࡳࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࡠࠤࡗ࡫ࡣࡦ࡫ࡹࡩࡩࠦ࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧࠫࡷ࠮ࠦࡦࡰࡴࠣࡷࡴࡳࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࡷࠥ࡯࡮ࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧ᙭"))
        return bstack111l1ll1l1_opy_
    def bstack11lll11ll1l_opy_(self):
        if not self.bstack11ll1lllll1_opy_:
            self.logger.error(bstack1ll11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠯ࠤ᙮"))
            return None
        bstack11ll1llll1l_opy_ = None
        test_files = []
        bstack11lll11111l_opy_ = int(time.time() * 1000) # bstack11lll1111l1_opy_ sec
        bstack11lll111l1l_opy_ = int(self.bstack11ll1lllll1_opy_.get(bstack1ll11_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙯ"), self.bstack11lll11lll1_opy_))
        bstack11lll11l111_opy_ = int(self.bstack11ll1lllll1_opy_.get(bstack1ll11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙰ"), self.default_timeout)) * 1000
        bstack11ll1ll1ll1_opy_ = self.bstack11ll1lllll1_opy_.get(bstack1ll11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙱ"), None)
        bstack11lll111lll_opy_ = self.bstack11ll1lllll1_opy_.get(bstack1ll11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙲ"), None)
        if bstack11lll111lll_opy_ is None and bstack11ll1ll1ll1_opy_ is None:
            return None
        try:
            while bstack11lll111lll_opy_ and (time.time() * 1000 - bstack11lll11111l_opy_) < bstack11lll11l111_opy_:
                response = bstack11ll1llllll_opy_.bstack11ll1lll111_opy_(bstack11lll111lll_opy_, {})
                if response and response.get(bstack1ll11_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙳ")):
                    bstack11ll1llll1l_opy_ = response.get(bstack1ll11_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙴ"))
                self.bstack11ll1lll1ll_opy_ += 1
                if bstack11ll1llll1l_opy_:
                    break
                time.sleep(bstack11lll111l1l_opy_)
                self.logger.debug(bstack1ll11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡊࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡶࡪࡹࡵ࡭ࡶ࡙ࠣࡗࡒࠠࡢࡨࡷࡩࡷࠦࡷࡢ࡫ࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࢀࢃࠠࡴࡧࡦࡳࡳࡪࡳ࠯ࠤᙵ").format(bstack11lll111l1l_opy_))
            if bstack11ll1ll1ll1_opy_ and not bstack11ll1llll1l_opy_:
                self.logger.debug(bstack1ll11_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡯࡭ࡦࡱࡸࡸ࡛ࠥࡒࡍࠤᙶ"))
                response = bstack11ll1llllll_opy_.bstack11ll1lll111_opy_(bstack11ll1ll1ll1_opy_, {})
                if response and response.get(bstack1ll11_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᙷ")):
                    bstack11ll1llll1l_opy_ = response.get(bstack1ll11_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙸ"))
            if bstack11ll1llll1l_opy_ and len(bstack11ll1llll1l_opy_) > 0:
                for bstack1ll1l111_opy_ in bstack11ll1llll1l_opy_:
                    file_path = bstack1ll1l111_opy_.get(bstack1ll11_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣᙹ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1llll1l_opy_:
                return None
            self.logger.debug(bstack1ll11_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡑࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡲࡦࡥࡨ࡭ࡻ࡫ࡤ࠻ࠢࡾࢁࠧᙺ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1ll11_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧᙻ").format(e))
            return None
    def bstack11ll1lll1l1_opy_(self):
        bstack1ll11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡥࡤࡰࡱࡹࠠ࡮ࡣࡧࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᙼ")
        return self.bstack11ll1lll1ll_opy_
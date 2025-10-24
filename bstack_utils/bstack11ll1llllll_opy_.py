# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import time
from bstack_utils.bstack11ll1l1ll1l_opy_ import bstack11ll1lll1ll_opy_
from bstack_utils.constants import bstack11ll1ll1111_opy_
from bstack_utils.helper import get_host_info, bstack11lll1111l1_opy_
class bstack11ll1ll111l_opy_:
    bstack1l1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡎࡡ࡯ࡦ࡯ࡩࡸࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳࠦࡷࡪࡶ࡫ࠤࡹ࡮ࡥࠡࡄࡵࡳࡼࡹࡥࡳࡕࡷࡥࡨࡱࠠࡴࡧࡵࡺࡪࡸ࠮ࠋࠢࠣࠤࠥࠨࠢࠣᙎ")
    def __init__(self, config, logger):
        bstack1l1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣ࠾ࡵࡧࡲࡢ࡯ࠣࡧࡴࡴࡦࡪࡩ࠽ࠤࡩ࡯ࡣࡵ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࠡࡥࡲࡲ࡫࡯ࡧࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡡࡶࡸࡷࡧࡴࡦࡩࡼ࠾ࠥࡹࡴࡳ࠮ࠣࡸࡪࡹࡴࠡࡱࡵࡨࡪࡸࡩ࡯ࡩࠣࡷࡹࡸࡡࡵࡧࡪࡽࠥࡴࡡ࡮ࡧࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙏ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll11l1_opy_ = bstack1l1_opy_ (u"ࠢࡵࡧࡶࡸࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱ࠳ࡦࡶࡩ࠰ࡸ࠴࠳ࡸࡶ࡬ࡪࡶ࠰ࡸࡪࡹࡴࡴࠤᙐ")
        self.bstack11ll1l1l1ll_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1l1ll11_opy_ = 5
        self.bstack11ll1lllll1_opy_ = 0
    def bstack11ll1lll111_opy_(self, test_files, orchestration_strategy, orchestration_metadata={}):
        bstack1l1_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤࠥࡏ࡮ࡪࡶ࡬ࡥࡹ࡫ࡳࠡࡶ࡫ࡩࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡶࡪࡷࡵࡦࡵࡷࠤࡦࡴࡤࠡࡵࡷࡳࡷ࡫ࡳࠡࡶ࡫ࡩࠥࡸࡥࡴࡲࡲࡲࡸ࡫ࠠࡥࡣࡷࡥࠥ࡬࡯ࡳࠢࡳࡳࡱࡲࡩ࡯ࡩ࠱ࠎࠥࠦࠠࠡࠢࠣࠤࠥࠨࠢࠣᙑ")
        self.logger.debug(bstack1l1_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡋࡱ࡭ࡹ࡯ࡡࡵ࡫ࡱ࡫ࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡻ࡮ࡺࡨࠡࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࢀࢃࠢᙒ").format(orchestration_strategy))
        try:
            bstack11ll1llll1l_opy_ = []
            bstack1l1_opy_ (u"ࠥࠦࠧ࡝ࡥࠡࡹ࡬ࡰࡱࠦ࡮ࡰࡶࠣࡪࡪࡺࡣࡩࠢࡪ࡭ࡹࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡ࡫ࡶࠤࡸࡵࡵࡳࡥࡨࠤ࡮ࡹࠠࡵࡻࡳࡩࠥࡵࡦࠡࡣࡵࡶࡦࡿࠠࡢࡰࡧࠤ࡮ࡺࠧࡴࠢࡨࡰࡪࡳࡥ࡯ࡶࡶࠤࡦࡸࡥࠡࡱࡩࠤࡹࡿࡰࡦࠢࡧ࡭ࡨࡺࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࡨࡥࡤࡣࡸࡷࡪࠦࡩ࡯ࠢࡷ࡬ࡦࡺࠠࡤࡣࡶࡩ࠱ࠦࡵࡴࡧࡵࠤ࡭ࡧࡳࠡࡲࡵࡳࡻ࡯ࡤࡦࡦࠣࡱࡺࡲࡴࡪ࠯ࡵࡩࡵࡵࠠࡴࡱࡸࡶࡨ࡫ࠠࡸ࡫ࡷ࡬ࠥ࡬ࡥࡢࡶࡸࡶࡪࡈࡲࡢࡰࡦ࡬ࠥ࡯࡮ࠡࡤࡵࡳࡼࡹࡥࡳࡵࡷࡥࡨࡱࠢࠣࠤᙓ")
            source = orchestration_metadata[bstack1l1_opy_ (u"ࠫࡷࡻ࡮ࡠࡵࡰࡥࡷࡺ࡟ࡴࡧ࡯ࡩࡨࡺࡩࡰࡰࠪᙔ")].get(bstack1l1_opy_ (u"ࠬࡹ࡯ࡶࡴࡦࡩࠬᙕ"), [])
            bstack11ll1ll11ll_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if orchestration_metadata[bstack1l1_opy_ (u"࠭ࡲࡶࡰࡢࡷࡲࡧࡲࡵࡡࡶࡩࡱ࡫ࡣࡵ࡫ࡲࡲࠬᙖ")].get(bstack1l1_opy_ (u"ࠧࡦࡰࡤࡦࡱ࡫ࡤࠨᙗ"), False) and not bstack11ll1ll11ll_opy_:
                bstack11ll1llll1l_opy_ = bstack11lll1111l1_opy_(source) # bstack11ll1ll1l11_opy_-repo is handled bstack11ll1ll1lll_opy_
            payload = {
                bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᙘ"): [{bstack1l1_opy_ (u"ࠤࡩ࡭ࡱ࡫ࡐࡢࡶ࡫ࠦᙙ"): f} for f in test_files],
                bstack1l1_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡖࡸࡷࡧࡴࡦࡩࡼࠦᙚ"): orchestration_strategy,
                bstack1l1_opy_ (u"ࠦࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࡑࡪࡺࡡࡥࡣࡷࡥࠧᙛ"): orchestration_metadata,
                bstack1l1_opy_ (u"ࠧࡴ࡯ࡥࡧࡌࡲࡩ࡫ࡸࠣᙜ"): int(os.environ.get(bstack1l1_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡔࡏࡅࡇࡢࡍࡓࡊࡅ࡙ࠤᙝ")) or bstack1l1_opy_ (u"ࠢ࠱ࠤᙞ")),
                bstack1l1_opy_ (u"ࠣࡶࡲࡸࡦࡲࡎࡰࡦࡨࡷࠧᙟ"): int(os.environ.get(bstack1l1_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡖࡒࡘࡆࡒ࡟ࡏࡑࡇࡉࡤࡉࡏࡖࡐࡗࠦᙠ")) or bstack1l1_opy_ (u"ࠥ࠵ࠧᙡ")),
                bstack1l1_opy_ (u"ࠦࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠤᙢ"): self.config.get(bstack1l1_opy_ (u"ࠬࡶࡲࡰ࡬ࡨࡧࡹࡔࡡ࡮ࡧࠪᙣ"), bstack1l1_opy_ (u"࠭ࠧᙤ")),
                bstack1l1_opy_ (u"ࠢࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠥᙥ"): self.config.get(bstack1l1_opy_ (u"ࠨࡤࡸ࡭ࡱࡪࡎࡢ࡯ࡨࠫᙦ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack1l1_opy_ (u"ࠤࡥࡹ࡮ࡲࡤࡓࡷࡱࡍࡩ࡫࡮ࡵ࡫ࡩ࡭ࡪࡸࠢᙧ"): os.environ.get(bstack1l1_opy_ (u"ࠥࡆࡗࡕࡗࡔࡇࡕࡗ࡙ࡇࡃࡌࡡࡅ࡙ࡎࡒࡄࡠࡔࡘࡒࡤࡏࡄࡆࡐࡗࡍࡋࡏࡅࡓࠤᙨ"), bstack1l1_opy_ (u"ࠦࠧᙩ")),
                bstack1l1_opy_ (u"ࠧ࡮࡯ࡴࡶࡌࡲ࡫ࡵࠢᙪ"): get_host_info(),
                bstack1l1_opy_ (u"ࠨࡰࡳࡆࡨࡸࡦ࡯࡬ࡴࠤᙫ"): bstack11ll1llll1l_opy_
            }
            self.logger.debug(bstack1l1_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡦࡰࡧ࡭ࡳ࡭ࠠࡵࡧࡶࡸࠥ࡬ࡩ࡭ࡧࡶ࠾ࠥࢁࡽࠣᙬ").format(payload))
            response = bstack11ll1lll1ll_opy_.bstack11ll1lll11l_opy_(self.bstack11ll1ll11l1_opy_, payload)
            if response:
                self.bstack11ll1l1l1ll_opy_ = self._11lll111l1l_opy_(response)
                self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡔࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠺ࠡࡽࢀࠦ᙭").format(self.bstack11ll1l1l1ll_opy_))
            else:
                self.logger.error(bstack1l1_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡈࡤ࡭ࡱ࡫ࡤࠡࡶࡲࠤ࡬࡫ࡴࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡵࡳࡳࡳࡹࡥ࠯ࠤ᙮"))
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡵࡨࡲࡩ࡯࡮ࡨࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࡀ࠺ࠡࡽࢀࠦᙯ").format(e))
    def _11lll111l1l_opy_(self, response):
        bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡒࡵࡳࡨ࡫ࡳࡴࡧࡶࠤࡹ࡮ࡥࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠥࡧ࡮ࡥࠢࡨࡼࡹࡸࡡࡤࡶࡶࠤࡷ࡫࡬ࡦࡸࡤࡲࡹࠦࡦࡪࡧ࡯ࡨࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᙰ")
        bstack11111l1ll_opy_ = {}
        bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙱ")] = response.get(bstack1l1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࠢᙲ"), self.default_timeout)
        bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙳ")] = response.get(bstack1l1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡋࡱࡸࡪࡸࡶࡢ࡮ࠥᙴ"), self.bstack11ll1l1ll11_opy_)
        bstack11ll1llll11_opy_ = response.get(bstack1l1_opy_ (u"ࠤࡵࡩࡸࡻ࡬ࡵࡗࡵࡰࠧᙵ"))
        bstack11lll111l11_opy_ = response.get(bstack1l1_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙶ"))
        if bstack11ll1llll11_opy_:
            bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙷ")] = bstack11ll1llll11_opy_.split(bstack11ll1ll1111_opy_ + bstack1l1_opy_ (u"ࠧ࠵ࠢᙸ"))[1] if bstack11ll1ll1111_opy_ + bstack1l1_opy_ (u"ࠨ࠯ࠣᙹ") in bstack11ll1llll11_opy_ else bstack11ll1llll11_opy_
        else:
            bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙺ")] = None
        if bstack11lll111l11_opy_:
            bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࡗࡵࡰࠧᙻ")] = bstack11lll111l11_opy_.split(bstack11ll1ll1111_opy_ + bstack1l1_opy_ (u"ࠤ࠲ࠦᙼ"))[1] if bstack11ll1ll1111_opy_ + bstack1l1_opy_ (u"ࠥ࠳ࠧᙽ") in bstack11lll111l11_opy_ else bstack11lll111l11_opy_
        else:
            bstack11111l1ll_opy_[bstack1l1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙾ")] = None
        if (
            response.get(bstack1l1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙿ")) is None or
            response.get(bstack1l1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣ ")) is None or
            response.get(bstack1l1_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᚁ")) is None or
            response.get(bstack1l1_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᚂ")) is None
        ):
            self.logger.debug(bstack1l1_opy_ (u"ࠤ࡞ࡴࡷࡵࡣࡦࡵࡶࡣࡸࡶ࡬ࡪࡶࡢࡸࡪࡹࡴࡴࡡࡵࡩࡸࡶ࡯࡯ࡵࡨࡡࠥࡘࡥࡤࡧ࡬ࡺࡪࡪࠠ࡯ࡷ࡯ࡰࠥࡼࡡ࡭ࡷࡨࠬࡸ࠯ࠠࡧࡱࡵࠤࡸࡵ࡭ࡦࠢࡤࡸࡹࡸࡩࡣࡷࡷࡩࡸࠦࡩ࡯ࠢࡶࡴࡱ࡯ࡴࠡࡶࡨࡷࡹࡹࠠࡂࡒࡌࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠨᚃ"))
        return bstack11111l1ll_opy_
    def bstack11lll111111_opy_(self):
        if not self.bstack11ll1l1l1ll_opy_:
            self.logger.error(bstack1l1_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡓࡵࠠࡳࡧࡴࡹࡪࡹࡴࠡࡦࡤࡸࡦࠦࡡࡷࡣ࡬ࡰࡦࡨ࡬ࡦࠢࡷࡳࠥ࡬ࡥࡵࡥ࡫ࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠰ࠥᚄ"))
            return None
        bstack11ll1ll1ll1_opy_ = None
        test_files = []
        bstack11lll1111ll_opy_ = int(time.time() * 1000) # bstack11ll1l1lll1_opy_ sec
        bstack11ll1ll1l1l_opy_ = int(self.bstack11ll1l1l1ll_opy_.get(bstack1l1_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᚅ"), self.bstack11ll1l1ll11_opy_))
        bstack11ll1lll1l1_opy_ = int(self.bstack11ll1l1l1ll_opy_.get(bstack1l1_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᚆ"), self.default_timeout)) * 1000
        bstack11lll111l11_opy_ = self.bstack11ll1l1l1ll_opy_.get(bstack1l1_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᚇ"), None)
        bstack11ll1llll11_opy_ = self.bstack11ll1l1l1ll_opy_.get(bstack1l1_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᚈ"), None)
        if bstack11ll1llll11_opy_ is None and bstack11lll111l11_opy_ is None:
            return None
        try:
            while bstack11ll1llll11_opy_ and (time.time() * 1000 - bstack11lll1111ll_opy_) < bstack11ll1lll1l1_opy_:
                response = bstack11ll1lll1ll_opy_.bstack11lll11111l_opy_(bstack11ll1llll11_opy_, {})
                if response and response.get(bstack1l1_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢᚉ")):
                    bstack11ll1ll1ll1_opy_ = response.get(bstack1l1_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣᚊ"))
                self.bstack11ll1lllll1_opy_ += 1
                if bstack11ll1ll1ll1_opy_:
                    break
                time.sleep(bstack11ll1ll1l1l_opy_)
                self.logger.debug(bstack1l1_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡷ࡫ࡳࡶ࡮ࡷࠤ࡚ࡘࡌࠡࡣࡩࡸࡪࡸࠠࡸࡣ࡬ࡸ࡮ࡴࡧࠡࡨࡲࡶࠥࢁࡽࠡࡵࡨࡧࡴࡴࡤࡴ࠰ࠥᚋ").format(bstack11ll1ll1l1l_opy_))
            if bstack11lll111l11_opy_ and not bstack11ll1ll1ll1_opy_:
                self.logger.debug(bstack1l1_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡌࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࡹࠠࡧࡴࡲࡱࠥࡺࡩ࡮ࡧࡲࡹࡹࠦࡕࡓࡎࠥᚌ"))
                response = bstack11ll1lll1ll_opy_.bstack11lll11111l_opy_(bstack11lll111l11_opy_, {})
                if response and response.get(bstack1l1_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᚍ")):
                    bstack11ll1ll1ll1_opy_ = response.get(bstack1l1_opy_ (u"ࠨࡴࡦࡵࡷࡷࠧᚎ"))
            if bstack11ll1ll1ll1_opy_ and len(bstack11ll1ll1ll1_opy_) > 0:
                for bstack1l11lll1_opy_ in bstack11ll1ll1ll1_opy_:
                    file_path = bstack1l11lll1_opy_.get(bstack1l1_opy_ (u"ࠢࡧ࡫࡯ࡩࡕࡧࡴࡩࠤᚏ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1ll1ll1_opy_:
                return None
            self.logger.debug(bstack1l1_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡒࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹࠠࡳࡧࡦࡩ࡮ࡼࡥࡥ࠼ࠣࡿࢂࠨᚐ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack1l1_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡩ࡯ࠢࡩࡩࡹࡩࡨࡪࡰࡪࠤࡴࡸࡤࡦࡴࡨࡨࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼ࠣࡿࢂࠨᚑ").format(e))
            return None
    def bstack11ll1l1llll_opy_(self):
        bstack1l1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡓࡧࡷࡹࡷࡴࡳࠡࡶ࡫ࡩࠥࡩ࡯ࡶࡰࡷࠤࡴ࡬ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡦࡥࡱࡲࡳࠡ࡯ࡤࡨࡪ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᚒ")
        return self.bstack11ll1lllll1_opy_
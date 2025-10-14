# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import time
from bstack_utils.bstack11lll111l1l_opy_ import bstack11ll1lllll1_opy_
from bstack_utils.constants import bstack11ll1llllll_opy_
from bstack_utils.helper import get_host_info, bstack11lll1111ll_opy_
class bstack11lll111lll_opy_:
    bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡍࡧ࡮ࡥ࡮ࡨࡷࠥࡺࡥࡴࡶࠣࡳࡷࡪࡥࡳ࡫ࡱ࡫ࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࠥࡽࡩࡵࡪࠣࡸ࡭࡫ࠠࡃࡴࡲࡻࡸ࡫ࡲࡔࡶࡤࡧࡰࠦࡳࡦࡴࡹࡩࡷ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᘱ")
    def __init__(self, config, logger):
        bstack11l1l11_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢ࠽ࡴࡦࡸࡡ࡮ࠢࡦࡳࡳ࡬ࡩࡨ࠼ࠣࡨ࡮ࡩࡴ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࠠࡤࡱࡱࡪ࡮࡭ࠊࠡࠢࠣࠤࠥࠦࠠࠡ࠼ࡳࡥࡷࡧ࡭ࠡࡱࡵࡧ࡭࡫ࡳࡵࡴࡤࡸ࡮ࡵ࡮ࡠࡵࡷࡶࡦࡺࡥࡨࡻ࠽ࠤࡸࡺࡲ࠭ࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡶࡸࡷࡧࡴࡦࡩࡼࠤࡳࡧ࡭ࡦࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᘲ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1ll1_opy_ = bstack11l1l11_opy_ (u"ࠨࡴࡦࡵࡷࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰ࠲ࡥࡵ࡯࠯ࡷ࠳࠲ࡷࡵࡲࡩࡵ࠯ࡷࡩࡸࡺࡳࠣᘳ")
        self.bstack11ll1ll1lll_opy_ = None
        self.default_timeout = 60
        self.bstack11lll111ll1_opy_ = 5
        self.bstack11lll11l11l_opy_ = 0
    def bstack11lll11l111_opy_(self, test_files, orchestration_strategy, bstack1l1l1ll1lll_opy_={}):
        bstack11l1l11_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡎࡴࡩࡵ࡫ࡤࡸࡪࡹࠠࡵࡪࡨࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡶࡻࡥࡴࡶࠣࡥࡳࡪࠠࡴࡶࡲࡶࡪࡹࠠࡵࡪࡨࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࠦࡤࡢࡶࡤࠤ࡫ࡵࡲࠡࡲࡲࡰࡱ࡯࡮ࡨ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘴ")
        self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡊࡰ࡬ࡸ࡮ࡧࡴࡪࡰࡪࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡺ࡭ࡹ࡮ࠠࡴࡶࡵࡥࡹ࡫ࡧࡺ࠼ࠣࡿࢂࠨᘵ").format(orchestration_strategy))
        try:
            bstack11ll1lll1ll_opy_ = []
            bstack11l1l11_opy_ (u"ࠤࠥࠦ࡜࡫ࠠࡸ࡫࡯ࡰࠥࡴ࡯ࡵࠢࡩࡩࡹࡩࡨࠡࡩ࡬ࡸࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡪࡵࠣࡷࡴࡻࡲࡤࡧࠣ࡭ࡸࠦࡴࡺࡲࡨࠤࡴ࡬ࠠࡢࡴࡵࡥࡾࠦࡡ࡯ࡦࠣ࡭ࡹ࠭ࡳࠡࡧ࡯ࡩࡲ࡫࡮ࡵࡵࠣࡥࡷ࡫ࠠࡰࡨࠣࡸࡾࡶࡥࠡࡦ࡬ࡧࡹࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࡧ࡫ࡣࡢࡷࡶࡩࠥ࡯࡮ࠡࡶ࡫ࡥࡹࠦࡣࡢࡵࡨ࠰ࠥࡻࡳࡦࡴࠣ࡬ࡦࡹࠠࡱࡴࡲࡺ࡮ࡪࡥࡥࠢࡰࡹࡱࡺࡩ࠮ࡴࡨࡴࡴࠦࡳࡰࡷࡵࡧࡪࠦࡷࡪࡶ࡫ࠤ࡫࡫ࡡࡵࡷࡵࡩࡇࡸࡡ࡯ࡥ࡫ࠤ࡮ࡴࠠࡣࡴࡲࡻࡸ࡫ࡲࡴࡶࡤࡧࡰࠨࠢࠣᘶ")
            source = bstack1l1l1ll1lll_opy_[bstack11l1l11_opy_ (u"ࠪࡶࡺࡴ࡟ࡴ࡯ࡤࡶࡹࡥࡳࡦ࡮ࡨࡧࡹ࡯࡯࡯ࠩᘷ")].get(bstack11l1l11_opy_ (u"ࠫࡸࡵࡵࡳࡥࡨࠫᘸ"), [])
            bstack11lll1111l1_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if bstack1l1l1ll1lll_opy_[bstack11l1l11_opy_ (u"ࠬࡸࡵ࡯ࡡࡶࡱࡦࡸࡴࡠࡵࡨࡰࡪࡩࡴࡪࡱࡱࠫᘹ")].get(bstack11l1l11_opy_ (u"࠭ࡥ࡯ࡣࡥࡰࡪࡪࠧᘺ"), False) and not bstack11lll1111l1_opy_:
                bstack11ll1lll1ll_opy_ = bstack11lll1111ll_opy_(source) # bstack11lll11l1l1_opy_-repo is handled bstack11ll1lll1l1_opy_
            payload = {
                bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᘻ"): [{bstack11l1l11_opy_ (u"ࠣࡨ࡬ࡰࡪࡖࡡࡵࡪࠥᘼ"): f} for f in test_files],
                bstack11l1l11_opy_ (u"ࠤࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࡕࡷࡶࡦࡺࡥࡨࡻࠥᘽ"): orchestration_strategy,
                bstack11l1l11_opy_ (u"ࠥࡳࡷࡩࡨࡦࡵࡷࡶࡦࡺࡩࡰࡰࡐࡩࡹࡧࡤࡢࡶࡤࠦᘾ"): bstack1l1l1ll1lll_opy_,
                bstack11l1l11_opy_ (u"ࠦࡳࡵࡤࡦࡋࡱࡨࡪࡾࠢᘿ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣࡓࡕࡄࡆࡡࡌࡒࡉࡋࡘࠣᙀ")) or bstack11l1l11_opy_ (u"ࠨ࠰ࠣᙁ")),
                bstack11l1l11_opy_ (u"ࠢࡵࡱࡷࡥࡱࡔ࡯ࡥࡧࡶࠦᙂ"): int(os.environ.get(bstack11l1l11_opy_ (u"ࠣࡄࡕࡓ࡜࡙ࡅࡓࡕࡗࡅࡈࡑ࡟ࡕࡑࡗࡅࡑࡥࡎࡐࡆࡈࡣࡈࡕࡕࡏࡖࠥᙃ")) or bstack11l1l11_opy_ (u"ࠤ࠴ࠦᙄ")),
                bstack11l1l11_opy_ (u"ࠥࡴࡷࡵࡪࡦࡥࡷࡒࡦࡳࡥࠣᙅ"): self.config.get(bstack11l1l11_opy_ (u"ࠫࡵࡸ࡯࡫ࡧࡦࡸࡓࡧ࡭ࡦࠩᙆ"), bstack11l1l11_opy_ (u"ࠬ࠭ᙇ")),
                bstack11l1l11_opy_ (u"ࠨࡢࡶ࡫࡯ࡨࡓࡧ࡭ࡦࠤᙈ"): self.config.get(bstack11l1l11_opy_ (u"ࠧࡣࡷ࡬ࡰࡩࡔࡡ࡮ࡧࠪᙉ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack11l1l11_opy_ (u"ࠣࡤࡸ࡭ࡱࡪࡒࡶࡰࡌࡨࡪࡴࡴࡪࡨ࡬ࡩࡷࠨᙊ"): os.environ.get(bstack11l1l11_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡄࡘࡍࡑࡊ࡟ࡓࡗࡑࡣࡎࡊࡅࡏࡖࡌࡊࡎࡋࡒࠣᙋ"), bstack11l1l11_opy_ (u"ࠥࠦᙌ")),
                bstack11l1l11_opy_ (u"ࠦ࡭ࡵࡳࡵࡋࡱࡪࡴࠨᙍ"): get_host_info(),
                bstack11l1l11_opy_ (u"ࠧࡶࡲࡅࡧࡷࡥ࡮ࡲࡳࠣᙎ"): bstack11ll1lll1ll_opy_
            }
            self.logger.debug(bstack11l1l11_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡ࡙ࠥࡥ࡯ࡦ࡬ࡲ࡬ࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵ࠽ࠤࢀࢃࠢᙏ").format(payload))
            response = bstack11ll1lllll1_opy_.bstack11ll1ll1l11_opy_(self.bstack11ll1ll1ll1_opy_, payload)
            if response:
                self.bstack11ll1ll1lll_opy_ = self._11lll111l11_opy_(response)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡵࡳࡰ࡮ࡺࡔࡦࡵࡷࡷࡢࠦࡓࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡷ࡫ࡳࡱࡱࡱࡷࡪࡀࠠࡼࡿࠥᙐ").format(self.bstack11ll1ll1lll_opy_))
            else:
                self.logger.error(bstack11l1l11_opy_ (u"ࠣ࡝ࡶࡴࡱ࡯ࡴࡕࡧࡶࡸࡸࡣࠠࡇࡣ࡬ࡰࡪࡪࠠࡵࡱࠣ࡫ࡪࡺࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡸࡥࡴࡲࡲࡲࡸ࡫࠮ࠣᙑ"))
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤ࡞ࡷࡵࡲࡩࡵࡖࡨࡷࡹࡹ࡝ࠡࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤ࡮ࡴࠠࡴࡧࡱࡨ࡮ࡴࡧࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࡀࠠࡼࡿࠥᙒ").format(e))
    def _11lll111l11_opy_(self, response):
        bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡑࡴࡲࡧࡪࡹࡳࡦࡵࠣࡸ࡭࡫ࠠࡴࡲ࡯࡭ࡹࠦࡴࡦࡵࡷࡷࠥࡇࡐࡊࠢࡵࡩࡸࡶ࡯࡯ࡵࡨࠤࡦࡴࡤࠡࡧࡻࡸࡷࡧࡣࡵࡵࠣࡶࡪࡲࡥࡷࡣࡱࡸࠥ࡬ࡩࡦ࡮ࡧࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᙓ")
        bstack1ll11l11l1_opy_ = {}
        bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙔ")] = response.get(bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࠨᙕ"), self.default_timeout)
        bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡉ࡯ࡶࡨࡶࡻࡧ࡬ࠣᙖ")] = response.get(bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙗ"), self.bstack11lll111ll1_opy_)
        bstack11ll1ll11ll_opy_ = response.get(bstack11l1l11_opy_ (u"ࠣࡴࡨࡷࡺࡲࡴࡖࡴ࡯ࠦᙘ"))
        bstack11ll1ll1l1l_opy_ = response.get(bstack11l1l11_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᙙ"))
        if bstack11ll1ll11ll_opy_:
            bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙚ")] = bstack11ll1ll11ll_opy_.split(bstack11ll1llllll_opy_ + bstack11l1l11_opy_ (u"ࠦ࠴ࠨᙛ"))[1] if bstack11ll1llllll_opy_ + bstack11l1l11_opy_ (u"ࠧ࠵ࠢᙜ") in bstack11ll1ll11ll_opy_ else bstack11ll1ll11ll_opy_
        else:
            bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙝ")] = None
        if bstack11ll1ll1l1l_opy_:
            bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙞ")] = bstack11ll1ll1l1l_opy_.split(bstack11ll1llllll_opy_ + bstack11l1l11_opy_ (u"ࠣ࠱ࠥᙟ"))[1] if bstack11ll1llllll_opy_ + bstack11l1l11_opy_ (u"ࠤ࠲ࠦᙠ") in bstack11ll1ll1l1l_opy_ else bstack11ll1ll1l1l_opy_
        else:
            bstack1ll11l11l1_opy_[bstack11l1l11_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙡ")] = None
        if (
            response.get(bstack11l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙢ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹࡏ࡮ࡵࡧࡵࡺࡦࡲࠢᙣ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙤ")) is None or
            response.get(bstack11l1l11_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙥ")) is None
        ):
            self.logger.debug(bstack11l1l11_opy_ (u"ࠣ࡝ࡳࡶࡴࡩࡥࡴࡵࡢࡷࡵࡲࡩࡵࡡࡷࡩࡸࡺࡳࡠࡴࡨࡷࡵࡵ࡮ࡴࡧࡠࠤࡗ࡫ࡣࡦ࡫ࡹࡩࡩࠦ࡮ࡶ࡮࡯ࠤࡻࡧ࡬ࡶࡧࠫࡷ࠮ࠦࡦࡰࡴࠣࡷࡴࡳࡥࠡࡣࡷࡸࡷ࡯ࡢࡶࡶࡨࡷࠥ࡯࡮ࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡁࡑࡋࠣࡶࡪࡹࡰࡰࡰࡶࡩࠧᙦ"))
        return bstack1ll11l11l1_opy_
    def bstack11ll1ll11l1_opy_(self):
        if not self.bstack11ll1ll1lll_opy_:
            self.logger.error(bstack11l1l11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡒࡴࠦࡲࡦࡳࡸࡩࡸࡺࠠࡥࡣࡷࡥࠥࡧࡶࡢ࡫࡯ࡥࡧࡲࡥࠡࡶࡲࠤ࡫࡫ࡴࡤࡪࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠯ࠤᙧ"))
            return None
        bstack11ll1lll111_opy_ = None
        test_files = []
        bstack11ll1llll1l_opy_ = int(time.time() * 1000) # bstack11ll1llll11_opy_ sec
        bstack11lll111111_opy_ = int(self.bstack11ll1ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙨ"), self.bstack11lll111ll1_opy_))
        bstack11ll1lll11l_opy_ = int(self.bstack11ll1ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࠧᙩ"), self.default_timeout)) * 1000
        bstack11ll1ll1l1l_opy_ = self.bstack11ll1ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠧࡺࡩ࡮ࡧࡲࡹࡹ࡛ࡲ࡭ࠤᙪ"), None)
        bstack11ll1ll11ll_opy_ = self.bstack11ll1ll1lll_opy_.get(bstack11l1l11_opy_ (u"ࠨࡲࡦࡵࡸࡰࡹ࡛ࡲ࡭ࠤᙫ"), None)
        if bstack11ll1ll11ll_opy_ is None and bstack11ll1ll1l1l_opy_ is None:
            return None
        try:
            while bstack11ll1ll11ll_opy_ and (time.time() * 1000 - bstack11ll1llll1l_opy_) < bstack11ll1lll11l_opy_:
                response = bstack11ll1lllll1_opy_.bstack11lll11l1ll_opy_(bstack11ll1ll11ll_opy_, {})
                if response and response.get(bstack11l1l11_opy_ (u"ࠢࡵࡧࡶࡸࡸࠨᙬ")):
                    bstack11ll1lll111_opy_ = response.get(bstack11l1l11_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢ᙭"))
                self.bstack11lll11l11l_opy_ += 1
                if bstack11ll1lll111_opy_:
                    break
                time.sleep(bstack11lll111111_opy_)
                self.logger.debug(bstack11l1l11_opy_ (u"ࠤ࡞࡫ࡪࡺࡏࡳࡦࡨࡶࡪࡪࡔࡦࡵࡷࡊ࡮ࡲࡥࡴ࡟ࠣࡊࡪࡺࡣࡩ࡫ࡱ࡫ࠥࡵࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࡷࠥ࡬ࡲࡰ࡯ࠣࡶࡪࡹࡵ࡭ࡶ࡙ࠣࡗࡒࠠࡢࡨࡷࡩࡷࠦࡷࡢ࡫ࡷ࡭ࡳ࡭ࠠࡧࡱࡵࠤࢀࢃࠠࡴࡧࡦࡳࡳࡪࡳ࠯ࠤ᙮").format(bstack11lll111111_opy_))
            if bstack11ll1ll1l1l_opy_ and not bstack11ll1lll111_opy_:
                self.logger.debug(bstack11l1l11_opy_ (u"ࠥ࡟࡬࡫ࡴࡐࡴࡧࡩࡷ࡫ࡤࡕࡧࡶࡸࡋ࡯࡬ࡦࡵࡠࠤࡋ࡫ࡴࡤࡪ࡬ࡲ࡬ࠦ࡯ࡳࡦࡨࡶࡪࡪࠠࡵࡧࡶࡸࡸࠦࡦࡳࡱࡰࠤࡹ࡯࡭ࡦࡱࡸࡸ࡛ࠥࡒࡍࠤᙯ"))
                response = bstack11ll1lllll1_opy_.bstack11lll11l1ll_opy_(bstack11ll1ll1l1l_opy_, {})
                if response and response.get(bstack11l1l11_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᙰ")):
                    bstack11ll1lll111_opy_ = response.get(bstack11l1l11_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙱ"))
            if bstack11ll1lll111_opy_ and len(bstack11ll1lll111_opy_) > 0:
                for bstack1l11lll1_opy_ in bstack11ll1lll111_opy_:
                    file_path = bstack1l11lll1_opy_.get(bstack11l1l11_opy_ (u"ࠨࡦࡪ࡮ࡨࡔࡦࡺࡨࠣᙲ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11ll1lll111_opy_:
                return None
            self.logger.debug(bstack11l1l11_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡑࡵࡨࡪࡸࡥࡥࠢࡷࡩࡸࡺࠠࡧ࡫࡯ࡩࡸࠦࡲࡦࡥࡨ࡭ࡻ࡫ࡤ࠻ࠢࡾࢁࠧᙳ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack11l1l11_opy_ (u"ࠣ࡝ࡪࡩࡹࡕࡲࡥࡧࡵࡩࡩ࡚ࡥࡴࡶࡉ࡭ࡱ࡫ࡳ࡞ࠢࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥ࡯࡮ࠡࡨࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࠢࡩ࡭ࡱ࡫ࡳ࠻ࠢࡾࢁࠧᙴ").format(e))
            return None
    def bstack11lll11111l_opy_(self):
        bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡒࡦࡶࡸࡶࡳࡹࠠࡵࡪࡨࠤࡨࡵࡵ࡯ࡶࠣࡳ࡫ࠦࡳࡱ࡮࡬ࡸࠥࡺࡥࡴࡶࡶࠤࡆࡖࡉࠡࡥࡤࡰࡱࡹࠠ࡮ࡣࡧࡩ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᙵ")
        return self.bstack11lll11l11l_opy_
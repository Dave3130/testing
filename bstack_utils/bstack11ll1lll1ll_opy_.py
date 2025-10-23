# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import os
import time
from bstack_utils.bstack11ll1lllll1_opy_ import bstack11lll111111_opy_
from bstack_utils.constants import bstack11lll11111l_opy_
from bstack_utils.helper import get_host_info, bstack11lll111l11_opy_
class bstack11ll1ll11l1_opy_:
    bstack111111l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡊࡤࡲࡩࡲࡥࡴࠢࡷࡩࡸࡺࠠࡰࡴࡧࡩࡷ࡯࡮ࡨࠢࡲࡶࡨ࡮ࡥࡴࡶࡵࡥࡹ࡯࡯࡯ࠢࡺ࡭ࡹ࡮ࠠࡵࡪࡨࠤࡇࡸ࡯ࡸࡵࡨࡶࡘࡺࡡࡤ࡭ࠣࡷࡪࡸࡶࡦࡴ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᘮ")
    def __init__(self, config, logger):
        bstack111111l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦ࠺ࡱࡣࡵࡥࡲࠦࡣࡰࡰࡩ࡭࡬ࡀࠠࡥ࡫ࡦࡸ࠱ࠦࡴࡦࡵࡷࠤࡴࡸࡣࡩࡧࡶࡸࡷࡧࡴࡪࡱࡱࠤࡨࡵ࡮ࡧ࡫ࡪࠎࠥࠦࠠࠡࠢࠣࠤࠥࡀࡰࡢࡴࡤࡱࠥࡵࡲࡤࡪࡨࡷࡹࡸࡡࡵ࡫ࡲࡲࡤࡹࡴࡳࡣࡷࡩ࡬ࡿ࠺ࠡࡵࡷࡶ࠱ࠦࡴࡦࡵࡷࠤࡴࡸࡤࡦࡴ࡬ࡲ࡬ࠦࡳࡵࡴࡤࡸࡪ࡭ࡹࠡࡰࡤࡱࡪࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᘯ")
        self.config = config
        self.logger = logger
        self.bstack11ll1ll1l11_opy_ = bstack111111l_opy_ (u"ࠥࡸࡪࡹࡴࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴ࠯ࡢࡲ࡬࠳ࡻ࠷࠯ࡴࡲ࡯࡭ࡹ࠳ࡴࡦࡵࡷࡷࠧᘰ")
        self.bstack11lll11l11l_opy_ = None
        self.default_timeout = 60
        self.bstack11ll1ll1lll_opy_ = 5
        self.bstack11lll1111l1_opy_ = 0
    def bstack11lll11l111_opy_(self, test_files, orchestration_strategy, bstack1l11lllll1l_opy_={}):
        bstack111111l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡋࡱ࡭ࡹ࡯ࡡࡵࡧࡶࠤࡹ࡮ࡥࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡲࡦࡳࡸࡩࡸࡺࠠࡢࡰࡧࠤࡸࡺ࡯ࡳࡧࡶࠤࡹ࡮ࡥࠡࡴࡨࡷࡵࡵ࡮ࡴࡧࠣࡨࡦࡺࡡࠡࡨࡲࡶࠥࡶ࡯࡭࡮࡬ࡲ࡬࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘱ")
        self.logger.debug(bstack111111l_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡎࡴࡩࡵ࡫ࡤࡸ࡮ࡴࡧࠡࡵࡳࡰ࡮ࡺࠠࡵࡧࡶࡸࡸࠦࡷࡪࡶ࡫ࠤࡸࡺࡲࡢࡶࡨ࡫ࡾࡀࠠࡼࡿࠥᘲ").format(orchestration_strategy))
        try:
            bstack11ll1ll11ll_opy_ = []
            bstack111111l_opy_ (u"ࠨ࡙ࠢࠣࡨࠤࡼ࡯࡬࡭ࠢࡱࡳࡹࠦࡦࡦࡶࡦ࡬ࠥ࡭ࡩࡵࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤ࡮ࡹࠠࡴࡱࡸࡶࡨ࡫ࠠࡪࡵࠣࡸࡾࡶࡥࠡࡱࡩࠤࡦࡸࡲࡢࡻࠣࡥࡳࡪࠠࡪࡶࠪࡷࠥ࡫࡬ࡦ࡯ࡨࡲࡹࡹࠠࡢࡴࡨࠤࡴ࡬ࠠࡵࡻࡳࡩࠥࡪࡩࡤࡶࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࡤࡨࡧࡦࡻࡳࡦࠢ࡬ࡲࠥࡺࡨࡢࡶࠣࡧࡦࡹࡥ࠭ࠢࡸࡷࡪࡸࠠࡩࡣࡶࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡩࠦ࡭ࡶ࡮ࡷ࡭࠲ࡸࡥࡱࡱࠣࡷࡴࡻࡲࡤࡧࠣࡻ࡮ࡺࡨࠡࡨࡨࡥࡹࡻࡲࡦࡄࡵࡥࡳࡩࡨࠡ࡫ࡱࠤࡧࡸ࡯ࡸࡵࡨࡶࡸࡺࡡࡤ࡭ࠥࠦࠧᘳ")
            source = bstack1l11lllll1l_opy_[bstack111111l_opy_ (u"ࠧࡳࡷࡱࡣࡸࡳࡡࡳࡶࡢࡷࡪࡲࡥࡤࡶ࡬ࡳࡳ࠭ᘴ")].get(bstack111111l_opy_ (u"ࠨࡵࡲࡹࡷࡩࡥࠨᘵ"), [])
            bstack11ll1ll1l1l_opy_ = isinstance(source, list) and all(isinstance(src, dict) and src is not None for src in source) and len(source) > 0
            if bstack1l11lllll1l_opy_[bstack111111l_opy_ (u"ࠩࡵࡹࡳࡥࡳ࡮ࡣࡵࡸࡤࡹࡥ࡭ࡧࡦࡸ࡮ࡵ࡮ࠨᘶ")].get(bstack111111l_opy_ (u"ࠪࡩࡳࡧࡢ࡭ࡧࡧࠫᘷ"), False) and not bstack11ll1ll1l1l_opy_:
                bstack11ll1ll11ll_opy_ = bstack11lll111l11_opy_(source) # bstack11lll11l1ll_opy_-repo is handled bstack11ll1llll11_opy_
            payload = {
                bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᘸ"): [{bstack111111l_opy_ (u"ࠧ࡬ࡩ࡭ࡧࡓࡥࡹ࡮ࠢᘹ"): f} for f in test_files],
                bstack111111l_opy_ (u"ࠨ࡯ࡳࡥ࡫ࡩࡸࡺࡲࡢࡶ࡬ࡳࡳ࡙ࡴࡳࡣࡷࡩ࡬ࡿࠢᘺ"): orchestration_strategy,
                bstack111111l_opy_ (u"ࠢࡰࡴࡦ࡬ࡪࡹࡴࡳࡣࡷ࡭ࡴࡴࡍࡦࡶࡤࡨࡦࡺࡡࠣᘻ"): bstack1l11lllll1l_opy_,
                bstack111111l_opy_ (u"ࠣࡰࡲࡨࡪࡏ࡮ࡥࡧࡻࠦᘼ"): int(os.environ.get(bstack111111l_opy_ (u"ࠤࡅࡖࡔ࡝ࡓࡆࡔࡖࡘࡆࡉࡋࡠࡐࡒࡈࡊࡥࡉࡏࡆࡈ࡜ࠧᘽ")) or bstack111111l_opy_ (u"ࠥ࠴ࠧᘾ")),
                bstack111111l_opy_ (u"ࠦࡹࡵࡴࡢ࡮ࡑࡳࡩ࡫ࡳࠣᘿ"): int(os.environ.get(bstack111111l_opy_ (u"ࠧࡈࡒࡐ࡙ࡖࡉࡗ࡙ࡔࡂࡅࡎࡣ࡙ࡕࡔࡂࡎࡢࡒࡔࡊࡅࡠࡅࡒ࡙ࡓ࡚ࠢᙀ")) or bstack111111l_opy_ (u"ࠨ࠱ࠣᙁ")),
                bstack111111l_opy_ (u"ࠢࡱࡴࡲ࡮ࡪࡩࡴࡏࡣࡰࡩࠧᙂ"): self.config.get(bstack111111l_opy_ (u"ࠨࡲࡵࡳ࡯࡫ࡣࡵࡐࡤࡱࡪ࠭ᙃ"), bstack111111l_opy_ (u"ࠩࠪᙄ")),
                bstack111111l_opy_ (u"ࠥࡦࡺ࡯࡬ࡥࡐࡤࡱࡪࠨᙅ"): self.config.get(bstack111111l_opy_ (u"ࠫࡧࡻࡩ࡭ࡦࡑࡥࡲ࡫ࠧᙆ"), os.path.basename(os.path.abspath(os.getcwd()))),
                bstack111111l_opy_ (u"ࠧࡨࡵࡪ࡮ࡧࡖࡺࡴࡉࡥࡧࡱࡸ࡮࡬ࡩࡦࡴࠥᙇ"): os.environ.get(bstack111111l_opy_ (u"ࠨࡂࡓࡑ࡚ࡗࡊࡘࡓࡕࡃࡆࡏࡤࡈࡕࡊࡎࡇࡣࡗ࡛ࡎࡠࡋࡇࡉࡓ࡚ࡉࡇࡋࡈࡖࠧᙈ"), bstack111111l_opy_ (u"ࠢࠣᙉ")),
                bstack111111l_opy_ (u"ࠣࡪࡲࡷࡹࡏ࡮ࡧࡱࠥᙊ"): get_host_info(),
                bstack111111l_opy_ (u"ࠤࡳࡶࡉ࡫ࡴࡢ࡫࡯ࡷࠧᙋ"): bstack11ll1ll11ll_opy_
            }
            self.logger.debug(bstack111111l_opy_ (u"ࠥ࡟ࡸࡶ࡬ࡪࡶࡗࡩࡸࡺࡳ࡞ࠢࡖࡩࡳࡪࡩ࡯ࡩࠣࡸࡪࡹࡴࠡࡨ࡬ࡰࡪࡹ࠺ࠡࡽࢀࠦᙌ").format(payload))
            response = bstack11lll111111_opy_.bstack11ll1llllll_opy_(self.bstack11ll1ll1l11_opy_, payload)
            if response:
                self.bstack11lll11l11l_opy_ = self._11lll111lll_opy_(response)
                self.logger.debug(bstack111111l_opy_ (u"ࠦࡠࡹࡰ࡭࡫ࡷࡘࡪࡹࡴࡴ࡟ࠣࡗࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡴࡨࡷࡵࡵ࡮ࡴࡧ࠽ࠤࢀࢃࠢᙍ").format(self.bstack11lll11l11l_opy_))
            else:
                self.logger.error(bstack111111l_opy_ (u"ࠧࡡࡳࡱ࡮࡬ࡸ࡙࡫ࡳࡵࡵࡠࠤࡋࡧࡩ࡭ࡧࡧࠤࡹࡵࠠࡨࡧࡷࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡵࡩࡸࡶ࡯࡯ࡵࡨ࠲ࠧᙎ"))
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠨ࡛ࡴࡲ࡯࡭ࡹ࡚ࡥࡴࡶࡶࡡࠥࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡ࡫ࡱࠤࡸ࡫࡮ࡥ࡫ࡱ࡫ࠥࡺࡥࡴࡶࠣࡪ࡮ࡲࡥࡴ࠼࠽ࠤࢀࢃࠢᙏ").format(e))
    def _11lll111lll_opy_(self, response):
        bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࠡࠢࠣࠤࡕࡸ࡯ࡤࡧࡶࡷࡪࡹࠠࡵࡪࡨࠤࡸࡶ࡬ࡪࡶࠣࡸࡪࡹࡴࡴࠢࡄࡔࡎࠦࡲࡦࡵࡳࡳࡳࡹࡥࠡࡣࡱࡨࠥ࡫ࡸࡵࡴࡤࡧࡹࡹࠠࡳࡧ࡯ࡩࡻࡧ࡮ࡵࠢࡩ࡭ࡪࡲࡤࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙐ")
        bstack111ll1111_opy_ = {}
        bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤᙑ")] = response.get(bstack111111l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࠥᙒ"), self.default_timeout)
        bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷࡍࡳࡺࡥࡳࡸࡤࡰࠧᙓ")] = response.get(bstack111111l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸࡎࡴࡴࡦࡴࡹࡥࡱࠨᙔ"), self.bstack11ll1ll1lll_opy_)
        bstack11ll1lll11l_opy_ = response.get(bstack111111l_opy_ (u"ࠧࡸࡥࡴࡷ࡯ࡸ࡚ࡸ࡬ࠣᙕ"))
        bstack11ll1lll1l1_opy_ = response.get(bstack111111l_opy_ (u"ࠨࡴࡪ࡯ࡨࡳࡺࡺࡕࡳ࡮ࠥᙖ"))
        if bstack11ll1lll11l_opy_:
            bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠢࡳࡧࡶࡹࡱࡺࡕࡳ࡮ࠥᙗ")] = bstack11ll1lll11l_opy_.split(bstack11lll11111l_opy_ + bstack111111l_opy_ (u"ࠣ࠱ࠥᙘ"))[1] if bstack11lll11111l_opy_ + bstack111111l_opy_ (u"ࠤ࠲ࠦᙙ") in bstack11ll1lll11l_opy_ else bstack11ll1lll11l_opy_
        else:
            bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙚ")] = None
        if bstack11ll1lll1l1_opy_:
            bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠦࡹ࡯࡭ࡦࡱࡸࡸ࡚ࡸ࡬ࠣᙛ")] = bstack11ll1lll1l1_opy_.split(bstack11lll11111l_opy_ + bstack111111l_opy_ (u"ࠧ࠵ࠢᙜ"))[1] if bstack11lll11111l_opy_ + bstack111111l_opy_ (u"ࠨ࠯ࠣᙝ") in bstack11ll1lll1l1_opy_ else bstack11ll1lll1l1_opy_
        else:
            bstack111ll1111_opy_[bstack111111l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡖࡴ࡯ࠦᙞ")] = None
        if (
            response.get(bstack111111l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤᙟ")) is None or
            response.get(bstack111111l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡌࡲࡹ࡫ࡲࡷࡣ࡯ࠦᙠ")) is None or
            response.get(bstack111111l_opy_ (u"ࠥࡸ࡮ࡳࡥࡰࡷࡷ࡙ࡷࡲࠢᙡ")) is None or
            response.get(bstack111111l_opy_ (u"ࠦࡷ࡫ࡳࡶ࡮ࡷ࡙ࡷࡲࠢᙢ")) is None
        ):
            self.logger.debug(bstack111111l_opy_ (u"ࠧࡡࡰࡳࡱࡦࡩࡸࡹ࡟ࡴࡲ࡯࡭ࡹࡥࡴࡦࡵࡷࡷࡤࡸࡥࡴࡲࡲࡲࡸ࡫࡝ࠡࡔࡨࡧࡪ࡯ࡶࡦࡦࠣࡲࡺࡲ࡬ࠡࡸࡤࡰࡺ࡫ࠨࡴࠫࠣࡪࡴࡸࠠࡴࡱࡰࡩࠥࡧࡴࡵࡴ࡬ࡦࡺࡺࡥࡴࠢ࡬ࡲࠥࡹࡰ࡭࡫ࡷࠤࡹ࡫ࡳࡵࡵࠣࡅࡕࡏࠠࡳࡧࡶࡴࡴࡴࡳࡦࠤᙣ"))
        return bstack111ll1111_opy_
    def bstack11lll111l1l_opy_(self):
        if not self.bstack11lll11l11l_opy_:
            self.logger.error(bstack111111l_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡏࡱࠣࡶࡪࡷࡵࡦࡵࡷࠤࡩࡧࡴࡢࠢࡤࡺࡦ࡯࡬ࡢࡤ࡯ࡩࠥࡺ࡯ࠡࡨࡨࡸࡨ࡮ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠳ࠨᙤ"))
            return None
        bstack11lll11ll11_opy_ = None
        test_files = []
        bstack11ll1lll111_opy_ = int(time.time() * 1000) # bstack11lll111ll1_opy_ sec
        bstack11lll11l1l1_opy_ = int(self.bstack11lll11l11l_opy_.get(bstack111111l_opy_ (u"ࠢࡵ࡫ࡰࡩࡴࡻࡴࡊࡰࡷࡩࡷࡼࡡ࡭ࠤᙥ"), self.bstack11ll1ll1lll_opy_))
        bstack11ll1ll1ll1_opy_ = int(self.bstack11lll11l11l_opy_.get(bstack111111l_opy_ (u"ࠣࡶ࡬ࡱࡪࡵࡵࡵࠤᙦ"), self.default_timeout)) * 1000
        bstack11ll1lll1l1_opy_ = self.bstack11lll11l11l_opy_.get(bstack111111l_opy_ (u"ࠤࡷ࡭ࡲ࡫࡯ࡶࡶࡘࡶࡱࠨᙧ"), None)
        bstack11ll1lll11l_opy_ = self.bstack11lll11l11l_opy_.get(bstack111111l_opy_ (u"ࠥࡶࡪࡹࡵ࡭ࡶࡘࡶࡱࠨᙨ"), None)
        if bstack11ll1lll11l_opy_ is None and bstack11ll1lll1l1_opy_ is None:
            return None
        try:
            while bstack11ll1lll11l_opy_ and (time.time() * 1000 - bstack11ll1lll111_opy_) < bstack11ll1ll1ll1_opy_:
                response = bstack11lll111111_opy_.bstack11lll1111ll_opy_(bstack11ll1lll11l_opy_, {})
                if response and response.get(bstack111111l_opy_ (u"ࠦࡹ࡫ࡳࡵࡵࠥᙩ")):
                    bstack11lll11ll11_opy_ = response.get(bstack111111l_opy_ (u"ࠧࡺࡥࡴࡶࡶࠦᙪ"))
                self.bstack11lll1111l1_opy_ += 1
                if bstack11lll11ll11_opy_:
                    break
                time.sleep(bstack11lll11l1l1_opy_)
                self.logger.debug(bstack111111l_opy_ (u"ࠨ࡛ࡨࡧࡷࡓࡷࡪࡥࡳࡧࡧࡘࡪࡹࡴࡇ࡫࡯ࡩࡸࡣࠠࡇࡧࡷࡧ࡭࡯࡮ࡨࠢࡲࡶࡩ࡫ࡲࡦࡦࠣࡸࡪࡹࡴࡴࠢࡩࡶࡴࡳࠠࡳࡧࡶࡹࡱࡺࠠࡖࡔࡏࠤࡦ࡬ࡴࡦࡴࠣࡻࡦ࡯ࡴࡪࡰࡪࠤ࡫ࡵࡲࠡࡽࢀࠤࡸ࡫ࡣࡰࡰࡧࡷ࠳ࠨᙫ").format(bstack11lll11l1l1_opy_))
            if bstack11ll1lll1l1_opy_ and not bstack11lll11ll11_opy_:
                self.logger.debug(bstack111111l_opy_ (u"ࠢ࡜ࡩࡨࡸࡔࡸࡤࡦࡴࡨࡨ࡙࡫ࡳࡵࡈ࡬ࡰࡪࡹ࡝ࠡࡈࡨࡸࡨ࡮ࡩ࡯ࡩࠣࡳࡷࡪࡥࡳࡧࡧࠤࡹ࡫ࡳࡵࡵࠣࡪࡷࡵ࡭ࠡࡶ࡬ࡱࡪࡵࡵࡵࠢࡘࡖࡑࠨᙬ"))
                response = bstack11lll111111_opy_.bstack11lll1111ll_opy_(bstack11ll1lll1l1_opy_, {})
                if response and response.get(bstack111111l_opy_ (u"ࠣࡶࡨࡷࡹࡹࠢ᙭")):
                    bstack11lll11ll11_opy_ = response.get(bstack111111l_opy_ (u"ࠤࡷࡩࡸࡺࡳࠣ᙮"))
            if bstack11lll11ll11_opy_ and len(bstack11lll11ll11_opy_) > 0:
                for bstack1l11ll11_opy_ in bstack11lll11ll11_opy_:
                    file_path = bstack1l11ll11_opy_.get(bstack111111l_opy_ (u"ࠥࡪ࡮ࡲࡥࡑࡣࡷ࡬ࠧᙯ"))
                    if file_path:
                        test_files.append(file_path)
            if not bstack11lll11ll11_opy_:
                return None
            self.logger.debug(bstack111111l_opy_ (u"ࠦࡠ࡭ࡥࡵࡑࡵࡨࡪࡸࡥࡥࡖࡨࡷࡹࡌࡩ࡭ࡧࡶࡡࠥࡕࡲࡥࡧࡵࡩࡩࠦࡴࡦࡵࡷࠤ࡫࡯࡬ࡦࡵࠣࡶࡪࡩࡥࡪࡸࡨࡨ࠿ࠦࡻࡾࠤᙰ").format(test_files))
            return test_files
        except Exception as e:
            self.logger.error(bstack111111l_opy_ (u"ࠧࡡࡧࡦࡶࡒࡶࡩ࡫ࡲࡦࡦࡗࡩࡸࡺࡆࡪ࡮ࡨࡷࡢࠦࡅࡹࡥࡨࡴࡹ࡯࡯࡯ࠢ࡬ࡲࠥ࡬ࡥࡵࡥ࡫࡭ࡳ࡭ࠠࡰࡴࡧࡩࡷ࡫ࡤࠡࡶࡨࡷࡹࠦࡦࡪ࡮ࡨࡷ࠿ࠦࡻࡾࠤᙱ").format(e))
            return None
    def bstack11ll1llll1l_opy_(self):
        bstack111111l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡖࡪࡺࡵࡳࡰࡶࠤࡹ࡮ࡥࠡࡥࡲࡹࡳࡺࠠࡰࡨࠣࡷࡵࡲࡩࡵࠢࡷࡩࡸࡺࡳࠡࡃࡓࡍࠥࡩࡡ࡭࡮ࡶࠤࡲࡧࡤࡦ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᙲ")
        return self.bstack11lll1111l1_opy_
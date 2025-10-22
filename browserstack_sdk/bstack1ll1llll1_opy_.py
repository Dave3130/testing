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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1lll1l_opy_ = {}
        bstack1ll1lllll_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৹"), bstack11l1l11_opy_ (u"࠭ࠧ৺"))
        if not bstack1ll1lllll_opy_:
            return bstack1ll1lll1l_opy_
        try:
            bstack1lll11111_opy_ = json.loads(bstack1ll1lllll_opy_)
            if bstack11l1l11_opy_ (u"ࠢࡰࡵࠥ৻") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠣࡱࡶࠦৼ")] = bstack1lll11111_opy_[bstack11l1l11_opy_ (u"ࠤࡲࡷࠧ৽")]
            if bstack11l1l11_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৾") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ৿") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ਀")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥਁ"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥਂ")))
            if bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤਃ") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ਄") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣਅ")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧਆ"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥਇ")))
            if bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਈ") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣਉ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤਊ")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ਋"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦ਌")))
            if bstack11l1l11_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦ਍") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ਎") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਏ")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢਐ"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ਑")))
            if bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ਒") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤਓ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥਔ")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢਕ"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧਖ")))
            if bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥਗ") in bstack1lll11111_opy_ or bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥਘ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦਙ")] = bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨਚ"), bstack1lll11111_opy_.get(bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨਛ")))
            if bstack11l1l11_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢਜ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਝ")] = bstack1lll11111_opy_[bstack11l1l11_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਞ")]
        except Exception as error:
            logger.error(bstack11l1l11_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡣࡷࡥ࠿ࠦࠢਟ") +  str(error))
        return bstack1ll1lll1l_opy_
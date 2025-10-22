# coding: UTF-8
import sys
bstack1ll1lll_opy_ = sys.version_info [0] == 2
bstack1l1ll_opy_ = 2048
bstack11l1l1_opy_ = 7
def bstack111l1l_opy_ (bstack1l_opy_):
    global bstack11111ll_opy_
    bstack1lll11l_opy_ = ord (bstack1l_opy_ [-1])
    bstack111ll1_opy_ = bstack1l_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1lll11l_opy_ % len (bstack111ll1_opy_)
    bstack11l111_opy_ = bstack111ll1_opy_ [:bstack1ll11l_opy_] + bstack111ll1_opy_ [bstack1ll11l_opy_:]
    if bstack1ll1lll_opy_:
        bstack1l11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    else:
        bstack1l11l11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll_opy_ - (bstack11llll_opy_ + bstack1lll11l_opy_) % bstack11l1l1_opy_) for bstack11llll_opy_, char in enumerate (bstack11l111_opy_)])
    return eval (bstack1l11l11_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1lll1l_opy_ = {}
        bstack1ll1llll1_opy_ = os.environ.get(bstack111l1l_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ৺"), bstack111l1l_opy_ (u"ࠧࠨ৻"))
        if not bstack1ll1llll1_opy_:
            return bstack1ll1lll1l_opy_
        try:
            bstack1lll11111_opy_ = json.loads(bstack1ll1llll1_opy_)
            if bstack111l1l_opy_ (u"ࠣࡱࡶࠦৼ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠤࡲࡷࠧ৽")] = bstack1lll11111_opy_[bstack111l1l_opy_ (u"ࠥࡳࡸࠨ৾")]
            if bstack111l1l_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ৿") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ਀") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤਁ")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦਂ"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦਃ")))
            if bstack111l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥ਄") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣਅ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤਆ")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨਇ"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦਈ")))
            if bstack111l1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਉ") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤਊ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ਋")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ਌"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧ਍")))
            if bstack111l1l_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧ਎") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਏ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦਐ")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣ਑"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ਒")))
            if bstack111l1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧਓ") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥਔ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦਕ")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣਖ"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨਗ")))
            if bstack111l1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦਘ") in bstack1lll11111_opy_ or bstack111l1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦਙ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧਚ")] = bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢਛ"), bstack1lll11111_opy_.get(bstack111l1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢਜ")))
            if bstack111l1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਝ") in bstack1lll11111_opy_:
                bstack1ll1lll1l_opy_[bstack111l1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਞ")] = bstack1lll11111_opy_[bstack111l1l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਟ")]
        except Exception as error:
            logger.error(bstack111l1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣਠ") +  str(error))
        return bstack1ll1lll1l_opy_
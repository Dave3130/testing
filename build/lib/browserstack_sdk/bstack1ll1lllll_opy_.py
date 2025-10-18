# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1llll1_opy_ = {}
        bstack1ll1lll1l_opy_ = os.environ.get(bstack11ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧਁ"), bstack11ll_opy_ (u"ࠧࠨਂ"))
        if not bstack1ll1lll1l_opy_:
            return bstack1ll1llll1_opy_
        try:
            bstack1lll11111_opy_ = json.loads(bstack1ll1lll1l_opy_)
            if bstack11ll_opy_ (u"ࠣࡱࡶࠦਃ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠤࡲࡷࠧ਄")] = bstack1lll11111_opy_[bstack11ll_opy_ (u"ࠥࡳࡸࠨਅ")]
            if bstack11ll_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਆ") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣਇ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤਈ")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦਉ"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦਊ")))
            if bstack11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥ਋") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣ਌") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ਍")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ਎"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦਏ")))
            if bstack11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਐ") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤ਑") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ਒")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧਓ"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧਔ")))
            if bstack11ll_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧਕ") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਖ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦਗ")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣਘ"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨਙ")))
            if bstack11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧਚ") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥਛ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦਜ")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣਝ"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨਞ")))
            if bstack11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦਟ") in bstack1lll11111_opy_ or bstack11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦਠ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧਡ")] = bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢਢ"), bstack1lll11111_opy_.get(bstack11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢਣ")))
            if bstack11ll_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਤ") in bstack1lll11111_opy_:
                bstack1ll1llll1_opy_[bstack11ll_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਥ")] = bstack1lll11111_opy_[bstack11ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਦ")]
        except Exception as error:
            logger.error(bstack11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣਧ") +  str(error))
        return bstack1ll1llll1_opy_
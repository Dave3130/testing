# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1llll1_opy_ = {}
        bstack1ll1lll1l_opy_ = os.environ.get(bstack11l11ll_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧਈ"), bstack11l11ll_opy_ (u"ࠧࠨਉ"))
        if not bstack1ll1lll1l_opy_:
            return bstack1ll1llll1_opy_
        try:
            bstack1ll1lll11_opy_ = json.loads(bstack1ll1lll1l_opy_)
            if bstack11l11ll_opy_ (u"ࠣࡱࡶࠦਊ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠤࡲࡷࠧ਋")] = bstack1ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠥࡳࡸࠨ਌")]
            if bstack11l11ll_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ਍") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ਎") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤਏ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦਐ"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ਑")))
            if bstack11l11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥ਒") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣਓ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤਔ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨਕ"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦਖ")))
            if bstack11l11ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਗ") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤਘ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥਙ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧਚ"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧਛ")))
            if bstack11l11ll_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧਜ") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਝ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦਞ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣਟ"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨਠ")))
            if bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧਡ") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥਢ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦਣ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣਤ"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨਥ")))
            if bstack11l11ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦਦ") in bstack1ll1lll11_opy_ or bstack11l11ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦਧ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧਨ")] = bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ਩"), bstack1ll1lll11_opy_.get(bstack11l11ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢਪ")))
            if bstack11l11ll_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਫ") in bstack1ll1lll11_opy_:
                bstack1ll1llll1_opy_[bstack11l11ll_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਬ")] = bstack1ll1lll11_opy_[bstack11l11ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਭ")]
        except Exception as error:
            logger.error(bstack11l11ll_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣਮ") +  str(error))
        return bstack1ll1llll1_opy_
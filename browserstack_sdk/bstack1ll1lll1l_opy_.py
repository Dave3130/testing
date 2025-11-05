# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1lllll_opy_ = {}
        bstack1lll11111_opy_ = os.environ.get(bstack11ll1ll_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨਉ"), bstack11ll1ll_opy_ (u"ࠨࠩਊ"))
        if not bstack1lll11111_opy_:
            return bstack1ll1lllll_opy_
        try:
            bstack1ll1llll1_opy_ = json.loads(bstack1lll11111_opy_)
            if bstack11ll1ll_opy_ (u"ࠤࡲࡷࠧ਋") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠥࡳࡸࠨ਌")] = bstack1ll1llll1_opy_[bstack11ll1ll_opy_ (u"ࠦࡴࡹࠢ਍")]
            if bstack11ll1ll_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ਎") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤਏ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥਐ")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ਑"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ਒")))
            if bstack11ll1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦਓ") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤਔ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥਕ")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢਖ"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧਗ")))
            if bstack11ll1ll_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥਘ") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥਙ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦਚ")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨਛ"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨਜ")))
            if bstack11ll1ll_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨਝ") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦਞ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧਟ")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤਠ"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢਡ")))
            if bstack11ll1ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨਢ") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦਣ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧਤ")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤਥ"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢਦ")))
            if bstack11ll1ll_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧਧ") in bstack1ll1llll1_opy_ or bstack11ll1ll_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧਨ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ਩")] = bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਪ"), bstack1ll1llll1_opy_.get(bstack11ll1ll_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣਫ")))
            if bstack11ll1ll_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਬ") in bstack1ll1llll1_opy_:
                bstack1ll1lllll_opy_[bstack11ll1ll_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਭ")] = bstack1ll1llll1_opy_[bstack11ll1ll_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦਮ")]
        except Exception as error:
            logger.error(bstack11ll1ll_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡥࡹࡧ࠺ࠡࠤਯ") +  str(error))
        return bstack1ll1lllll_opy_
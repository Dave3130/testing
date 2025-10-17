# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll11lll_opy_ = {}
        bstack1lll11ll1_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪৌ"), bstack11l111_opy_ (u"্ࠪࠫ"))
        if not bstack1lll11ll1_opy_:
            return bstack1lll11lll_opy_
        try:
            bstack1lll1l111_opy_ = json.loads(bstack1lll11ll1_opy_)
            if bstack11l111_opy_ (u"ࠦࡴࡹࠢৎ") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠧࡵࡳࠣ৏")] = bstack1lll1l111_opy_[bstack11l111_opy_ (u"ࠨ࡯ࡴࠤ৐")]
            if bstack11l111_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ৑") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ৒") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৓")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৔"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ৕")))
            if bstack11l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ৖") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦৗ") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ৘")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ৙"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ৚")))
            if bstack11l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৛") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧড়") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨঢ়")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ৞"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣয়")))
            if bstack11l111_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣৠ") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨৡ") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢৢ")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦৣ"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ৤")))
            if bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ৥") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ০") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ১")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ২"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ৩")))
            if bstack11l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৪") in bstack1lll1l111_opy_ or bstack11l111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ৫") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৬")] = bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥ৭"), bstack1lll1l111_opy_.get(bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ৮")))
            if bstack11l111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ৯") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack11l111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧৰ")] = bstack1lll1l111_opy_[bstack11l111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨৱ")]
        except Exception as error:
            logger.error(bstack11l111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦ৲") +  str(error))
        return bstack1lll11lll_opy_
# coding: UTF-8
import sys
bstack111l11_opy_ = sys.version_info [0] == 2
bstack111ll1l_opy_ = 2048
bstack1_opy_ = 7
def bstack11111_opy_ (bstack1l111ll_opy_):
    global bstack111ll11_opy_
    bstack1lllll_opy_ = ord (bstack1l111ll_opy_ [-1])
    bstack1l1llll_opy_ = bstack1l111ll_opy_ [:-1]
    bstack11l11l_opy_ = bstack1lllll_opy_ % len (bstack1l1llll_opy_)
    bstack111l_opy_ = bstack1l1llll_opy_ [:bstack11l11l_opy_] + bstack1l1llll_opy_ [bstack11l11l_opy_:]
    if bstack111l11_opy_:
        bstack1l1l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1l1l1l_opy_ = str () .join ([chr (ord (char) - bstack111ll1l_opy_ - (bstack1l_opy_ + bstack1lllll_opy_) % bstack1_opy_) for bstack1l_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1l1l1l_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l11l_opy_ = {}
        bstack1lll1l111_opy_ = os.environ.get(bstack11111_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪৌ"), bstack11111_opy_ (u"্ࠪࠫ"))
        if not bstack1lll1l111_opy_:
            return bstack1lll1l11l_opy_
        try:
            bstack1lll11lll_opy_ = json.loads(bstack1lll1l111_opy_)
            if bstack11111_opy_ (u"ࠦࡴࡹࠢৎ") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠧࡵࡳࠣ৏")] = bstack1lll11lll_opy_[bstack11111_opy_ (u"ࠨ࡯ࡴࠤ৐")]
            if bstack11111_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ৑") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ৒") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৓")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৔"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ৕")))
            if bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ৖") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦৗ") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ৘")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ৙"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ৚")))
            if bstack11111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৛") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧড়") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨঢ়")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ৞"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣয়")))
            if bstack11111_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣৠ") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨৡ") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢৢ")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦৣ"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ৤")))
            if bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ৥") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ০") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ১")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ২"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ৩")))
            if bstack11111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৪") in bstack1lll11lll_opy_ or bstack11111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ৫") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৬")] = bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥ৭"), bstack1lll11lll_opy_.get(bstack11111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ৮")))
            if bstack11111_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ৯") in bstack1lll11lll_opy_:
                bstack1lll1l11l_opy_[bstack11111_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧৰ")] = bstack1lll11lll_opy_[bstack11111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨৱ")]
        except Exception as error:
            logger.error(bstack11111_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦ৲") +  str(error))
        return bstack1lll1l11l_opy_
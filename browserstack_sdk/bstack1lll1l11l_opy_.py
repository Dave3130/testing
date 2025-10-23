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
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l111_opy_ = {}
        bstack1lll1l1l1_opy_ = os.environ.get(bstack111111l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ৒"), bstack111111l_opy_ (u"ࠩࠪ৓"))
        if not bstack1lll1l1l1_opy_:
            return bstack1lll1l111_opy_
        try:
            bstack1lll11lll_opy_ = json.loads(bstack1lll1l1l1_opy_)
            if bstack111111l_opy_ (u"ࠥࡳࡸࠨ৔") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠦࡴࡹࠢ৕")] = bstack1lll11lll_opy_[bstack111111l_opy_ (u"ࠧࡵࡳࠣ৖")]
            if bstack111111l_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥৗ") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ৘") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ৙")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ৚"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৛")))
            if bstack111111l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧড়") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥঢ়") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ৞")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣয়"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨৠ")))
            if bstack111111l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦৡ") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦৢ") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧৣ")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৤"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢ৥")))
            if bstack111111l_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢ০") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ১") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ২")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥ৩"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣ৪")))
            if bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢ৫") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ৬") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ৭")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ৮"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ৯")))
            if bstack111111l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨৰ") in bstack1lll11lll_opy_ or bstack111111l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨৱ") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ৲")] = bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৳"), bstack1lll11lll_opy_.get(bstack111111l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ৴")))
            if bstack111111l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥ৵") in bstack1lll11lll_opy_:
                bstack1lll1l111_opy_[bstack111111l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ৶")] = bstack1lll11lll_opy_[bstack111111l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧ৷")]
        except Exception as error:
            logger.error(bstack111111l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡦࡺࡡ࠻ࠢࠥ৸") +  str(error))
        return bstack1lll1l111_opy_
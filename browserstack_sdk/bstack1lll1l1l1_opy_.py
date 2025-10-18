# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll11lll_opy_ = {}
        bstack1lll1l11l_opy_ = os.environ.get(bstack1l1lll1_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨ৘"), bstack1l1lll1_opy_ (u"ࠨࠩ৙"))
        if not bstack1lll1l11l_opy_:
            return bstack1lll11lll_opy_
        try:
            bstack1lll1l111_opy_ = json.loads(bstack1lll1l11l_opy_)
            if bstack1l1lll1_opy_ (u"ࠤࡲࡷࠧ৚") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠥࡳࡸࠨ৛")] = bstack1lll1l111_opy_[bstack1l1lll1_opy_ (u"ࠦࡴࡹࠢড়")]
            if bstack1l1lll1_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤঢ়") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৞") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥয়")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧৠ"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧৡ")))
            if bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦৢ") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤৣ") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ৤")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢ৥"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ০")))
            if bstack1l1lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ১") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ২") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦ৩")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ৪"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৫")))
            if bstack1l1lll1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ৬") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৭") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ৮")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤ৯"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢৰ")))
            if bstack1l1lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨৱ") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৲") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ৳")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤ৴"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢ৵")))
            if bstack1l1lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৶") in bstack1lll1l111_opy_ or bstack1l1lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৷") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৸")] = bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ৹"), bstack1lll1l111_opy_.get(bstack1l1lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৺")))
            if bstack1l1lll1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤ৻") in bstack1lll1l111_opy_:
                bstack1lll11lll_opy_[bstack1l1lll1_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥৼ")] = bstack1lll1l111_opy_[bstack1l1lll1_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ৽")]
        except Exception as error:
            logger.error(bstack1l1lll1_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡥࡹࡧ࠺ࠡࠤ৾") +  str(error))
        return bstack1lll11lll_opy_
# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1ll11_opy_ = {}
        bstack1lll1l11l_opy_ = os.environ.get(bstack1l_opy_ (u"ࠧࡄࡗࡕࡖࡊࡔࡔࡠࡒࡏࡅ࡙ࡌࡏࡓࡏࡢࡈࡆ࡚ࡁࠨয়"), bstack1l_opy_ (u"ࠨࠩৠ"))
        if not bstack1lll1l11l_opy_:
            return bstack1lll1ll11_opy_
        try:
            bstack1lll1l1l1_opy_ = json.loads(bstack1lll1l11l_opy_)
            if bstack1l_opy_ (u"ࠤࡲࡷࠧৡ") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠥࡳࡸࠨৢ")] = bstack1lll1l1l1_opy_[bstack1l_opy_ (u"ࠦࡴࡹࠢৣ")]
            if bstack1l_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৤") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৥") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ০")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠣࡱࡶࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ১"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ২")))
            if bstack1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦ৩") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ৪") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ৫")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࠢ৬"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧ৭")))
            if bstack1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ৮") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ৯") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦৰ")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡤࡼࡥࡳࡵ࡬ࡳࡳࠨৱ"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৲")))
            if bstack1l_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ৳") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৴") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ৵")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࠤ৶"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢ৷")))
            if bstack1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ৸") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৹") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ৺")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠤ৻"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢৼ")))
            if bstack1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৽") in bstack1lll1l1l1_opy_ or bstack1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৾") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৿")] = bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ਀"), bstack1lll1l1l1_opy_.get(bstack1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣਁ")))
            if bstack1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਂ") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਃ")] = bstack1lll1l1l1_opy_[bstack1l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ਄")]
        except Exception as error:
            logger.error(bstack1l_opy_ (u"ࠥࡉࡽࡩࡥࡱࡶ࡬ࡳࡳࠦࡷࡩ࡫࡯ࡩࠥ࡭ࡥࡵࡶ࡬ࡲ࡬ࠦࡣࡶࡴࡵࡩࡳࡺࠠࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࠢࡧࡥࡹࡧ࠺ࠡࠤਅ") +  str(error))
        return bstack1lll1ll11_opy_
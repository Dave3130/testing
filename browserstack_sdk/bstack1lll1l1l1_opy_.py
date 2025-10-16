# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l11l_opy_ = {}
        bstack1lll1l1ll_opy_ = os.environ.get(bstack1ll1ll1_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧ৞"), bstack1ll1ll1_opy_ (u"ࠧࠨয়"))
        if not bstack1lll1l1ll_opy_:
            return bstack1lll1l11l_opy_
        try:
            bstack1lll1ll11_opy_ = json.loads(bstack1lll1l1ll_opy_)
            if bstack1ll1ll1_opy_ (u"ࠣࡱࡶࠦৠ") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠤࡲࡷࠧৡ")] = bstack1lll1ll11_opy_[bstack1ll1ll1_opy_ (u"ࠥࡳࡸࠨৢ")]
            if bstack1ll1ll1_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣৣ") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৤") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৥")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦ০"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ১")))
            if bstack1ll1ll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥ২") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣ৩") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ৪")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ৫"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ৬")))
            if bstack1ll1ll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৭") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤ৮") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ৯")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧৰ"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧৱ")))
            if bstack1ll1ll1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧ৲") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥ৳") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৴")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣ৵"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ৶")))
            if bstack1ll1ll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧ৷") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ৸") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৹")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ৺"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ৻")))
            if bstack1ll1ll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦৼ") in bstack1lll1ll11_opy_ or bstack1ll1ll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ৽") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৾")] = bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৿"), bstack1lll1ll11_opy_.get(bstack1ll1ll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ਀")))
            if bstack1ll1ll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਁ") in bstack1lll1ll11_opy_:
                bstack1lll1l11l_opy_[bstack1ll1ll1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਂ")] = bstack1lll1ll11_opy_[bstack1ll1ll1_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥਃ")]
        except Exception as error:
            logger.error(bstack1ll1ll1_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣ਄") +  str(error))
        return bstack1lll1l11l_opy_
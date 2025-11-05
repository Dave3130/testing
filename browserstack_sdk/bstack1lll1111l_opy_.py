# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll111l1_opy_ = {}
        bstack1lll111ll_opy_ = os.environ.get(bstack1lll11l_opy_ (u"ࠨࡅࡘࡖࡗࡋࡎࡕࡡࡓࡐࡆ࡚ࡆࡐࡔࡐࡣࡉࡇࡔࡂࠩ৮"), bstack1lll11l_opy_ (u"ࠩࠪ৯"))
        if not bstack1lll111ll_opy_:
            return bstack1lll111l1_opy_
        try:
            bstack1lll11l11_opy_ = json.loads(bstack1lll111ll_opy_)
            if bstack1lll11l_opy_ (u"ࠥࡳࡸࠨৰ") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠦࡴࡹࠢৱ")] = bstack1lll11l11_opy_[bstack1lll11l_opy_ (u"ࠧࡵࡳࠣ৲")]
            if bstack1lll11l_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥ৳") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ৴") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦ৵")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ৶"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৷")))
            if bstack1lll11l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧ৸") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ৹") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ৺")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣ৻"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨৼ")))
            if bstack1lll11l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ৽") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦ৾") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৿")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ਀"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢਁ")))
            if bstack1lll11l_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢਂ") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧਃ") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ਄")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥਅ"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣਆ")))
            if bstack1lll11l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢਇ") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧਈ") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨਉ")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥਊ"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ਋")))
            if bstack1lll11l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ਌") in bstack1lll11l11_opy_ or bstack1lll11l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ਍") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ਎")] = bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਏ"), bstack1lll11l11_opy_.get(bstack1lll11l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤਐ")))
            if bstack1lll11l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥ਑") in bstack1lll11l11_opy_:
                bstack1lll111l1_opy_[bstack1lll11l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦ਒")] = bstack1lll11l11_opy_[bstack1lll11l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧਓ")]
        except Exception as error:
            logger.error(bstack1lll11l_opy_ (u"ࠦࡊࡾࡣࡦࡲࡷ࡭ࡴࡴࠠࡸࡪ࡬ࡰࡪࠦࡧࡦࡶࡷ࡭ࡳ࡭ࠠࡤࡷࡵࡶࡪࡴࡴࠡࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠣࡨࡦࡺࡡ࠻ࠢࠥਔ") +  str(error))
        return bstack1lll111l1_opy_
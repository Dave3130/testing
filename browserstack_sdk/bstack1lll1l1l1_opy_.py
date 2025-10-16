# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l1ll_opy_ = {}
        bstack1lll1l11l_opy_ = os.environ.get(bstack1lllll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭ঢ়"), bstack1lllll1_opy_ (u"࠭ࠧ৞"))
        if not bstack1lll1l11l_opy_:
            return bstack1lll1l1ll_opy_
        try:
            bstack1lll1ll11_opy_ = json.loads(bstack1lll1l11l_opy_)
            if bstack1lllll1_opy_ (u"ࠢࡰࡵࠥয়") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠣࡱࡶࠦৠ")] = bstack1lll1ll11_opy_[bstack1lllll1_opy_ (u"ࠤࡲࡷࠧৡ")]
            if bstack1lllll1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢৢ") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢৣ") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৤")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥ৥"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ০")))
            if bstack1lllll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤ১") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ২") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣ৩")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧ৪"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ৫")))
            if bstack1lllll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣ৬") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৭") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤ৮")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ৯"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦৰ")))
            if bstack1lllll1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦৱ") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ৲") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥ৳")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢ৴"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ৵")))
            if bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ৶") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ৷") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ৸")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢ৹"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧ৺")))
            if bstack1lllll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥ৻") in bstack1lll1ll11_opy_ or bstack1lllll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥৼ") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ৽")] = bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ৾"), bstack1lll1ll11_opy_.get(bstack1lllll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৿")))
            if bstack1lllll1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢ਀") in bstack1lll1ll11_opy_:
                bstack1lll1l1ll_opy_[bstack1lllll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਁ")] = bstack1lll1ll11_opy_[bstack1lllll1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਂ")]
        except Exception as error:
            logger.error(bstack1lllll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡣࡷࡥ࠿ࠦࠢਃ") +  str(error))
        return bstack1lll1l1ll_opy_
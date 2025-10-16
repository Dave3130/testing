# coding: UTF-8
import sys
bstack11llll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1l1l1l1_opy_ = 7
def bstack1ll11_opy_ (bstack11l11ll_opy_):
    global bstack11l1lll_opy_
    bstack1l1l111_opy_ = ord (bstack11l11ll_opy_ [-1])
    bstack11_opy_ = bstack11l11ll_opy_ [:-1]
    bstack1l1llll_opy_ = bstack1l1l111_opy_ % len (bstack11_opy_)
    bstack11111_opy_ = bstack11_opy_ [:bstack1l1llll_opy_] + bstack11_opy_ [bstack1l1llll_opy_:]
    if bstack11llll1_opy_:
        bstack111_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    else:
        bstack111_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1111ll1_opy_ + bstack1l1l111_opy_) % bstack1l1l1l1_opy_) for bstack1111ll1_opy_, char in enumerate (bstack11111_opy_)])
    return eval (bstack111_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1ll11_opy_ = {}
        bstack1lll1l11l_opy_ = os.environ.get(bstack1ll11_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬড়"), bstack1ll11_opy_ (u"ࠬ࠭ঢ়"))
        if not bstack1lll1l11l_opy_:
            return bstack1lll1ll11_opy_
        try:
            bstack1lll1l1l1_opy_ = json.loads(bstack1lll1l11l_opy_)
            if bstack1ll11_opy_ (u"ࠨ࡯ࡴࠤ৞") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠢࡰࡵࠥয়")] = bstack1lll1l1l1_opy_[bstack1ll11_opy_ (u"ࠣࡱࡶࠦৠ")]
            if bstack1ll11_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨৡ") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨৢ") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢৣ")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৤"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৥")))
            if bstack1ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣ০") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨ১") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ২")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦ৩"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ৪")))
            if bstack1ll11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৫") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢ৬") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৭")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ৮"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ৯")))
            if bstack1ll11_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥৰ") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣৱ") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ৲")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ৳"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৴")))
            if bstack1ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ৵") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ৶") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ৷")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨ৸"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৹")))
            if bstack1ll11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৺") in bstack1lll1l1l1_opy_ or bstack1ll11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ৻") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥৼ")] = bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৽"), bstack1lll1l1l1_opy_.get(bstack1ll11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৾")))
            if bstack1ll11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨ৿") in bstack1lll1l1l1_opy_:
                bstack1lll1ll11_opy_[bstack1ll11_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢ਀")] = bstack1lll1l1l1_opy_[bstack1ll11_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਁ")]
        except Exception as error:
            logger.error(bstack1ll11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡢࡶࡤ࠾ࠥࠨਂ") +  str(error))
        return bstack1lll1ll11_opy_
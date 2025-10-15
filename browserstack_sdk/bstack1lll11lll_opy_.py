# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l111_opy_ = {}
        bstack1lll1l1l1_opy_ = os.environ.get(bstack1ll1l_opy_ (u"࠭ࡃࡖࡔࡕࡉࡓ࡚࡟ࡑࡎࡄࡘࡋࡕࡒࡎࡡࡇࡅ࡙ࡇࠧৗ"), bstack1ll1l_opy_ (u"ࠧࠨ৘"))
        if not bstack1lll1l1l1_opy_:
            return bstack1lll1l111_opy_
        try:
            bstack1lll1l11l_opy_ = json.loads(bstack1lll1l1l1_opy_)
            if bstack1ll1l_opy_ (u"ࠣࡱࡶࠦ৙") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠤࡲࡷࠧ৚")] = bstack1lll1l11l_opy_[bstack1ll1l_opy_ (u"ࠥࡳࡸࠨ৛")]
            if bstack1ll1l_opy_ (u"ࠦࡴࡹ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣড়") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣঢ়") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৞")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦয়"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦৠ")))
            if bstack1ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࠥৡ") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣৢ") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤৣ")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨ৤"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦ৥")))
            if bstack1ll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ০") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤ১") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ২")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৩"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৪")))
            if bstack1ll1l_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࠧ৫") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥ৬") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৭")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣ৮"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ৯")))
            if bstack1ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࠧৰ") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥৱ") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৲")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣ৳"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨ৴")))
            if bstack1ll1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡢࡺࡪࡸࡳࡪࡱࡱࠦ৵") in bstack1lll1l11l_opy_ or bstack1ll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ৶") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৷")] = bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৸"), bstack1lll1l11l_opy_.get(bstack1ll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢ৹")))
            if bstack1ll1l_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣ৺") in bstack1lll1l11l_opy_:
                bstack1lll1l111_opy_[bstack1ll1l_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤ৻")] = bstack1lll1l11l_opy_[bstack1ll1l_opy_ (u"ࠣࡥࡸࡷࡹࡵ࡭ࡗࡣࡵ࡭ࡦࡨ࡬ࡦࡵࠥৼ")]
        except Exception as error:
            logger.error(bstack1ll1l_opy_ (u"ࠤࡈࡼࡨ࡫ࡰࡵ࡫ࡲࡲࠥࡽࡨࡪ࡮ࡨࠤ࡬࡫ࡴࡵ࡫ࡱ࡫ࠥࡩࡵࡳࡴࡨࡲࡹࠦࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠡࡦࡤࡸࡦࡀࠠࠣ৽") +  str(error))
        return bstack1lll1l111_opy_
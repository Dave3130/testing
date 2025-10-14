# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1l1l1_opy_ = {}
        bstack1lll1l11l_opy_ = os.environ.get(bstack11l1l11_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ৕"), bstack11l1l11_opy_ (u"ࠬ࠭৖"))
        if not bstack1lll1l11l_opy_:
            return bstack1lll1l1l1_opy_
        try:
            bstack1lll1l111_opy_ = json.loads(bstack1lll1l11l_opy_)
            if bstack11l1l11_opy_ (u"ࠨ࡯ࡴࠤৗ") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠢࡰࡵࠥ৘")] = bstack1lll1l111_opy_[bstack11l1l11_opy_ (u"ࠣࡱࡶࠦ৙")]
            if bstack11l1l11_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ৚") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨ৛") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢড়")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤঢ়"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤ৞")))
            if bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣয়") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨৠ") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢৡ")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦৢ"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤৣ")))
            if bstack11l1l11_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৤") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢ৥") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣ০")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ১"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ২")))
            if bstack11l1l11_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥ৩") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣ৪") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ৫")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨ৬"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦ৭")))
            if bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥ৮") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣ৯") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤৰ")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨৱ"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦ৲")))
            if bstack11l1l11_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤ৳") in bstack1lll1l111_opy_ or bstack11l1l11_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤ৴") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ৵")] = bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ৶"), bstack1lll1l111_opy_.get(bstack11l1l11_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧ৷")))
            if bstack11l1l11_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨ৸") in bstack1lll1l111_opy_:
                bstack1lll1l1l1_opy_[bstack11l1l11_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢ৹")] = bstack1lll1l111_opy_[bstack11l1l11_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣ৺")]
        except Exception as error:
            logger.error(bstack11l1l11_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡢࡶࡤ࠾ࠥࠨ৻") +  str(error))
        return bstack1lll1l1l1_opy_
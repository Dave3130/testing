# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll11l11_opy_ = {}
        bstack1lll111l1_opy_ = os.environ.get(bstack1l1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৲"), bstack1l1_opy_ (u"࠭ࠧ৳"))
        if not bstack1lll111l1_opy_:
            return bstack1lll11l11_opy_
        try:
            bstack1lll1111l_opy_ = json.loads(bstack1lll111l1_opy_)
            if bstack1l1_opy_ (u"ࠢࡰࡵࠥ৴") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠣࡱࡶࠦ৵")] = bstack1lll1111l_opy_[bstack1l1_opy_ (u"ࠤࡲࡷࠧ৶")]
            if bstack1l1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৷") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ৸") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ৹")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥ৺"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥ৻")))
            if bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤৼ") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ৽") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣ৾")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧ৿"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥ਀")))
            if bstack1l1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਁ") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣਂ") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤਃ")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ਄"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦਅ")))
            if bstack1l1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦਆ") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤਇ") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਈ")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢਉ"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧਊ")))
            if bstack1l1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ਋") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤ਌") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥ਍")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢ਎"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧਏ")))
            if bstack1l1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥਐ") in bstack1lll1111l_opy_ or bstack1l1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥ਑") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦ਒")] = bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨਓ"), bstack1lll1111l_opy_.get(bstack1l1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨਔ")))
            if bstack1l1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢਕ") in bstack1lll1111l_opy_:
                bstack1lll11l11_opy_[bstack1l1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਖ")] = bstack1lll1111l_opy_[bstack1l1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਗ")]
        except Exception as error:
            logger.error(bstack1l1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡣࡷࡥ࠿ࠦࠢਘ") +  str(error))
        return bstack1lll11l11_opy_
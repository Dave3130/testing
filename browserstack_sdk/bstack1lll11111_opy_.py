# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1lll1111l_opy_ = {}
        bstack1ll1llll1_opy_ = os.environ.get(bstack1lllll1l_opy_ (u"ࠩࡆ࡙ࡗࡘࡅࡏࡖࡢࡔࡑࡇࡔࡇࡑࡕࡑࡤࡊࡁࡕࡃࠪ৽"), bstack1lllll1l_opy_ (u"ࠪࠫ৾"))
        if not bstack1ll1llll1_opy_:
            return bstack1lll1111l_opy_
        try:
            bstack1ll1lllll_opy_ = json.loads(bstack1ll1llll1_opy_)
            if bstack1lllll1l_opy_ (u"ࠦࡴࡹࠢ৿") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠧࡵࡳࠣ਀")] = bstack1ll1lllll_opy_[bstack1lllll1l_opy_ (u"ࠨ࡯ࡴࠤਁ")]
            if bstack1lllll1l_opy_ (u"ࠢࡰࡵࡢࡺࡪࡸࡳࡪࡱࡱࠦਂ") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠣࡱࡶ࡚ࡪࡸࡳࡪࡱࡱࠦਃ") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠤࡲࡷ࡛࡫ࡲࡴ࡫ࡲࡲࠧ਄")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢਅ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢਆ")))
            if bstack1lllll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࠨਇ") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡎࡢ࡯ࡨࠦਈ") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡏࡣࡰࡩࠧਉ")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤਊ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ਋")))
            if bstack1lllll1l_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧ਌") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶ࡛࡫ࡲࡴ࡫ࡲࡲࠧ਍") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷ࡜ࡥࡳࡵ࡬ࡳࡳࠨ਎")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਏ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣਐ")))
            if bstack1lllll1l_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࠣ਑") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠤࡧࡩࡻ࡯ࡣࡦࡐࡤࡱࡪࠨ਒") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࡑࡥࡲ࡫ࠢਓ")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦਔ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤਕ")))
            if bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࠣਖ") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡐࡤࡱࡪࠨਗ") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࡑࡥࡲ࡫ࠢਘ")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦਙ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤਚ")))
            if bstack1lllll1l_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡥࡶࡦࡴࡶ࡭ࡴࡴࠢਛ") in bstack1ll1lllll_opy_ or bstack1lllll1l_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡖࡦࡴࡶ࡭ࡴࡴࠢਜ") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡗࡧࡵࡷ࡮ࡵ࡮ࠣਝ")] = bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥਞ"), bstack1ll1lllll_opy_.get(bstack1lllll1l_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥਟ")))
            if bstack1lllll1l_opy_ (u"ࠤࡦࡹࡸࡺ࡯࡮ࡘࡤࡶ࡮ࡧࡢ࡭ࡧࡶࠦਠ") in bstack1ll1lllll_opy_:
                bstack1lll1111l_opy_[bstack1lllll1l_opy_ (u"ࠥࡧࡺࡹࡴࡰ࡯࡙ࡥࡷ࡯ࡡࡣ࡮ࡨࡷࠧਡ")] = bstack1ll1lllll_opy_[bstack1lllll1l_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨਢ")]
        except Exception as error:
            logger.error(bstack1lllll1l_opy_ (u"ࠧࡋࡸࡤࡧࡳࡸ࡮ࡵ࡮ࠡࡹ࡫࡭ࡱ࡫ࠠࡨࡧࡷࡸ࡮ࡴࡧࠡࡥࡸࡶࡷ࡫࡮ࡵࠢࡳࡰࡦࡺࡦࡰࡴࡰࠤࡩࡧࡴࡢ࠼ࠣࠦਣ") +  str(error))
        return bstack1lll1111l_opy_
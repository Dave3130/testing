# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1llll1_opy_ = {}
        bstack1lll1111l_opy_ = os.environ.get(bstack11lll1_opy_ (u"ࠬࡉࡕࡓࡔࡈࡒ࡙ࡥࡐࡍࡃࡗࡊࡔࡘࡍࡠࡆࡄࡘࡆ࠭৹"), bstack11lll1_opy_ (u"࠭ࠧ৺"))
        if not bstack1lll1111l_opy_:
            return bstack1ll1llll1_opy_
        try:
            bstack1ll1lllll_opy_ = json.loads(bstack1lll1111l_opy_)
            if bstack11lll1_opy_ (u"ࠢࡰࡵࠥ৻") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠣࡱࡶࠦৼ")] = bstack1ll1lllll_opy_[bstack11lll1_opy_ (u"ࠤࡲࡷࠧ৽")]
            if bstack11lll1_opy_ (u"ࠥࡳࡸࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ৾") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢ৿") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠧࡵࡳࡗࡧࡵࡷ࡮ࡵ࡮ࠣ਀")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠨ࡯ࡴࡡࡹࡩࡷࡹࡩࡰࡰࠥਁ"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠢࡰࡵ࡙ࡩࡷࡹࡩࡰࡰࠥਂ")))
            if bstack11lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࠤਃ") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ਄") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࡒࡦࡳࡥࠣਅ")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࠧਆ"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡔࡡ࡮ࡧࠥਇ")))
            if bstack11lll1_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸ࡟ࡷࡧࡵࡷ࡮ࡵ࡮ࠣਈ") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣਉ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡘࡨࡶࡸ࡯࡯࡯ࠤਊ")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡢࡺࡪࡸࡳࡪࡱࡱࠦ਋"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵ࡚ࡪࡸࡳࡪࡱࡱࠦ਌")))
            if bstack11lll1_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࠦ਍") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤ਎") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࡔࡡ࡮ࡧࠥਏ")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࠢਐ"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠣࡦࡨࡺ࡮ࡩࡥࡏࡣࡰࡩࠧ਑")))
            if bstack11lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࠦ਒") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤਓ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࡔࡡ࡮ࡧࠥਔ")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࠢਕ"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡏࡣࡰࡩࠧਖ")))
            if bstack11lll1_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡡࡹࡩࡷࡹࡩࡰࡰࠥਗ") in bstack1ll1lllll_opy_ or bstack11lll1_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥਘ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰ࡚ࡪࡸࡳࡪࡱࡱࠦਙ")] = bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡤࡼࡥࡳࡵ࡬ࡳࡳࠨਚ"), bstack1ll1lllll_opy_.get(bstack11lll1_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲ࡜ࡥࡳࡵ࡬ࡳࡳࠨਛ")))
            if bstack11lll1_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢਜ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11lll1_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਝ")] = bstack1ll1lllll_opy_[bstack11lll1_opy_ (u"ࠢࡤࡷࡶࡸࡴࡳࡖࡢࡴ࡬ࡥࡧࡲࡥࡴࠤਞ")]
        except Exception as error:
            logger.error(bstack11lll1_opy_ (u"ࠣࡇࡻࡧࡪࡶࡴࡪࡱࡱࠤࡼ࡮ࡩ࡭ࡧࠣ࡫ࡪࡺࡴࡪࡰࡪࠤࡨࡻࡲࡳࡧࡱࡸࠥࡶ࡬ࡢࡶࡩࡳࡷࡳࠠࡥࡣࡷࡥ࠿ࠦࠢਟ") +  str(error))
        return bstack1ll1llll1_opy_
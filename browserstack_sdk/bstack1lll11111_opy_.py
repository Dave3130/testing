# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import os
import json
import logging
logger = logging.getLogger(__name__)
class BrowserStackSdk:
    def get_current_platform():
        bstack1ll1llll1_opy_ = {}
        bstack1lll1111l_opy_ = os.environ.get(bstack11l111_opy_ (u"ࠫࡈ࡛ࡒࡓࡇࡑࡘࡤࡖࡌࡂࡖࡉࡓࡗࡓ࡟ࡅࡃࡗࡅࠬ৿"), bstack11l111_opy_ (u"ࠬ࠭਀"))
        if not bstack1lll1111l_opy_:
            return bstack1ll1llll1_opy_
        try:
            bstack1ll1lllll_opy_ = json.loads(bstack1lll1111l_opy_)
            if bstack11l111_opy_ (u"ࠨ࡯ࡴࠤਁ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠢࡰࡵࠥਂ")] = bstack1ll1lllll_opy_[bstack11l111_opy_ (u"ࠣࡱࡶࠦਃ")]
            if bstack11l111_opy_ (u"ࠤࡲࡷࡤࡼࡥࡳࡵ࡬ࡳࡳࠨ਄") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠥࡳࡸ࡜ࡥࡳࡵ࡬ࡳࡳࠨਅ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠦࡴࡹࡖࡦࡴࡶ࡭ࡴࡴࠢਆ")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠧࡵࡳࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਇ"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠨ࡯ࡴࡘࡨࡶࡸ࡯࡯࡯ࠤਈ")))
            if bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࠣਉ") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡐࡤࡱࡪࠨਊ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴࡑࡥࡲ࡫ࠢ਋")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠥࡦࡷࡵࡷࡴࡧࡵࠦ਌"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠦࡧࡸ࡯ࡸࡵࡨࡶࡓࡧ࡭ࡦࠤ਍")))
            if bstack11l111_opy_ (u"ࠧࡨࡲࡰࡹࡶࡩࡷࡥࡶࡦࡴࡶ࡭ࡴࡴࠢ਎") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠨࡢࡳࡱࡺࡷࡪࡸࡖࡦࡴࡶ࡭ࡴࡴࠢਏ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠢࡣࡴࡲࡻࡸ࡫ࡲࡗࡧࡵࡷ࡮ࡵ࡮ࠣਐ")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠣࡤࡵࡳࡼࡹࡥࡳࡡࡹࡩࡷࡹࡩࡰࡰࠥ਑"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠤࡥࡶࡴࡽࡳࡦࡴ࡙ࡩࡷࡹࡩࡰࡰࠥ਒")))
            if bstack11l111_opy_ (u"ࠥࡨࡪࡼࡩࡤࡧࠥਓ") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠦࡩ࡫ࡶࡪࡥࡨࡒࡦࡳࡥࠣਔ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠧࡪࡥࡷ࡫ࡦࡩࡓࡧ࡭ࡦࠤਕ")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠨࡤࡦࡸ࡬ࡧࡪࠨਖ"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠢࡥࡧࡹ࡭ࡨ࡫ࡎࡢ࡯ࡨࠦਗ")))
            if bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯ࠥਘ") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡒࡦࡳࡥࠣਙ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱࡓࡧ࡭ࡦࠤਚ")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠦࡵࡲࡡࡵࡨࡲࡶࡲࠨਛ"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠧࡶ࡬ࡢࡶࡩࡳࡷࡳࡎࡢ࡯ࡨࠦਜ")))
            if bstack11l111_opy_ (u"ࠨࡰ࡭ࡣࡷࡪࡴࡸ࡭ࡠࡸࡨࡶࡸ࡯࡯࡯ࠤਝ") in bstack1ll1lllll_opy_ or bstack11l111_opy_ (u"ࠢࡱ࡮ࡤࡸ࡫ࡵࡲ࡮ࡘࡨࡶࡸ࡯࡯࡯ࠤਞ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠣࡲ࡯ࡥࡹ࡬࡯ࡳ࡯࡙ࡩࡷࡹࡩࡰࡰࠥਟ")] = bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠤࡳࡰࡦࡺࡦࡰࡴࡰࡣࡻ࡫ࡲࡴ࡫ࡲࡲࠧਠ"), bstack1ll1lllll_opy_.get(bstack11l111_opy_ (u"ࠥࡴࡱࡧࡴࡧࡱࡵࡱ࡛࡫ࡲࡴ࡫ࡲࡲࠧਡ")))
            if bstack11l111_opy_ (u"ࠦࡨࡻࡳࡵࡱࡰ࡚ࡦࡸࡩࡢࡤ࡯ࡩࡸࠨਢ") in bstack1ll1lllll_opy_:
                bstack1ll1llll1_opy_[bstack11l111_opy_ (u"ࠧࡩࡵࡴࡶࡲࡱ࡛ࡧࡲࡪࡣࡥࡰࡪࡹࠢਣ")] = bstack1ll1lllll_opy_[bstack11l111_opy_ (u"ࠨࡣࡶࡵࡷࡳࡲ࡜ࡡࡳ࡫ࡤࡦࡱ࡫ࡳࠣਤ")]
        except Exception as error:
            logger.error(bstack11l111_opy_ (u"ࠢࡆࡺࡦࡩࡵࡺࡩࡰࡰࠣࡻ࡭࡯࡬ࡦࠢࡪࡩࡹࡺࡩ࡯ࡩࠣࡧࡺࡸࡲࡦࡰࡷࠤࡵࡲࡡࡵࡨࡲࡶࡲࠦࡤࡢࡶࡤ࠾ࠥࠨਥ") +  str(error))
        return bstack1ll1llll1_opy_
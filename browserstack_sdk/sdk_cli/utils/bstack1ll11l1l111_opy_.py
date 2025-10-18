# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack111l11l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1111ll1l_opy_:
    bstack1l1lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡱࡴࡲࡺ࡮ࡪࡥࡴࠢࡸࡸ࡮ࡲࡩࡵࡻࠣࡱࡪࡺࡨࡰࡦࡶࠤࡹࡵࠠࡴࡧࡷࠤࡦࡴࡤࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࠠ࡮ࡧࡷࡥࡩࡧࡴࡢ࠰ࠍࠤࠥࠦࠠࡊࡶࠣࡱࡦ࡯࡮ࡵࡣ࡬ࡲࡸࠦࡴࡸࡱࠣࡷࡪࡶࡡࡳࡣࡷࡩࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴ࡬ࡩࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡢࡰࡧࠤࡧࡻࡩ࡭ࡦࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹ࠮ࠋࠢࠣࠤࠥࡋࡡࡤࡪࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡫࡮ࡵࡴࡼࠤ࡮ࡹࠠࡦࡺࡳࡩࡨࡺࡥࡥࠢࡷࡳࠥࡨࡥࠡࡵࡷࡶࡺࡩࡴࡶࡴࡨࡨࠥࡧࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢ࡮ࡩࡾࡀࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡧ࡫ࡨࡰࡩࡥࡴࡺࡲࡨࠦ࠿ࠦࠢ࡮ࡷ࡯ࡸ࡮ࡥࡤࡳࡱࡳࡨࡴࡽ࡮ࠣ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡸࡤࡰࡺ࡫ࡳࠣ࠼ࠣ࡟ࡱ࡯ࡳࡵࠢࡲࡪࠥࡺࡡࡨࠢࡹࡥࡱࡻࡥࡴ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࢁࠏࠦࠠࠡࠢࠥࠦࠧᘀ")
    _11lll1lllll_opy_: Dict[str, Dict[str, Any]] = {}
    _11llll11lll_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll11111_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1l1lll1_opy_ (u"ࠧࠨᘁ") or key_value.strip() == bstack1l1lll1_opy_ (u"ࠨࠢᘂ"):
            logger.error(bstack1l1lll1_opy_ (u"ࠢ࡬ࡧࡼࡣࡳࡧ࡭ࡦࠢࡤࡲࡩࠦ࡫ࡦࡻࡢࡺࡦࡲࡵࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡲࡴࡴ࠭࡯ࡷ࡯ࡰࠥࡧ࡮ࡥࠢࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽࠧᘃ"))
        values: List[str] = bstack1ll1111ll1l_opy_.bstack11llll111l1_opy_(key_value)
        bstack11llll11l1l_opy_ = {bstack1l1lll1_opy_ (u"ࠣࡨ࡬ࡩࡱࡪ࡟ࡵࡻࡳࡩࠧᘄ"): bstack1l1lll1_opy_ (u"ࠤࡰࡹࡱࡺࡩࡠࡦࡵࡳࡵࡪ࡯ࡸࡰࠥᘅ"), bstack1l1lll1_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘆ"): values}
        bstack11llll11l11_opy_ = bstack1ll1111ll1l_opy_._11llll11lll_opy_ if bstack11llll11111_opy_ else bstack1ll1111ll1l_opy_._11lll1lllll_opy_
        if key_name in bstack11llll11l11_opy_:
            bstack11lll1llll1_opy_ = bstack11llll11l11_opy_[key_name]
            bstack11llll1111l_opy_ = bstack11lll1llll1_opy_.get(bstack1l1lll1_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࡶࠦᘇ"), [])
            for val in values:
                if val not in bstack11llll1111l_opy_:
                    bstack11llll1111l_opy_.append(val)
            bstack11lll1llll1_opy_[bstack1l1lll1_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࡷࠧᘈ")] = bstack11llll1111l_opy_
        else:
            bstack11llll11l11_opy_[key_name] = bstack11llll11l1l_opy_
    @staticmethod
    def bstack1ll1l1l1ll1_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1111ll1l_opy_._11lll1lllll_opy_
    @staticmethod
    def bstack11llll111ll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1111ll1l_opy_._11llll11lll_opy_
    @staticmethod
    def bstack11llll111l1_opy_(bstack11llll11ll1_opy_: str) -> List[str]:
        bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡵࡲࡩࡵࡵࠣࡸ࡭࡫ࠠࡪࡰࡳࡹࡹࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡢࡺࠢࡦࡳࡲࡳࡡࡴࠢࡺ࡬࡮ࡲࡥࠡࡴࡨࡷࡵ࡫ࡣࡵ࡫ࡱ࡫ࠥࡪ࡯ࡶࡤ࡯ࡩ࠲ࡷࡵࡰࡶࡨࡨࠥࡹࡵࡣࡵࡷࡶ࡮ࡴࡧࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡻࡥࡲࡶ࡬ࡦ࠼ࠣࠫࡦ࠲ࠠࠣࡤ࠯ࡧࠧ࠲ࠠࡥࠩࠣ࠱ࡃ࡛ࠦࠨࡣࠪ࠰ࠥ࠭ࡢ࠭ࡥࠪ࠰ࠥ࠭ࡤࠨ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘉ")
        pattern = re.compile(bstack1l1lll1_opy_ (u"ࡲࠨࠤࠫ࡟ࡣࠨ࡝ࠫࠫࠥࢀ࠭ࡡ࡞࠭࡟࠮࠭ࠬᘊ"))
        result = []
        for match in pattern.finditer(bstack11llll11ll1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1l1lll1_opy_ (u"ࠣࡗࡷ࡭ࡱ࡯ࡴࡺࠢࡦࡰࡦࡹࡳࠡࡵ࡫ࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡵ࡫ࡤࡸࡪࡪࠢᘋ"))
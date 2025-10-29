# coding: UTF-8
import sys
bstack1l1l111_opy_ = sys.version_info [0] == 2
bstack11l1ll_opy_ = 2048
bstack1llll11_opy_ = 7
def bstack11ll1l_opy_ (bstack1llllll1_opy_):
    global bstack1ll11_opy_
    bstack11ll111_opy_ = ord (bstack1llllll1_opy_ [-1])
    bstack1lll111_opy_ = bstack1llllll1_opy_ [:-1]
    bstack11l11l_opy_ = bstack11ll111_opy_ % len (bstack1lll111_opy_)
    bstack1l1ll11_opy_ = bstack1lll111_opy_ [:bstack11l11l_opy_] + bstack1lll111_opy_ [bstack11l11l_opy_:]
    if bstack1l1l111_opy_:
        bstack11111l1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    else:
        bstack11111l1_opy_ = str () .join ([chr (ord (char) - bstack11l1ll_opy_ - (bstack1l11111_opy_ + bstack11ll111_opy_) % bstack1llll11_opy_) for bstack1l11111_opy_, char in enumerate (bstack1l1ll11_opy_)])
    return eval (bstack11111l1_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack1l11111111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1l1l11_opy_:
    bstack11ll1l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡄࡷࡶࡸࡴࡳࡔࡢࡩࡐࡥࡳࡧࡧࡦࡴࠣࡴࡷࡵࡶࡪࡦࡨࡷࠥࡻࡴࡪ࡮࡬ࡸࡾࠦ࡭ࡦࡶ࡫ࡳࡩࡹࠠࡵࡱࠣࡷࡪࡺࠠࡢࡰࡧࠤࡷ࡫ࡴࡳ࡫ࡨࡺࡪࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࠣࡱࡪࡺࡡࡥࡣࡷࡥ࠳ࠐࠠࠡࠢࠣࡍࡹࠦ࡭ࡢ࡫ࡱࡸࡦ࡯࡮ࡴࠢࡷࡻࡴࠦࡳࡦࡲࡤࡶࡦࡺࡥࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡨ࡮ࡩࡴࡪࡱࡱࡥࡷ࡯ࡥࡴࠢࡩࡳࡷࠦࡴࡦࡵࡷࠤࡱ࡫ࡶࡦ࡮ࠣࡥࡳࡪࠠࡣࡷ࡬ࡰࡩࠦ࡬ࡦࡸࡨࡰࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࡵ࠱ࠎࠥࠦࠠࠡࡇࡤࡧ࡭ࠦ࡭ࡦࡶࡤࡨࡦࡺࡡࠡࡧࡱࡸࡷࡿࠠࡪࡵࠣࡩࡽࡶࡥࡤࡶࡨࡨࠥࡺ࡯ࠡࡤࡨࠤࡸࡺࡲࡶࡥࡷࡹࡷ࡫ࡤࠡࡣࡶ࠾ࠏࠦࠠࠡࠢࠣࠤࠥࡱࡥࡺ࠼ࠣࡿࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡪ࡮࡫࡬ࡥࡡࡷࡽࡵ࡫ࠢ࠻ࠢࠥࡱࡺࡲࡴࡪࡡࡧࡶࡴࡶࡤࡰࡹࡱࠦ࠱ࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦࡻࡧ࡬ࡶࡧࡶࠦ࠿࡛ࠦ࡭࡫ࡶࡸࠥࡵࡦࠡࡶࡤ࡫ࠥࡼࡡ࡭ࡷࡨࡷࡢࠐࠠࠡࠢࠣࠤࠥࠦࡽࠋࠢࠣࠤࠥࠨࠢࠣᘴ")
    _11lll1ll1ll_opy_: Dict[str, Dict[str, Any]] = {}
    _11lll1l1l11_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11lll1l11ll_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack11ll1l_opy_ (u"ࠣࠤᘵ") or key_value.strip() == bstack11ll1l_opy_ (u"ࠤࠥᘶ"):
            logger.error(bstack11ll1l_opy_ (u"ࠥ࡯ࡪࡿ࡟࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢ࡮ࡩࡾࡥࡶࡢ࡮ࡸࡩࠥࡳࡵࡴࡶࠣࡦࡪࠦ࡮ࡰࡰ࠰ࡲࡺࡲ࡬ࠡࡣࡱࡨࠥࡴ࡯࡯࠯ࡨࡱࡵࡺࡹࠣᘷ"))
        values: List[str] = bstack1ll1l1l1l11_opy_.bstack11lll1l1l1l_opy_(key_value)
        bstack11lll1l1ll1_opy_ = {bstack11ll1l_opy_ (u"ࠦ࡫࡯ࡥ࡭ࡦࡢࡸࡾࡶࡥࠣᘸ"): bstack11ll1l_opy_ (u"ࠧࡳࡵ࡭ࡶ࡬ࡣࡩࡸ࡯ࡱࡦࡲࡻࡳࠨᘹ"), bstack11ll1l_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࡸࠨᘺ"): values}
        bstack11lll1l1lll_opy_ = bstack1ll1l1l1l11_opy_._11lll1l1l11_opy_ if bstack11lll1l11ll_opy_ else bstack1ll1l1l1l11_opy_._11lll1ll1ll_opy_
        if key_name in bstack11lll1l1lll_opy_:
            bstack11lll1ll111_opy_ = bstack11lll1l1lll_opy_[key_name]
            bstack11lll1ll11l_opy_ = bstack11lll1ll111_opy_.get(bstack11ll1l_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࡹࠢᘻ"), [])
            for val in values:
                if val not in bstack11lll1ll11l_opy_:
                    bstack11lll1ll11l_opy_.append(val)
            bstack11lll1ll111_opy_[bstack11ll1l_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࡳࠣᘼ")] = bstack11lll1ll11l_opy_
        else:
            bstack11lll1l1lll_opy_[key_name] = bstack11lll1l1ll1_opy_
    @staticmethod
    def bstack1ll11ll11ll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1l1l11_opy_._11lll1ll1ll_opy_
    @staticmethod
    def bstack11lll1ll1l1_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1l1l11_opy_._11lll1l1l11_opy_
    @staticmethod
    def bstack11lll1l1l1l_opy_(bstack11lll1l11l1_opy_: str) -> List[str]:
        bstack11ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࠣࠤࠥࠦࡓࡱ࡮࡬ࡸࡸࠦࡴࡩࡧࠣ࡭ࡳࡶࡵࡵࠢࡶࡸࡷ࡯࡮ࡨࠢࡥࡽࠥࡩ࡯࡮࡯ࡤࡷࠥࡽࡨࡪ࡮ࡨࠤࡷ࡫ࡳࡱࡧࡦࡸ࡮ࡴࡧࠡࡦࡲࡹࡧࡲࡥ࠮ࡳࡸࡳࡹ࡫ࡤࠡࡵࡸࡦࡸࡺࡲࡪࡰࡪࡷ࠳ࠐࠠࠡࠢࠣࠤࠥࠦࠠࡇࡱࡵࠤࡪࡾࡡ࡮ࡲ࡯ࡩ࠿ࠦࠧࡢ࠮ࠣࠦࡧ࠲ࡣࠣ࠮ࠣࡨࠬࠦ࠭࠿ࠢ࡞ࠫࡦ࠭ࠬࠡࠩࡥ࠰ࡨ࠭ࠬࠡࠩࡧࠫࡢࠐࠠࠡࠢࠣࠤࠥࠦࠠࠣࠤࠥᘽ")
        pattern = re.compile(bstack11ll1l_opy_ (u"ࡵࠫࠧ࠮࡛࡟ࠤࡠ࠮࠮ࠨࡼࠩ࡝ࡡ࠰ࡢ࠱ࠩࠨᘾ"))
        result = []
        for match in pattern.finditer(bstack11lll1l11l1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack11ll1l_opy_ (u"࡚ࠦࡺࡩ࡭࡫ࡷࡽࠥࡩ࡬ࡢࡵࡶࠤࡸ࡮࡯ࡶ࡮ࡧࠤࡳࡵࡴࠡࡤࡨࠤ࡮ࡴࡳࡵࡣࡱࡸ࡮ࡧࡴࡦࡦࠥᘿ"))
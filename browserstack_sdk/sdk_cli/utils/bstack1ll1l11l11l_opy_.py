# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack1lll11ll11_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l11111_opy_:
    bstack11l111_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡃࡶࡵࡷࡳࡲ࡚ࡡࡨࡏࡤࡲࡦ࡭ࡥࡳࠢࡳࡶࡴࡼࡩࡥࡧࡶࠤࡺࡺࡩ࡭࡫ࡷࡽࠥࡳࡥࡵࡪࡲࡨࡸࠦࡴࡰࠢࡶࡩࡹࠦࡡ࡯ࡦࠣࡶࡪࡺࡲࡪࡧࡹࡩࠥࡩࡵࡴࡶࡲࡱࠥࡺࡡࡨࠢࡰࡩࡹࡧࡤࡢࡶࡤ࠲ࠏࠦࠠࠡࠢࡌࡸࠥࡳࡡࡪࡰࡷࡥ࡮ࡴࡳࠡࡶࡺࡳࠥࡹࡥࡱࡣࡵࡥࡹ࡫ࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡧ࡭ࡨࡺࡩࡰࡰࡤࡶ࡮࡫ࡳࠡࡨࡲࡶࠥࡺࡥࡴࡶࠣࡰࡪࡼࡥ࡭ࠢࡤࡲࡩࠦࡢࡶ࡫࡯ࡨࠥࡲࡥࡷࡧ࡯ࠤࡨࡻࡳࡵࡱࡰࠤࡹࡧࡧࡴ࠰ࠍࠤࠥࠦࠠࡆࡣࡦ࡬ࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡦࡰࡷࡶࡾࠦࡩࡴࠢࡨࡼࡵ࡫ࡣࡵࡧࡧࠤࡹࡵࠠࡣࡧࠣࡷࡹࡸࡵࡤࡶࡸࡶࡪࡪࠠࡢࡵ࠽ࠎࠥࠦࠠࠡࠢࠣࠤࡰ࡫ࡹ࠻ࠢࡾࠎࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠤࡩ࡭ࡪࡲࡤࡠࡶࡼࡴࡪࠨ࠺ࠡࠤࡰࡹࡱࡺࡩࡠࡦࡵࡳࡵࡪ࡯ࡸࡰࠥ࠰ࠏࠦࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠥࡺࡦࡲࡵࡦࡵࠥ࠾ࠥࡡ࡬ࡪࡵࡷࠤࡴ࡬ࠠࡵࡣࡪࠤࡻࡧ࡬ࡶࡧࡶࡡࠏࠦࠠࠡࠢࠣࠤࠥࢃࠊࠡࠢࠣࠤࠧࠨࠢᗴ")
    _11lll1lll1l_opy_: Dict[str, Dict[str, Any]] = {}
    _11lll1llll1_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll11l11_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack11l111_opy_ (u"ࠢࠣᗵ") or key_value.strip() == bstack11l111_opy_ (u"ࠣࠤᗶ"):
            logger.error(bstack11l111_opy_ (u"ࠤ࡮ࡩࡾࡥ࡮ࡢ࡯ࡨࠤࡦࡴࡤࠡ࡭ࡨࡽࡤࡼࡡ࡭ࡷࡨࠤࡲࡻࡳࡵࠢࡥࡩࠥࡴ࡯࡯࠯ࡱࡹࡱࡲࠠࡢࡰࡧࠤࡳࡵ࡮࠮ࡧࡰࡴࡹࡿࠢᗷ"))
        values: List[str] = bstack1ll11l11111_opy_.bstack11llll11l1l_opy_(key_value)
        bstack11llll11ll1_opy_ = {bstack11l111_opy_ (u"ࠥࡪ࡮࡫࡬ࡥࡡࡷࡽࡵ࡫ࠢᗸ"): bstack11l111_opy_ (u"ࠦࡲࡻ࡬ࡵ࡫ࡢࡨࡷࡵࡰࡥࡱࡺࡲࠧᗹ"), bstack11l111_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࡷࠧᗺ"): values}
        bstack11llll11111_opy_ = bstack1ll11l11111_opy_._11lll1llll1_opy_ if bstack11llll11l11_opy_ else bstack1ll11l11111_opy_._11lll1lll1l_opy_
        if key_name in bstack11llll11111_opy_:
            bstack11llll111ll_opy_ = bstack11llll11111_opy_[key_name]
            bstack11llll1111l_opy_ = bstack11llll111ll_opy_.get(bstack11l111_opy_ (u"ࠨࡶࡢ࡮ࡸࡩࡸࠨᗻ"), [])
            for val in values:
                if val not in bstack11llll1111l_opy_:
                    bstack11llll1111l_opy_.append(val)
            bstack11llll111ll_opy_[bstack11l111_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࡹࠢᗼ")] = bstack11llll1111l_opy_
        else:
            bstack11llll11111_opy_[key_name] = bstack11llll11ll1_opy_
    @staticmethod
    def bstack1ll11l11l11_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11111_opy_._11lll1lll1l_opy_
    @staticmethod
    def bstack11lll1lllll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11111_opy_._11lll1llll1_opy_
    @staticmethod
    def bstack11llll11l1l_opy_(bstack11llll111l1_opy_: str) -> List[str]:
        bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࠢࠣࠤ࡙ࠥࡰ࡭࡫ࡷࡷࠥࡺࡨࡦࠢ࡬ࡲࡵࡻࡴࠡࡵࡷࡶ࡮ࡴࡧࠡࡤࡼࠤࡨࡵ࡭࡮ࡣࡶࠤࡼ࡮ࡩ࡭ࡧࠣࡶࡪࡹࡰࡦࡥࡷ࡭ࡳ࡭ࠠࡥࡱࡸࡦࡱ࡫࠭ࡲࡷࡲࡸࡪࡪࠠࡴࡷࡥࡷࡹࡸࡩ࡯ࡩࡶ࠲ࠏࠦࠠࠡࠢࠣࠤࠥࠦࡆࡰࡴࠣࡩࡽࡧ࡭ࡱ࡮ࡨ࠾ࠥ࠭ࡡ࠭ࠢࠥࡦ࠱ࡩࠢ࠭ࠢࡧࠫࠥ࠳࠾ࠡ࡝ࠪࡥࠬ࠲ࠠࠨࡤ࠯ࡧࠬ࠲ࠠࠨࡦࠪࡡࠏࠦࠠࠡࠢࠣࠤࠥࠦࠢࠣࠤᗽ")
        pattern = re.compile(bstack11l111_opy_ (u"ࡴࠪࠦ࠭ࡡ࡞ࠣ࡟࠭࠭ࠧࢂࠨ࡜ࡠ࠯ࡡ࠰࠯ࠧᗾ"))
        result = []
        for match in pattern.finditer(bstack11llll111l1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack11l111_opy_ (u"࡙ࠥࡹ࡯࡬ࡪࡶࡼࠤࡨࡲࡡࡴࡵࠣࡷ࡭ࡵࡵ࡭ࡦࠣࡲࡴࡺࠠࡣࡧࠣ࡭ࡳࡹࡴࡢࡰࡷ࡭ࡦࡺࡥࡥࠤᗿ"))
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
import re
from typing import List, Dict, Any
from bstack_utils.bstack1l1l1l1111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l111lll_opy_:
    bstack1ll11_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡅࡸࡷࡹࡵ࡭ࡕࡣࡪࡑࡦࡴࡡࡨࡧࡵࠤࡵࡸ࡯ࡷ࡫ࡧࡩࡸࠦࡵࡵ࡫࡯࡭ࡹࡿࠠ࡮ࡧࡷ࡬ࡴࡪࡳࠡࡶࡲࠤࡸ࡫ࡴࠡࡣࡱࡨࠥࡸࡥࡵࡴ࡬ࡩࡻ࡫ࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࠤࡲ࡫ࡴࡢࡦࡤࡸࡦ࠴ࠊࠡࠢࠣࠤࡎࡺࠠ࡮ࡣ࡬ࡲࡹࡧࡩ࡯ࡵࠣࡸࡼࡵࠠࡴࡧࡳࡥࡷࡧࡴࡦࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡩ࡯ࡣࡵ࡫ࡲࡲࡦࡸࡩࡦࡵࠣࡪࡴࡸࠠࡵࡧࡶࡸࠥࡲࡥࡷࡧ࡯ࠤࡦࡴࡤࠡࡤࡸ࡭ࡱࡪࠠ࡭ࡧࡹࡩࡱࠦࡣࡶࡵࡷࡳࡲࠦࡴࡢࡩࡶ࠲ࠏࠦࠠࠡࠢࡈࡥࡨ࡮ࠠ࡮ࡧࡷࡥࡩࡧࡴࡢࠢࡨࡲࡹࡸࡹࠡ࡫ࡶࠤࡪࡾࡰࡦࡥࡷࡩࡩࠦࡴࡰࠢࡥࡩࠥࡹࡴࡳࡷࡦࡸࡺࡸࡥࡥࠢࡤࡷ࠿ࠐࠠࠡࠢࠣࠤࠥࠦ࡫ࡦࡻ࠽ࠤࢀࠐࠠࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠦ࡫࡯ࡥ࡭ࡦࡢࡸࡾࡶࡥࠣ࠼ࠣࠦࡲࡻ࡬ࡵ࡫ࡢࡨࡷࡵࡰࡥࡱࡺࡲࠧ࠲ࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧࡼࡡ࡭ࡷࡨࡷࠧࡀࠠ࡜࡮࡬ࡷࡹࠦ࡯ࡧࠢࡷࡥ࡬ࠦࡶࡢ࡮ࡸࡩࡸࡣࠊࠡࠢࠣࠤࠥࠦࠠࡾࠌࠣࠤࠥࠦࠢࠣࠤᘄ")
    _11llll1l111_opy_: Dict[str, Dict[str, Any]] = {}
    _11llll111l1_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll1l11l_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1ll11_opy_ (u"ࠤࠥᘅ") or key_value.strip() == bstack1ll11_opy_ (u"ࠥࠦᘆ"):
            logger.error(bstack1ll11_opy_ (u"ࠦࡰ࡫ࡹࡠࡰࡤࡱࡪࠦࡡ࡯ࡦࠣ࡯ࡪࡿ࡟ࡷࡣ࡯ࡹࡪࠦ࡭ࡶࡵࡷࠤࡧ࡫ࠠ࡯ࡱࡱ࠱ࡳࡻ࡬࡭ࠢࡤࡲࡩࠦ࡮ࡰࡰ࠰ࡩࡲࡶࡴࡺࠤᘇ"))
        values: List[str] = bstack1ll1l111lll_opy_.bstack11llll11ll1_opy_(key_value)
        bstack11llll1111l_opy_ = {bstack1ll11_opy_ (u"ࠧ࡬ࡩࡦ࡮ࡧࡣࡹࡿࡰࡦࠤᘈ"): bstack1ll11_opy_ (u"ࠨ࡭ࡶ࡮ࡷ࡭ࡤࡪࡲࡰࡲࡧࡳࡼࡴࠢᘉ"), bstack1ll11_opy_ (u"ࠢࡷࡣ࡯ࡹࡪࡹࠢᘊ"): values}
        bstack11llll111ll_opy_ = bstack1ll1l111lll_opy_._11llll111l1_opy_ if bstack11llll1l11l_opy_ else bstack1ll1l111lll_opy_._11llll1l111_opy_
        if key_name in bstack11llll111ll_opy_:
            bstack11llll11l1l_opy_ = bstack11llll111ll_opy_[key_name]
            bstack11llll11lll_opy_ = bstack11llll11l1l_opy_.get(bstack1ll11_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࡳࠣᘋ"), [])
            for val in values:
                if val not in bstack11llll11lll_opy_:
                    bstack11llll11lll_opy_.append(val)
            bstack11llll11l1l_opy_[bstack1ll11_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᘌ")] = bstack11llll11lll_opy_
        else:
            bstack11llll111ll_opy_[key_name] = bstack11llll1111l_opy_
    @staticmethod
    def bstack1ll1l11ll11_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l111lll_opy_._11llll1l111_opy_
    @staticmethod
    def bstack11llll11l11_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l111lll_opy_._11llll111l1_opy_
    @staticmethod
    def bstack11llll11ll1_opy_(bstack11llll1l1l1_opy_: str) -> List[str]:
        bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࠤࠥࠦࠠࡔࡲ࡯࡭ࡹࡹࠠࡵࡪࡨࠤ࡮ࡴࡰࡶࡶࠣࡷࡹࡸࡩ࡯ࡩࠣࡦࡾࠦࡣࡰ࡯ࡰࡥࡸࠦࡷࡩ࡫࡯ࡩࠥࡸࡥࡴࡲࡨࡧࡹ࡯࡮ࡨࠢࡧࡳࡺࡨ࡬ࡦ࠯ࡴࡹࡴࡺࡥࡥࠢࡶࡹࡧࡹࡴࡳ࡫ࡱ࡫ࡸ࠴ࠊࠡࠢࠣࠤࠥࠦࠠࠡࡈࡲࡶࠥ࡫ࡸࡢ࡯ࡳࡰࡪࡀࠠࠨࡣ࠯ࠤࠧࡨࠬࡤࠤ࠯ࠤࡩ࠭ࠠ࠮ࡀࠣ࡟ࠬࡧࠧ࠭ࠢࠪࡦ࠱ࡩࠧ࠭ࠢࠪࡨࠬࡣࠊࠡࠢࠣࠤࠥࠦࠠࠡࠤࠥࠦᘍ")
        pattern = re.compile(bstack1ll11_opy_ (u"ࡶࠬࠨࠨ࡜ࡠࠥࡡ࠯࠯ࠢࡽࠪ࡞ࡢ࠱ࡣࠫࠪࠩᘎ"))
        result = []
        for match in pattern.finditer(bstack11llll1l1l1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1ll11_opy_ (u"࡛ࠧࡴࡪ࡮࡬ࡸࡾࠦࡣ࡭ࡣࡶࡷࠥࡹࡨࡰࡷ࡯ࡨࠥࡴ࡯ࡵࠢࡥࡩࠥ࡯࡮ࡴࡶࡤࡲࡹ࡯ࡡࡵࡧࡧࠦᘏ"))
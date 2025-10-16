# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l111l1_opy_:
    bstack1l_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡈࡻࡳࡵࡱࡰࡘࡦ࡭ࡍࡢࡰࡤ࡫ࡪࡸࠠࡱࡴࡲࡺ࡮ࡪࡥࡴࠢࡸࡸ࡮ࡲࡩࡵࡻࠣࡱࡪࡺࡨࡰࡦࡶࠤࡹࡵࠠࡴࡧࡷࠤࡦࡴࡤࠡࡴࡨࡸࡷ࡯ࡥࡷࡧࠣࡧࡺࡹࡴࡰ࡯ࠣࡸࡦ࡭ࠠ࡮ࡧࡷࡥࡩࡧࡴࡢ࠰ࠍࠤࠥࠦࠠࡊࡶࠣࡱࡦ࡯࡮ࡵࡣ࡬ࡲࡸࠦࡴࡸࡱࠣࡷࡪࡶࡡࡳࡣࡷࡩࠥࡳࡥࡵࡣࡧࡥࡹࡧࠠࡥ࡫ࡦࡸ࡮ࡵ࡮ࡢࡴ࡬ࡩࡸࠦࡦࡰࡴࠣࡸࡪࡹࡴࠡ࡮ࡨࡺࡪࡲࠠࡢࡰࡧࠤࡧࡻࡩ࡭ࡦࠣࡰࡪࡼࡥ࡭ࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࡹ࠮ࠋࠢࠣࠤࠥࡋࡡࡤࡪࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥ࡫࡮ࡵࡴࡼࠤ࡮ࡹࠠࡦࡺࡳࡩࡨࡺࡥࡥࠢࡷࡳࠥࡨࡥࠡࡵࡷࡶࡺࡩࡴࡶࡴࡨࡨࠥࡧࡳ࠻ࠌࠣࠤࠥࠦࠠࠡࠢ࡮ࡩࡾࡀࠠࡼࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡧ࡫ࡨࡰࡩࡥࡴࡺࡲࡨࠦ࠿ࠦࠢ࡮ࡷ࡯ࡸ࡮ࡥࡤࡳࡱࡳࡨࡴࡽ࡮ࠣ࠮ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠠࠣࡸࡤࡰࡺ࡫ࡳࠣ࠼ࠣ࡟ࡱ࡯ࡳࡵࠢࡲࡪࠥࡺࡡࡨࠢࡹࡥࡱࡻࡥࡴ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࢁࠏࠦࠠࠡࠢࠥࠦࠧᘇ")
    _11llll1l11l_opy_: Dict[str, Dict[str, Any]] = {}
    _11llll1l1l1_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll111ll_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1l_opy_ (u"ࠧࠨᘈ") or key_value.strip() == bstack1l_opy_ (u"ࠨࠢᘉ"):
            logger.error(bstack1l_opy_ (u"ࠢ࡬ࡧࡼࡣࡳࡧ࡭ࡦࠢࡤࡲࡩࠦ࡫ࡦࡻࡢࡺࡦࡲࡵࡦࠢࡰࡹࡸࡺࠠࡣࡧࠣࡲࡴࡴ࠭࡯ࡷ࡯ࡰࠥࡧ࡮ࡥࠢࡱࡳࡳ࠳ࡥ࡮ࡲࡷࡽࠧᘊ"))
        values: List[str] = bstack1ll11l111l1_opy_.bstack11llll111l1_opy_(key_value)
        bstack11llll11ll1_opy_ = {bstack1l_opy_ (u"ࠣࡨ࡬ࡩࡱࡪ࡟ࡵࡻࡳࡩࠧᘋ"): bstack1l_opy_ (u"ࠤࡰࡹࡱࡺࡩࡠࡦࡵࡳࡵࡪ࡯ࡸࡰࠥᘌ"), bstack1l_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘍ"): values}
        bstack11llll1111l_opy_ = bstack1ll11l111l1_opy_._11llll1l1l1_opy_ if bstack11llll111ll_opy_ else bstack1ll11l111l1_opy_._11llll1l11l_opy_
        if key_name in bstack11llll1111l_opy_:
            bstack11llll1l111_opy_ = bstack11llll1111l_opy_[key_name]
            bstack11llll11l11_opy_ = bstack11llll1l111_opy_.get(bstack1l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࡶࠦᘎ"), [])
            for val in values:
                if val not in bstack11llll11l11_opy_:
                    bstack11llll11l11_opy_.append(val)
            bstack11llll1l111_opy_[bstack1l_opy_ (u"ࠧࡼࡡ࡭ࡷࡨࡷࠧᘏ")] = bstack11llll11l11_opy_
        else:
            bstack11llll1111l_opy_[key_name] = bstack11llll11ll1_opy_
    @staticmethod
    def bstack1ll11lllll1_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l111l1_opy_._11llll1l11l_opy_
    @staticmethod
    def bstack11llll11l1l_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l111l1_opy_._11llll1l1l1_opy_
    @staticmethod
    def bstack11llll111l1_opy_(bstack11llll11lll_opy_: str) -> List[str]:
        bstack1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࠠࠡࠢࠣࡗࡵࡲࡩࡵࡵࠣࡸ࡭࡫ࠠࡪࡰࡳࡹࡹࠦࡳࡵࡴ࡬ࡲ࡬ࠦࡢࡺࠢࡦࡳࡲࡳࡡࡴࠢࡺ࡬࡮ࡲࡥࠡࡴࡨࡷࡵ࡫ࡣࡵ࡫ࡱ࡫ࠥࡪ࡯ࡶࡤ࡯ࡩ࠲ࡷࡵࡰࡶࡨࡨࠥࡹࡵࡣࡵࡷࡶ࡮ࡴࡧࡴ࠰ࠍࠤࠥࠦࠠࠡࠢࠣࠤࡋࡵࡲࠡࡧࡻࡥࡲࡶ࡬ࡦ࠼ࠣࠫࡦ࠲ࠠࠣࡤ࠯ࡧࠧ࠲ࠠࡥࠩࠣ࠱ࡃ࡛ࠦࠨࡣࠪ࠰ࠥ࠭ࡢ࠭ࡥࠪ࠰ࠥ࠭ࡤࠨ࡟ࠍࠤࠥࠦࠠࠡࠢࠣࠤࠧࠨࠢᘐ")
        pattern = re.compile(bstack1l_opy_ (u"ࡲࠨࠤࠫ࡟ࡣࠨ࡝ࠫࠫࠥࢀ࠭ࡡ࡞࠭࡟࠮࠭ࠬᘑ"))
        result = []
        for match in pattern.finditer(bstack11llll11lll_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1l_opy_ (u"ࠣࡗࡷ࡭ࡱ࡯ࡴࡺࠢࡦࡰࡦࡹࡳࠡࡵ࡫ࡳࡺࡲࡤࠡࡰࡲࡸࠥࡨࡥࠡ࡫ࡱࡷࡹࡧ࡮ࡵ࡫ࡤࡸࡪࡪࠢᘒ"))
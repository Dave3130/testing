# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l11ll1_opy_:
    bstack1lllll1_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡶࡲࡰࡸ࡬ࡨࡪࡹࠠࡶࡶ࡬ࡰ࡮ࡺࡹࠡ࡯ࡨࡸ࡭ࡵࡤࡴࠢࡷࡳࠥࡹࡥࡵࠢࡤࡲࡩࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࠥࡳࡥࡵࡣࡧࡥࡹࡧ࠮ࠋࠢࠣࠤࠥࡏࡴࠡ࡯ࡤ࡭ࡳࡺࡡࡪࡰࡶࠤࡹࡽ࡯ࠡࡵࡨࡴࡦࡸࡡࡵࡧࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡪࡧࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡧ࡮ࡥࠢࡥࡹ࡮ࡲࡤࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷ࠳ࠐࠠࠡࠢࠣࡉࡦࡩࡨࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡩࡳࡺࡲࡺࠢ࡬ࡷࠥ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡵࡱࠣࡦࡪࠦࡳࡵࡴࡸࡧࡹࡻࡲࡦࡦࠣࡥࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠ࡬ࡧࡼ࠾ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧ࡬ࡩࡦ࡮ࡧࡣࡹࡿࡰࡦࠤ࠽ࠤࠧࡳࡵ࡭ࡶ࡬ࡣࡩࡸ࡯ࡱࡦࡲࡻࡳࠨࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡶࡢ࡮ࡸࡩࡸࠨ࠺ࠡ࡝࡯࡭ࡸࡺࠠࡰࡨࠣࡸࡦ࡭ࠠࡷࡣ࡯ࡹࡪࡹ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠣࠤࠥᘅ")
    _11llll1l111_opy_: Dict[str, Dict[str, Any]] = {}
    _11llll11l11_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll1l11l_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1lllll1_opy_ (u"ࠥࠦᘆ") or key_value.strip() == bstack1lllll1_opy_ (u"ࠦࠧᘇ"):
            logger.error(bstack1lllll1_opy_ (u"ࠧࡱࡥࡺࡡࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡰ࡫ࡹࡠࡸࡤࡰࡺ࡫ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡥࡳࡪࠠ࡯ࡱࡱ࠱ࡪࡳࡰࡵࡻࠥᘈ"))
        values: List[str] = bstack1ll11l11ll1_opy_.bstack11llll11l1l_opy_(key_value)
        bstack11llll11ll1_opy_ = {bstack1lllll1_opy_ (u"ࠨࡦࡪࡧ࡯ࡨࡤࡺࡹࡱࡧࠥᘉ"): bstack1lllll1_opy_ (u"ࠢ࡮ࡷ࡯ࡸ࡮ࡥࡤࡳࡱࡳࡨࡴࡽ࡮ࠣᘊ"), bstack1lllll1_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࡳࠣᘋ"): values}
        bstack11llll111l1_opy_ = bstack1ll11l11ll1_opy_._11llll11l11_opy_ if bstack11llll1l11l_opy_ else bstack1ll11l11ll1_opy_._11llll1l111_opy_
        if key_name in bstack11llll111l1_opy_:
            bstack11llll111ll_opy_ = bstack11llll111l1_opy_[key_name]
            bstack11llll11lll_opy_ = bstack11llll111ll_opy_.get(bstack1lllll1_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᘌ"), [])
            for val in values:
                if val not in bstack11llll11lll_opy_:
                    bstack11llll11lll_opy_.append(val)
            bstack11llll111ll_opy_[bstack1lllll1_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘍ")] = bstack11llll11lll_opy_
        else:
            bstack11llll111l1_opy_[key_name] = bstack11llll11ll1_opy_
    @staticmethod
    def bstack1ll111ll1ll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11ll1_opy_._11llll1l111_opy_
    @staticmethod
    def bstack11llll1111l_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11ll1_opy_._11llll11l11_opy_
    @staticmethod
    def bstack11llll11l1l_opy_(bstack11llll1l1l1_opy_: str) -> List[str]:
        bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡳࡰ࡮ࡺࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡱࡷࡷࠤࡸࡺࡲࡪࡰࡪࠤࡧࡿࠠࡤࡱࡰࡱࡦࡹࠠࡸࡪ࡬ࡰࡪࠦࡲࡦࡵࡳࡩࡨࡺࡩ࡯ࡩࠣࡨࡴࡻࡢ࡭ࡧ࠰ࡵࡺࡵࡴࡦࡦࠣࡷࡺࡨࡳࡵࡴ࡬ࡲ࡬ࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡉࡳࡷࠦࡥࡹࡣࡰࡴࡱ࡫࠺ࠡࠩࡤ࠰ࠥࠨࡢ࠭ࡥࠥ࠰ࠥࡪࠧࠡ࠯ࡁࠤࡠ࠭ࡡࠨ࠮ࠣࠫࡧ࠲ࡣࠨ࠮ࠣࠫࡩ࠭࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᘎ")
        pattern = re.compile(bstack1lllll1_opy_ (u"ࡷ࠭ࠢࠩ࡝ࡡࠦࡢ࠰ࠩࠣࡾࠫ࡟ࡣ࠲࡝ࠬࠫࠪᘏ"))
        result = []
        for match in pattern.finditer(bstack11llll1l1l1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1lllll1_opy_ (u"ࠨࡕࡵ࡫࡯࡭ࡹࡿࠠࡤ࡮ࡤࡷࡸࠦࡳࡩࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡩ࡯ࡵࡷࡥࡳࡺࡩࡢࡶࡨࡨࠧᘐ"))
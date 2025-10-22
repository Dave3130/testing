# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack111l11ll1l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11llll11_opy_:
    bstack11l1l11_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡆࡹࡸࡺ࡯࡮ࡖࡤ࡫ࡒࡧ࡮ࡢࡩࡨࡶࠥࡶࡲࡰࡸ࡬ࡨࡪࡹࠠࡶࡶ࡬ࡰ࡮ࡺࡹࠡ࡯ࡨࡸ࡭ࡵࡤࡴࠢࡷࡳࠥࡹࡥࡵࠢࡤࡲࡩࠦࡲࡦࡶࡵ࡭ࡪࡼࡥࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࠥࡳࡥࡵࡣࡧࡥࡹࡧ࠮ࠋࠢࠣࠤࠥࡏࡴࠡ࡯ࡤ࡭ࡳࡺࡡࡪࡰࡶࠤࡹࡽ࡯ࠡࡵࡨࡴࡦࡸࡡࡵࡧࠣࡱࡪࡺࡡࡥࡣࡷࡥࠥࡪࡩࡤࡶ࡬ࡳࡳࡧࡲࡪࡧࡶࠤ࡫ࡵࡲࠡࡶࡨࡷࡹࠦ࡬ࡦࡸࡨࡰࠥࡧ࡮ࡥࠢࡥࡹ࡮ࡲࡤࠡ࡮ࡨࡺࡪࡲࠠࡤࡷࡶࡸࡴࡳࠠࡵࡣࡪࡷ࠳ࠐࠠࠡࠢࠣࡉࡦࡩࡨࠡ࡯ࡨࡸࡦࡪࡡࡵࡣࠣࡩࡳࡺࡲࡺࠢ࡬ࡷࠥ࡫ࡸࡱࡧࡦࡸࡪࡪࠠࡵࡱࠣࡦࡪࠦࡳࡵࡴࡸࡧࡹࡻࡲࡦࡦࠣࡥࡸࡀࠊࠡࠢࠣࠤࠥࠦࠠ࡬ࡧࡼ࠾ࠥࢁࠊࠡࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠧ࡬ࡩࡦ࡮ࡧࡣࡹࡿࡰࡦࠤ࠽ࠤࠧࡳࡵ࡭ࡶ࡬ࡣࡩࡸ࡯ࡱࡦࡲࡻࡳࠨࠬࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡶࡢ࡮ࡸࡩࡸࠨ࠺ࠡ࡝࡯࡭ࡸࡺࠠࡰࡨࠣࡸࡦ࡭ࠠࡷࡣ࡯ࡹࡪࡹ࡝ࠋࠢࠣࠤࠥࠦࠠࠡࡿࠍࠤࠥࠦࠠࠣࠤࠥᘡ")
    _11lll1lll1l_opy_: Dict[str, Dict[str, Any]] = {}
    _11lll1lll11_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11lll1l1l1l_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack11l1l11_opy_ (u"ࠥࠦᘢ") or key_value.strip() == bstack11l1l11_opy_ (u"ࠦࠧᘣ"):
            logger.error(bstack11l1l11_opy_ (u"ࠧࡱࡥࡺࡡࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡰ࡫ࡹࡠࡸࡤࡰࡺ࡫ࠠ࡮ࡷࡶࡸࠥࡨࡥࠡࡰࡲࡲ࠲ࡴࡵ࡭࡮ࠣࡥࡳࡪࠠ࡯ࡱࡱ࠱ࡪࡳࡰࡵࡻࠥᘤ"))
        values: List[str] = bstack1ll11llll11_opy_.bstack11lll1ll11l_opy_(key_value)
        bstack11lll1ll111_opy_ = {bstack11l1l11_opy_ (u"ࠨࡦࡪࡧ࡯ࡨࡤࡺࡹࡱࡧࠥᘥ"): bstack11l1l11_opy_ (u"ࠢ࡮ࡷ࡯ࡸ࡮ࡥࡤࡳࡱࡳࡨࡴࡽ࡮ࠣᘦ"), bstack11l1l11_opy_ (u"ࠣࡸࡤࡰࡺ࡫ࡳࠣᘧ"): values}
        bstack11lll1ll1l1_opy_ = bstack1ll11llll11_opy_._11lll1lll11_opy_ if bstack11lll1l1l1l_opy_ else bstack1ll11llll11_opy_._11lll1lll1l_opy_
        if key_name in bstack11lll1ll1l1_opy_:
            bstack11lll1l1lll_opy_ = bstack11lll1ll1l1_opy_[key_name]
            bstack11lll1l1l11_opy_ = bstack11lll1l1lll_opy_.get(bstack11l1l11_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᘨ"), [])
            for val in values:
                if val not in bstack11lll1l1l11_opy_:
                    bstack11lll1l1l11_opy_.append(val)
            bstack11lll1l1lll_opy_[bstack11l1l11_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘩ")] = bstack11lll1l1l11_opy_
        else:
            bstack11lll1ll1l1_opy_[key_name] = bstack11lll1ll111_opy_
    @staticmethod
    def bstack1ll11llllll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11llll11_opy_._11lll1lll1l_opy_
    @staticmethod
    def bstack11lll1l1ll1_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11llll11_opy_._11lll1lll11_opy_
    @staticmethod
    def bstack11lll1ll11l_opy_(bstack11lll1ll1ll_opy_: str) -> List[str]:
        bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࠥࠦࠠࠡࡕࡳࡰ࡮ࡺࡳࠡࡶ࡫ࡩࠥ࡯࡮ࡱࡷࡷࠤࡸࡺࡲࡪࡰࡪࠤࡧࡿࠠࡤࡱࡰࡱࡦࡹࠠࡸࡪ࡬ࡰࡪࠦࡲࡦࡵࡳࡩࡨࡺࡩ࡯ࡩࠣࡨࡴࡻࡢ࡭ࡧ࠰ࡵࡺࡵࡴࡦࡦࠣࡷࡺࡨࡳࡵࡴ࡬ࡲ࡬ࡹ࠮ࠋࠢࠣࠤࠥࠦࠠࠡࠢࡉࡳࡷࠦࡥࡹࡣࡰࡴࡱ࡫࠺ࠡࠩࡤ࠰ࠥࠨࡢ࠭ࡥࠥ࠰ࠥࡪࠧࠡ࠯ࡁࠤࡠ࠭ࡡࠨ࠮ࠣࠫࡧ࠲ࡣࠨ࠮ࠣࠫࡩ࠭࡝ࠋࠢࠣࠤࠥࠦࠠࠡࠢࠥࠦࠧᘪ")
        pattern = re.compile(bstack11l1l11_opy_ (u"ࡷ࠭ࠢࠩ࡝ࡡࠦࡢ࠰ࠩࠣࡾࠫ࡟ࡣ࠲࡝ࠬࠫࠪᘫ"))
        result = []
        for match in pattern.finditer(bstack11lll1ll1ll_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack11l1l11_opy_ (u"ࠨࡕࡵ࡫࡯࡭ࡹࡿࠠࡤ࡮ࡤࡷࡸࠦࡳࡩࡱࡸࡰࡩࠦ࡮ࡰࡶࠣࡦࡪࠦࡩ࡯ࡵࡷࡥࡳࡺࡩࡢࡶࡨࡨࠧᘬ"))
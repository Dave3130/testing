# coding: UTF-8
import sys
bstack11_opy_ = sys.version_info [0] == 2
bstack1l111ll_opy_ = 2048
bstack11lll1l_opy_ = 7
def bstack1lll11l_opy_ (bstack11l11l_opy_):
    global bstack11l1l1_opy_
    bstack1l111_opy_ = ord (bstack11l11l_opy_ [-1])
    bstack1ll11l1_opy_ = bstack11l11l_opy_ [:-1]
    bstack1l_opy_ = bstack1l111_opy_ % len (bstack1ll11l1_opy_)
    bstack1l11ll1_opy_ = bstack1ll11l1_opy_ [:bstack1l_opy_] + bstack1ll11l1_opy_ [bstack1l_opy_:]
    if bstack11_opy_:
        bstack1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    else:
        bstack1ll_opy_ = str () .join ([chr (ord (char) - bstack1l111ll_opy_ - (bstack1l11ll_opy_ + bstack1l111_opy_) % bstack11lll1l_opy_) for bstack1l11ll_opy_, char in enumerate (bstack1l11ll1_opy_)])
    return eval (bstack1ll_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack11ll1111l_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll1l1l1ll1_opy_:
    bstack1lll11l_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡳࠡࡷࡷ࡭ࡱ࡯ࡴࡺࠢࡰࡩࡹ࡮࡯ࡥࡵࠣࡸࡴࠦࡳࡦࡶࠣࡥࡳࡪࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࠦ࡭ࡦࡶࡤࡨࡦࡺࡡ࠯ࠌࠣࠤࠥࠦࡉࡵࠢࡰࡥ࡮ࡴࡴࡢ࡫ࡱࡷࠥࡺࡷࡰࠢࡶࡩࡵࡧࡲࡢࡶࡨࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳ࡫ࡨࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡡ࡯ࡦࠣࡦࡺ࡯࡬ࡥࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸ࠴ࠊࠡࠢࠣࠤࡊࡧࡣࡩࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡪࡴࡴࡳࡻࠣ࡭ࡸࠦࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡧ࡫ࠠࡴࡶࡵࡹࡨࡺࡵࡳࡧࡧࠤࡦࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡ࡭ࡨࡽ࠿ࠦࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡦࡪࡧ࡯ࡨࡤࡺࡹࡱࡧࠥ࠾ࠥࠨ࡭ࡶ࡮ࡷ࡭ࡤࡪࡲࡰࡲࡧࡳࡼࡴࠢ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡷࡣ࡯ࡹࡪࡹࠢ࠻ࠢ࡞ࡰ࡮ࡹࡴࠡࡱࡩࠤࡹࡧࡧࠡࡸࡤࡰࡺ࡫ࡳ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࢀࠎࠥࠦࠠࠡࠤࠥࠦᘩ")
    _11lll1ll1l1_opy_: Dict[str, Dict[str, Any]] = {}
    _11lll1l1l1l_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11lll1l1lll_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1lll11l_opy_ (u"ࠦࠧᘪ") or key_value.strip() == bstack1lll11l_opy_ (u"ࠧࠨᘫ"):
            logger.error(bstack1lll11l_opy_ (u"ࠨ࡫ࡦࡻࡢࡲࡦࡳࡥࠡࡣࡱࡨࠥࡱࡥࡺࡡࡹࡥࡱࡻࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡦࡴࡤࠡࡰࡲࡲ࠲࡫࡭ࡱࡶࡼࠦᘬ"))
        values: List[str] = bstack1ll1l1l1ll1_opy_.bstack11lll1l11l1_opy_(key_value)
        bstack11lll1ll11l_opy_ = {bstack1lll11l_opy_ (u"ࠢࡧ࡫ࡨࡰࡩࡥࡴࡺࡲࡨࠦᘭ"): bstack1lll11l_opy_ (u"ࠣ࡯ࡸࡰࡹ࡯࡟ࡥࡴࡲࡴࡩࡵࡷ࡯ࠤᘮ"), bstack1lll11l_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᘯ"): values}
        bstack11lll1l1l11_opy_ = bstack1ll1l1l1ll1_opy_._11lll1l1l1l_opy_ if bstack11lll1l1lll_opy_ else bstack1ll1l1l1ll1_opy_._11lll1ll1l1_opy_
        if key_name in bstack11lll1l1l11_opy_:
            bstack11lll1ll111_opy_ = bstack11lll1l1l11_opy_[key_name]
            bstack11lll1l11ll_opy_ = bstack11lll1ll111_opy_.get(bstack1lll11l_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘰ"), [])
            for val in values:
                if val not in bstack11lll1l11ll_opy_:
                    bstack11lll1l11ll_opy_.append(val)
            bstack11lll1ll111_opy_[bstack1lll11l_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࡶࠦᘱ")] = bstack11lll1l11ll_opy_
        else:
            bstack11lll1l1l11_opy_[key_name] = bstack11lll1ll11l_opy_
    @staticmethod
    def bstack1ll1111ll11_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1l1ll1_opy_._11lll1ll1l1_opy_
    @staticmethod
    def bstack11lll1l111l_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll1l1l1ll1_opy_._11lll1l1l1l_opy_
    @staticmethod
    def bstack11lll1l11l1_opy_(bstack11lll1l1ll1_opy_: str) -> List[str]:
        bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡴࡱ࡯ࡴࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡲࡸࡸࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡨࡹࠡࡥࡲࡱࡲࡧࡳࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡧࡶࡴࡪࡩࡴࡪࡰࡪࠤࡩࡵࡵࡣ࡮ࡨ࠱ࡶࡻ࡯ࡵࡧࡧࠤࡸࡻࡢࡴࡶࡵ࡭ࡳ࡭ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡦࡺࡤࡱࡵࡲࡥ࠻ࠢࠪࡥ࠱ࠦࠢࡣ࠮ࡦࠦ࠱ࠦࡤࠨࠢ࠰ࡂࠥࡡࠧࡢࠩ࠯ࠤࠬࡨࠬࡤࠩ࠯ࠤࠬࡪࠧ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᘲ")
        pattern = re.compile(bstack1lll11l_opy_ (u"ࡸࠧࠣࠪ࡞ࡢࠧࡣࠪࠪࠤࡿࠬࡠࡤࠬ࡞࠭ࠬࠫᘳ"))
        result = []
        for match in pattern.finditer(bstack11lll1l1ll1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1lll11l_opy_ (u"ࠢࡖࡶ࡬ࡰ࡮ࡺࡹࠡࡥ࡯ࡥࡸࡹࠠࡴࡪࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡪࡰࡶࡸࡦࡴࡴࡪࡣࡷࡩࡩࠨᘴ"))
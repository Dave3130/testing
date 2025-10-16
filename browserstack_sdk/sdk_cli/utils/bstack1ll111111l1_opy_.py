# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import re
from typing import List, Dict, Any
from bstack_utils.bstack1l1l1ll111_opy_ import get_logger
logger = get_logger(__name__)
class bstack1ll11l11ll1_opy_:
    bstack1ll1ll1_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡇࡺࡹࡴࡰ࡯ࡗࡥ࡬ࡓࡡ࡯ࡣࡪࡩࡷࠦࡰࡳࡱࡹ࡭ࡩ࡫ࡳࠡࡷࡷ࡭ࡱ࡯ࡴࡺࠢࡰࡩࡹ࡮࡯ࡥࡵࠣࡸࡴࠦࡳࡦࡶࠣࡥࡳࡪࠠࡳࡧࡷࡶ࡮࡫ࡶࡦࠢࡦࡹࡸࡺ࡯࡮ࠢࡷࡥ࡬ࠦ࡭ࡦࡶࡤࡨࡦࡺࡡ࠯ࠌࠣࠤࠥࠦࡉࡵࠢࡰࡥ࡮ࡴࡴࡢ࡫ࡱࡷࠥࡺࡷࡰࠢࡶࡩࡵࡧࡲࡢࡶࡨࠤࡲ࡫ࡴࡢࡦࡤࡸࡦࠦࡤࡪࡥࡷ࡭ࡴࡴࡡࡳ࡫ࡨࡷࠥ࡬࡯ࡳࠢࡷࡩࡸࡺࠠ࡭ࡧࡹࡩࡱࠦࡡ࡯ࡦࠣࡦࡺ࡯࡬ࡥࠢ࡯ࡩࡻ࡫࡬ࠡࡥࡸࡷࡹࡵ࡭ࠡࡶࡤ࡫ࡸ࠴ࠊࠡࠢࠣࠤࡊࡧࡣࡩࠢࡰࡩࡹࡧࡤࡢࡶࡤࠤࡪࡴࡴࡳࡻࠣ࡭ࡸࠦࡥࡹࡲࡨࡧࡹ࡫ࡤࠡࡶࡲࠤࡧ࡫ࠠࡴࡶࡵࡹࡨࡺࡵࡳࡧࡧࠤࡦࡹ࠺ࠋࠢࠣࠤࠥࠦࠠࠡ࡭ࡨࡽ࠿ࠦࡻࠋࠢࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠨࡦࡪࡧ࡯ࡨࡤࡺࡹࡱࡧࠥ࠾ࠥࠨ࡭ࡶ࡮ࡷ࡭ࡤࡪࡲࡰࡲࡧࡳࡼࡴࠢ࠭ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠤࠥࠦࠢࡷࡣ࡯ࡹࡪࡹࠢ࠻ࠢ࡞ࡰ࡮ࡹࡴࠡࡱࡩࠤࡹࡧࡧࠡࡸࡤࡰࡺ࡫ࡳ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࢀࠎࠥࠦࠠࠡࠤࠥࠦᘆ")
    _11llll1l111_opy_: Dict[str, Dict[str, Any]] = {}
    _11llll1l11l_opy_: Dict[str, Dict[str, Any]] = {}
    @staticmethod
    def set_custom_tag(key_name: str, key_value: str, bstack11llll11l1l_opy_: bool = False) -> None:
        if not key_name or not key_value or key_name.strip() == bstack1ll1ll1_opy_ (u"ࠦࠧᘇ") or key_value.strip() == bstack1ll1ll1_opy_ (u"ࠧࠨᘈ"):
            logger.error(bstack1ll1ll1_opy_ (u"ࠨ࡫ࡦࡻࡢࡲࡦࡳࡥࠡࡣࡱࡨࠥࡱࡥࡺࡡࡹࡥࡱࡻࡥࠡ࡯ࡸࡷࡹࠦࡢࡦࠢࡱࡳࡳ࠳࡮ࡶ࡮࡯ࠤࡦࡴࡤࠡࡰࡲࡲ࠲࡫࡭ࡱࡶࡼࠦᘉ"))
        values: List[str] = bstack1ll11l11ll1_opy_.bstack11llll11lll_opy_(key_value)
        bstack11llll111l1_opy_ = {bstack1ll1ll1_opy_ (u"ࠢࡧ࡫ࡨࡰࡩࡥࡴࡺࡲࡨࠦᘊ"): bstack1ll1ll1_opy_ (u"ࠣ࡯ࡸࡰࡹ࡯࡟ࡥࡴࡲࡴࡩࡵࡷ࡯ࠤᘋ"), bstack1ll1ll1_opy_ (u"ࠤࡹࡥࡱࡻࡥࡴࠤᘌ"): values}
        bstack11llll111ll_opy_ = bstack1ll11l11ll1_opy_._11llll1l11l_opy_ if bstack11llll11l1l_opy_ else bstack1ll11l11ll1_opy_._11llll1l111_opy_
        if key_name in bstack11llll111ll_opy_:
            bstack11llll11l11_opy_ = bstack11llll111ll_opy_[key_name]
            bstack11llll11ll1_opy_ = bstack11llll11l11_opy_.get(bstack1ll1ll1_opy_ (u"ࠥࡺࡦࡲࡵࡦࡵࠥᘍ"), [])
            for val in values:
                if val not in bstack11llll11ll1_opy_:
                    bstack11llll11ll1_opy_.append(val)
            bstack11llll11l11_opy_[bstack1ll1ll1_opy_ (u"ࠦࡻࡧ࡬ࡶࡧࡶࠦᘎ")] = bstack11llll11ll1_opy_
        else:
            bstack11llll111ll_opy_[key_name] = bstack11llll111l1_opy_
    @staticmethod
    def bstack1ll1l1l1lll_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11ll1_opy_._11llll1l111_opy_
    @staticmethod
    def bstack11llll1111l_opy_() -> Dict[str, Dict[str, Any]]:
        return bstack1ll11l11ll1_opy_._11llll1l11l_opy_
    @staticmethod
    def bstack11llll11lll_opy_(bstack11llll1l1l1_opy_: str) -> List[str]:
        bstack1ll1ll1_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࠦࠠࠡࠢࡖࡴࡱ࡯ࡴࡴࠢࡷ࡬ࡪࠦࡩ࡯ࡲࡸࡸࠥࡹࡴࡳ࡫ࡱ࡫ࠥࡨࡹࠡࡥࡲࡱࡲࡧࡳࠡࡹ࡫࡭ࡱ࡫ࠠࡳࡧࡶࡴࡪࡩࡴࡪࡰࡪࠤࡩࡵࡵࡣ࡮ࡨ࠱ࡶࡻ࡯ࡵࡧࡧࠤࡸࡻࡢࡴࡶࡵ࡭ࡳ࡭ࡳ࠯ࠌࠣࠤࠥࠦࠠࠡࠢࠣࡊࡴࡸࠠࡦࡺࡤࡱࡵࡲࡥ࠻ࠢࠪࡥ࠱ࠦࠢࡣ࠮ࡦࠦ࠱ࠦࡤࠨࠢ࠰ࡂࠥࡡࠧࡢࠩ࠯ࠤࠬࡨࠬࡤࠩ࠯ࠤࠬࡪࠧ࡞ࠌࠣࠤࠥࠦࠠࠡࠢࠣࠦࠧࠨᘏ")
        pattern = re.compile(bstack1ll1ll1_opy_ (u"ࡸࠧࠣࠪ࡞ࡢࠧࡣࠪࠪࠤࡿࠬࡠࡤࠬ࡞࠭ࠬࠫᘐ"))
        result = []
        for match in pattern.finditer(bstack11llll1l1l1_opy_):
            if match.group(1) is not None:
                result.append(match.group(1).strip())
            elif match.group(2) is not None:
                result.append(match.group(2).strip())
        return result
    def __new__(cls, *args, **kwargs):
        raise Exception(bstack1ll1ll1_opy_ (u"ࠢࡖࡶ࡬ࡰ࡮ࡺࡹࠡࡥ࡯ࡥࡸࡹࠠࡴࡪࡲࡹࡱࡪࠠ࡯ࡱࡷࠤࡧ࡫ࠠࡪࡰࡶࡸࡦࡴࡴࡪࡣࡷࡩࡩࠨᘑ"))
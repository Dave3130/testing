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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l11111111_opy_ import get_logger
from bstack_utils.bstack1ll1l1lll_opy_ import bstack1llll111ll1_opy_
bstack1ll1l1lll_opy_ = bstack1llll111ll1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11l111llll_opy_: Optional[str] = None):
    bstack11ll1l_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡇࡩࡨࡵࡲࡢࡶࡲࡶࠥࡺ࡯ࠡ࡮ࡲ࡫ࠥࡺࡨࡦࠢࡶࡸࡦࡸࡴࠡࡶ࡬ࡱࡪࠦ࡯ࡧࠢࡤࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࡡ࡭ࡱࡱ࡫ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࠢࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡸࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᚭ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111l1l1l_opy_: str = bstack1ll1l1lll_opy_.bstack11ll1l11l11_opy_(label)
            start_mark: str = label + bstack11ll1l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᚮ")
            end_mark: str = label + bstack11ll1l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᚯ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll11l1l1l_opy_.value:
                    bstack1ll1l1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll1l1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11l111llll_opy_)
                elif stage.value == STAGE.bstack11ll11lll_opy_.value:
                    start_mark: str = bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚰ")
                    end_mark: str = bstack1ll111l1l1l_opy_ + bstack11ll1l_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᚱ")
                    bstack1ll1l1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll1l1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11l111llll_opy_)
            except Exception as e:
                bstack1ll1l1lll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11l111llll_opy_)
            return result
        return wrapper
    return decorator
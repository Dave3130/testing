# coding: UTF-8
import sys
bstack1ll1111_opy_ = sys.version_info [0] == 2
bstack1ll_opy_ = 2048
bstack1ll1l1_opy_ = 7
def bstack11l111_opy_ (bstack1ll1_opy_):
    global bstack11l1l_opy_
    bstack11l1l1_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack111ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack11111ll_opy_ = bstack11l1l1_opy_ % len (bstack111ll_opy_)
    bstack1l1lll_opy_ = bstack111ll_opy_ [:bstack11111ll_opy_] + bstack111ll_opy_ [bstack11111ll_opy_:]
    if bstack1ll1111_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1ll_opy_ - (bstack1l111_opy_ + bstack11l1l1_opy_) % bstack1ll1l1_opy_) for bstack1l111_opy_, char in enumerate (bstack1l1lll_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11l111l1ll_opy_ import get_logger
from bstack_utils.bstack1111lll1l_opy_ import bstack1llll11ll11_opy_
bstack1111lll1l_opy_ = bstack1llll11ll11_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11l111l1l_opy_: Optional[str] = None):
    bstack11l111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᚠ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1l11l1_opy_: str = bstack1111lll1l_opy_.bstack11ll1l1l111_opy_(label)
            start_mark: str = label + bstack11l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᚡ")
            end_mark: str = label + bstack11l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᚢ")
            result = None
            try:
                if stage.value == STAGE.bstack1lll111l1l_opy_.value:
                    bstack1111lll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1111lll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11l111l1l_opy_)
                elif stage.value == STAGE.bstack1l11lll11_opy_.value:
                    start_mark: str = bstack1ll1l1l11l1_opy_ + bstack11l111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚣ")
                    end_mark: str = bstack1ll1l1l11l1_opy_ + bstack11l111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᚤ")
                    bstack1111lll1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1111lll1l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11l111l1l_opy_)
            except Exception as e:
                bstack1111lll1l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11l111l1l_opy_)
            return result
        return wrapper
    return decorator
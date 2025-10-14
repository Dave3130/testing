# coding: UTF-8
import sys
bstack1_opy_ = sys.version_info [0] == 2
bstack11l1ll1_opy_ = 2048
bstack1l1l1ll_opy_ = 7
def bstack11l1l11_opy_ (bstack111l1ll_opy_):
    global bstack1l1lll1_opy_
    bstack1l1l11_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack111l1l1_opy_ = bstack111l1ll_opy_ [:-1]
    bstack111ll_opy_ = bstack1l1l11_opy_ % len (bstack111l1l1_opy_)
    bstack11l11l1_opy_ = bstack111l1l1_opy_ [:bstack111ll_opy_] + bstack111l1l1_opy_ [bstack111ll_opy_:]
    if bstack1_opy_:
        bstack1111l1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    else:
        bstack1111l1l_opy_ = str () .join ([chr (ord (char) - bstack11l1ll1_opy_ - (bstack1l111ll_opy_ + bstack1l1l11_opy_) % bstack1l1l1ll_opy_) for bstack1l111ll_opy_, char in enumerate (bstack11l11l1_opy_)])
    return eval (bstack1111l1l_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1ll1111ll_opy_ import get_logger
from bstack_utils.bstack1l1l1111ll_opy_ import bstack111111111l_opy_
bstack1l1l1111ll_opy_ = bstack111111111l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack111111ll1_opy_: Optional[str] = None):
    bstack11l1l11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᙶ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11lll11l_opy_: str = bstack1l1l1111ll_opy_.bstack11ll1ll111l_opy_(label)
            start_mark: str = label + bstack11l1l11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᙷ")
            end_mark: str = label + bstack11l1l11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᙸ")
            result = None
            try:
                if stage.value == STAGE.bstack111ll111l_opy_.value:
                    bstack1l1l1111ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1l1l1111ll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack111111ll1_opy_)
                elif stage.value == STAGE.bstack11l1lllll_opy_.value:
                    start_mark: str = bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᙹ")
                    end_mark: str = bstack1ll11lll11l_opy_ + bstack11l1l11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᙺ")
                    bstack1l1l1111ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1l1l1111ll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack111111ll1_opy_)
            except Exception as e:
                bstack1l1l1111ll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack111111ll1_opy_)
            return result
        return wrapper
    return decorator
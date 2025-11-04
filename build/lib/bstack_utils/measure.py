# coding: UTF-8
import sys
bstack11l111_opy_ = sys.version_info [0] == 2
bstack1l11ll_opy_ = 2048
bstack1l1l11_opy_ = 7
def bstack11l1111_opy_ (bstack111l11l_opy_):
    global bstack1ll1l1l_opy_
    bstack1ll1ll_opy_ = ord (bstack111l11l_opy_ [-1])
    bstack1lll11_opy_ = bstack111l11l_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1ll_opy_ % len (bstack1lll11_opy_)
    bstack1l1l1ll_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l111_opy_:
        bstack1l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    else:
        bstack1l11_opy_ = str () .join ([chr (ord (char) - bstack1l11ll_opy_ - (bstack1llll_opy_ + bstack1ll1ll_opy_) % bstack1l1l11_opy_) for bstack1llll_opy_, char in enumerate (bstack1l1l1ll_opy_)])
    return eval (bstack1l11_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11ll1l11l1_opy_ import get_logger
from bstack_utils.bstack111111l1l1_opy_ import bstack1llll1l1111_opy_
bstack111111l1l1_opy_ = bstack1llll1l1111_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11lll11l1l_opy_: Optional[str] = None):
    bstack11l1111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᚼ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1l1llll111l_opy_: str = bstack111111l1l1_opy_.bstack11ll11lllll_opy_(label)
            start_mark: str = label + bstack11l1111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᚽ")
            end_mark: str = label + bstack11l1111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᚾ")
            result = None
            try:
                if stage.value == STAGE.bstack11l1llll1l_opy_.value:
                    bstack111111l1l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111111l1l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11lll11l1l_opy_)
                elif stage.value == STAGE.bstack1111ll111_opy_.value:
                    start_mark: str = bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚿ")
                    end_mark: str = bstack1l1llll111l_opy_ + bstack11l1111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᛀ")
                    bstack111111l1l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111111l1l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11lll11l1l_opy_)
            except Exception as e:
                bstack111111l1l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11lll11l1l_opy_)
            return result
        return wrapper
    return decorator
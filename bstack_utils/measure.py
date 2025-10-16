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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l1l1l1111_opy_ import get_logger
from bstack_utils.bstack11l111l1l_opy_ import bstack1llll1lllll_opy_
bstack11l111l1l_opy_ = bstack1llll1lllll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack111ll11l1l_opy_: Optional[str] = None):
    bstack1ll11_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᙽ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1ll1l1_opy_: str = bstack11l111l1l_opy_.bstack11ll1ll11ll_opy_(label)
            start_mark: str = label + bstack1ll11_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᙾ")
            end_mark: str = label + bstack1ll11_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᙿ")
            result = None
            try:
                if stage.value == STAGE.bstack11l111lll_opy_.value:
                    bstack11l111l1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l111l1l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack111ll11l1l_opy_)
                elif stage.value == STAGE.bstack1111l1111_opy_.value:
                    start_mark: str = bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨ ")
                    end_mark: str = bstack1ll1l1ll1l1_opy_ + bstack1ll11_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᚁ")
                    bstack11l111l1l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l111l1l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack111ll11l1l_opy_)
            except Exception as e:
                bstack11l111l1l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack111ll11l1l_opy_)
            return result
        return wrapper
    return decorator
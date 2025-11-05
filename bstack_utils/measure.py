# coding: UTF-8
import sys
bstack1111l1_opy_ = sys.version_info [0] == 2
bstack1l1ll11_opy_ = 2048
bstack11l11l_opy_ = 7
def bstack11111_opy_ (bstack11lll_opy_):
    global bstack111l1l1_opy_
    bstack1l1l1_opy_ = ord (bstack11lll_opy_ [-1])
    bstack1l111ll_opy_ = bstack11lll_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1l111ll_opy_)
    bstack1l11l11_opy_ = bstack1l111ll_opy_ [:bstack1l1l11_opy_] + bstack1l111ll_opy_ [bstack1l1l11_opy_:]
    if bstack1111l1_opy_:
        bstack1llll11_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    else:
        bstack1llll11_opy_ = str () .join ([chr (ord (char) - bstack1l1ll11_opy_ - (bstack1111ll1_opy_ + bstack1l1l1_opy_) % bstack11l11l_opy_) for bstack1111ll1_opy_, char in enumerate (bstack1l11l11_opy_)])
    return eval (bstack1llll11_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111111l11l_opy_ import get_logger
from bstack_utils.bstack1ll11111ll_opy_ import bstack1llll1ll1l1_opy_
bstack1ll11111ll_opy_ = bstack1llll1ll1l1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack111111111_opy_: Optional[str] = None):
    bstack11111_opy_ (u"ࠥࠦࠧࠐࠠࠡࠢࠣࡈࡪࡩ࡯ࡳࡣࡷࡳࡷࠦࡴࡰࠢ࡯ࡳ࡬ࠦࡴࡩࡧࠣࡷࡹࡧࡲࡵࠢࡷ࡭ࡲ࡫ࠠࡰࡨࠣࡥࠥ࡬ࡵ࡯ࡥࡷ࡭ࡴࡴࠠࡦࡺࡨࡧࡺࡺࡩࡰࡰࠍࠤࠥࠦࠠࡢ࡮ࡲࡲ࡬ࠦࡷࡪࡶ࡫ࠤࡪࡼࡥ࡯ࡶࠣࡲࡦࡳࡥࠡࡣࡱࡨࠥࡹࡴࡢࡩࡨ࠲ࠏࠦࠠࠡࠢࠥࠦࠧᚼ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11llll1l_opy_: str = bstack1ll11111ll_opy_.bstack11ll11lllll_opy_(label)
            start_mark: str = label + bstack11111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᚽ")
            end_mark: str = label + bstack11111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᚾ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll1111ll_opy_.value:
                    bstack1ll11111ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll11111ll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack111111111_opy_)
                elif stage.value == STAGE.bstack111l1l11l_opy_.value:
                    start_mark: str = bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚿ")
                    end_mark: str = bstack1ll11llll1l_opy_ + bstack11111_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᛀ")
                    bstack1ll11111ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll11111ll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack111111111_opy_)
            except Exception as e:
                bstack1ll11111ll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack111111111_opy_)
            return result
        return wrapper
    return decorator
# coding: UTF-8
import sys
bstack1lll1l_opy_ = sys.version_info [0] == 2
bstack111l11l_opy_ = 2048
bstack1l1llll_opy_ = 7
def bstack111111l_opy_ (bstack1ll1_opy_):
    global bstack11l1ll_opy_
    bstack11ll1l_opy_ = ord (bstack1ll1_opy_ [-1])
    bstack11ll_opy_ = bstack1ll1_opy_ [:-1]
    bstack1lllll1_opy_ = bstack11ll1l_opy_ % len (bstack11ll_opy_)
    bstack111l1l1_opy_ = bstack11ll_opy_ [:bstack1lllll1_opy_] + bstack11ll_opy_ [bstack1lllll1_opy_:]
    if bstack1lll1l_opy_:
        bstack1111_opy_ = unicode () .join ([unichr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    else:
        bstack1111_opy_ = str () .join ([chr (ord (char) - bstack111l11l_opy_ - (bstack1l1l1l_opy_ + bstack11ll1l_opy_) % bstack1l1llll_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack111l1l1_opy_)])
    return eval (bstack1111_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11111ll111_opy_ import get_logger
from bstack_utils.bstack1l11ll11l1_opy_ import bstack1llllll1lll_opy_
bstack1l11ll11l1_opy_ = bstack1llllll1lll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l111l1ll_opy_: Optional[str] = None):
    bstack111111l_opy_ (u"ࠢࠣࠤࠍࠤࠥࠦࠠࡅࡧࡦࡳࡷࡧࡴࡰࡴࠣࡸࡴࠦ࡬ࡰࡩࠣࡸ࡭࡫ࠠࡴࡶࡤࡶࡹࠦࡴࡪ࡯ࡨࠤࡴ࡬ࠠࡢࠢࡩࡹࡳࡩࡴࡪࡱࡱࠤࡪࡾࡥࡤࡷࡷ࡭ࡴࡴࠊࠡࠢࠣࠤࡦࡲ࡯࡯ࡩࠣࡻ࡮ࡺࡨࠡࡧࡹࡩࡳࡺࠠ࡯ࡣࡰࡩࠥࡧ࡮ࡥࠢࡶࡸࡦ࡭ࡥ࠯ࠌࠣࠤࠥࠦࠢࠣࠤᙳ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1ll1ll_opy_: str = bstack1l11ll11l1_opy_.bstack11ll1ll111l_opy_(label)
            start_mark: str = label + bstack111111l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᙴ")
            end_mark: str = label + bstack111111l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᙵ")
            result = None
            try:
                if stage.value == STAGE.bstack11l11l1l1l_opy_.value:
                    bstack1l11ll11l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1l11ll11l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l111l1ll_opy_)
                elif stage.value == STAGE.bstack11l11ll11_opy_.value:
                    start_mark: str = bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᙶ")
                    end_mark: str = bstack1ll1l1ll1ll_opy_ + bstack111111l_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᙷ")
                    bstack1l11ll11l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1l11ll11l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l111l1ll_opy_)
            except Exception as e:
                bstack1l11ll11l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l111l1ll_opy_)
            return result
        return wrapper
    return decorator
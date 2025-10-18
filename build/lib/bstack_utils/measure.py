# coding: UTF-8
import sys
bstack11ll1l1_opy_ = sys.version_info [0] == 2
bstack11111ll_opy_ = 2048
bstack111lll1_opy_ = 7
def bstack1l1lll1_opy_ (bstack1lllll_opy_):
    global bstack111111l_opy_
    bstack1llll_opy_ = ord (bstack1lllll_opy_ [-1])
    bstack11lll1l_opy_ = bstack1lllll_opy_ [:-1]
    bstack1111_opy_ = bstack1llll_opy_ % len (bstack11lll1l_opy_)
    bstack11ll11l_opy_ = bstack11lll1l_opy_ [:bstack1111_opy_] + bstack11lll1l_opy_ [bstack1111_opy_:]
    if bstack11ll1l1_opy_:
        bstack1llll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    else:
        bstack1llll1_opy_ = str () .join ([chr (ord (char) - bstack11111ll_opy_ - (bstack1l1l1ll_opy_ + bstack1llll_opy_) % bstack111lll1_opy_) for bstack1l1l1ll_opy_, char in enumerate (bstack11ll11l_opy_)])
    return eval (bstack1llll1_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111l11l1l_opy_ import get_logger
from bstack_utils.bstack11l1l1111l_opy_ import bstack1llll1ll11l_opy_
bstack11l1l1111l_opy_ = bstack1llll1ll11l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11l1l1l1ll_opy_: Optional[str] = None):
    bstack1l1lll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡄࡦࡥࡲࡶࡦࡺ࡯ࡳࠢࡷࡳࠥࡲ࡯ࡨࠢࡷ࡬ࡪࠦࡳࡵࡣࡵࡸࠥࡺࡩ࡮ࡧࠣࡳ࡫ࠦࡡࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࡥࡱࡵ࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࠦ࡮ࡢ࡯ࡨࠤࡦࡴࡤࠡࡵࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣᙹ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l11l111_opy_: str = bstack11l1l1111l_opy_.bstack11ll1ll1111_opy_(label)
            start_mark: str = label + bstack1l1lll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᙺ")
            end_mark: str = label + bstack1l1lll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᙻ")
            result = None
            try:
                if stage.value == STAGE.bstack111ll111l_opy_.value:
                    bstack11l1l1111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l1l1111l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11l1l1l1ll_opy_)
                elif stage.value == STAGE.bstack1111llll1l_opy_.value:
                    start_mark: str = bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᙼ")
                    end_mark: str = bstack1ll1l11l111_opy_ + bstack1l1lll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᙽ")
                    bstack11l1l1111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l1l1111l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11l1l1l1ll_opy_)
            except Exception as e:
                bstack11l1l1111l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11l1l1l1ll_opy_)
            return result
        return wrapper
    return decorator
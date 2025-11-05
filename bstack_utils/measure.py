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
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11ll1111l_opy_ import get_logger
from bstack_utils.bstack1ll1ll1lll_opy_ import bstack1llll1l1l1l_opy_
bstack1ll1ll1lll_opy_ = bstack1llll1l1l1l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1llll1l_opy_: Optional[str] = None):
    bstack1lll11l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᚢ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111111l1_opy_: str = bstack1ll1ll1lll_opy_.bstack11ll1l111ll_opy_(label)
            start_mark: str = label + bstack1lll11l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚣ")
            end_mark: str = label + bstack1lll11l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᚤ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll1lllll_opy_.value:
                    bstack1ll1ll1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1llll1l_opy_)
                elif stage.value == STAGE.bstack1ll1l1l11_opy_.value:
                    start_mark: str = bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᚥ")
                    end_mark: str = bstack1ll111111l1_opy_ + bstack1lll11l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᚦ")
                    bstack1ll1ll1lll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1llll1l_opy_)
            except Exception as e:
                bstack1ll1ll1lll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1llll1l_opy_)
            return result
        return wrapper
    return decorator
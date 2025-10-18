# coding: UTF-8
import sys
bstack1llll11_opy_ = sys.version_info [0] == 2
bstack1l1l11_opy_ = 2048
bstack11111ll_opy_ = 7
def bstack11ll_opy_ (bstack1111l1l_opy_):
    global bstack1lll_opy_
    bstack1ll11_opy_ = ord (bstack1111l1l_opy_ [-1])
    bstack1111l1_opy_ = bstack1111l1l_opy_ [:-1]
    bstack111l1_opy_ = bstack1ll11_opy_ % len (bstack1111l1_opy_)
    bstack11l11ll_opy_ = bstack1111l1_opy_ [:bstack111l1_opy_] + bstack1111l1_opy_ [bstack111l1_opy_:]
    if bstack1llll11_opy_:
        bstack11l1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    else:
        bstack11l1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l11_opy_ - (bstack11l1l11_opy_ + bstack1ll11_opy_) % bstack11111ll_opy_) for bstack11l1l11_opy_, char in enumerate (bstack11l11ll_opy_)])
    return eval (bstack11l1ll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11l1l1l1ll_opy_ import get_logger
from bstack_utils.bstack11l1l1ll11_opy_ import bstack1llll11ll11_opy_
bstack11l1l1ll11_opy_ = bstack1llll11ll11_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack111l111l1l_opy_: Optional[str] = None):
    bstack11ll_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᚢ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111l11ll_opy_: str = bstack11l1l1ll11_opy_.bstack11ll1l11lll_opy_(label)
            start_mark: str = label + bstack11ll_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᚣ")
            end_mark: str = label + bstack11ll_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᚤ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1lll1lll_opy_.value:
                    bstack11l1l1ll11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l1l1ll11_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack111l111l1l_opy_)
                elif stage.value == STAGE.bstack1ll1111l1_opy_.value:
                    start_mark: str = bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᚥ")
                    end_mark: str = bstack1ll111l11ll_opy_ + bstack11ll_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᚦ")
                    bstack11l1l1ll11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l1l1ll11_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack111l111l1l_opy_)
            except Exception as e:
                bstack11l1l1ll11_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack111l111l1l_opy_)
            return result
        return wrapper
    return decorator
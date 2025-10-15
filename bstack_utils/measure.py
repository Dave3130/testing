# coding: UTF-8
import sys
bstack1l1lll_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1lllllll_opy_ = 7
def bstack1ll1l_opy_ (bstack1ll1l1l_opy_):
    global bstack11ll1l_opy_
    bstack111l111_opy_ = ord (bstack1ll1l1l_opy_ [-1])
    bstack1l111ll_opy_ = bstack1ll1l1l_opy_ [:-1]
    bstack1ll_opy_ = bstack111l111_opy_ % len (bstack1l111ll_opy_)
    bstack111l_opy_ = bstack1l111ll_opy_ [:bstack1ll_opy_] + bstack1l111ll_opy_ [bstack1ll_opy_:]
    if bstack1l1lll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack1111lll_opy_ + bstack111l111_opy_) % bstack1lllllll_opy_) for bstack1111lll_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1ll1ll111_opy_ import get_logger
from bstack_utils.bstack111l11llll_opy_ import bstack1llll1l1l11_opy_
bstack111l11llll_opy_ = bstack1llll1l1l11_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1llll111ll_opy_: Optional[str] = None):
    bstack1ll1l_opy_ (u"ࠧࠨࠢࠋࠢࠣࠤࠥࡊࡥࡤࡱࡵࡥࡹࡵࡲࠡࡶࡲࠤࡱࡵࡧࠡࡶ࡫ࡩࠥࡹࡴࡢࡴࡷࠤࡹ࡯࡭ࡦࠢࡲࡪࠥࡧࠠࡧࡷࡱࡧࡹ࡯࡯࡯ࠢࡨࡼࡪࡩࡵࡵ࡫ࡲࡲࠏࠦࠠࠡࠢࡤࡰࡴࡴࡧࠡࡹ࡬ࡸ࡭ࠦࡥࡷࡧࡱࡸࠥࡴࡡ࡮ࡧࠣࡥࡳࡪࠠࡴࡶࡤ࡫ࡪ࠴ࠊࠡࠢࠣࠤࠧࠨࠢᙸ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1l1lllll111_opy_: str = bstack111l11llll_opy_.bstack11ll1ll111l_opy_(label)
            start_mark: str = label + bstack1ll1l_opy_ (u"ࠨ࠺ࡴࡶࡤࡶࡹࠨᙹ")
            end_mark: str = label + bstack1ll1l_opy_ (u"ࠢ࠻ࡧࡱࡨࠧᙺ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll1l1l1l1_opy_.value:
                    bstack111l11llll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l11llll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1llll111ll_opy_)
                elif stage.value == STAGE.bstack11lll11ll_opy_.value:
                    start_mark: str = bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠣ࠼ࡶࡸࡦࡸࡴࠣᙻ")
                    end_mark: str = bstack1l1lllll111_opy_ + bstack1ll1l_opy_ (u"ࠤ࠽ࡩࡳࡪࠢᙼ")
                    bstack111l11llll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l11llll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1llll111ll_opy_)
            except Exception as e:
                bstack111l11llll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1llll111ll_opy_)
            return result
        return wrapper
    return decorator
# coding: UTF-8
import sys
bstack1l11l_opy_ = sys.version_info [0] == 2
bstack1111_opy_ = 2048
bstack1lll1_opy_ = 7
def bstack1lllll1l_opy_ (bstack1ll1l11_opy_):
    global bstack11l1ll_opy_
    bstack111lll_opy_ = ord (bstack1ll1l11_opy_ [-1])
    bstack1l111l1_opy_ = bstack1ll1l11_opy_ [:-1]
    bstack1111l_opy_ = bstack111lll_opy_ % len (bstack1l111l1_opy_)
    bstack1111ll_opy_ = bstack1l111l1_opy_ [:bstack1111l_opy_] + bstack1l111l1_opy_ [bstack1111l_opy_:]
    if bstack1l11l_opy_:
        bstack1l1l1_opy_ = unicode () .join ([unichr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    else:
        bstack1l1l1_opy_ = str () .join ([chr (ord (char) - bstack1111_opy_ - (bstack1ll1111_opy_ + bstack111lll_opy_) % bstack1lll1_opy_) for bstack1ll1111_opy_, char in enumerate (bstack1111ll_opy_)])
    return eval (bstack1l1l1_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11llll111l_opy_ import get_logger
from bstack_utils.bstack111l1111l_opy_ import bstack1llllllll1l_opy_
bstack111l1111l_opy_ = bstack1llllllll1l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack11lll11l1l_opy_: Optional[str] = None):
    bstack1lllll1l_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡆࡨࡧࡴࡸࡡࡵࡱࡵࠤࡹࡵࠠ࡭ࡱࡪࠤࡹ࡮ࡥࠡࡵࡷࡥࡷࡺࠠࡵ࡫ࡰࡩࠥࡵࡦࠡࡣࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࡧ࡬ࡰࡰࡪࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࠡࡰࡤࡱࡪࠦࡡ࡯ࡦࠣࡷࡹࡧࡧࡦ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ᚞")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111ll1l1_opy_: str = bstack111l1111l_opy_.bstack11ll1l1l111_opy_(label)
            start_mark: str = label + bstack1lllll1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ᚟")
            end_mark: str = label + bstack1lllll1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᚠ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1l11111l_opy_.value:
                    bstack111l1111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l1111l_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack11lll11l1l_opy_)
                elif stage.value == STAGE.bstack1l11ll1ll_opy_.value:
                    start_mark: str = bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᚡ")
                    end_mark: str = bstack1ll111ll1l1_opy_ + bstack1lllll1l_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᚢ")
                    bstack111l1111l_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l1111l_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack11lll11l1l_opy_)
            except Exception as e:
                bstack111l1111l_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack11lll11l1l_opy_)
            return result
        return wrapper
    return decorator
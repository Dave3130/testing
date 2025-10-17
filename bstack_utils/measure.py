# coding: UTF-8
import sys
bstack1111l11_opy_ = sys.version_info [0] == 2
bstack11111l_opy_ = 2048
bstack1111111_opy_ = 7
def bstack11l111_opy_ (bstack1ll1l1_opy_):
    global bstack1llll1_opy_
    bstack1l1l1_opy_ = ord (bstack1ll1l1_opy_ [-1])
    bstack1lll1_opy_ = bstack1ll1l1_opy_ [:-1]
    bstack1l1l11_opy_ = bstack1l1l1_opy_ % len (bstack1lll1_opy_)
    bstack1l1l111_opy_ = bstack1lll1_opy_ [:bstack1l1l11_opy_] + bstack1lll1_opy_ [bstack1l1l11_opy_:]
    if bstack1111l11_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11111l_opy_ - (bstack1llllll_opy_ + bstack1l1l1_opy_) % bstack1111111_opy_) for bstack1llllll_opy_, char in enumerate (bstack1l1l111_opy_)])
    return eval (bstack1111lll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1lll11ll11_opy_ import get_logger
from bstack_utils.bstack1ll1111111_opy_ import bstack1lllll111l1_opy_
bstack1ll1111111_opy_ = bstack1lllll111l1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1l111l11_opy_: Optional[str] = None):
    bstack11l111_opy_ (u"ࠣࠤࠥࠎࠥࠦࠠࠡࡆࡨࡧࡴࡸࡡࡵࡱࡵࠤࡹࡵࠠ࡭ࡱࡪࠤࡹ࡮ࡥࠡࡵࡷࡥࡷࡺࠠࡵ࡫ࡰࡩࠥࡵࡦࠡࡣࠣࡪࡺࡴࡣࡵ࡫ࡲࡲࠥ࡫ࡸࡦࡥࡸࡸ࡮ࡵ࡮ࠋࠢࠣࠤࠥࡧ࡬ࡰࡰࡪࠤࡼ࡯ࡴࡩࠢࡨࡺࡪࡴࡴࠡࡰࡤࡱࡪࠦࡡ࡯ࡦࠣࡷࡹࡧࡧࡦ࠰ࠍࠤࠥࠦࠠࠣࠤࠥ᙭")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11l1lll1_opy_: str = bstack1ll1111111_opy_.bstack11ll1l1llll_opy_(label)
            start_mark: str = label + bstack11l111_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤ᙮")
            end_mark: str = label + bstack11l111_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᙯ")
            result = None
            try:
                if stage.value == STAGE.bstack11111l1ll1_opy_.value:
                    bstack1ll1111111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1ll1111111_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1l111l11_opy_)
                elif stage.value == STAGE.bstack1l111l11l_opy_.value:
                    start_mark: str = bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠦ࠿ࡹࡴࡢࡴࡷࠦᙰ")
                    end_mark: str = bstack1ll11l1lll1_opy_ + bstack11l111_opy_ (u"ࠧࡀࡥ࡯ࡦࠥᙱ")
                    bstack1ll1111111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1ll1111111_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1l111l11_opy_)
            except Exception as e:
                bstack1ll1111111_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1l111l11_opy_)
            return result
        return wrapper
    return decorator
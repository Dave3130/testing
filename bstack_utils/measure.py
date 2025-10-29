# coding: UTF-8
import sys
bstack1llll1l_opy_ = sys.version_info [0] == 2
bstack11ll1l_opy_ = 2048
bstack11l1_opy_ = 7
def bstack11l11ll_opy_ (bstack1lll_opy_):
    global bstack11111l_opy_
    bstack11ll11l_opy_ = ord (bstack1lll_opy_ [-1])
    bstack1l1l_opy_ = bstack1lll_opy_ [:-1]
    bstack1lll1l1_opy_ = bstack11ll11l_opy_ % len (bstack1l1l_opy_)
    bstack1l11ll_opy_ = bstack1l1l_opy_ [:bstack1lll1l1_opy_] + bstack1l1l_opy_ [bstack1lll1l1_opy_:]
    if bstack1llll1l_opy_:
        bstack1lllll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    else:
        bstack1lllll1l_opy_ = str () .join ([chr (ord (char) - bstack11ll1l_opy_ - (bstack11ll1ll_opy_ + bstack11ll11l_opy_) % bstack11l1_opy_) for bstack11ll1ll_opy_, char in enumerate (bstack1l11ll_opy_)])
    return eval (bstack1lllll1l_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11l1l11ll1_opy_ import get_logger
from bstack_utils.bstack1l111l1l1_opy_ import bstack1lllllll1ll_opy_
bstack1l111l1l1_opy_ = bstack1lllllll1ll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1lll1ll1ll_opy_: Optional[str] = None):
    bstack11l11ll_opy_ (u"ࠤࠥࠦࠏࠦࠠࠡࠢࡇࡩࡨࡵࡲࡢࡶࡲࡶࠥࡺ࡯ࠡ࡮ࡲ࡫ࠥࡺࡨࡦࠢࡶࡸࡦࡸࡴࠡࡶ࡬ࡱࡪࠦ࡯ࡧࠢࡤࠤ࡫ࡻ࡮ࡤࡶ࡬ࡳࡳࠦࡥࡹࡧࡦࡹࡹ࡯࡯࡯ࠌࠣࠤࠥࠦࡡ࡭ࡱࡱ࡫ࠥࡽࡩࡵࡪࠣࡩࡻ࡫࡮ࡵࠢࡱࡥࡲ࡫ࠠࡢࡰࡧࠤࡸࡺࡡࡨࡧ࠱ࠎࠥࠦࠠࠡࠤࠥࠦᚭ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11l11lll_opy_: str = bstack1l111l1l1_opy_.bstack11ll1l11l11_opy_(label)
            start_mark: str = label + bstack11l11ll_opy_ (u"ࠥ࠾ࡸࡺࡡࡳࡶࠥᚮ")
            end_mark: str = label + bstack11l11ll_opy_ (u"ࠦ࠿࡫࡮ࡥࠤᚯ")
            result = None
            try:
                if stage.value == STAGE.bstack1l1111l111_opy_.value:
                    bstack1l111l1l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1l111l1l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1lll1ll1ll_opy_)
                elif stage.value == STAGE.bstack1l1l1l1lll_opy_.value:
                    start_mark: str = bstack1ll11l11lll_opy_ + bstack11l11ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚰ")
                    end_mark: str = bstack1ll11l11lll_opy_ + bstack11l11ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᚱ")
                    bstack1l111l1l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1l111l1l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1lll1ll1ll_opy_)
            except Exception as e:
                bstack1l111l1l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1lll1ll1ll_opy_)
            return result
        return wrapper
    return decorator
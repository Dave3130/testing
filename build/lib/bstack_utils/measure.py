# coding: UTF-8
import sys
bstack111lll1_opy_ = sys.version_info [0] == 2
bstack11l1l1_opy_ = 2048
bstack11lllll_opy_ = 7
def bstack11lll1_opy_ (bstack111lll_opy_):
    global bstack11ll1l_opy_
    bstack11l11l1_opy_ = ord (bstack111lll_opy_ [-1])
    bstack1l1l_opy_ = bstack111lll_opy_ [:-1]
    bstack1l11l1_opy_ = bstack11l11l1_opy_ % len (bstack1l1l_opy_)
    bstack1lll1l_opy_ = bstack1l1l_opy_ [:bstack1l11l1_opy_] + bstack1l1l_opy_ [bstack1l11l1_opy_:]
    if bstack111lll1_opy_:
        bstack1111lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    else:
        bstack1111lll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1_opy_ - (bstack1ll1ll1_opy_ + bstack11l11l1_opy_) % bstack11lllll_opy_) for bstack1ll1ll1_opy_, char in enumerate (bstack1lll1l_opy_)])
    return eval (bstack1111lll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l1l1llll1_opy_ import get_logger
from bstack_utils.bstack1111l111l1_opy_ import bstack1lllllll111_opy_
bstack1111l111l1_opy_ = bstack1lllllll111_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1lll11l1l1_opy_: Optional[str] = None):
    bstack11lll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᚚ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1111ll_opy_: str = bstack1111l111l1_opy_.bstack11ll1l11lll_opy_(label)
            start_mark: str = label + bstack11lll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ᚛")
            end_mark: str = label + bstack11lll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ᚜")
            result = None
            try:
                if stage.value == STAGE.bstack1ll1ll11l_opy_.value:
                    bstack1111l111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1111l111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1lll11l1l1_opy_)
                elif stage.value == STAGE.bstack11ll1ll11_opy_.value:
                    start_mark: str = bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ᚝")
                    end_mark: str = bstack1ll1l1111ll_opy_ + bstack11lll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ᚞")
                    bstack1111l111l1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1111l111l1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1lll11l1l1_opy_)
            except Exception as e:
                bstack1111l111l1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1lll11l1l1_opy_)
            return result
        return wrapper
    return decorator
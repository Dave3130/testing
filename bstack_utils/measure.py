# coding: UTF-8
import sys
bstack1llllll_opy_ = sys.version_info [0] == 2
bstack11l1l1l_opy_ = 2048
bstack1111ll_opy_ = 7
def bstack1lllll1_opy_ (bstack1l1_opy_):
    global bstack111ll11_opy_
    bstackl_opy_ = ord (bstack1l1_opy_ [-1])
    bstack1l1l_opy_ = bstack1l1_opy_ [:-1]
    bstack111ll_opy_ = bstackl_opy_ % len (bstack1l1l_opy_)
    bstack111l_opy_ = bstack1l1l_opy_ [:bstack111ll_opy_] + bstack1l1l_opy_ [bstack111ll_opy_:]
    if bstack1llllll_opy_:
        bstack1lll1ll_opy_ = unicode () .join ([unichr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    else:
        bstack1lll1ll_opy_ = str () .join ([chr (ord (char) - bstack11l1l1l_opy_ - (bstack11ll11_opy_ + bstackl_opy_) % bstack1111ll_opy_) for bstack11ll11_opy_, char in enumerate (bstack111l_opy_)])
    return eval (bstack1lll1ll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1ll11111l1_opy_ import get_logger
from bstack_utils.bstack11l11l1111_opy_ import bstack1lllllllll1_opy_
bstack11l11l1111_opy_ = bstack1lllllllll1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1lllll1l11_opy_: Optional[str] = None):
    bstack1lllll1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᙾ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1l1111_opy_: str = bstack11l11l1111_opy_.bstack11ll1ll11ll_opy_(label)
            start_mark: str = label + bstack1lllll1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᙿ")
            end_mark: str = label + bstack1lllll1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ ")
            result = None
            try:
                if stage.value == STAGE.bstack1llll1lll1_opy_.value:
                    bstack11l11l1111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11l11l1111_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1lllll1l11_opy_)
                elif stage.value == STAGE.bstack11l1l111l1_opy_.value:
                    start_mark: str = bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚁ")
                    end_mark: str = bstack1ll1l1l1111_opy_ + bstack1lllll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᚂ")
                    bstack11l11l1111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11l11l1111_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1lllll1l11_opy_)
            except Exception as e:
                bstack11l11l1111_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1lllll1l11_opy_)
            return result
        return wrapper
    return decorator
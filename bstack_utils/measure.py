# coding: UTF-8
import sys
bstack1lllll1_opy_ = sys.version_info [0] == 2
bstack11lll1l_opy_ = 2048
bstack1lll1l_opy_ = 7
def bstack11l11l1_opy_ (bstack111l1ll_opy_):
    global bstack1ll1l_opy_
    bstack1l1l1ll_opy_ = ord (bstack111l1ll_opy_ [-1])
    bstack1l11l_opy_ = bstack111l1ll_opy_ [:-1]
    bstack1lllll1l_opy_ = bstack1l1l1ll_opy_ % len (bstack1l11l_opy_)
    bstack11ll1l1_opy_ = bstack1l11l_opy_ [:bstack1lllll1l_opy_] + bstack1l11l_opy_ [bstack1lllll1l_opy_:]
    if bstack1lllll1_opy_:
        bstack1lll_opy_ = unicode () .join ([unichr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    else:
        bstack1lll_opy_ = str () .join ([chr (ord (char) - bstack11lll1l_opy_ - (bstack1l1ll11_opy_ + bstack1l1l1ll_opy_) % bstack1lll1l_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11ll1l1_opy_)])
    return eval (bstack1lll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11111l1l1_opy_ import get_logger
from bstack_utils.bstack11ll111ll1_opy_ import bstack1lllll1l111_opy_
bstack11ll111ll1_opy_ = bstack1lllll1l111_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack111ll1l1ll_opy_: Optional[str] = None):
    bstack11l11l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᚓ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11llllll_opy_: str = bstack11ll111ll1_opy_.bstack11ll1l1l1l1_opy_(label)
            start_mark: str = label + bstack11l11l1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚔ")
            end_mark: str = label + bstack11l11l1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᚕ")
            result = None
            try:
                if stage.value == STAGE.bstack111l111ll1_opy_.value:
                    bstack11ll111ll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack11ll111ll1_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack111ll1l1ll_opy_)
                elif stage.value == STAGE.bstack1ll1lllll_opy_.value:
                    start_mark: str = bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚖ")
                    end_mark: str = bstack1ll11llllll_opy_ + bstack11l11l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᚗ")
                    bstack11ll111ll1_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack11ll111ll1_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack111ll1l1ll_opy_)
            except Exception as e:
                bstack11ll111ll1_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack111ll1l1ll_opy_)
            return result
        return wrapper
    return decorator
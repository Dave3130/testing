# coding: UTF-8
import sys
bstack1lll1_opy_ = sys.version_info [0] == 2
bstack11l11_opy_ = 2048
bstack1_opy_ = 7
def bstack1l1_opy_ (bstack1llllll_opy_):
    global bstack1l11111_opy_
    bstack1l111l_opy_ = ord (bstack1llllll_opy_ [-1])
    bstack11l1ll1_opy_ = bstack1llllll_opy_ [:-1]
    bstack11l1l1l_opy_ = bstack1l111l_opy_ % len (bstack11l1ll1_opy_)
    bstack11111l1_opy_ = bstack11l1ll1_opy_ [:bstack11l1l1l_opy_] + bstack11l1ll1_opy_ [bstack11l1l1l_opy_:]
    if bstack1lll1_opy_:
        bstack1lllll1_opy_ = unicode () .join ([unichr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    else:
        bstack1lllll1_opy_ = str () .join ([chr (ord (char) - bstack11l11_opy_ - (bstack1l1ll11_opy_ + bstack1l111l_opy_) % bstack1_opy_) for bstack1l1ll11_opy_, char in enumerate (bstack11111l1_opy_)])
    return eval (bstack1lllll1_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1ll1111l1_opy_ import get_logger
from bstack_utils.bstack111l11l11_opy_ import bstack1lllllll11l_opy_
bstack111l11l11_opy_ = bstack1lllllll11l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1lll1ll111_opy_: Optional[str] = None):
    bstack1l1_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᚓ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll11ll1lll_opy_: str = bstack111l11l11_opy_.bstack11ll1l1l1l1_opy_(label)
            start_mark: str = label + bstack1l1_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚔ")
            end_mark: str = label + bstack1l1_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᚕ")
            result = None
            try:
                if stage.value == STAGE.bstack11l11l1ll_opy_.value:
                    bstack111l11l11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l11l11_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1lll1ll111_opy_)
                elif stage.value == STAGE.bstack1lllll1l1l_opy_.value:
                    start_mark: str = bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚖ")
                    end_mark: str = bstack1ll11ll1lll_opy_ + bstack1l1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᚗ")
                    bstack111l11l11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l11l11_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1lll1ll111_opy_)
            except Exception as e:
                bstack111l11l11_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1lll1ll111_opy_)
            return result
        return wrapper
    return decorator
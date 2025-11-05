# coding: UTF-8
import sys
bstack11l1ll_opy_ = sys.version_info [0] == 2
bstack1111ll1_opy_ = 2048
bstack11llll_opy_ = 7
def bstack11ll1ll_opy_ (bstack1111l11_opy_):
    global bstack1l111l1_opy_
    bstack1llll11_opy_ = ord (bstack1111l11_opy_ [-1])
    bstack1l1lll1_opy_ = bstack1111l11_opy_ [:-1]
    bstack11111l1_opy_ = bstack1llll11_opy_ % len (bstack1l1lll1_opy_)
    bstack1111l_opy_ = bstack1l1lll1_opy_ [:bstack11111l1_opy_] + bstack1l1lll1_opy_ [bstack11111l1_opy_:]
    if bstack11l1ll_opy_:
        bstack11l11_opy_ = unicode () .join ([unichr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    else:
        bstack11l11_opy_ = str () .join ([chr (ord (char) - bstack1111ll1_opy_ - (bstack1l_opy_ + bstack1llll11_opy_) % bstack11llll_opy_) for bstack1l_opy_, char in enumerate (bstack1111l_opy_)])
    return eval (bstack11l11_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack11111l1ll1_opy_ import get_logger
from bstack_utils.bstack111l11l111_opy_ import bstack1llll11l11l_opy_
bstack111l11l111_opy_ = bstack1llll11l11l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1111l1l1ll_opy_: Optional[str] = None):
    bstack11ll1ll_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᚽ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1l1lll1l1ll_opy_: str = bstack111l11l111_opy_.bstack11ll11lllll_opy_(label)
            start_mark: str = label + bstack11ll1ll_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧᚾ")
            end_mark: str = label + bstack11ll1ll_opy_ (u"ࠨ࠺ࡦࡰࡧࠦᚿ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll111111_opy_.value:
                    bstack111l11l111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l11l111_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1111l1l1ll_opy_)
                elif stage.value == STAGE.bstack11l11ll1ll_opy_.value:
                    start_mark: str = bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᛀ")
                    end_mark: str = bstack1l1lll1l1ll_opy_ + bstack11ll1ll_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᛁ")
                    bstack111l11l111_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l11l111_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1111l1l1ll_opy_)
            except Exception as e:
                bstack111l11l111_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1111l1l1ll_opy_)
            return result
        return wrapper
    return decorator
# coding: UTF-8
import sys
bstack111111l_opy_ = sys.version_info [0] == 2
bstack111lll_opy_ = 2048
bstack11ll111_opy_ = 7
def bstack11l1l11_opy_ (bstack1l11111_opy_):
    global bstack11l1ll1_opy_
    bstack1l1l111_opy_ = ord (bstack1l11111_opy_ [-1])
    bstack1lll11_opy_ = bstack1l11111_opy_ [:-1]
    bstack1ll11l_opy_ = bstack1l1l111_opy_ % len (bstack1lll11_opy_)
    bstack1ll1l_opy_ = bstack1lll11_opy_ [:bstack1ll11l_opy_] + bstack1lll11_opy_ [bstack1ll11l_opy_:]
    if bstack111111l_opy_:
        bstack1ll1_opy_ = unicode () .join ([unichr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    else:
        bstack1ll1_opy_ = str () .join ([chr (ord (char) - bstack111lll_opy_ - (bstack1l1l1l_opy_ + bstack1l1l111_opy_) % bstack11ll111_opy_) for bstack1l1l1l_opy_, char in enumerate (bstack1ll1l_opy_)])
    return eval (bstack1ll1_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111l11ll1l_opy_ import get_logger
from bstack_utils.bstack1111ll11ll_opy_ import bstack1llllll1ll1_opy_
bstack1111ll11ll_opy_ = bstack1llllll1ll1_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1111lll111_opy_: Optional[str] = None):
    bstack11l1l11_opy_ (u"ࠦࠧࠨࠊࠡࠢࠣࠤࡉ࡫ࡣࡰࡴࡤࡸࡴࡸࠠࡵࡱࠣࡰࡴ࡭ࠠࡵࡪࡨࠤࡸࡺࡡࡳࡶࠣࡸ࡮ࡳࡥࠡࡱࡩࠤࡦࠦࡦࡶࡰࡦࡸ࡮ࡵ࡮ࠡࡧࡻࡩࡨࡻࡴࡪࡱࡱࠎࠥࠦࠠࠡࡣ࡯ࡳࡳ࡭ࠠࡸ࡫ࡷ࡬ࠥ࡫ࡶࡦࡰࡷࠤࡳࡧ࡭ࡦࠢࡤࡲࡩࠦࡳࡵࡣࡪࡩ࠳ࠐࠠࠡࠢࠣࠦࠧࠨᚚ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l11llll_opy_: str = bstack1111ll11ll_opy_.bstack11ll1l11ll1_opy_(label)
            start_mark: str = label + bstack11l1l11_opy_ (u"ࠧࡀࡳࡵࡣࡵࡸࠧ᚛")
            end_mark: str = label + bstack11l1l11_opy_ (u"ࠨ࠺ࡦࡰࡧࠦ᚜")
            result = None
            try:
                if stage.value == STAGE.bstack1l1l1l1l1l_opy_.value:
                    bstack1111ll11ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1111ll11ll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1111lll111_opy_)
                elif stage.value == STAGE.bstack111llllll_opy_.value:
                    start_mark: str = bstack1ll1l11llll_opy_ + bstack11l1l11_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢ᚝")
                    end_mark: str = bstack1ll1l11llll_opy_ + bstack11l1l11_opy_ (u"ࠣ࠼ࡨࡲࡩࠨ᚞")
                    bstack1111ll11ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1111ll11ll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1111lll111_opy_)
            except Exception as e:
                bstack1111ll11ll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1111lll111_opy_)
            return result
        return wrapper
    return decorator
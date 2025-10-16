# coding: UTF-8
import sys
bstack111ll1_opy_ = sys.version_info [0] == 2
bstack1l11l1_opy_ = 2048
bstack11111l_opy_ = 7
def bstack1ll1ll1_opy_ (bstack11lll1l_opy_):
    global bstack1ll11l1_opy_
    bstack1l1ll_opy_ = ord (bstack11lll1l_opy_ [-1])
    bstack1ll1l1l_opy_ = bstack11lll1l_opy_ [:-1]
    bstack1l1l1ll_opy_ = bstack1l1ll_opy_ % len (bstack1ll1l1l_opy_)
    bstack11ll1ll_opy_ = bstack1ll1l1l_opy_ [:bstack1l1l1ll_opy_] + bstack1ll1l1l_opy_ [bstack1l1l1ll_opy_:]
    if bstack111ll1_opy_:
        bstack111ll_opy_ = unicode () .join ([unichr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    else:
        bstack111ll_opy_ = str () .join ([chr (ord (char) - bstack1l11l1_opy_ - (bstack111111l_opy_ + bstack1l1ll_opy_) % bstack11111l_opy_) for bstack111111l_opy_, char in enumerate (bstack11ll1ll_opy_)])
    return eval (bstack111ll_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack1l1l1ll111_opy_ import get_logger
from bstack_utils.bstack111l11l1ll_opy_ import bstack1lllll1l11l_opy_
bstack111l11l1ll_opy_ = bstack1lllll1l11l_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1lllll11_opy_: Optional[str] = None):
    bstack1ll1ll1_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡄࡦࡥࡲࡶࡦࡺ࡯ࡳࠢࡷࡳࠥࡲ࡯ࡨࠢࡷ࡬ࡪࠦࡳࡵࡣࡵࡸࠥࡺࡩ࡮ࡧࠣࡳ࡫ࠦࡡࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࡥࡱࡵ࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࠦ࡮ࡢ࡯ࡨࠤࡦࡴࡤࠡࡵࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣ ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll111l11ll_opy_: str = bstack111l11l1ll_opy_.bstack11ll1ll11ll_opy_(label)
            start_mark: str = label + bstack1ll1ll1_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚁ")
            end_mark: str = label + bstack1ll1ll1_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᚂ")
            result = None
            try:
                if stage.value == STAGE.bstack11llll1111_opy_.value:
                    bstack111l11l1ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack111l11l1ll_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1lllll11_opy_)
                elif stage.value == STAGE.bstack111l1l111_opy_.value:
                    start_mark: str = bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᚃ")
                    end_mark: str = bstack1ll111l11ll_opy_ + bstack1ll1ll1_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᚄ")
                    bstack111l11l1ll_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack111l11l1ll_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1lllll11_opy_)
            except Exception as e:
                bstack111l11l1ll_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1lllll11_opy_)
            return result
        return wrapper
    return decorator
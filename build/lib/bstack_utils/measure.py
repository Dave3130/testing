# coding: UTF-8
import sys
bstack11l1_opy_ = sys.version_info [0] == 2
bstack1l1l1ll_opy_ = 2048
bstack1llllll1_opy_ = 7
def bstack1l_opy_ (bstack11l1lll_opy_):
    global bstack1ll1ll1_opy_
    bstack1ll1l_opy_ = ord (bstack11l1lll_opy_ [-1])
    bstack1lll11_opy_ = bstack11l1lll_opy_ [:-1]
    bstack111l111_opy_ = bstack1ll1l_opy_ % len (bstack1lll11_opy_)
    bstack1ll11l_opy_ = bstack1lll11_opy_ [:bstack111l111_opy_] + bstack1lll11_opy_ [bstack111l111_opy_:]
    if bstack11l1_opy_:
        bstack1l1ll1l_opy_ = unicode () .join ([unichr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    else:
        bstack1l1ll1l_opy_ = str () .join ([chr (ord (char) - bstack1l1l1ll_opy_ - (bstack111l11_opy_ + bstack1ll1l_opy_) % bstack1llllll1_opy_) for bstack111l11_opy_, char in enumerate (bstack1ll11l_opy_)])
    return eval (bstack1l1ll1l_opy_)
import logging
from functools import wraps
from typing import Optional
from bstack_utils.constants import EVENTS, STAGE
from bstack_utils.bstack111ll1l1l_opy_ import get_logger
from bstack_utils.bstack1lll11ll11_opy_ import bstack1llll1l1lll_opy_
bstack1lll11ll11_opy_ = bstack1llll1l1lll_opy_()
logger = get_logger(__name__)
def measure(event_name: EVENTS, stage: STAGE, hook_type: Optional[str] = None, bstack1l1ll1ll1_opy_: Optional[str] = None):
    bstack1l_opy_ (u"ࠨࠢࠣࠌࠣࠤࠥࠦࡄࡦࡥࡲࡶࡦࡺ࡯ࡳࠢࡷࡳࠥࡲ࡯ࡨࠢࡷ࡬ࡪࠦࡳࡵࡣࡵࡸࠥࡺࡩ࡮ࡧࠣࡳ࡫ࠦࡡࠡࡨࡸࡲࡨࡺࡩࡰࡰࠣࡩࡽ࡫ࡣࡶࡶ࡬ࡳࡳࠐࠠࠡࠢࠣࡥࡱࡵ࡮ࡨࠢࡺ࡭ࡹ࡮ࠠࡦࡸࡨࡲࡹࠦ࡮ࡢ࡯ࡨࠤࡦࡴࡤࠡࡵࡷࡥ࡬࡫࠮ࠋࠢࠣࠤࠥࠨࠢࠣ ")
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            label: str = event_name.value
            bstack1ll1l1lll11_opy_: str = bstack1lll11ll11_opy_.bstack11ll1ll11ll_opy_(label)
            start_mark: str = label + bstack1l_opy_ (u"ࠢ࠻ࡵࡷࡥࡷࡺࠢᚁ")
            end_mark: str = label + bstack1l_opy_ (u"ࠣ࠼ࡨࡲࡩࠨᚂ")
            result = None
            try:
                if stage.value == STAGE.bstack1ll1lll11l_opy_.value:
                    bstack1lll11ll11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                elif stage.value == STAGE.END.value:
                    result = func(*args, **kwargs)
                    bstack1lll11ll11_opy_.end(label, start_mark, end_mark, status=True, failure=None,hook_type=hook_type,test_name=bstack1l1ll1ll1_opy_)
                elif stage.value == STAGE.bstack11ll111111_opy_.value:
                    start_mark: str = bstack1ll1l1lll11_opy_ + bstack1l_opy_ (u"ࠤ࠽ࡷࡹࡧࡲࡵࠤᚃ")
                    end_mark: str = bstack1ll1l1lll11_opy_ + bstack1l_opy_ (u"ࠥ࠾ࡪࡴࡤࠣᚄ")
                    bstack1lll11ll11_opy_.mark(start_mark)
                    result = func(*args, **kwargs)
                    bstack1lll11ll11_opy_.end(label, start_mark, end_mark, status=True, failure=None, hook_type=hook_type,test_name=bstack1l1ll1ll1_opy_)
            except Exception as e:
                bstack1lll11ll11_opy_.end(label, start_mark, end_mark, status=False, failure=str(e), hook_type=hook_type,
                                       test_name=bstack1l1ll1ll1_opy_)
            return result
        return wrapper
    return decorator